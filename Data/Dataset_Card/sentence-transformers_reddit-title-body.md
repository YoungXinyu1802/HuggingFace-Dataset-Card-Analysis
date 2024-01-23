# Reddit (Title, Body)-Pairs

This dataset contains jsonl-Files about (title, body) pairs from Reddit. Each line is a JSON object of the following format:
```
{'title': 'The title of a thread', 'body': 'The longer body of the thread', 'subreddit': 'subreddit_name'}
```

The 2021 file contains submissions up until including 2021-06. Entries in the respective files are shuffled on a monthly basis.

The data has been filtered for:
- Remove threads with an upvote_ratio < 0.5
- Only include threads with a title more than 25 characters and bodies with `len(title)+25 < len(body) < 4096`
- Only keep threads with at least 3 comments or at least 3 upvotes.



## Overview

| File | Lines |
| --- | :---: |
| reddit_title_text_2010.jsonl.gz | 431,782
| reddit_title_text_2011.jsonl.gz | 1,673,264
| reddit_title_text_2012.jsonl.gz | 3,727,526
| reddit_title_text_2013.jsonl.gz | 5,713,956
| reddit_title_text_2014.jsonl.gz | 8,538,976
| reddit_title_text_2015.jsonl.gz | 11,064,453
| reddit_title_text_2016.jsonl.gz | 12,224,789
| reddit_title_text_2017.jsonl.gz | 13,558,139
| reddit_title_text_2018.jsonl.gz | 15,552,110
| reddit_title_text_2019.jsonl.gz | 19,224,970
| reddit_title_text_2020.jsonl.gz | 23,030,988
| reddit_title_text_2021.jsonl.gz | 12,704,958


Note: The data comes from [Pushshift](https://files.pushshift.io/reddit/). Please have a look at the respective license of Reddit and Pushshift before using the data.

Be aware that this dataset is not filtered for biases, hate-speech, spam, racial slurm etc. It depicts the content as it is posted on Reddit.