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

<div id='gallery-14' class='gallery galleryid-1292 gallery-columns-2 gallery-size-thumbnail'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://nickwhyte.com/2013/10/21/determining-movement-of-a-distant-object-on-a-small-sensor/img_1849/'><img width="250" height="250" src="http://cdn.nickwhyte.com/static/2013/10/IMG_1849-250x250.jpg" class="attachment-thumbnail" alt="IMG_1849" /></a>
    </dt>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://nickwhyte.com/2013/10/21/determining-movement-of-a-distant-object-on-a-small-sensor/img_1850/'><img width="250" height="250" src="http://cdn.nickwhyte.com/static/2013/10/IMG_1850-250x250.jpg" class="attachment-thumbnail" alt="IMG_1850" /></a>
    </dt>
  </dl>
  
  <br style="clear: both" />
</div>

Once completed, I found that the equation can be noted as this through the above working (although incorrect):

πS(r+a)h/43200\*ø\*a  
Where:  
ø = Horizontal angle of projection from the lens (in radians)  
a = orbital altitude of object  
r = radius of the earth  
S = shutter time in second  
h = horizontal resolution of sensor

&nbsp;