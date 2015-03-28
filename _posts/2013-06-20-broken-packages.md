---
title: Broken Packages
author: nickw
layout: post

dsq_thread_id:
  - 
categories:
  - Blog
  - Hosting
---
Silly me &#8211; I just wanted to install SQLite for my [Avocado hosting website][1]. Yes, take a look. It hosts images of my avocado seedling I&#8217;ve grown over the past 3 months, taking a photo every 2 minutes (soon to be once every 15 minutes).

Anyways, I needed to install SQLite to host the database on my VPS, however, upon trying to install the required libraries, I was greeted with a dependency error. I had no clue why &#8211; all my packages /were/ up to date. After 2 hours of headaches, and trying to run apt-get update it turns out my sources were the issue. After changing my sources around (by this time I had also removed php5-fpm, nginx and mysql), I tried to re-install php and all the other required things to run my web server. This time it successfully installed SQLite.

Lesson Learned: Check your apt sources before removing packages and wasting time.

 [1]: http://nickwhyte.com/avocado