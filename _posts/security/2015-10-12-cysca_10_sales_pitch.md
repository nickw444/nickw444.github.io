---
title: CySCA 2015 - Corporate Pentest 1.0 - Sales Pitch
author: nickw
layout: post

dsq_thread_id:
  - 809215685
categories:
  - Blog
  - Security
---

**Task:** Connect to the management panel of the proxy server

Proxy is misconfigured, allowing anyone externally to use it to access 
internal infrastructure.

We take advantage of this. We set our HTTP proxy to it, however we still don't know what the box's internal IP is. 

We try `127.0.0.1` via the proxy, however no luck. Upon inspecting the "Frontend" page we realise it has `INT: x.x.x.x EXT: x.x.x.x` in the `<title></title>` html tag.

We load up `INT: x.x.x.x` via the proxy and the flag is revealed.
