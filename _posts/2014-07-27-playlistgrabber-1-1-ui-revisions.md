---
title: PlaylistGrabber 1.1 (UI Revisions)
author: nickw
layout: post

dsq_thread_id:
  - 2875215405
categories:
  - Blog
  - PlaylistGrabber
  - Programming
  - Projects
---

Due to the large response to the initial release of PlaylistGrabber, I have quickly revised some of the UI and functionality to bring it up to scratch with user expectations.

#### Changelog:

  * Added App Icon (Green iTunes yeah close enough)
  * You can now select a playlist by clicking the entire row, not just the checkbox
  * PlaylistGrabber now remembers what playlists you selected last time
  * You can save your progress of playlist selection by pressing &#8220;Save Selected&#8221;
  * PlaylistGrabber now remembers what XML File you last used. Quick and Easy Startup.
  * PlaylistGrabber skips copying files that already exist in the destination (good if you&#8217;re using a cloud service). It will however re-generate M3U Files so you will get playlist updates.
  * Tableview now has pretty icons
  * Tableview nests items inside folders at their level as depicted within itunes. Wish i could indent the icon too.
  * &#8220;About&#8221; window updated.
  * Auto build incrementing (current release is build 110)
  * Automatically quits app on window close.

#### Things I&#8217;d Like it to do better

  * Nest icons for folder indentation levels
  * Delete songs when a playlist is de-selected. This could prove quite tricky

I&#8217;m pretty happy with what I have achieved over the few hours I&#8217;ve worked on this project. And after all, I&#8217;ve learnt how to program for Mac OSX.

#### Download

~~You can download release 1.1 build 110 here:~~

  * ~~[PlaylistGrabber][1] (.app, drag to your applications folder to install, run whenever you want to enumerate music on your device)~~


You can obtain the source and self-compile [here](https://github.com/nickw444/playlist-grabber).

[1]: /static/legacy/2014/07/PlaylistGrabber1.zip