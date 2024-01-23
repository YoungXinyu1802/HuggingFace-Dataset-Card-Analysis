---
tags:
- reddit
language: en
---

# Dataset Card for reddit_one_ups_seq2seq_2014

## Dataset Description

- **Homepage:** https://github.com/Georeactor/reddit-one-ups

### Dataset Summary

Reddit 'one-ups' or 'clapbacks' - replies which scored higher than the original comments.

This dataset chose freeform replies, which did not follow repetitive meme replies. The IAmA subreddit was excluded to avoid an issue where their answers frequently score higher than questions.

For commentary on predictions with a previous version of the dataset, see https://blog.goodaudience.com/can-deepclapback-learn-when-to-lol-e4a2092a8f2c

For meme / text-classification version of this dataset, see https://huggingface.co/datasets/georeactor/reddit_one_ups_2014

Replies were selected from PushShift's archive of posts from 2014.

### Supported Tasks

seq2seq writing of replies to Reddit comments

### Languages

Primarily English - includes some emoticons such as ┬─┬ノ(ಠ_ಠノ)

## Dataset Structure

### Data Instances

19,992 rows

### Data Fields

- id: the Reddit alphanumeric ID for the reply
- body: the content of the original reply
- score: the net vote score of the original reply
- parent_id: the Reddit alphanumeric ID for the parent
- author: the Reddit username of the reply
- subreddit: the Reddit community where the discussion occurred
- parent_score: the net vote score of the parent comment
- tstamp: the timestamp of the reply
- parent_body: the content of the original parent

## Dataset Creation

### Source Data

Reddit comments collected through PushShift.io archives for 2014.

#### Initial Data Collection and Normalization

- Removed deleted or empty comments.
- Selected only replies which scored 1.5x higher than a parent comment, where both have a positive score.
- Found top/repeating phrases common to these one-ups/clapback comments; selected only replies which DID NOT have these phrases.
- Selected the top-scored ~1,667 replies from each month in 2014, avoiding /r/IAmA.
- Made rows in PostgreSQL and output as CSV.

## Considerations for Using the Data

Comments and responses in the Reddit archives and output datasets all include NSFW and otherwise toxic language and links!

You can use the subreddit and score columns to filter, and subreddit and timestamps to improve predictions of reply content.

Reddit comments are properties of Reddit and comment owners using their Terms of Service.