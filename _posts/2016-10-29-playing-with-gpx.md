---
title: Understanding and Tweaking some GPX data
author: nickw
layout: post

categories:
  - Blog
  - Programming
---

As a casual bike rider, I enjoy tracking my rides with [Strava](https://www.strava.com)
so I can take a look at how my ride went and how well I performed throughout. 

However, very rarely the Strava tracking application randomly 
crashes, or gets killed by iOS on my phone, during the ride. This means
that the data was never recorded between the point at which the app died and 
the point when I became aware the app had died.

If we plot this type of failure, it looks something like this:


<p class="text-center">
    <img style="max-width: 450px; width:100%" src="/images/playing-with-gpx.png" alt="Map with missing data" />
</p>


Fortunately in this case, there wasn't too much missing data. However, I was
still determined to learn about the GPX format and see if I could patch up the 
GPX file programatically.

In the specific case of the above map, I was riding north west, and at a point
Strava crashed. Between this point and when I pulled out my phone to check my 
progress, no points were plotted. Google maps interprets this lack of data as 
a straight line between to the 2 points (as per GPX specification).

If we crack open the GPX file and take a look, we can see exactly what this looks
like:

{% highlight xml %}
...
<trkpt lat="-33.9014420" lon="151.1066810">
    <ele>6.6</ele>
    <time>2016-10-28T23:38:50Z</time>
</trkpt>
<trkpt lat="-33.8802920" lon="151.0702190">
    <ele>20.9</ele>
    <time>2016-10-28T23:51:14Z</time>
</trkpt>
...
{% endhighlight %}

In it's simplest form, a GPX file is an XML document that contains a sequence 
of GPS points (with associated metadata like elevation, and other depending
on the tracker). This makes it reasonably simple for us to get our hands
dirty and begin fixing the data set.

In order to add the missing data back into the GPX file, we need 3 things:

 - The last coordinate recorded before the app crashed
 - The coordinate when the app was revived
 - A list of points of the track we want to use for our data points. 

Fortunately, I was able to obtain a list of coordinates for the missing data
since I travelled the same path on the return journey (As can be seen on the 
map above). 

The other 2 app state points of interest are reasonably easy to find - just
find 2 data points that have a (reasonably) large time distance between them.

In order to process the data, I used a python library called `gpxpy` which 
provided some good utilities for reading and processing a GPX file. 

With this library, I was able to find the crash point, the revival point, and 
the list of the points of the track. With this data, I interpolated the start/end 
times of the crash points onto the track data, and spliced it back into the 
dataset.

After exporting the data set, we achieve a map that looks like:


<p class="text-center">
    <img style="max-width: 450px; width:100%" src="/images/playing-with-gpx-fixed-map.png" alt="Map with resolved data" />
</p>


Quite clearly, this has a few limitations, for example, the calculated velocity
through all of the data points is simply an average. However, this did provide
me with an improved dataset which I could re-upload to Strava.

You can find all the source for this script 
[on my github](https://github.com/nickw444/strava-fixer)



