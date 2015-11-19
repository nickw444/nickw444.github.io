---
title: CySCA 2015 - Web Application Pentest 0 - In Plain Sight
author: nickw
layout: post

categories:
  - Blog
  - Security
---

This was any easy one - Snoop around the html source code on the login page. 
You'll find a HTML Comment around line 99:

{% highlight html %}
<!-- X marks the spot -->
<!-- RkxBR3sxYTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMH0N -->
{% endhighlight %}

We notice that it's Base64 looking. We decode this as base64:

{% highlight python %}
>>> str = 'RkxBR3sxYTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMH0N'
>>> print(str.decode('base64'))
FLAG{1a000000000000000000000000000000}
{% endhighlight %}