---
title: 'Bridging the Gap: iTunes to Android'
author: nickw
layout: post
permalink: /2014/06/13/bridging-the-gap-itunes-to-android/
dsq_thread_id:
  - 2760734824
categories:
  - Blog
  - PlaylistGrabber
  - Programming
  - Projects
---
I hate proprietary things. Specifically iTunes. It&#8217;s a great music manager, it&#8217;s robust, stable, and has a brilliant store. It also offers fantastic integration with iOS devices. As much as that is great for iOS users, it sucks for anyone on Android. In my opinion this is driving people to move to streaming music services such as Google Play Music or Spotify (both of which I am contemplating).

There are various tools available which bridge the gap. Apps such as DoubleTwist for Mac & Android do the job, however they&#8217;re just too clunky.

For me, leaving my iTunes Library and picking up some new music management tool would be a big hassle. iTunes has all my music, including over 300 of my playlists. I need a program to bridge iTunes and my Android Device.

At the moment I&#8217;m on the verge of writing a tool to extract iTunes music, track playlists and keep music in sync onto my Android phone. My roadmap for the tool is as follows:

  1. Read iTunes Library & Copy Playlists onto device without duplicates
  2. Synchronise Playlists with the device, so songs removed in iTunes are removed on the Phone.
  3. Write metadata to the device for playlists
  4. OR Write a music playing app &#8211; however this may be overkill.

Anyway, this will be a learning process. I&#8217;m aware tools are available to do this task, however building one tailored to my needs to possibly the best solution in my case. Looking at the iTunes Library XML files, they look relatively easy to work with, and maybe eventually I&#8217;ll set up a auto importer for my &#8220;external purchases&#8221; to automatically add them to my Library and put them in the right folder on my computer.