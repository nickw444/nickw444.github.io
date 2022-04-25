---
title: Ender 3 v2 Pen Plotter
author: nickw
layout: post

categories:
- Blog

social_image: /static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2585.jpeg
---


<p>
    <img class="img-responsive alignright" width="40%" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2585.jpeg" />
    Last year I purchased myself an Ender 3 V2 3D Printer. It was a logical purchase, to compliment my home automation hobby, allowing me to design and print custom enclosures for miscellaneous ESPHome and Zigbee nodes.
</p>

It turns out having a [CoreXY](https://all3dp.com/2/corexy-3d-printer-is-it-worth-buying/) 3D printer allows you to do more than just 3D printing if you're willing to get creative. For example, adding on a [laser engraver](https://all3dp.com/2/ender-3-laser-engraver-upgrade-all-you-need-to-know/). 

In my case, I was tasked with automating the process of drawing an embroidery pattern onto fabric using a heat/friction erasable pen for my partner, [Kate](https://kateescott.com/). 

Unsurprisingly, there are services available which can do this, albeit using machine washable dye rather than heat reactive dye in most cases. However, in almost every case these are cost prohibitive for hobby embroidery projects and also happen to incur a long turn around time from order to delivery.   

So as with most projects I undertake, rather than re-designing from scratch, I opted to start searching for existing projects. Surely someone had done this before! I managed to find a handful of models (e.g. [ Ender 3 v2 Pen Plotter addon ](https://www.printables.com/model/121808-ender-3-v2-pen-plotter-addon)), however most of these either required you to fully remove the hotend assembly or did not accomodate mounting a BL-Touch levelling probe.

Fortunately I managed to find [this model](https://www.thingiverse.com/thing:4664467) which both accommodated both of my requirements. It supported mounting of the BL-Touch probe without needing to remove the hotend assembly. I printed it and mounted it to the printer... job done... right? Unfortunately not. Due to the way it mounted it now meant that the hot-end carriage could no longer hit the x-axis limit switch. Not good!

From here, **the only logical solution was to design my own**, which accommodated for my specific requirements. I've been getting more and more familiar with Fusion 360 since buying the printer, so was confident to get straight to prototyping a design. 

I started off by importing dimensionally accurate models of both the Ender 3 v2 print head assembly/x-carriage and the BL-Touch:

<p><img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/prototyping-models.png" /></p>

By doing so, I would be able to project the precise positions of mounting holes onto the sketches for component of my attachment, rather than measuring by hand with some amount of inaccuracies.

Another requirement I came to realise was that it would be useful would be the ability to remove the plotter attachment when it is not in use. As such I arrived at my first design iteration:

<p><img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/prototyping-iteration-1.png" /></p>

The design was relatively simple. Two main parts; a mounting arm to hold the BL-Touch probe to the hotend assembly, and a three-piece arm to hold the pen, which is mounted to the mounting arm using the same screws from the BL-Touch probe. The three-piece arm was designed to allow a pen to be mounted with some spring tension, however in actual fact once it was printed there was too much friction to provide any reasonable amount of travel. Back to the drawing board.

On to the next iteration, I re-thought the design. I reused the same mounting arm to the hotend assembly, but changed the mounting angle of the pen attachment. Instead, it would side-mount to the mounting arm using M3 bolts into heat-set inserts. I thought I would give this a try, without any tension mechanism, as an automatically leveled bed should suffice. 

<p><img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/prototyping-iteration-2.png" /></p>

One printed, I came to realise that the side mounting again caused some interference with the x-axis limit switch, so I found that in order to solve this problem I needed to move the rear bolt closer to the front, and additionally provide a countersunk for the bolt head to sit inside.

<p><img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/prototyping-iteration-3.png" /></p>

After a handful more prints and some more tweaks to the height of mounting arm and hole sizes, I had a final design:

<p><img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/final-render.png" /></p>

Now, with the mounting bracket complete, it was time to move onto the software aspect of the project. Fortunately for me, this is a solved problem. [Uri Shaked has written an excellent post](https://urish.medium.com/how-to-turn-your-3d-printer-into-a-plotter-in-one-hour-d6fe14559f1a) about using Inkscape with the Gcodetools extension to produce plotting toolpats from SVG files. Inkscape isn't the nicest software to run on MacOS, so the experience is a little clunky (and crashy), but it does the job. However, I plan on exploring [other tools](https://www.reddit.com/r/3Dprinting/comments/lla1is/comment/gnqo577/?utm_source=share&utm_medium=web2x&context=3), like [Inkcut](https://github.com/inkcut/inkcut), [JScut](http://jscut.org/), [juicy-gcode](https://hackage.haskell.org/package/juicy-gcode), [SVG-toGcode](https://github.com/avwuff/SVG-to-GCode) and [hp2xx](https://www.gnu.org/software/hp2xx/) in due time.

Gcodetools allows you to specify a custom header and footer for produced gcode files. I used this to provide a more ergonomic printing experience by ensuring the printer was homed, bed levelling mesh is enabled, and the print timer is initiated to allow for on-the-fly tweaking of the z-height.

Header:

{% highlight gcode %}
M420 S1 ; Enable Jyers Mesh
M75 ; Start print timer
G28 ; home all axis
{% endhighlight %}

Footer:

{% highlight gcode %}
G1 Z20.00 F600 ; Move print head up
G1 X5 Y180 F9000 ; present print
M84 X Y E ; disable motors
M77 ; Stop print timer
{% endhighlight %}

Now, with some G-code produced, it was time for a test. As a software engineer, there's no better way to test the output capability of something than to `print("hello world")`, and so that is exactly what I did:

<p><img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2585.jpeg" /></p>

Great success! From here, I did some further tests on fabric and found it worked just fine, albeit a little faint since more pen pressure resulted in snagging the fabric, so for fabric prints 2 or 3 passes is generally necessary. Beyond just plotting SVGs I've started to explore generative art using mathematical functions ([like a spirograph](https://github.com/asharkinwater/spirograph-)). Here are a few pictures from testing and a video:

<div class="row">
    <div class="col-xs-6">
            <p>
                <a target="_blank" href="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2573.jpeg">
                    <img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2573.jpeg" />
                </a>
            </p>
    </div>
    <div class="col-xs-6">
            <p>
                <a target="_blank" href="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2575.jpeg">
                    <img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2575.jpeg" />
                </a>
            </p>
    </div>
</div>
<div class="row">
    <div class="col-xs-6">
            <p>
                <a target="_blank" href="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2602.jpeg">
                    <img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2602.jpeg" />
                </a>
            </p>
    </div>
    <div class="col-xs-6">
            <p>
                <a target="_blank" href="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2616.jpeg">
                    <img class="img-responsive center-block" src="/static/posts/2022-04-25-ender-3-v2-pen-plotter/IMG_2616.jpeg" />
                </a>
            </p>
    </div>
</div>

<p></p>

<div class="embed-responsive embed-responsive-16by9">
    <iframe width="640" height="360" src="//www.youtube.com/embed/-DLPJjCscFY?rel=0" frameborder="0" allowfullscreen></iframe>
</div>

<p></p>

You can find the model for my Ender 3 V2 BL Touch Mount and Pen Plotter on [Thingiverse](https://www.thingiverse.com/thing:5363733) and [Thangs](https://thangs.com/mythangs/file/62724)


