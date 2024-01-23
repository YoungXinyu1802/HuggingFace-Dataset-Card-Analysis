---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- ru
multilinguality:
- monolingual
pretty_name: Kill-Me-Please Dataset
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- stories
- website
task_categories:
- text-generation
- text-classification
---
# Dataset Card for Kill-Me-Please Dataset


## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Description

- **Repository:** [github pet project repo](https://github.com/takiholadi/generative-kill-me-please)

### Dataset Summary

It is an Russian-language dataset containing just over 30k unique stories as written as users of https://killpls.me as of period from March 2009 to October 2022. This resource was blocked by Roskomnadzor so consider text-generation task if you want more stories.

### Languages

ru-RU

## Dataset Structure

### Data Instances

Here is an example of instance:

```
{'text': 'По глупости удалил всю 10 летнюю базу. Восстановлению не подлежит. Мне конец. КМП!'
 'tags': 'техника'
 'votes': 2914
 'url': 'https://killpls.me/story/616'
 'datetime': '4 июля 2009, 23:20'}
```

### Data Fields

- `text`: a string containing the body of the story
- `tags`: a string containing a comma-separated tags in a multi-label setup, fullset of tags (except of one empty-tagged record): `внешность`, `деньги`, `друзья`, `здоровье`, `отношения`, `работа`, `разное`, `родители`, `секс`, `семья`, `техника`, `учеба`
- `votes`: an integer sum of upvotes/downvotes
- `url`: a string containing the url where the story was web-scraped from
- `datetime`: a string containing with the datetime the story was written

### Data Splits

The has 2 multi-label stratified splits: train and test.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 27,321                                      |
| Test          | 2,772                                       |
