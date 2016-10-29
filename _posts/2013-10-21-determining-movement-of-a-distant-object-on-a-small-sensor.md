---
title: Determining Movement of a Distant Object on a Small Sensor
author: nickw
layout: post

dsq_thread_id:
  - 1881495648
categories:
  - Blog
---
I took a few pictures of the moon last night, which got me thinking &#8211; how many pixels on my sensor will the moon move in a specific time frame. I noticed results where I left the shutter open for more than 4 seconds, a motion blur can be seen, and anything > 1/50th of a second shows a slight elongation of the moon.

I set out to calculate this elongation; however the results weren&#8217;t great, and I know my equations are definitely wrong. The following images outline the process to determine the movement. I will return to this at a later date, and determine how to calculate the movement on a sensor.

<p>
  <img class="img-responsive center-block" src="//cdn.nickwhyte.com/2013/IMG_1849.jpg" />
</p>
<p>
  <img class="img-responsive center-block" src="//cdn.nickwhyte.com/2013/IMG_1850.jpg" />
</p>


Once completed, I found that the equation can be noted as this through the above working (although incorrect):

πS(r+a)h/43200\*ø\*a  
Where:  
ø = Horizontal angle of projection from the lens (in radians)  
a = orbital altitude of object  
r = radius of the earth  
S = shutter time in second  
h = horizontal resolution of sensor

&nbsp;