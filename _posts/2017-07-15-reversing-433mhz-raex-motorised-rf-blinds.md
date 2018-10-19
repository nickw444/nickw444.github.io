---
title: Reverse Engineering a 433MHz Motorised Blind RF Protocol
author: nickw
layout: post

categories:
  - Programming
  - Electronics
---

I've been doing a fair bit of DIY home automation hacking lately across many different devices - mostly interested in adding DIY homekit integrations. A couple of months ago, my dad purchased a bulk order of [RAEX 433MHz RF motorised blinds](http://www.raexmotor.com/index.php?m=content&c=index&a=show&catid=9&id=23) to install around the house, replacing our existing manual roller blinds.

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/IMG_8745_crop.jpg" alt="RAEX Motorised Blind" %}

<small>Note: If you are based in Australia, you can purchase these in bulk or individually via [www.raexaustralia.com](https://www.raexaustralia.com?utm_source=nickwhyte.com&utm_medium=post&utm_content=433mhz-reversing) (Full disclosure – my father runs the site).</small>

The blinds are a fantastic addition to the house, and allow me to be super lazy opening/closing my windows, however in order to control them you need to purchase the RAEX brand remotes. RAEX manufacture many different types of remotes, of which, I have access to two of the types, depicted below:

<div style="display: flex; align-items: center; margin:20px 0">
  <div style="text-align: center;">
    <a href="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/remote_r.jpg"><img width="70%" src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/remote_r.jpg" alt="R Type Remote" /></a>
    <p><code>R</code> Type Remote (YRL2016)</p>
  </div>
  <div style="text-align: center;">
    <a href="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/remote_x.jpg"><img width="70%" src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/remote_x.jpg" alt="X Type Remote" /></a>
    <p><code>X</code> Type Remote (YR3144)</p>
  </div>
</div>

Having a remote in every room of the house isn't feasible, since many channels would be unused on these remotes and thus a waste of $$$ purchasing all the remotes. Instead, multiple rooms are programmed onto the same remote. Unfortunately due to this, remotes are highly contended for.

An alternate solution to using the RAEX remotes is to use a piece of hardware called the [RM Pro](http://www.ibroadlink.com/rm/). This allows you to control the remotes via your smartphone using their app

<div style="display: flex; align-items: center; margin: 20px 0">
  <div style="text-align: center;">
    <a href="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/rmpro_home.jpg"><img width="70%" src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/rmpro_home.jpg" alt="RM Pro Home Screen" /></a>
  </div>
  <div style="text-align: center;">
    <a href="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/rmpro_blind.jpg"><img width="70%" src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/rmpro_blind.jpg" alt="RM Pro Blind Control Screen" /></a>
  </div>
</div>

The app is slow, buggy and for me, doesn't fit well into the home-automation ecosystem. I want my roller blinds to be accessible via Apple Homekit.

In order to control these blinds, I knew I'd need to either:

  1. Reverse engineer how the RM Pro App communicated with the RM Pro and piggy-back onto this
  2. Reverse engineer the RF protocol the remotes used to communicate with the blinds.


I attempted option 1 for a little while, but ruled it out as I was unable to intercept the traffic used to communicate between the iPhone and the hub. Therefore, I began my adventure to reverse engineer the RF protocol.

I purchased a 433MHz transmitter/receiver pair for Arduino on [Ebay](http://www.ebay.com.au/itm/433Mhz-RF-transmitter-receiver-link-kit-for-Arduino-Free-Postage-/302377132217?). In case that link stops working, try searching Ebay for _433Mhz RF transmitter receiver link kit for Arduino_.

<div class="text-center">
  <a href="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/rf-transmitter-receiver.jpg">
      <img src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/rf-transmitter-receiver.jpg" width="50%" alt="RF Transmitter / Receiver" />
  </a>
</div>

### Initial Research

A handful of Google searches didn't yield many results for finding a technical specification of the protocol RAEX were using.

- I could not find any technical specification of the protocol via FCC or patent lookup
- Emailed RM Pro to obtain technical specification; they did not understand my English.
- Emailed RAEX to obtain technical specification; they would not release without confidentiality agreement.
- I did find that [RFXTRX](http://www.rfxcom.com/) was able to control the blind via their BlindsT4 mode, which appears to also work for _Outlook Motion Blinds_.
- After opening one of the remotes and identifying the micro-controllers in use, I was unable to find any documentation explaining a generic RF encoding scheme being used.
- It _may_ have been possible to reverse engineer the firmware on a remote by taking an I2C [dump of the ROM chip](/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/remote-pcb.jpg). It seems similar remotes [allow dumping at any point after boot](http://travisgoodspeed.blogspot.co.uk/2010/07/reversing-rf-clicker.html)

### Capturing the data

Once my package had arrived I hooked up the receiver to an Arduino and began searching for an Arduino sketch that could capture the data being transmitted. I tried [many things](https://www.liwen.id.au/arduino-rf-codes/) that all failed, however eventually [found one](https://github.com/nickw444/homekit/blob/master/blindkit/sketches/receive_manchester.ino) that appeared to capture the data.

Once I captured what I deemed to be enough data, I began [analysing it](https://github.com/nickw444/homekit/blob/master/blindkit/research/initial-captures-analysis.txt). It was really difficult to make any sense of this data, and I didn't even know if what had been captured was correct.

I did [some](http://mightydevices.com/?p=300) [further](http://rayshobby.net/?p=3381) [reading](http://rayshobby.net/interface-with-remote-power-sockets-final-version/) and read a few RF reverse engineering write-ups. A lot of them experimented with the idea of using Audacity to capture the signal via the receiver plugged into the microphone port of the computer. I thought, why not, and began working on this.

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/capturing-rig.jpg" alt="The RF capturing setup" %}

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/audacity1.png" alt="Audacity capture" %}

This captures _a lot_ of data. I captured 4 different `R` type remotes, along with 2 different `X` type remotes, and to make things even more fun, 8 different devices pairings from the Broadlink RM Pro (`B` type).

From this, I was able to determine a few things

  1. The transmissions did not have a rolling code. Therefore, I could simply replay captured signals and make the blind do the exact same thing each time. This would be the worst-case scenario if I could not reverse engineer the protocol.
  2. The transmissions were repeated at least 3 times (changed depending on the remote type being used)

Zooming into the waveform, we can see the different parts of a captured transmission. This example below is the capture of Remote 1, Channel 1, for the **pairing** action:

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/r1c1pairing1.png" alt="R1, CH1 PAIR capture" %}

Zooming in:

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/r1c1pairing2.png" alt="Zoomed R1, CH1 PAIR capture" %}

In the zoomed image you can see that the transmission begins with a oscillating `0101` AGC pattern, followed by a further double width preamble pattern, followed by a longer header pattern, and then by data.

This preamble, header and data is repeated 3 times for R type remotes (The AGC pattern is only sent once at the beginning of transmission). This can be seen in the first image.

Looking at this data won't be too useful. I need a way to turn it digital and analyse the bits and determine some patterns between different remotes, channels and actions.

### Decoding the waveform.

We need to determine how the waveform is encoded. It's very common for these kinds of hardware applications to use one of the following:

  - [Manchester Encoding](http://www.erg.abdn.ac.uk/users/gorry/course/phy-pages/man.html),
  - [Tri-State/Tri-bit Encoding](http://tinkerman.cat/decoding-433mhz-rf-data-from-wireless-switches/), [Additional info](http://tinkerman.cat/decoding-433mhz-rf-data-from-wireless-switches-the-data/)
  - PWM Encoding
  - Raw? high long = `11`, high short = `1`, low long = `00`, low short = `0`?

By doing some [research](https://www.youtube.com/watch?v=i_TLLACZuRk), I was able to determine that the encoding used was most likely manchester encoding. Let's keep this in mind for later.


### Digitising the data

I began processing the data as the raw scheme outlined above (even though I believed it was manchester). The reason for this is that if it happened to not be manchester, I could try decode it again with another scheme. (Also writing out raw by hand was easier than doing manchester decoding in my head).

I wrote out each capture into a [Google Sheets spreadsheet](https://docs.google.com/spreadsheets/d/1oP6-OY93fNaIKRSyX8hcdRp30glidLyhRHn7Lt-4DNo/edit?usp=sharing). It took about 5 minutes to write out each action for each channel, and there were 6 channels per remote. I began to think this would take a while to actually get enough data to analyse. (Considering I had 160 captures to digitise)

I stopped once I collected all actions from 8 different channels across 2 remotes. This gave me 32 captures to play with. From this much data, I was able to infer a few things about the raw bits:

  - Some bits changed per channel
  - Some bits changed per remote.
  - Some bits changed seemingly randomly for each channel/remote/action combination.
      - Could this be some sort of checksum?

I still needed more data, but I had way too many captures to decode by hand. In order to get anywhere with this, I needed a script to process WAV files I captured via Audacity. I [wrote a script](https://github.com/nickw444/homekit/blob/master/blindkit/rf-process/process_waveform.py) that detected headers and extracted data as its raw encoding equivalent (as I had been doing by hand). This script produced output in JSON so I could add additional metadata and cross-check the captures with the waveform:

{% highlight json %}
[
  {
    "filename": "/Users/nickw/Dropbox/RF_Blinds/Export_Audio2/tracks2/R1_CH1.wav",
    "captures": [
      {
        "data": "01100101100110011001100101101001011010010110011010011010101010101010101010011001101010101010101010101010101",
        "header_pos": 15751,
        "preamble_pos": 15071
      },
      {
        "data": "01100101100110011001100101101001011010010110011010100110101010101001101010011001101010101010101010101010101",
        "header_pos": 46307,
        "preamble_pos": 45628
      },
      {
        "data": "01100101100110011001100101101001011010010110011010010110101010101010011010011001101010101010101010101010101",
        "header_pos": 73514,
        "preamble_pos": 72836
      },
      {
        "data": "01100101100110011001100101101001011010010110011010101010101010100101010101101001011010101010101010101010101",
        "header_pos": 103575,
        "preamble_pos": 102895
      }
    ]
  }
]
{% endhighlight %}

Once verified, I tabulated this data and inserted it into my spreadsheet for further processing. Unfortunately there was too many bits per capture to keep myself sane:

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-raw-captures.png" alt="Raw captures inside a spreadsheet" %}

I decided it would be best if I decoded this as manchester. To do this, I [wrote a script](https://github.com/nickw444/homekit/blob/master/blindkit/rf-process/tabulate.py) that processes the raw capture data into manchester (or other encoding types). Migrating this data into my spreadsheet, it begins to make a lot more sense.

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-manchester-1.png" alt="Manchester captures inside a spreadsheet" %}

Looking at this data we can immediately see some relationship between the bits and their purpose:

  - 6 bits for channel (`C`)
  - 2 bits for action (`A`)
  - 6 bits for some checksum, appears to be a function of action and channel. `F(A, C)`
      - Changes when action changes
      - Changes when channel changes.
      - Cannot be certain it changes across remotes, since no channels are equal.
  - 1 bit appears to be a function of Action `F(A)`
  - 1 bit appears to be a function of `F(A)`, thus, `G(F(A))`. It changes depending on `F(A)`'s value, sometimes 1-1 mapping, sometimes inverse mapping.

After some further investigation, I determined that for the same remote and channel, for each different action, the `F(A, C)` increased by 1. (if you consider the bits to be big-endian.).

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-manchester-2.png" alt="Encoded value increasing per different action" %}

Looking a bit more into this, I also determined that for adjacent channels, the bits associated with `C` (Channel) count upwards/backwards (X type remotes count upwards, R type remotes count backward). Additionally `F(C)` also increases/decreases together. Pay attention to the `C` column.

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-manchester-3.png" alt="Encoded value increasing with adjacent channels" %}

From this, I can confirm a relationship between `F(A, C)` and `C`, such that `F(A, C) = F(PAIR, C0) == F(PAIR, C1) ± 1`. After this discovery, I also determine that there's another mathematical relationship between `F(A, C)` and `A` (Action).


### Making More Data

From the information we've now gathered, it seems plausible that we can create new remotes by changing 6 bits of channel data, and mutating the checksum accordingly, following the mathematical relationship we found above. This means we can generate 64 channels from a single seed channel. This many channels is enough to control all the blinds in the house, however I really wanted to fully decode the checksum field and in turn, be able to generate an (almost) infinite amount of remotes.

I wrote a [tool](https://github.com/nickw444/homekit/blob/2cac1db865a8a74d784d8d8f56c7e17caa654d96/blindkit/remote-gen/generate_cmd.go) to output all channels for a seed capture:

{% highlight text %}
./remote-gen generate 01000110110100100001010110111111111010101
...
{% endhighlight %}

My reasoning behind generating more data was that maybe we could determine how the checksum is formed if we can view different remotes on the same channel. I.e. `R0CH0`, `R1CH0`, `X1CH0`, etc...

Essentially what I wanted to do was solve the following equation's function `G`:

{% highlight text %}
F(ACTION_PAIR, CH0) == G(F(ACTION_PAIR, CH0))
{% endhighlight %}

However, looking at all Channel 0's PAIR captures, the checksum still appeared to be totally jumbled/random:

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-jumbled-checksum.png" alt="Identical channels / action jumbled checksums" %}

Whilst looking at this data, however, another pattern stands out. `G(F(A))` sits an entire byte offset (8 bits) away from `F(A)`. Additionally the first 2 bits of `F(A, C)` sit at the byte boundary and also align with `A` (Action). As Action increases, so does `F(A, C)`. Lets line up all the bits at their byte boundaries and see what prevails:

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-byte-boundaries-1.png" alt="Identified Boundaries" caption="Colours denoting byte boundaries" %}

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-byte-boundaries-2.png" alt="Aligned byte boundaries" caption="Aligned boundaries" %}

From here, we need to determine some function that produces the known checksum based on the first 4 bytes. Initially I try to do XOR across the bytes:

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-checksum-xor.png" alt="Attempt to find checksum function via XOR" %}

Not so successful. The output appears random and XOR'ing the output with the checksum does not produce a constant key. Therefore, I deduce the checksum isn't produced via XOR. How about mathematical addition? We've already seen some addition/subtraction relationship above.

  {% include linked-img.html src="/static/posts/2017-07-15-reversing-433mhz-raex-motorised-rf-blinds/findings-checksum-addition.png" alt="Attempt to find checksum function via addition" %}

This appeared to be more promising - there was a constant difference between channels for identical type remotes. Could this constant be different across different type remotes because my generation program had a bug? Were we not wrapping the correct number of bits or using the wrong byte boundaries when mutating the channel or checksum?

_It turns out that this was the reason_ 😑.


### Solving the Checksum

Looking at the original captures, and performing the same modulo additions, we determine the checksum is computed by adding the leading 4 bytes and adding 3. I can't determine why a `3` is used here, other than RAEX wanting to make decoding their checksum more difficult or to ensure a correct transmission pattern.

I refactored my application to handle the boundaries we had just identified:

{% highlight go %}
type RemoteCode struct {
    LeadingBit uint // Single bit
    Channel    uint8
    Remote     uint16
    Action     uint8
    Checksum   uint8
}
{% endhighlight %}

Looking at the data like this began to make more sense. It turns out that `F(A)` wasn't a function of `A` (Action), it was actually part of the action data being transmitted:

{% highlight go %}
type BlindAction struct {
    Name  string
    Value uint8
}

var validActions = []BlindAction{
    BlindAction{Value: 127, Name: "PAIR"},
    BlindAction{Value: 252, Name: "DOWN"},
    BlindAction{Value: 253, Name: "STOP"},
    BlindAction{Value: 254, Name: "UP"},
}
{% endhighlight %}

Additionally, the fact there is a split between channel and remote probably isn't necessary. Instead this could just be an arbitrary 24 bit integer, however it is easier to work with splitting it up as an 8 bit int and a 16 bit int. Based on this, I can deduce that the protocol has room for 2^24 remotes (~16.7 million)! That's a lot of blinds!

I formally write out the checksum function:

{% highlight go %}
func (r *RemoteCode) GuessChecksum() uint8 {
    return r.Channel + r.Remote.GetHigh() + r.Remote.GetLow() + r.Action.Value + 3
}
{% endhighlight %}


### Additional Tooling

My [`remote-gen`](https://github.com/nickw444/homekit/tree/master/blindkit/remote-gen) program was good for the purpose of generating codes using a seed remote (although, incorrect due to wrapping issues), however it now needed some additional functionality.

I needed a way to extract information from the captures and verify that all their checksums align with our rule-set for generating checksums. I wrote an info command:


{% highlight text %}
./remote-gen info 00010001110001001101010111011111101010100 --validate
Channel:    196
Remote:     54673
Action:     STOP
Checksum:          42
Guessed Checksum:  42
{% endhighlight %}

Running with `--validate` exits with an error if the guessed checksum != checksum. Running this across all of our captures proved that our checksum function was correct.


Another piece of functionality the tool needed was the ability to generate arbitrary codes to create our own _remotes_:

{% highlight text %}
./remote-gen create --channel=196 --remote=54654 --verbose
00010001101111110101010111111111010011001    Action: PAIR
00010001101111110101010110011111101101000    Action: DOWN
00010001101111110101010111011111111101000    Action: STOP
00010001101111110101010110111111100011000    Action: UP
{% endhighlight %}

I now can generate any remote I deem necessary using this tool.

### Wrapping Up

There you have it, that's how I reverse engineered an unknown protocol. I plan to follow up this post with some additional home-automation oriented blog posts in the future.

From here I'm going to need to build my transmitter to transmit my new, generated codes and build an interface into homekit for this via my [homebridge](https://github.com/nickw444/homekit/tree/master/bridges/mainbridge) program.

You can view all the work related to this project in the [nickw444/homekit/blindkit](https://github.com/nickw444/homekit/tree/master/blindkit) repo.

As mentioned above, if you are based in Australia, you can purchase these blinds and associated accessories in bulk or individually via [www.raexaustralia.com](https://www.raexaustralia.com?utm_source=nickwhyte.com&utm_medium=post&utm_content=433mhz-reversing) (Full disclosure – my father runs the site)
