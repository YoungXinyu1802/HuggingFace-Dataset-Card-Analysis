---
task_categories:
- text-classification
tags:
- reddit
language: en
---

# Dataset Card for reddit_one_ups_2014

## Dataset Description

- **Homepage:** https://github.com/Georeactor/reddit-one-ups

### Dataset Summary

Reddit 'one-ups' or 'clapbacks' - replies which scored higher than the original comments. This task makes one-ups easier by focusing on a set of common, often meme-like replies (e.g. 'yes', 'nope', '(͡°͜ʖ͡°)').

For commentary on predictions with a previous version of the dataset, see https://blog.goodaudience.com/can-deepclapback-learn-when-to-lol-e4a2092a8f2c

For unique / non-meme seq2seq version of this dataset, see https://huggingface.co/datasets/georeactor/reddit_one_ups_seq2seq_2014

Replies were selected from PushShift's archive of posts from 2014.

### Supported Tasks

Text classification task: finding the common reply (out of ~37) to match the parent comment text.

Text prediction task: estimating the vote score, or parent:reply ratio, of a meme response, as a measure of relevancy/cleverness of reply.

### Languages

Primarily English - includes some emoticons such as ┬─┬ノ(ಠ_ಠノ)

## Dataset Structure

### Data Instances

29,375 rows

### Data Fields

- id: the Reddit alphanumeric ID for the reply
- body: the content of the original reply
- score: the net vote score of the original reply
- parent_id: the Reddit alphanumeric ID for the parent
- author: the Reddit username of the reply
- subreddit: the Reddit community where the discussion occurred
- parent_score: the net vote score of the parent comment
- cleantext: the simplified reply (one of 37 classes)
- tstamp: the timestamp of the reply
- parent_body: the content of the original parent

## Dataset Creation

### Source Data

Reddit comments collected through PushShift.io archives for 2014.

#### Initial Data Collection and Normalization

- Removed deleted or empty comments.
- Selected only replies which scored 1.5x higher than a parent comment, where both have a positive score.
- Found the top/repeating phrases common to these one-ups/clapback comments.
- Selected only replies which had one of these top/repeating phrases.
- Made rows in PostgreSQL and output as CSV.

## Considerations for Using the Data

Comments and responses in the Reddit archives and output datasets all include NSFW and otherwise toxic language and links!

- You can use the subreddit and score columns to filter content.
- Imbalanced dataset: replies 'yes' and 'no' are more common than others.
- Overlap of labels: replies such as 'yes', 'yep', and 'yup' serve similar purposes; in other cases 'no' vs. 'nope' may be interesting.
- Timestamps: the given timestamp may help identify trends in meme replies
- Usernames: a username was included to identify the 'username checks out' meme, but this was not common enough in 2014, and the included username is from the reply.

Reddit comments are properties of Reddit and comment owners using their Terms of Service.