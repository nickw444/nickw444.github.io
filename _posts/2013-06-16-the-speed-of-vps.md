---
title: The Speed of VPS
author: nickw
layout: post

dsq_thread_id:
  - 1405140395
categories:
  - Blog
  - Hosting
---
Recently, I decided to take the leap from GoDaddy&#8217;s stupid document root shared hosting to a VPS. I found a really inexpensive company called [Prgmr][1]. This transfer is the main reason I actually blog more &#8211; It&#8217;s no longer a tedious task of having to wait 30 seconds for each damn page to load.

GoDaddy was a horrible provider, and every time I complained, they said there was no issue, and that they couldn&#8217;t see anything wrong. I finally took a stand to them once I set myself up on prgmr &#8211; I told them I&#8217;m leaving. They were nice enough to give me a refund for the unused months I had left (which was quite nice of them, considering I don&#8217;t have any other services with them).

Once my payment for Prgmr went through, I was set up with a blank vps in about 2 working days. The xen virtual platform, is pretty cool, from the direct console, to the way it can schedule cpu usage, it impresses me. Once I was logged into my vps, I created an account for myself, as by default &#8211; and for good reason &#8211; allowing the root user to access remotely is asking for trouble.

I installed my web server stack &#8211; I chose nginx over apache, after using it on my Raspberry pi, and finding the config for virtual hosts amazingly easy &#8211; and that&#8217;s the simplicity I needed for this server. I don&#8217;t have time to stuff around with the <virtualhost> directives every time I need to add a new site. The only issue I have with nginx is that it cannot use .htaccess files, which are surprisingly convenient at times.

Once I&#8217;d setup all the server stack, I setup backups, writing my own backup script for auto rotation, and uploading of backups to an offsite location.

I&#8217;m very happy with the service of prgmr and would recommend them to anyone looking to rent a VPS for a low monthly cost.

 [1]: http://prgmr.com/