---
title: CySCA 2015 - Web Application Pentest 2 - The Eagle Has Landed
author: nickw
layout: post

categories:
  - Blog
  - Security
---

<div style="font-size:0.7em"><i>Note: If you're interested in actually doing these challenges, <a href="/post/2015/cysca-2015/">check out this post</a> on 
how to get the environment set up.</i>
</div>

* * *

We need to obtain a working account on the system. 

We Register with the following details:

{% highlight text %}
Name: Nick
Email: nick@fake.com
Password: nick
Confirm: nick
Secret Q: q
Secret A: a
{% endhighlight %}

We notice a message at the top:

> Account Registered - Awaiting IT approval.

<!--break-->

Trying to log in yields this error message: 

> ACCOUNT LOCKED
> This is either a newly unverified account or you have had too many failed 
login attempts. If you require assistance please contact an IT administrator.

We're going to need to find a way to get in. Sometimes websites have flaws in 
their signup process, such that resetting a password will unlock an account.

Lets try that. We reset the password to the same one that I set it to. The 
banner now reads:

> Account unlocked - Password reset

Awesome. Let's try logging in. Aaaand we're in. The flag is revealed in the 
ticker:

> You're a User! - FLAG{2a000000000000000000000000000000}
