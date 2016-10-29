---
title: 'Listy: Progress is being made'
author: nickw
layout: post

dsq_thread_id:
  - 884347897
categories:
  - Blog
  - Programming
tags:
  - ios
  - iPhone
  - listy
  - programming
  - projects
---
So, as shown in my previous post, my app &#8216;Listy&#8217; was recently approved on the app store. The initial release had a bug for all iOS5 users, causing it to crash, but I released version 1.02 to fix this.

Anyways, 2 weeks later (when I should be studying for my HSC IPT/IT), the project has become so appealing to work on. I&#8217;m learning *so* much through this. The latest version I&#8217;m working on (Version 1.03), has been modified to work on iPhone as well as iPad, better customisation of lists, it&#8217;s quicker, it&#8217;s easier to use, and uses **CoreData. <!--more-->**

If you take a look at the following screenshots, you can see the new interface elements, such as being able to &#8216;star&#8217; items on a list. At the present time I&#8217;m working on allowing lists to be customised to specific user needs, ie &#8211; allowing them to choose what they are sorted by, allowing priorities of items, or to create a traditional to-do list. You can **now edit items** on the list, and depending on the sort of list you set up initially, you can attach geolocations, longer descriptions, links, and images. You can also choose **who** gets to see the list, determined by the email address you enter for the user. A much more private way of sharing lists.

As this new version uses CoreData, the syncing methods are going to be a challenge on the server side, especially with shared lists. I&#8217;ll work it out, but this next release could be months away.

As for my own personal education &#8211; boy have I learnt a lot. I&#8217;m still learning ObjC, self taught, just like all my other languages, but as I do more advanced things, I understand the concepts as a whole. For example, the custom star button, I implemented a delegate method to tell the parent controller that the star had been checked and needed to update and save CoreData. I&#8217;ve also learnt CoreData, how to open records, and modify &#8211; and in turn, this actually allowed me to understand the concept of pointers*. It&#8217;s all so much magic. It&#8217;s all hard work, but it&#8217;s really what I love doing.