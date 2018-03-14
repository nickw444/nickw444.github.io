---
title: Weekly Roundup 27 May 2013
author: nickw
layout: post

dsq_thread_id:
  - 1325532232
categories:
  - Blog
  - Programming
---
I totally forgot yesterday that I had to write this post - however, I'm doing it now, so I guess this kind of counts. This week's been a bit of a busy one. I've had a couple of school assesments to do, as well as a tonne of homework, which is still waiting for me to do, Anyways, let's get into this.

This week I discovered the world of cocoapods (however almost ruined my whole SDD project git repo, but I rolled back and was all good.), The world of RESTkit, which seems like it'll solve all my data persistance troubles in my SDD project, and finally all about reaver WPS, which i've written a nice little piece about below;

Before I get into the story of BT linux and reaver, I must share my obsession with the [Great Gatsby Soundtrack,][1] which caught my eye when I heard the song [&#8216;Together' by The XX][2] on pandora radio. I highly recommend anyone to check it out, due to it's gigantic mix of genres.

Continuing on, this week I ventured into the world of reaver-WPS - But this came at a cost - My time. Lots of time. I ran BT linux from a live USB HDD, created with [unetbootin][3], which worked really well - except i couldn't save anything, but I knew that. So on saturday, my surprisingly cheap GTX660TI came ($140 factory repaired + warrantee), so I decided if I was going to install the CUDA drivers, i'd actually like them to stick around after reboots. I ran the BT installer planning to install onto a 500GB disk I had in my cupboard, however, silly me - I didn't unplug my stash of HDD's in my PC after plugging in the new 500GB. Wisely, I did install BT to the correct partition - however, this is where it all went wrong. The bootloader decided it would install to /dev/sda0.. My SSD. Containing my OSX86 bootloader. Somehow the installer broke the GPT, and even after trying about 20 times to re-install many different flavours of the a GUID bootloader, I eventually came to the realisation i'd screwed something up pretty badly. I made a full system image using Carbon Copy Cloner to a sparseimage file (I also have a live recovery partition which is a weekly backup of my system, which is how I planned to restore this sparseimage file. I didn't want to write over the recovery drive as I was worried i'd broken something inside OSX). Anyways, Booted into recovery, formatted my SSD, and cloned my sparseimage back to it. I installed chimera, and rebooted. Horray! bootloader. 4 hours later, I now have a working osx86 system again. I rebooted again, this time, ensuring all my hdd's were unplugged. I ran the BT installer, and all good.

I continued to install the Nvidia CUDA drivers, however, I was unable to get pyrit to work on my card. Benching pyrit on my CPU yielded results around 4000pmk/s - it now wonders me what my GTX660TI could be doing. The amusement of BT linux began to wear off, and I decided i'd save it for another rainy day, reaver WPS seemed like a bit of an eh sort of thing anyways - Right now, I needed to sort out the GTX660TI in OSX.

<img class="alignleft  wp-image-1046" alt="3fba7794afbb11e2ad1322000a9e28e6_7" src="/static/legacy/2013/11205652_1444005629231362_658619705_n.jpg" width="180" height="180" /> I have 3 monitors, so how my original setup worked prior to my new 660 card, was pretty fragile. I originally started with a GT640, running a single monitor, however, once I acquired another two monitors for either side of my primary, I realised, not all 3 ports on the GT640 would work at the same time inside OSX (But it works in windows :S). I had to enable the HD4000 integrated to make this work. I needed to find a way to allow these to work side by side, but eventually found a way using a &lt;device property&gt; string inside my com.chameleon.boot.plist file.  This worked nicely - until my 660 came along. I know the device property was for the 640, so that was no use to me, so, I had to ditch it, but all my attempts to make anything work failed. I'm unable yet to determine if I can use more than 2 outputs on the 660 as I don't have a DP to DVI or a HDMI to DVI cable (I have ordered one however). My attempts to fix this display dilemma, was simply to disable the onboard gfx, and put back in my GT640 (Which i know is also natively supported). My system is happy, and now has really nice CUDA acceleration.


&nbsp;

 [1]: https://itunes.apple.com/au/album/great-gatsby-music-from-baz/id636199212
 [2]: http://www.youtube.com/watch?v=yoj2I6ZJLx8
 [3]: http://unetbootin.sourceforge.net/
