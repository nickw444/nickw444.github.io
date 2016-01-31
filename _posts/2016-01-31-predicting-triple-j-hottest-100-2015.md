---
title: Accurately Predicting Triple J's Hottest 100 of 2015
author: nickw
layout: post

categories:
  - Blog
  - Programming
---

<div class="pull-right hidden-xs" style="font-size:128px; padding: 5px 5px 5px 20px;">🔥💯</div>
<div class="pull-right hidden-sm hidden-lg hidden-md" style="font-size:68px; padding: 5px 5px 5px 20px;">🔥💯</div>

In 2014, a prediction was accurately made for the Hottest 100 of 2013. The results were posted on [warmest100.com.au](http://warmest100.com.au/).

The author of the prediction in 2014 managed to acquire accurate results because Triple J featured a social share button on their voting page, which posted your votes to your Facebook in text form. The author scraped results from public Facebook posts and aggregated all the votes. They managed to obtain `1.3%` (`1779` entries) of the expected total vote.

Consequently, voting for the Hottest 100 2014 and 2015 did not contain such a feature. Fortunately, voters still felt the need to share these results with their friends, and taking a screen shot or a photo of their screen and posting to social media was a concrete alternative. Using these images posted to Instagram, I was able to accurately predict the results of Triple J's Hottest 100 of 2015. 


### Some Cool Stats Before You Continue

- Triple J Tallied `2094350` Votes (`209435` Entries) for Hottest 100 2015
- I collected a sample size of `~2.5%` of all entries
    - I collected `7191` images collected initially
    - I categorised `5529` images as votes
    - `~4900` images contained the words "vote/votes/voting"
- My Top 3 Results were `100%` accurate

You'll probably find this article interesting, but if you're super eager, you can **[Skip To The Results](#final-results)**.


### Taking Advantage of Social Media
I decided to only target votes that were posted to Instagram, since a high majority of the pictures hashtagged with `#hottest100` were in fact votes, and there was a reasonably high volume of them, and most publicly accessible.

I required means to acquire all pictures that had been posted to Instagram. Instagram have an official API, however you are required to have your API app usage approved before it can interface with non-sandbox users. Additionally, Instagram impose a rate limit on non-approved apps, as well as approved apps. I did not have time to waste, and wanted results immediately, so I found an alternative.

Fortunately, Instagram exposes a non-public API through their website ajax loading when you browse to a hashtag. By imitating the web browser with a simple python script using the `requests` library I managed to download all images from the latest until a cut off date that I specified (the day voting opened).

After scraping the hashtag `#hottest100`, I expanded my search to `#hottest1002015` and `#triplejhottest100`.

### Processing Images
After downloading `7191` images from Instagram, I needed to find an accurate way to filter out the images that were not votes. 

I've had previous experience with using `PIL` in Python, so using `PIL`, I wrote a simple script to sort the photos into 2 categories; photos that appeared white-ish, and photos that were not. 

A good vote looked like this:

<div class="text-center"><a href="https://i.imgur.com/PNxGusD.jpg"><img style="width:100%; max-width:400px;" src="https://i.imgur.com/PNxGusD.jpg" alt="A Good Vote" /></a></div>

Unfortunately, not every image ended up in the right folder, and I ended up with both false negatives and false positives, however I wasn't too concerned about false positives, as my OCR processing step would exclude them. Instead, I was more concerned about false negatives. 

As the image processing and sorting continued, I manually moved false negatives to the positives folder. I calculated about `5%` of the non-matching photos were incorrectly classified, however this was due to them being pictures taken of computer screens, similar to the photo below:


<div class="text-center" style="margin-bottom:30px;"><a href="https://i.imgur.com/SObXzST.jpg"><img style="width:100%; max-width:400px;" src="https://i.imgur.com/SObXzST.jpg" alt="A Bad Vote" /></a></div>

#### Some image statistics:

- `7191` images collected initially
- `1662` images categorised as non-votes
- `5529` images categorised as votes
- `~4900` images contained the words `vote/votes/voting`

### Improving OCR Performance

After experimenting on raw photos from Instagram, I found that OCR accuracy was not very accurate. To remediate this, I utilised [Imagemagick](http://www.imagemagick.org/script/index.php) to flatten image definition to improve text results.

<div class="text-center"><a href="https://i.imgur.com/DbHuW2w.jpg"><img style="width:100%; max-width:400px;" src="https://i.imgur.com/DbHuW2w.jpg" alt="An improved image" /></a></div>

### Bringing in Tesseract (OCR)

After weeding out the junk, I still needed to turn these images into readable text. 

Using [Google's Tesseract library](https://github.com/tesseract-ocr/tesseract), I slowly processed all the images and extracted the text from them.

Unfortunately, due to the layout of the Hottest 100 voting website the two columns were broken up inconsistently over the results.

Some were processed as:

<div class="row">
    <div class="col-xs-12 col-sm-6">
        <div class="text-center"><a href="https://i.imgur.com/DbHuW2w.jpg"><img style="width:100%; max-width:400px;" src="https://i.imgur.com/DbHuW2w.jpg" alt="Line by Line processing" /></a></div>
    </div>
    <div class="col-xs-12 col-sm-6">
    <pre>...
Flight Facilities
Hayden James
Hermilude
Major Lazer
RUFUS
Weeknd, The
ZHU x Skrillex x THEY.
Jarryd James
Disclosure
Kendrick Lamar
Heart Attack {FL Owl Eyes)
(Radio Edit)
Something About You
The Buzz (Ft. Malaya/Young
Tapz}
Lean On (Ft. Mé/DJ Snake}
Innerbloom
...</pre>
    </div>
</div>

And others processed as:

<div class="row">
    <div class="col-xs-12 col-sm-6">
        <div class="text-center"><a href="https://i.imgur.com/k81RQVp.jpg"><img style="width:100%; max-width:400px;" src="https://i.imgur.com/k81RQVp.jpg" alt="Song/Artist line by line" /></a></div>
    </div>
    <div class="col-xs-12 col-sm-6">
    <pre>...
Lucky Luke 1 Day
Mosquito Coast Call My Name
Tn ka Right By You
Tuka L.D.T.E.
Half Moon Run Trust
Spring King City
Tame Impala Let It Happen
Saskwatch I‘ll Be Fine
Jungle Giants. T Kooky Eyes
he
...</pre>
    </div>
</div>


And others just did not process at all, due to resolution, colour, skewing, or simply because they were a photo of a computer screen:

<div class="row">
    <div class="col-xs-12 col-sm-6">
        <div class="text-center"><a href="https://i.imgur.com/dSAU6ph.jpg"><img style="width:100%; max-width:400px;" src="https://i.imgur.com/dSAU6ph.jpg" alt="Bad Image" /></a></div>
    </div>
    <div class="col-xs-12 col-sm-6">
    <pre>'VHotllne Bling
Regardless (Ft. Julia Stone)</pre>
    </div>
</div>

### Parsing the Results
I processed the results line by line, and call these "terms". These such terms could contain a single song title, a single artist, an artist name with song name, or just junk overhang from a previous line. Initially there were `31062` uncategorised terms.

I processed each term and aggregated number of results for each. This worked really well for songs with short names that were less prone to error, such as `Hoops`, however did not correctly capture terms where artist name and song name occurred on the same line, or where the OCR library interpreted a few characters incorrectly.


#### OCR Inaccuracy & Levenshtein

Even with photo enhancements, the OCR accuracy was somewhat subpar for some votes. Some `l`'s were interpreted as `t`'s, `i`'s as `l`'s, etc. Additionally, the longer the name of the song, the more prone to error it was.

{% highlight text %}
Fiesh Without Blood
L D R U Keepmo Score Fl Pavqe IV)
Yam: unpala The Les I Knew The Bauer
The Tlouble Wilh US
{% endhighlight %}

A technique that can be used to fix these spelling errors of single/multi character errors is the [Levenshtein algorithm](https://en.wikipedia.org/wiki/Levenshtein_distance) for edit distance. Using this algorithm, we can compare 2 strings and determine how many edits need to be made to make the strings equal each other. 

In order to perform this kind of matching, we needed an accurate list of songs that were released this year, along with a list of artists that released music this year. 

#### Using Spotify To Help

To acquire an accurate list of songs released this year, I used Spotify and crawled various playlists from 2015. These included Spotify Charts, Triple J Hitlist, and various other genre-alike playlists.

In the end I ended up with a songs list with `1781 songs`, and an artists list with `1229 artists`. After the Hottest 100 aired, I compared the results of the countdown to the songs found in my list, and only 6 songs that occurred in the hottest 100 were not in my "truth" list. 

During list gathering, I made sure to [convert all unicode characters](https://pypi.python.org/pypi/Unidecode) to their ASCII counterparts, so that characters with accents and similar would be matched correctly.

#### Continuing Processing

Now carrying reasonably accurate artists and songs lists we continue categorisation and processing. The processing algorithm worked in the following way:

1. Load all terms from every image's `.txt` OCR result. Every line is a "term".
2. Clean all the terms by turning them into lowercase and stripping whitespace.
3. Loop through each term:
    1. If term exists in our known songs list, move the term to the songs aggregation and count the votes.
    2. If term exists in our known artists list, move the term to the artists aggregation and count the votes.
    3. If couldn't find it in either of those:
        1. Loop through all artists in our artist known artist list.
            1. Check if the term starts with the current artist. If it does split it into artist and unknown term. Add the votes to the artist aggregation.
            2. If matched artist, check if the new unknown term exists in the songs list, if it does, add it to the songs aggregation. If not, add it back to the unknown. break loop.
        2. If it didn't have a prefixed artist, just add it back to the unknown terms.

At this stage, we have a reasonably accurate aggregation of results. We have not yet used Levenshtein string matching. We now have `27294` uncategorised terms, **down** from `31062` uncategorised terms. So far our results:

{% highlight text %}
==       Results       ==
1   Hoops                          998
2   King Kunta                     765
3   Lean On                        750
4   The Buzz                       646
5   Like Soda                      568
6   Never Be                       484
7   Let It Happen                  476
8   Magnets                        465
9   Do You Remember                409
10  Ocean Drive                    405
==    853 unique terms    ==

==       Top Unknown Terms       ==
1   Your Hottest 100 Votes:        2279
2   Your Votes                     2127
3   }                              320
4   Hottest Io                     248
5   V                              231
6   Throne                         222
7   Triple J?                      209
8   D] Snake                       203
9   The Less | Know The Better     203
10  Asap Rocky                     199
==    27294 unique terms    ==
{% endhighlight %}

However, we still haven't aggregated any votes that had spelling errors due to OCR inaccuracies. 

Employing the Levenshtein algorithm, we continue to process the unknown terms. I configure matching to allow lenience based on the length of the term - the maximum edits that were allowed was `2/5 * length of term`. The process continues:


4. For all unknown terms:
    1. Check `term length > 3`. Break if `<= 3`. Can't match a short string.
    2. Match Songs:
        1. Loop through all songs in known songs list:
            1. Compare current song to current term. Get edit distance.
            2. If edit `distance == 1`, move votes for this term to the guessed song in our songs aggregation, then continue to the next term.
            3. Add distance to a dictionary of value/distances
        2. Using our value/distances dictionary, find the closest match that satisfies our `2/5 * len(term)` rule. If it matches, move the votes for this term to the guessed song in our songs aggregation, then continue to the next term.
    3. Match Artists using the same method.


Some of the results of string matching, providing some reasonably accurate re-matching.

{% highlight text %}
[A] weekncl, the -> weeknd, the with distance 2
[A] mm m. -> ms mr with distance 2
[S] km; kunta -> king kunta with distance 3
[A] macklelllore ex ryan lewis -> macklemore & ryan lewis with distance 5
[A] eulsch duke) -> deutsch duke with distance 3
[A] bloc pany -> bloc party with distance 2
[S] nommg's forevev -> nothing's forever with distance 5
[S] t he hllns -> the hills with distance 3
[S] emocons -> emoticons with distance 2
[S] better off without you -> better with you with distance 7
[S] - the less | know the better -> the less i know the better with distance 3
[S] vancejoy fire and the fiood -> fire and the flood with distance 10
[S] too much me togglhu -> too much time together with distance 6
[A] of mons-us and m. -> of monsters and men with distance 5
[S] gmek tragedy -> greek tragedy with distance 2
[S] marks to prove 1t -> marks to prove it with distance 1
[A] rlighx facilities -> flight facilities with distance 2
[A] gang 01 youth: -> gang of youths with distance 3
[A] fka lwlgs -> fka twigs with distance 2
[S] hoine bling -> hotline bling with distance 2
{% endhighlight %}

After performing this additional processing, I ended up with `18509` uncategorised terms, **down** from `27294` uncategorised terms. 

That means we were able to successfully categorize `8785` terms via the Levenshtein distance algorithm! 

{% highlight text %}
==       Results       ==
1   Hoops                          1011
2   King Kunta                     1008
3   Lean On                        793
4   The Buzz                       667
5   Let It Happen                  637
6   Like Soda                      617
7   The Less I Know The Better     602
8   Magnets                        521
9   Never Be                       520
10  The Trouble With Us            501
==    1143 unique terms    ==

==       Top Unknown Terms       ==
1   Your Hottest 100 Votes:        2279
2   }                              320
3   Hottest Io                     248
4   V                              231
5   Throne                         222
6   Triple J?                      209
7   Thanks For Voting!             174
8   Tapz)                          170
9   Suddenly                       155
10  Once                           140
==    18509 unique terms    ==
{% endhighlight %}

Quite an improvement, however still not great. Some of the terms there weren't able to be categorised which caught my attention included:

{% highlight text %}
9   Suddenly                       155
16  Big Jet Plane                  123
17  Heart Attack                   120
18  True Friends                   114
23  Rumour Mill                    107
35  The Less | Know The            76
63  & Chet Faker The Trouble With Us 46
{% endhighlight %}

Paying special attention to `The Less | Know The`, if I were to add it's sum to our results, it would have placed 4th, however, the results we already have look reasonably accurate.

### Final Results

{% highlight text %}
==       Results       ==
1   Hoops                          1011
2   King Kunta                     1008
3   Lean On                        793
4   The Buzz                       667
5   Let It Happen                  637
6   Like Soda                      617
7   The Less I Know The Better     602
8   Magnets                        521
9   Never Be                       520
10  The Trouble With Us            501
11  Do You Remember                480
12  Ocean Drive                    463
13  Can'T Feel My Face             457
14  You Were Right                 444
15  Middle                         423
16  Magnolia                       381
17  Young                          380
18  The Hills                      369
19  Hotline Bling                  356
20  Keeping Score                  321
21  Embracing Me                   319
22  Mountain At My Gates           318
23  Loud Places                    300
24  Run                            298
25  I Know There'S Gonna Be        287
26  Some Minds                     287
27  Say My Name                    283
28  Fire And The Flood             280
29  Visions                        275
30  Greek Tragedy                  274
31  Long Loud Hours                272
32  Shine On                       254
33  Asleep In The Machine          249
34  Leave A Trace                  242
35  Like An Animal                 235
36  Something About You            224
37  Dynamite                       224
38  All My Friends                 218
39  Deception Bay                  217
40  Downtown                       210
41  Ghost                          200
42  Son                            196
43  Hold Me Down                   196
44  No One                         196
45  Kamikaze                       196
46  Puppet Theatre                 192
47  Vice Grip                      191
48  Forces                         185
49  Better                         185
50  Counting Sheep                 184
==    1143 unique terms    ==
{% endhighlight %}

Some Notes

 - `Run` appeared so high on the leaderboard because both Seth Sentry and Alison Wonderland released similar tracks titled RUN/Run. Since I lowercased all comparisons and removed special characters, these votes merged.

### Improving the Analysis

After reviewing the method used for analysis, I have identified a few places for improvement that could possibly improve the results. 

1. Improved Levenshtein Algorithm. The Levenshtein algorithm is great for calculating edit distance, however I could not weigh edits of similar characters such as t's, i's and l's less, thus improving matching due to OCR inaccuracies. I expect that string matching could have been significantly improved if this was explored.
2. Songs that had long titles, such as `The Less I Know The Better` generally were split across multiple lines. This caused their aggregation to not sum correctly. It would be good if I could determine if a song was split across two lines.
3. Songs that were in the format of `artist song` and were spelt incorrectly were most likely not picked up by string matching, as we only matched against songs and artists individually. In order to improve matching for this, an additional list for joined songs/artists could have been used and compared against for remaining terms.

### Some Cool Stats

- Triple J Tallied `2094350` Votes (`209435` Entries)
- I collected a sample size of `~2.5%` of all entries
    - I collected `7191` images collected initially
    - I categorised `5529` images as votes
    - `~4900` images contained the words "vote/votes/voting"
- My Top 3 Results were `100%` accurate

