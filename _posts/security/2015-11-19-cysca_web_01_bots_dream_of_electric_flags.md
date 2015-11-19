---
title: CySCA 2015 - Web Application Pentest 1 - Bots Dream of Electric Flags
author: nickw
layout: post

categories:
  - Blog
  - Security
---
 
Our WebSec foo tells us we should have a look in robots.txt. Not only that, but
the title does give this one away - *Bots*. 


{% highlight text %}
GET /robots.txt HTTP/1.1

User-agent: *
Disallow: /admin
Disallow: /backup
Disallow: /protected
{% endhighlight %}

Lets take a look in these.

- `/admin` - Nothing here, just a picture
- `/backup` - Nothing here, just another picture
- `/protected` - Reveals the flag `FLAG{1b000000000000000000000000000000}`

