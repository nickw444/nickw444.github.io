---
title: Picaxe Microcontroller
author: nickw
layout: post

dsq_thread_id:
  - 2744444137
categories:
  - Blog
  - Electronics
  - Programming
---
This week was my last week for the semester at uni. At our last computing lecture our lecturer told us there would be a micro controller question as part of the test. He did state that if we wrote a micro controller emulator in C and shared it, it would be allowed into the test. This is greatly useful for checking machine code during the exam.

I decided I would set about writing up an emulator. I finished the task with no issues. I&#8217;m very happy with my emulator (of a fictional microprocessor).

The microprocessor is noted as the &#8220;8005&#8221; chip. A chip with 256 bytes of memory. It&#8217;s got about 17 different instructions. The sorts of programs we have written in machine code for these are amazing, we have written halving functions, as well as wondrous number generators. I&#8217;m certainly amazed.

Now, whilst writing the emulator, I remembered I had a picaxe micro controller stored away in my cupboard. I brought it down after I was done and started playing. My interest in this also comes about due to my father wanting to read RS232 data off our solar panel inverter and viewing it on his iPad. This is my challenge tomorrow &#8211; this was just the warm up.

I hooked up the picaxe on a breadboard, and wrote a basic program:

[<img class="aligncenter size-full wp-image-1350" src="http://cdn.nickwhyte.com/static/2014/06/Screen-Shot-2014-06-08-at-12.08.34-am.png" alt="Screen Shot 2014-06-08 at 12.08.34 am" width="520" height="199" />][1]

<!--more-->

Quite basic. However it&#8217;s made me surprisingly happy. I can control a LED via serial communication from my computer.



<p class="jetpack-slideshow-noscript robots-nocontent">
  This slideshow requires JavaScript.
</p>

<div id="gallery-1349-8-slideshow"  class="slideshow-window jetpack-slideshow slideshow-" data-width="984" data-height="410" data-trans="fade" data-gallery="[{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2014\/06\/IMG_14371.jpg&quot;,&quot;id&quot;:&quot;1358&quot;,&quot;caption&quot;:&quot;The Serial Stream&quot;},{&quot;src&quot;:&quot;http:\/\/nickwhyte.com\/wordpress\/wp-content\/uploads\/2014\/06\/IMG_14391.jpg&quot;,&quot;id&quot;:&quot;1357&quot;,&quot;caption&quot;:&quot;The Hardware&quot;}]">
</div>

 [1]: http://cdn.nickwhyte.com/static/2014/06/Screen-Shot-2014-06-08-at-12.08.34-am.png