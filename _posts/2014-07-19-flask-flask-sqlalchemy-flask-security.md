---
title: 'Flask, Flask-SQLAlchemy &#038; Flask-Security'
author: nickw
layout: post
permalink: /2014/07/19/flask-flask-sqlalchemy-flask-security/
dsq_thread_id:
  - 2856952904
categories:
  - Blog
  - Programming
---
My last 3 weeks has mostly consisted of programming for a Flask Web Environment.

What is flask? Flask is a fancy python library allowing rapid web application, api, and interface development. It tackles many of the hard parts of programming web apps in nice and easy paradigms.

Flask has many extensions available, two being Flask-SQLAlchemy and Flask-Security. These two are must haves for any kind of application development involving a database and a level of security management.

Back in my PHP days, I would slave away and create a fancy PHP permissions structure for whatever web application I was writing. Horrible. Probably filled with vulnerabilities & all sorts of bad things. Flask-Security is made so you don&#8217;t need to do this.

How about SQLAlchemy? SQLAlchemy is a database interface wrapper, but it&#8217;s more than just a wrapper. It does ORM, which means you can represent your database entities as objects/classes. A very similar paradigm to both CoreData on iOS AND my own, NWRestful/NWManagedObjects framework.

## So, how do we use all this?

As this isn&#8217;t a tutorial, I won&#8217;t go through it, however there are some AMAZING examples hosted on the Flask website and the Flask-SQLAlchemy website. I cannot say the same for Flask-Security however.

Over my first project, programming for Flask/Flask-security, I found the security library&#8217;s documentation to be greatly lacking. This was a slight drawback, however once I got my head around the library, everything went nicely.

I will aim to upload a Flask example package/boilerplate with the structure of how I use flask within the next few weeks.