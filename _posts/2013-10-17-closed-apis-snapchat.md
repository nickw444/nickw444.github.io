---
title: 'Closed API&#8217;s: SnapChat'
author: nickw
layout: post
permalink: /2013/10/17/closed-apis-snapchat/
dsq_thread_id:
  - 1867243468
categories:
  - Blog
  - Programming
---
<img class="alignright" alt="" src="http://cdn.nickwhyte.com/static/2013/10/snapchat.jpg" width="160" height="160" />[Snapchat][1]. It&#8217;s a big craze. The point: To send photo&#8217;s that self destruct after being viewed. However; there are hacks as well as entire apps which can allow the saving of images without the sender being notified. Awesome. Hardly.

I have spent the last 2 hours finding an efficient way to reverse engineer the protocols and data being passed between the SnapChat client and the SnapChat server, in hope that I&#8217;d gain some more knowledge about how snaps are encrypted/transmitted/received by the devices. Unfortunately I have been unable to find a way to read the data in a raw format. I&#8217;ve tried both packet sniffing via [WireShark][2], various HTTP Proxies, as well as my own Python creation. Nothing.

So now, I am writing this piece from my perspective, about how the service should work.

The service appears simple. For example;  Friend A sends a snap, the server holds this image and sends a push notification to User A&#8217;s phone, telling him/her they have an image awaiting collection. User A opens the app on their phone, SnapChat now downloads and caches all the snaps which have been awaiting collection; including Friend A&#8217;s snap.

You now have the snaps on your phone. Mods/Plugins like Phantom (iOS) simply save these cached images.

<img class="alignleft" alt="" src="http://a4.mzstatic.com/au/r30/Purple4/v4/92/84/8d/92848d4c-8911-9dff-d851-484dfac8d007/screen480x480.jpeg" height="130" />But what about other apps, like [&#8220;Snap Save&#8221;][3]? This is what I would have liked to gone into earlier. It appears the developer of Snap Save has reverse engineered the connection protocols, and mimics within it&#8217;s own app. This allows it to save the images straight to the device, instead of restricting the time limit like SnapChat does.

Could SnapChat fix this? Yes. They could.

&nbsp;

Why don&#8217;t we fix it for them. Here&#8217;s how:

  1. Server generates a **random string(****)**, seeded from the current time, therefore it always changes. Let&#8217;s set up a time window, to allow these to last for ~2 minutes
  2. Server encrypts this string using a public key (*KeyA*). The private key(*KeyA)* is within the App Bundle.
  3. Server sends the encrypted string to the client
  4. Client decrypts the original **random string(***stringA**) ***and uses the private key (*KeyA*)******

In the mean time, the server has done the following:

  1. Uses the original *stringA*
  2. Uses the secret algorithm to turn *StringA* into *StringC*

The server has now received *StringB* from the client

  1. Server decrypts the *Encrypted* *StringB* using *KeyB*
  2. Server should compare it&#8217;s own *StringC * to the client&#8217;s *StringB*
  3. If *StringC *is equal to *StringB*, we should in theory have an authorised client.
  4. The server should now give the *AuthorisedClient *an access token with an expiration time or only permissions to view a specific image to limit the damage an unauthorised client could do with it (ie, saving snaps).

It&#8217;s complex, and yes, it could most definitely simpler, I am sure there are more efficient ways (lol lots of server resources) to do this, however, I have never implemented such a system, nor have I began to research this topic. This is simply how I would jump in and solve the problem.

And a quick note, this does not solve issues of plugins such as [Phantom][4], as they hook into the SnapChat app itself.

 [1]: https://itunes.apple.com/us/app/snapchat/id447188370?mt=8
 [2]: http://www.wireshark.org/
 [3]: https://itunes.apple.com/au/app/snap-save-for-snapchat-screenshot/id662714487?mt=8
 [4]: http://www.addictivetips.com/ios/secretly-save-media-upload-longer-videos-in-snapchat-for-iphone-phantom/