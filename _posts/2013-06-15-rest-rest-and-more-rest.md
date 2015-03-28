---
title: Rest, Rest, and more Rest
author: nickw
layout: post

dsq_thread_id:
  - 1404187560
categories:
  - Blog
  - Programming
---
Nope, I&#8217;m not talking about sleeping. I&#8217;m talking about quite the opposite. Actually, as I type this, I should be sleeping, however, I am not. To be completely honest, REST is taking away my own rest.

Okay that&#8217;s enough late night rambling &#8211; Here&#8217;s what&#8217;s happening.

I&#8217;ve continue to play and implement with this REST server I&#8217;ve written, and now it&#8217;s time to play with the actual client data retrieval. In this case, the iPhone. It took about 3 hours for me to get my head around RESTKit for iOS, but with the help of [this tutorial][1], I managed to get it all set up, and working nicely, including integration with coreData for persistence.

Right now i&#8217;m up to the position of implementing authentication, however, I&#8217;m split between how I should model the getting of objects. I&#8217;m considering writing my own Objective C class to handle all the sending and retrieving of data &#8211; It will still interface through RestKit, but it&#8217;ll hold all the methods and keep everything neat and tidy &#8211; something I REALLY need to do with this project, as all code will be submitted as my major work for SDD.

Anyways, that&#8217;s probably enough for tonight, I&#8217;ll take another look at it in the morning, and maybe write down some plans for the class. It&#8217;s now real REST time&#8230;.

 [1]: http://www.alexedge.co.uk/blog/2013/03/08/introduction-restkit-0-20/