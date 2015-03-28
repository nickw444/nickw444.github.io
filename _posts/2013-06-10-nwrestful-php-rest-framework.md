---
title: 'NWRestful &#8211; PHP REST framework'
author: nickw
layout: post

dsq_thread_id:
  - 1385333117
categories:
  - Blog
  - Programming
---
Well, between my earlier blogging of photos and now I&#8217;ve been writing a little PHP REST framework. It has come from my need for a REST interface for my iPhone app for my major project. After much searching, I was unable to find a decent REST framework, or at least something that was easy to understand and use.

I began to follow a tutorial I found [here][1], which served as the complete base of the project.  That blog post doesn&#8217;t show you much, only a bunch of simple code snippets from a working server. I put some of these to use, writing my own implementations. The one thing this tutorial was missing was working with models &#8211; but that&#8217;s fine, the tutorial was just about REST.

I began wondering about CoreData on iOS and the magical ways it does things to data. It transforms the data and uses the NSManagedObject class along with a NSManagedContext to do all the database magic. I thought to myself &#8211; &#8220;why not take this approach to the issue&#8221;. So that&#8217;s what I did exactly. Now, I had multiple DB options, but I opted to use SQLite3 simply because I could take the DB around with me using git.

I wrote a standard class for handing all the data objects called NWManagedObjectModel. This model holds the methods for saving and purging. Any new data model can be created off this class. The subclass can define it&#8217;s own purging methods, saving methods, or whatever else it needs. The main idea is that each model simply hold the variables and their types.

When an object is saved, an SQL query checks to see if a table has been created, and if it hasn&#8217;t will create one. The table will be created to identically replicate the PHP object model/class object type you are saving. Once the table is created, it now inserts/updates the object to the database as  a new row.

Creating objects and adding them to the DB is relatively simple &#8211; Simply create a new PHP object for the model/entity you want, and call the save() method on the object.

Retrieving objects is equally easy &#8211; Simply create a NWManagedObjectContext object, and call either getEntitiesForStatement($entity, $statement), calling your own custom SQL statement, OR getEntityForInstance($entity, $instanceID). These return an array full of the entities/php objects you requested.

As for the REST and how it handles these different object model types &#8211; It&#8217;s really transparent. All you need to do is define a controller for the model, you don&#8217;t even need to define any methods on the class (provided you subclass &#8220;RoutingController&#8217;), all the work is done within the RoutingController class.

Anyways, that&#8217;s probably enough late night rambling &#8211; plus it&#8217;s a school night.

[Here&#8217;s a link to the GitHub Repo][2]. Currently i&#8217;m licensing under Creative Commons Attribution-NonCommercial 3.0 Unported License

 [1]: http://www.lornajane.net/posts/2012/building-a-restful-php-server-understanding-the-request
 [2]: https://github.com/nickw444/NWRestful