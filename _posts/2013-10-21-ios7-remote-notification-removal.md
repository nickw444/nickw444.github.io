---
title: iOS7 Remote Notification Removal
author: nickw
layout: post
permalink: /2013/10/21/ios7-remote-notification-removal/
dsq_thread_id:
  - 1881158530
categories:
  - Blog
  - Programming
---
<img class="alignright" alt="" src="http://cdn.nickwhyte.com/static/2013/10/ui_r_35.jpg" width="300" />I&#8217;ve noticed since the early builds of iOS7 that notification centre on both the lock screen and within the phone, now has this really nice feature.

It appears as though specific services such as Google Plus and Facebook which distribute notification to users phones will now remove the notifications from the lock screen if they have been viewed somewhere else (ie, on a computer).

A quick google search of this reveals no specific results for this phenomenon. I&#8217;m 100% sure this is a new addition to the OS, as previous builds of iOS with Facebook notifications would not be removed from your lock screen.

At the present time I am unsure of how the implementation works, however, I would assume that it would involve APNS sending a badge count of 0 to the phone, ideally removing all notifications. I will be testing this after my HSC and determining it&#8217;s results.