---
license: afl-3.0
---

This data set contains StockTwits posts from 01.11.2021 to 30.06.2022 for Bitcoin (BTC.X), Ethereum (ETH.X) and Shiba Inu (SHIB.X).

The full set contains 124,503 posts, including 72,247 bullish, 38,249 neutral and 14,007 bearish posts.

The training set ranges from 01.11.2021 to 30.04.2022, consists of 91,758 observations, including 57,932 bullish, 26,516 neutral, and 7310 bearish posts.

The validation set ranges from 01.05.2022 to 15.06.2022 and contains 4084 bearish, 7534 neutral, and 9143 bullish posts, amounting to 20,761 examples.
The test set ranges from 16.06.2022 to 30.06.2022 and consists of 5172 bullish, 4199 neutral, and 2613 bearish posts, having 11,984 observations in total.

The validation and test sets contain all StockTwits posts, with at least one emoji, from their respective periods, while the training set is further limited by only including posts that have possibly influential bullish or bearish emojis.

The training SVM dataset contains balanced samples used for training an SVM sentiment classifier. 
The bearish sets have 20K observations per class (pos is bearish, while neg is not bearish, so bullish and neutral). The bullish sets have 40K observations per class (pos is bullish, while neg is not bullish, so bearish and neutral).
