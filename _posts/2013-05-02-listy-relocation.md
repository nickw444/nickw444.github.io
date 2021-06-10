---
title: Listy relocation
author: nickw
layout: post

dsq_thread_id:
  - 1253813242
categories:
  - Blog
---
I have successfully relocated the Listy 2.0 Server!

I have also, as of now, found the issue to a very annoying bug &#8211; the duplication of items.

The syncing system of Listy uses the devices local time and compares this to the time of the online server. If the clock of the device syncing the items is slightly offset; syncing will not work&#8230;

Listy 2.02 is on its way; this will include minor bug fixes, updates to the location of the server (so it won&#8217;t need to go through a redirection tunnel), and a fix for the duplication bug (Unfortunately I need to track the devices now, and attach a device time to each in the online server &#8211; this shouldn&#8217;t be hard to do as all i need to do is create a random string and store it and send it to the server each time the device requests something new).

Anyways; I hope to push version 2.02 to apple tonight; they should approve it within 1 and a bit weeks!