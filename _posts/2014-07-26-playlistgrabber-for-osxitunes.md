---
title: PlaylistGrabber for OSX/iTunes
author: nickw
layout: post

dsq_thread_id:
  - 2874290111
categories:
  - PlaylistGrabber
  - Programming
  - Projects
---
Spotify was great. I had my music everywhere, could add new music without a computer, however it lacked in a major area &#8211; Playlists. It seems to be a growing trend of music players to suck at this. Being unable to shuffle all music on the device is also a massive drawback. I will be cancelling my Spotify subscription once my 3 month trial is over.

Let me introduce PlaylistGrabber for OSX. This is my first Cocoa application, targeted at 10.8 and upwards (not tested much). PlaylistGrabber reads your iTunes library XML file, and allows you to choose playlists to export. It creates a folder structure that you can drag and drop onto your device (or export directly to the device if you have mass storage capabilities). It exports playlists in M3U format and understands that the duplicate songs in different playlists are the SAME song &#8211; so no stupid duplicates in your library, just as iTunes handles it.

Due to the nature and simplicity of M3U playlists, most music players understand these, including PowerApp, Samsung Music App and Google Play Music. This is good news, as now you are free to roam to other solutions than DoubleTwist for all your iTunes Syncing needs.

Eventually I will tidy up the application, however at this present time, I do not have enough time to do so. Eventually I would like to make the app do the following:

  * <del>Save Chosen Playlist Preferences for re-loading later on if a user decides they want to re-sync </del>Implemented in newest version.
  * Sync Daemon &#8211; Watches when Library Changes, and writes changes to a sync directory, from where you could auto sync with google drive
  * Wifi Sync (With a client app on the phone)
  * Better Async Handling so the program doesn&#8217;t appear to &#8220;Lock Up&#8221;

If you come across any bugs or have any suggestions, let me know, it&#8217;ll be nice to track them in the future for new releases in summer this year.

[Latest version is available here][2]

 [2]: https://github.com/nickw444/playlist-grabber
