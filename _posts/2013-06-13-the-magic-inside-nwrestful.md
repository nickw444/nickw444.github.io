---
title: The magic inside NWRestful
author: nickw
layout: post

dsq_thread_id:
  - 1398653350
categories:
  - Blog
  - Programming
---
For both my own future reference, and for others, I&#8217;m going to write some basic ways to use NWRestful &#8211; well, the data structure framework underlying it.

### Creating a Model

To begin with, you&#8217;re going to need to create a model a data structure. This is relatively simple:

<pre class="lang:php decode:true">&lt;?php
	class EventModel extends NWManagedObjectModel {
		public $name;
		public $place;
		function __construct() {
			parent::__construct();
			settype($this-&gt;name, 'string');
			settype($this-&gt;place, 'string');
		}
	}

?&gt;</pre>

There&#8217;s not too much to it.  Simply define your variables, and define their data types. You must ensure you append the word &#8220;Model&#8221; to your class name. (Make sure you import the &#8220;NWManagedObjectModel&#8221; class if you&#8217;re not using an auto importer).  Once you&#8217;ve done that, we will see where the magic lies.

### Creating & Saving

NWManagedObjectModel does most of the work here. Upon the first save of a new object, it sets up the database, creating the columns and setting their data type. Let&#8217;s see how we create and save things:

<pre class="lang:php decode:true">&lt;?php
require_once("EventModel.php");
$event = new EventModel();
$event-&gt;name = "Some Name";
$event-&gt;place = "Some Place";
$event-&gt;save();

?&gt;</pre>

Pretty simple right? We just saved that object to the database &#8211; And don&#8217;t worry. Arrays and sub-objects will be serialised and encoded before insert, and will be exactly the same as you saved them upon retrieval.

### Retrieval

This is where we need to use a context class. We could ideally query the DB directly, but the context will give us back the objects as the object we saved into the database. Easy right?

<pre class="lang:php decode:true">require_once("NWManagedObjectContext");
$context = new NWManagedObjectContext();

//Option 1. Query all objects
$events = $context-&gt;getEntitiesForStatement("Event");

//Option 2. Query using a WHERE statement 
// nb. You need to filter your own injections. 
$events = $context-&gt;getEntitiesForStatement("Event", "`place` = 'Somewhere'");

//Option 3. Query for a specific instance.
// (Objects are given a unique instance ID upon insertion/creation).
$events = $context-&gt;getEntityForInstance("Event", 22);</pre>

Now, if we try view the $events variable, we should see:

<pre class="lang:default decode:true">Array(
    [0] =&gt; EventModel Object {
        place-&gt;"Some place"
        name-&gt;"Some Name"
    }
)</pre>

Everything is retrieved as restored into an EventModel object! That&#8217;s easy! Need to make a change? Just change the variable:

### Modification

<pre class="lang:php decode:true">$events = $context-&gt;getEntityForInstance("Event", 22);
$event = $events[0]; //Grab the first result.
$event-&gt;place = "Some new place";
$event-&gt;save();</pre>

It&#8217;s as easy as that.

### Wrapping Up

By the end of next week, I plan on releasing my DBMS/Sqlite interface as a separate package, as this really is the feature here &#8211; the REST library really is nothing. I Hope to see this framework get adopted in the future by many others. I do plan expanding the framework to more DB systems, such as MySQL, however, SQLite is keeping it simple for me at the moment in my current project.