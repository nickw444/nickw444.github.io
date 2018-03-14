---
title: 100 Warm Tunas 2016 Prediction Analysis
author: nickw
layout: post

categories:
  - Blog
  - Programming
---

It's been a long time since the Hottest 100 of 2016 was aired. Unfortunately, I never really got around to publishing some analysis I performed on the [prediction results](https://100-warm-tunas.nickwhyte.com/2016/). Fortunately, I managed to find some time recently!

Looking from afar, the results don't look _fantastic_ (when you compare them to [my results from 2015](https://nickwhyte.com/post/2016/predicting-triple-j-hottest-100-2015/) at least). The prediction unfortunately predicted the top two places out of order, however did manage to predict the third place correctly.

Lets take a look at the Top 10 of Triple J's list and match it up with 100 Warm Tunas:

{% include linked-img.html src="/static/posts/2017-12-17-100-warm-tunas-2016-analysis/triplej-rank-vs-tuna-rank.png" alt="Triple J Rank vs Tuna Rank" %}

Looking at this we see most predictions we can find some learnings:

  - The average error for the top ten rank was `1.9` rank positions.
  - If 100 Warm Tunas ignored rank and simply guessed the top ten, it would have predicted **8 of the top 10 songs**.
  - If 100 Warm Tunas ignored rank and simply guessed the top 3 songs to win, it would have predicted **all 3 songs**. _Woo!_

Lets dive into a chart that shows error for all ranks:

{% include linked-img.html src="/static/posts/2017-12-17-100-warm-tunas-2016-analysis/rank-error.png" alt="Rank error per position" %}

From this chart, we can deduce that the further away from position 1 we become, the higher the error. This information alone isn't very useful. We can get a better understanding of error by finding the average for each ranking group:

{% include linked-img.html src="/static/posts/2017-12-17-100-warm-tunas-2016-analysis/rank-error-avg.png" alt="Average Rank error per group" %}

As we get closer to rank 1, the results become more and more accurate, however they are not perfect. This is more obvious if we use a scatter plot to compare Triple J ranks against Warm Tunas predictions:

 {% include linked-img.html src="/static/posts/2017-12-17-100-warm-tunas-2016-analysis/triplej-vs-tunas-scatter.png" alt="Triple J vs Tunas Scatter Plot" %}

It's clear now that as we get closer to rank 1, the 100 Warm Tunas prediction gets better and converges upon the actual rankings played out on the day. However, unfortunately this year the difference between rank 1 and rank 2 was way too close to call - just `0.67%` of voting volume was separating the two. A difference that was not enough to provide an accurate prediction of the winner.

Overall, whilst 100 Warm Tunas 2016 did get the two top positions out of order, it's understandable as to why this happened. Hopefully [this year](https://100-warm-tunas.nickwhyte.com/2017/) there is a greater difference between ranks, giving further ability to predict the winner in position #1.
