---
title: PlaylistGrabber for OSX/iTunes
author: nickw
layout: post
permalink: /2014/07/26/playlistgrabber-for-osxitunes/
dsq_thread_id:
  - 2874290111
categories:
  - PlaylistGrabber
  - Programming
  - Projects
---
Spotify was great. I had my music everywhere, could add new music without a computer, however it lacked in a major area &#8211; Playlists. It seems to be a growing trend of music players to suck at this. Being unable to shuffle all music on the device is also a massive drawback. I will be cancelling my Spotify subscription once my 3 month trial is over.

[<img class="alignright wp-image-1447" src="http://cdn.nickwhyte.com/static/2014/07/Screen-Shot-2014-07-26-at-4.12.13-pm.png" alt="Screen Shot 2014-07-26 at 4.12.13 pm" width="300" height="283" />][1]Let me introduce PlaylistGrabber for OSX. This is my first Cocoa application, targeted at 10.8 and upwards (not tested much). PlaylistGrabber reads your iTunes library XML file, and allows you to choose playlists to export. It creates a folder structure that you can drag and drop onto your device (or export directly to the device if you have mass storage capabilities). It exports playlists in M3U format and understands that the duplicate songs in different playlists are the SAME song &#8211; so no stupid duplicates in your library, just as iTunes handles it.

Due to the nature and simplicity of M3U playlists, most music players understand these, including PowerApp, Samsung Music App and Google Play Music. This is good news, as now you are free to roam to other solutions than DoubleTwist for all your iTunes Syncing needs.

Eventually I will tidy up the application, however at this present time, I do not have enough time to do so. Eventually I would like to make the app do the following:

  * <del>Save Chosen Playlist Preferences for re-loading later on if a user decides they want to re-sync </del>Implemented in newest version.
  * Sync Daemon &#8211; Watches when Library Changes, and writes changes to a sync directory, from where you could auto sync with google drive
  * Wifi Sync (With a client app on the phone)
  * Better Async Handling so the program doesn&#8217;t appear to &#8220;Lock Up&#8221;

<del>If you want to download this and try it out, feel free to: <a href="http://cdn.nickwhyte.com/static/2014/07/PlaylistGrabber.zip">PlaylistGrabber</a>.</del> If you come across any bugs or have any suggestions, let me know, it&#8217;ll be nice to track them in the future for new releases in summer this year.

[Latest version is available here][2]

<!--more-->

Here are a few more screenshots:

<div id="attachment_1450" style="width: 505px" class="wp-caption aligncenter">
  <a href="http://cdn.nickwhyte.com/static/2014/07/Screen-Shot-2014-07-26-at-4.18.56-pm.png"><img class="wp-image-1450 size-full" src="http://cdn.nickwhyte.com/static/2014/07/Screen-Shot-2014-07-26-at-4.18.56-pm.png" alt="Screen Shot 2014-07-26 at 4.18.56 pm" width="495" height="205" /></a>
  
  <p class="wp-caption-text">
    Initial Screen to select your iTunes Library XML File
  </p>
</div>

<div id="attachment_1449" style="width: 523px" class="wp-caption aligncenter">
  <a href="http://cdn.nickwhyte.com/static/2014/07/Screen-Shot-2014-07-26-at-4.18.26-pm.png"><img class="wp-image-1449 size-full" src="http://cdn.nickwhyte.com/static/2014/07/Screen-Shot-2014-07-26-at-4.18.26-pm.png" alt="Screen Shot 2014-07-26 at 4.18.26 pm" width="513" height="432" /></a>
  
  <p class="wp-caption-text">
    Exported File Structure, Ready to place on your Android Phone (lol@null folder. dammit NSString)
  </p>
</div>

 [1]: http://cdn.nickwhyte.com/static/2014/07/Screen-Shot-2014-07-26-at-4.12.13-pm.png
 [2]: http://nickwhyte.com/category/projects/playlistgrabber/