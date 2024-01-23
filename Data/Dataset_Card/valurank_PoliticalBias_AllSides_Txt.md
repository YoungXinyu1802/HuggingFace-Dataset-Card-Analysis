---
license:
- other
language:
- en
multilinguality:
- monolingual
task_categories:
- classification
task_ids:
- classification
---

# Dataset Card for news-12factor

## Table of Contents
- [Dataset Description](#dataset-description)
- [Languages](#languages)
- [Dataset Structure](#dataset-structure)
- [Source Data](#source-data)
- [Annotations](#annotations)

## Dataset Description

~20k articles labeled left, right, or center by the editors of allsides.com. 

## Languages

The text in the dataset is in English

## Dataset Structure

3 folders, with many text files in each. Each text file represent the body text of one article.

## Source Data

URL data was scraped using https://github.com/mozilla/readability

## Annotations

Articles were manually annotated by news editors who were attempting to select representative articles from the left, right and center of each article topic. In other words, the dataset should generally be balanced - the left/right/center articles cover the same set of topics, and have roughly the same amount of articles in each.

