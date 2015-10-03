---
title: CSESoc Hackathon
author: nickw
layout: post

categories:
  - Blog
  - Programming
---

A couple of weeks back, the society I am a member of at Uni hosted a hackthon 
event, sponsered by [Freelancer](https://www.freelancer.com.au/). For the 
uninitiated, a hackathon is an event where programmers literally turn pizza and 
drink into applications/code. (But in all seriousness, it's an event where 
programmers develop a cool idea in a small timeframe and compete to be the 
'best' product).

I formed a team with 2 friends from Uni. We set out to build a web platform for
students of UNSW to list projects they have worked on in an easy to use web
directory that they could use for employment and their own portfolio. 

The webapp is written in Python/Python-Flask, uses MySQL as the backend 
(because mongo hates many to many relationships), and use Bootstrap to style
the frontend, statically served from the server. 

We wanted the following features from the service:

- A project has:
    - Web URL
    - Download URL
    - Marketing URL
    - Markdown formatted description
    - Ability to upload screenshots of the project
    - A project can have multiple contributors
- Project Page:
    - Showcase of all projects the user has worked on
    - About me for the user
    - Show who the user follows
    - Show who is following the user
- Home Page/General:
    - A-Z listing of all projects
    - Show latest 3 projects on the home page "ShowCase"
- Logins/Logouts use UNSW's LDAP service, so it's all UNSW SSO.

There are some additional features we wish to work into it, such as reading
README.md from github projects. 

There are a few bugs hanging around still, along with some non-implemented 
features, such as multi contributors for a project. We'll eventually get around
to these, and finally launch it!

We plan to put it up on [http://showc.se/](http://showc.se/), a domain I 
purchased for the project. It's a nice play on words, and also is a valid 
regular expression, which matches "ShowCase", but also is a play on CSE - 
Computer Science and Engineering.

It's probably important to note that we came first in the Hackathon, each of 
the team members winning a UE Boom portable bluetooth speaker thanks to 
Freelancer!

Stick around for more, i'll update this post when it's live!

