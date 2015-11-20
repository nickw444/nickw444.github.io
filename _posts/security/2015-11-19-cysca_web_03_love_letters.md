---
title: CySCA 2015 - Web Application Pentest 3 - Love Letters
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

Now that we're logged in, lets take a poke around and see what we're dealing 
with. There appears to be sections to:

- Apply for leave, where we submit a text request. Maybe XSS or Injection on 
  this?
- Staff Directory, details about different staff members. 
    - The "Network Administrator" has some binary in his profile. We'll decode 
      that later.

- There seems to also be a message board. Maybe XSS or Injection. 
- There's also a mail inbox.

<!--break-->

Since this challenge is called love letters, lets focus on the mail. 

We'll send a message to ourself. We send the message:

{% highlight text %}
To: nick@fake.com
Subject: Hello World

Hello
{% endhighlight %}

When we go back to our inbox, we take a look at the received message.

{% highlight text %}
Hello

IMPORTANT: This email remains the property of ECWI.0f
{% endhighlight %}

Loading of the mail seemed very ajaxy. Lets look at our network inspector. We 
notice a request made to `http://www.ecwi.cysca/mail/13`.

The loaded mail is actually encrypted, and decrypted on the client using 
javascript.

{% highlight text %}
===== ECWI INTERNAL MAIL =====
ENCRYPTED_FOR: Nick 
MAIL_FOLDER: RECV
DATE: 05:54 19/11/15
TO: nick@fake.com
FROM: nick@fake.com
SUBJECT: Hello World
===== BEGIN ENCRYPT MAIL =====
KiQNLwpuSC50Mw0zZScvY1lhZVwMFWQC
CwdZChZDVS4DKA8wRRAqAhkTMA5BAxND
GmFeUkUjBzAvSA
===== ENDOF ENCRYPT MAIL =====
{% endhighlight %}

Inspecting the decryption, hosted in `http://www.ecwi.cysca/js/main.js`, we 
notice it's just a simple XOR with a key (after base64 decoding the message)

We stab around the mail endpoint looking for other users mail. We notice
we can load all other mail. We notice at `http://www.ecwi.cysca/mail/9` that
the subject is `Decrypt me to win!`. It's addressed to *spacetrip.riverbrother@ecwi.com*
and encrypted for Spacetrip Riverbrother. Excellent. 

To decrypt this message, we need to know the key to decrypt it. The decryption
key is different for every user, hence, you can only decrypt your own mail.

There are numerous ways to crack the key for the message we want to decrypt. 
The easiest method is to crib drag using the known phrase in every email: 
`IMPORTANT: This email remains the property of ECWI.`, however we won't do 
that. We're going to do a *known plaintext attack*.

If we know the unencrypted text sent to the user, we simply XOR the known text 
with the encrypted text to give us the decrpytion key. The only thing we must 
ensure is that we send a message long enough to expose the entire key length.

We know a key is 32 characters long, looking at our own embeded in the /inbox 
html source.

Lets send a message to Spacetrip Riverbrother. 

{% highlight text %}
To: spacetrip.riverbrother@ecwi.com
Subject: We are going to win!
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
{% endhighlight %}

We go to the mail endpoint and load up the message, ensuring to find the copy
encrypted for Spacetrip Riverbrother (and from us). For me, it was found at 
[http://www.ecwi.cysca/mail/15](http://www.ecwi.cysca/mail/15), but your milage may vary.

{% highlight text %}
===== ECWI INTERNAL MAIL =====
ENCRYPTED_FOR: Spacetrip Riverbrother
MAIL_FOLDER: RECV
DATE: 05:54 19/11/15
TO: spacetrip.riverbrother@ecwi.com
FROM: nick@fake.com
SUBJECT: We are going to win!
===== BEGIN ENCRYPT MAIL =====
I3QCdnNxBHkEIwdxdngDcQIDJwJycHJ1
AAVzd3AHI3MjdAJ2c3EEeU9oD31ndhBk
AgwyeRNlW10yZFdbUC8OEhBQLlZbXjYY
MQojEEdLLUAmMBI6E15VFAQHZX8f
===== ENDOF ENCRYPT MAIL =====
{% endhighlight %}

Lets drop this into a python program and figure out the key. Knowing the symmetric 
decryption/encryption algorithm used, we craft the following python program:

{% highlight python %}
import base64
encrypted = "I3QCdnNxBHkEIwdxdngDcQIDJwJycHJ1AAVzd3AHI3MjdAJ2c3EEeU9oD31ndhBkAgwyeRNlW10yZFdbUC8OEhBQLlZbXjYYMQojEEdLLUAmMBI6E15VFAQHZX8f".decode('base64')
expected = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

key = ""
for encrypted, expected in zip(encrypted, expected):
    print(encrypted, expected)
    key += chr(ord(expected) ^ ord(encrypted))

print(key)
{% endhighlight %}

From that, out pops the key used: `b5C720E8EbF079B0CBfC3134AD261Fb2b5C720E8`

Let's decrypt the message.

{% highlight python %}
import base64
encrypted = "JHkCcEkFfXxxUQAEAHgGCXZ0UnYDAgoMeXUDAggHUHZRBHYBCk1PMgwvFn9lbQN+F3hGF1tYQBQkKVNfXWYQVw9UKllBEDFQIEI2QlhJJ0I3O0YsVRF2dxYNHA==".decode('base64')
key = "b5C720E8EbF079B0CBfC3134AD261Fb2b5C720E8"
out = ""
for i, ch in enumerate(encrypted):
    k = key[i % len(key)]
    out += chr(ord(ch) ^ ord(k))

print(out)
{% endhighlight %}

And out pops the flag `FLAG{58D43F47AD95645039881149A2D31568}`