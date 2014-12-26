---
title: 'Why the Media Sucks (Facebook Messenger Isn&#8217;t Bad)'
author: nickw
layout: post
permalink: /2014/08/18/why-the-media-sucks/
dsq_thread_id:
  - 2937231638
categories:
  - Blog
---
If you haven&#8217;t heard about latest news and debate surrounding Facebook&#8217;s Messenger app, I would honestly be surprised. In a brief rundown, many news agencies are giving Facebook Messenger a really, really bad rap, and in my opinion, it&#8217;s extremely unfair.

Some of the claims news agencies are making

  * It requires access to your front and back camera, this means it&#8217;s spying on us
  * It requires access to your text messages and phone calls so they must be seeing who we talk to.
  * It requires access to your contacts and are collecting all of their info.

These claims are indeed partially true &#8211; (the required permissions at least)

### Sandboxing on iOS

I&#8217;m an iOS developer, and have been for many years. Within the iOS platform, apps are contained within their own sandbox, and cannot communicate with other apps (except apps owned by the same organisation, although this is still limited). More importantly, when requiring special permissions, such as camera access and contact access, they are required to show a dialogue to the user. This is the flow of iOS.

Facebook does in fact require access to your front and back camera. This isn&#8217;t to spy on you. This is to take photos for you to send to your friends via messenger. The facebook app cannot invoke the camera without the app being in the foreground (due to the nature of the sandbox and lockdownd/fairplayd (i&#8217;m pretty sure they&#8217;re the two daemons who control this) .

Facebook also requires access to your contacts. It uses this info to match them to your friends for contact synchronisation so you can get their profile pictures on your phone. Additionally this also lets you message non-facebook friends (Something new facebook is trying to make catch on like iMessage did on iOS only)

However, Facebook CANNOT under any circumstance access your phone calls or SMS messages on iOS. The iOS sandbox disallows this completely. These are no API&#8217;s for this at all.

### Android

You&#8217;re probably a little less safe on android &#8211; Facebook requires the same permissions, but also gets access to your text messages. Nothing to worry about though &#8211; Facebook doesn&#8217;t read your messages. It only checks your messages for a confirmation message it sends to confirm your phone number. There seriously is nothing here to be worried about.

The other two permissions such as camera access and contacts are also used for the above reasons, however I am not 100% sure on the android sandbox and cannot confirm whether or not they can run the camera in the background (highly unlikely they would anyway &#8211; why they hell would they want to spy on you).

### Wrapping Up

Long story short, it&#8217;s some of these claims are absolutely ridiculous. More importantly, the above permissions that are required for Messenger, were part of the permissions the original Facebook app required anyway, so it&#8217;s rather a ridiculous argument for people to have.