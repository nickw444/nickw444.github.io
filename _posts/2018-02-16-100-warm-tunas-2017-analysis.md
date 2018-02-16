---
title: 100 Warm Tunas 2017 Prediction Analysis
author: nickw
layout: post

categories:
  - Blog
  - Programming
---

<div class="pull-right hidden-xs" style="font-size:100px; padding: 5px 5px 5px 20px;">&#128293;&#128175;</div>
<div class="pull-right hidden-sm hidden-lg hidden-md" style="font-size:68px; padding: 5px 5px 5px 20px;">&#128293;&#128175;</div>


Over the space of 6 weeks, [100 Warm Tunas](https://100-warm-tunas.nickwhyte.com/2017/) collected a large sum of data and chugged away at it to make some predictions about what the Hottest 100 of 2017 would look like. Along the way we encountered [a bug](http://127.0.0.1:4000/post/2018/100-warm-tunas-2017-update/) in the collection process, however data was backfilled and showed that I had collected a sample size around the same as in [2016](https://100-warm-tunas.nickwhyte.com/2016/).

### Summary

- 100 Warm Tunas collected **7,216 entries** (7.3% less than 2016 🔻)
- 100 Warm Tunas tallied **67,085** votes across these entries (2.6% more than 2017 🔺). This is due to improvements in 100 Warm Tunas' counting and recognition process. 
- Triple J counted **2,386,133 votes**.
- Therefore, 100 Warm Tunas, collected a sample of **2.8%**. Not bad! (The same as in 2016).
- Warm Tunas predicted **8 out of the top 10 songs** (Same as 2016) (Ignoring order)
- Warm Tunas predicted **16 out of the top 20 songs** (3 less than in 2016, where 19 out of 20 were predicted) (Ignoring order).
- Warm Tunas predicted **83 out of the 100 songs** played in the countdown. (1 less than in 2016) (Ignoring order)

Overall, even though the sample size was reasonably consistent between 2016 and 2017, it is clear that the results collected in 2016 were more accurate.  

### Technical Analysis

The results this year definitely show a more accurate 1st place prediction (predicting HUMBLE. to win), as opposed to last year where the top two positions were placed out of order, however looking at the data, it looks as though all other aspects of the prediction stayed almost the same.

To start this analysis, lets take a look at the top 10 of the official countdown and match it up with their predicted places in Warm Tunas:


| Artist | Title | ABC Rank | Tunas Rank | Difference |
| --- | --- | --- | --- | --- |
| Kendrick Lamar | HUMBLE. | 1 | 1 | 0 |
| Gang Of Youths | Let Me Down Easy | 2 | 3 | 1 |
| Angus & Julia Stone | Chateau | 3 | 6 | 3 |
| Methyl Ethel | Ubu | 4 | 4 | 0 |
| Gang Of Youths | The Deepest Sighs, The Frankest Shadows | 5 | 2 | 3 |
| Lorde | Green Light | 6 | 8 | 2 |
| PNAU | Go Bang | 7 | 5 | 2 |
| Thundamentals | Sally {Ft. Mataya} | 8 | 10 | 2 |
| Vance Joy | Lay It On Me | 9 | 15 | 6 |
| Gang Of Youths | What Can I Do If The Fire Goes Out? | 10 | 13 | 3 |
| BROCKHAMPTON | SWEET | 11 | 7 | 4 |
| Peking Duk & AlunaGeorge | Fake Magic | 12 | 16 | 4 |
| Khalid | Young Dumb & Broke | 13 | 24 | 11 |
| Lorde | Homemade Dynamite | 14 | 30 | 16 |
| Vera Blue | Regular Touch | 15 | 11 | 4 |
| Jungle Giants, The  | Feel The Way I Do | 16 | 32 | 16 |
| Baker Boy | Marryuna {Ft. Yirrmal} | 17 | 12 | 5 |
| Ball Park Music | Exactly How You Are | 18 | 14 | 4 |
| Killers, The  | The Man | 19 | 19 | 0 |
| Peking Duk | Let You Down {Ft. Icona Pop} | 20 | 38 | 18 |

Lets pull apart this table and grab some statistics about how we did with our prediction:

|Predicted|Out Of Top N|Percentage|
| --- | --- | --- |
|8|10|80.0%|
|16|20|80.0%|
|22|30|73.3%|
|33|40|82.5%|
|42|50|84.0%|
|50|60|83.3%|
|62|70|88.6%|
|68|80|85.0%|
|78|90|86.7%|
|83|100|83.0%|

So from the above data, it's apparent that once again:

  - The average error for the top ten ranks was `2.2` positions (an increase from 2016's `1.9` positions)
  - Warm Tunas predicted **8 out of the top 10 songs**
  - Warm Tunas predicted **16 out of the top 20 songs**
  - Warm Tunas predicted **83 out of the 100 songs** played in the countdown.

That's not a bad result at all!

The average rank prediction error, grouped into divisions of 10 is provided below. It shows that it's difficult to predict where songs will place once you leave the top 50:

| ABC Position | Warm Tunas Avg Error |
| --- | --- |
| 1-10 | 1.9000 |
| 11-20 | 8.2000 |
| 21-30 | 14.3000 |
| 31-40 | 12.5000 |
| 41-50 | 15.2000 |
| 51-60 | 24.7000 |
| 61-70 | 18.2000 |
| 71-80 | 29.9000 |
| 81-90 | 34.1000 |
| 91-100 | 29.5000 |

To compare Warm Tuna's predictions vs actual rankings, a scatter plot has been provided below. We can see as we get
closer to rank 1, the 100 Warm Tunas prediction gets better and converges upon the actual rankings played out on the day.

<div class="embed-responsive embed-responsive-4by3">
    <iframe width="640" height="480" frameborder="0" scrolling="no" src="//plot.ly/~nickw444/3.embed"></iframe>
</div>

Fortunately this year around, 100 Warm Tunas was able to successfully predict the winner of the countdown. The reason this prediction was able to be made was because the sample collected clearly indicated *HUMBLE.* as an outlier. – an entire 5% higher than the next track, predicted to place 2nd.

Anyway, that's a wrap. See you later this year for 100 Warm Tunas 2018 edition!
