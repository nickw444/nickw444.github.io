---
title: CTF Season
author: nickw
layout: post

categories:
  - Blog
  - Programming
---

It's currently CTF season, and as a member of 
[UNSW's security society](http://unswsecurity.com/), that means I get to play!

We began the season with [CSAW CTF](https://ctf.isis.poly.edu/scoreboard), 
where we (team K17) placed 1st in Australia/10th overall. 

I did not participate in this CTF as much as I would have liked to, since I was
already pre-occupied with the CSESoc Hackathon, however, I did lend a hand 
with Web 500 - A fake dating website where the aim was to recover Donald 
Trump's TOTP key as well as his password. I managed to solve have of the 
challenge by finding an SQL injectable endpoint in a CSP reporting endpoint, 
where I dumped a password hash and other info about the account. We recovered 
the password hash using a dictionary attack, However the full solution required 
dumping of source code to determine how the TOTP key was generated, which 
another member of the team did, and thus solved the challenge.

The following weekend, Trend Micro CTF was running, which K17 also played in. We 
ended up coming in at 1st place globally out of 359 teams - A fantastic effort. 
Once again, I only participated lightly in this CTF. I worked on an Android APK
reversing challenge, which I solved over the space of 2 hours. I will post a 
write up of this challenge soon! 

Additionally, I was selected to play in CySCA (Australia's Cyber Security 
Challenge) for UNSW3. UNSW entered 5 teams. My team (of 4) placed 3rd overall 
in the competition, but the entire UNSW effort was also amazing:

- 1st: UNSW1
- 2nd: UNSW2
- 3rd: UNSW3
- 4th: UNSW4
- 29th: UNSW5

I'll be posting my write ups over the next few weeks, explaining my solutions
to the problems that I solved for these CTF's!
