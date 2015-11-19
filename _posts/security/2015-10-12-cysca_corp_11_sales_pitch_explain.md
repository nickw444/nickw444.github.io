---
title: CySCA 2015 - Corporate Pentest 1.1 - Explain This Sales Pitch
author: nickw
layout: post

categories:
  - Blog
  - Security
---

**Task:** Explain the misconfiguration of the squid proxy

*Nb, this could only be answered once the flag for Murphy's law was captured, since there was no easy solution to cat /etc/squid3/squid.conf any other way.*

This is due to misconfiguration in the proxy configuration file:

{% highlight bash %}
$> cat /etc/squid3/squid.conf
{% endhighlight %}


{% highlight bash %}
# Allow connections to the internet
acl internet src all

# Allow connections from the internal network
acl internalsystems src fd00:dead:beef::0/64

# Allow connections to the internet
http_access allow internet
http_access allow internalsystems

acl Safe_ports port 80
acl Safe_ports port 443

#Only allow CONNECT on port 443
acl SSL_ports port 443
acl CONNECT method CONNECT

# Deny requests to unsafe ports
http_access deny !Safe_ports

# Only allow cachemgr access from localhost
http_access allow localhost manager
http_access deny manager

# And finally deny all other access to this proxy
http_access deny all

# Squid should listen on port 3128
http_port 3128

# Never cache
cache deny all
{% endhighlight %}


The misconfigured line: 
{% highlight bash %}
# Allow connections to the internet
acl internet src all
{% endhighlight %}

This instead is allowing all machines from the internet to use the proxy, 
allowing them to see internal infrastructure via the proxy.
