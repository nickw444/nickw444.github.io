---
title: NCSS Challenge Wk3 Problem 2
author: nickw
layout: post

dsq_thread_id:
  - 817787432
categories:
  - Blog
---
As per request, i&#8217;m uploading my solution to this problem:

<pre class="lang:python decode:true crayon-selected">inputs = raw_input("Message: ")
words = []
outs = ""
t = []
for word in inputs.split(' '):
    words.append(word)

for word in words:
    if word in t:
        outs += word + " "
    else:
        t.append(word)

if outs.strip() != "":
    print(outs.strip())</pre>

&nbsp;