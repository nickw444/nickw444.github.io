---
title: Quadcopter Electronics Assembly Complete
author: nickw
layout: post

dsq_thread_id:
  - 2785295561
categories:
  - Blog
images:
  - { image: 'http://cdn.nickwhyte.com/static/2014/06/2014-06-22-13.46.51.jpg',
      caption: 'Cardboard stopping the bottom of the RPi shorting. Featuring Electrical Tape Mounting'
    }
  - { image: 'http://cdn.nickwhyte.com/static/2014/06/2014-06-22-13.46.57.jpg',
      caption: 'Electrical Tape Mounting FTW'
    }
  - { image: 'http://cdn.nickwhyte.com/static/2014/06/2014-06-22-13.47.06.jpg',
      caption: 'Need to find a safer place to house the battery. These things explode.'
    }
youtube: lVxbO1KiBK8
---
So far i&#8217;ve almost completed all the electronics components of the quadcopter. I am now waiting for my 5v regulator to arrive. I will use this to drive the Raspberry Pi from the 7.2 Lipoly battery. Once this arrives the quad will be able to become fully wireless (currently 5v power inlet is requiring a cable).

I wrote a basic program to control the PWM speeds from the RPi. This is letting me test the power that the quad has. At the moment it can easily lift off at about 40/100 (however I&#8217;m not sure if this is linear).

This video shows me bringing the controller speed up to 30/100:

{% include youtube.html %}

The next challenge is going to be mounting everything in such a way that it&#8217;s accessible and still lightweight. At the moment electrical tape is a great mounting tool.

{% include gallery.html %}