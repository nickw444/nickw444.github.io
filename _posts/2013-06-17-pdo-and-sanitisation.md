---
title: PDO and Sanitisation
author: nickw
layout: post

dsq_thread_id:
  - 1409142394
categories:
  - Programming
---
No doubt in the world of programming, sanitisation is one of the most important things when implementing a web database of some sort. 

Typically I&#8217;ve used mysqli\_real\_escape_string, which does the job, but it&#8217;s so tedious to type. I only recently found out about PDO, and prepared statements. 

Due to my current decision to use SQLite instead of mysqli, I&#8217;ve needed to use PDO to escape all of my input data. My input data had double quotes, which is not escaped by the standard SQLite escaper. The SQLite docs state not to use addslashes to escape the strings either. 

After googling for a bit, I realised my only option was to use PDO &#8211; but to my surprise it was extremely simple. If anything just as easy as writing a standard query. The only modifications needed was my variable insert structure in my managedobjectmodel super class. 

I&#8217;ve now got to work on upgrading models inside the database (although I have a basic version of this already working), until I release the code on github. 

Anyways, what I&#8217;m trying to say here is &#8211; don&#8217;t risk SQL injection, use PDO, it may take an extra half minute to write, but it&#8217;s worth it in the long run. Alternatively, use my framework or similar to do the heavy lifting for you.