---
title: Weekly Roundup 27 May 2013
author: nickw
layout: post
permalink: /2013/05/27/weekly-roundup-27-may-2013/
dsq_thread_id:
  - 1325532232
categories:
  - Blog
  - Programming
---
I totally forgot yesterday that I had to write this post &#8211; however, I&#8217;m doing it now, so I guess this kind of counts. This week&#8217;s been a bit of a busy one. I&#8217;ve had a couple of school assesments to do, as well as a tonne of homework, which is still waiting for me to do&#8230; Anyways, let&#8217;s get into this.

This week I discovered the world of cocoapods (however almost ruined my whole SDD project git repo, but I rolled back and was all good.), The world of RESTkit, which seems like it&#8217;ll solve all my data persistance troubles in my SDD project, and finally all about reaver WPS, which i&#8217;ve written a nice little piece about below;

Before I get into the story of BT linux and reaver, I must share my obsession with the [Great Gatsby Soundtrack,][1] which caught my eye when I heard the song [&#8216;Together&#8217; by The XX][2] on pandora radio. I highly recommend anyone to check it out, due to it&#8217;s gigantic mix of genres.

Continuing on, this week I ventured into the world of reaver-WPS &#8211; But this came at a cost &#8211; My time. Lots of time. I ran BT linux from a live USB HDD, created with [unetbootin][3], which worked really well &#8211; except i couldn&#8217;t save anything, but I knew that. So on saturday, my surprisingly cheap GTX660TI came ($140 factory repaired + warrantee), so I decided if I was going to install the CUDA drivers, i&#8217;d actually like them to stick around after reboots. I ran the BT installer planning to install onto a 500GB disk I had in my cupboard, however, silly me &#8211; I didn&#8217;t unplug my stash of HDD&#8217;s in my PC after plugging in the new 500GB. Wisely, I did install BT to the correct partition &#8211; however, this is where it all went wrong. The bootloader decided it would install to /dev/sda0.. My SSD. Containing my OSX86 bootloader. Somehow the installer broke the GPT, and even after trying about 20 times to re-install many different flavours of the a GUID bootloader, I eventually came to the realisation i&#8217;d screwed something up pretty badly. I made a full system image using Carbon Copy Cloner to a sparseimage file (I also have a live recovery partition which is a weekly backup of my system, which is how I planned to restore this sparseimage file. I didn&#8217;t want to write over the recovery drive as I was worried i&#8217;d broken something inside OSX). Anyways, Booted into recovery, formatted my SSD, and cloned my sparseimage back to it. I installed chimera, and rebooted. Horray! bootloader. 4 hours later, I now have a working osx86 system again. I rebooted again, this time, ensuring all my hdd&#8217;s were unplugged. I ran the BT installer, and all good.

I continued to install the Nvidia CUDA drivers, however, I was unable to get pyrit to work on my card <img src="http://nickwhyte.com/wordpress/wp-includes/images/smilies/icon_sad.gif" alt=":(" class="wp-smiley" /> Benching pyrit on my CPU yielded results around 4000pmk/s &#8211; it now wonders me what my GTX660TI could be doing. The amusement of BT linux began to wear off, and I decided i&#8217;d save it for another rainy day, reaver WPS seemed like a bit of an eh sort of thing anyways &#8211; Right now, I needed to sort out the GTX660TI in OSX.

[<img class="alignleft  wp-image-1046" alt="3fba7794afbb11e2ad1322000a9e28e6_7" src="http://cdn.nickwhyte.com/static/2013/05/3fba7794afbb11e2ad1322000a9e28e6_7-300x300.jpg" width="180" height="180" />][4]I have 3 monitors, so how my original setup worked prior to my new 660 card, was pretty fragile. I originally started with a GT640, running a single monitor, however, once I acquired another two monitors for either side of my primary, I realised, not all 3 ports on the GT640 would work at the same time inside OSX (But it works in windows :S). I had to enable the HD4000 integrated to make this work. I needed to find a way to allow these to work side by side, but eventually found a way using a <device property>string inside my com.chameleon.boot.plist file.  This worked nicely &#8211; until my 660 came along. I know the device property was for the 640, so that was no use to me, so, I had to ditch it, but all my attempts to make anything work failed. I&#8217;m unable yet to determine if I can use more than 2 outputs on the 660 as I don&#8217;t have a DP to DVI or a HDMI to DVI cable (I have ordered one however). My attempts to fix this display dilemma, was simply to disable the onboard gfx, and put back in my GT640 (Which i know is also natively supported). My system is happy, and now has really nice CUDA acceleration.

<p class="jetpack-slideshow-noscript robots-nocontent">
  This slideshow requires JavaScript.
</p>

<div id="gallery-1041-1-slideshow"  class="slideshow-window jetpack-slideshow slideshow-" data-width="984" data-height="410" data-trans="fade" data-gallery="[{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2013\/05\/Screen-Shot-2013-05-27-at-7.38.39-PM.png&quot;,&quot;id&quot;:&quot;1042&quot;,&quot;caption&quot;:&quot;&quot;},{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2013\/05\/Screen-Shot-2013-05-27-at-7.39.00-PM.png&quot;,&quot;id&quot;:&quot;1043&quot;,&quot;caption&quot;:&quot;&quot;},{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2013\/05\/3fcea022b7ca11e29a6e22000a1fab27_7.jpg&quot;,&quot;id&quot;:&quot;1049&quot;,&quot;caption&quot;:&quot;&quot;},{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2013\/05\/bb6d29f0c50911e2a82422000a9e07ae_7.jpg&quot;,&quot;id&quot;:&quot;1048&quot;,&quot;caption&quot;:&quot;&quot;},{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2013\/05\/736fc878a3f411e29f5b22000a1fbc74_7.jpg&quot;,&quot;id&quot;:&quot;1047&quot;,&quot;caption&quot;:&quot;&quot;}]">
  
</div></p> 

</a>

&nbsp;

 [1]: https://itunes.apple.com/au/album/great-gatsby-music-from-baz/id636199212
 [2]: http://www.youtube.com/watch?v=yoj2I6ZJLx8
 [3]: http://unetbootin.sourceforge.net/
 [4]: http://cdn.nickwhyte.com/static/2013/05/3fba7794afbb11e2ad1322000a9e28e6_7.jpg