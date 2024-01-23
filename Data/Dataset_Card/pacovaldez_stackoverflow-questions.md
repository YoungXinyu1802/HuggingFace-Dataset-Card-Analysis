---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- found
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: stackoverflow_post_questions
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- stackoverflow
- technical questions
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# Dataset Card for [Stackoverflow Post Questions]

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
  - [Contributions](#contributions)

## Dataset Description

Companies that sell Open-source software tools usually hire an army of Customer representatives to try to answer every question asked about their tool. The first step in this process 
is the prioritization of the question. The classification scale usually consists of 4 values, P0, P1, P2, and P3, with different meanings across every participant in the industry. On 
the other hand, every software developer in the world has dealt with Stack Overflow (SO); the amount of shared knowledge there is incomparable to any other website. Questions in SO are 
usually annotated and curated by thousands of people, providing metadata about the quality of the question. This dataset aims to provide an accurate prioritization for programming 
questions.


### Dataset Summary

The dataset contains the title and body of stackoverflow questions and a label value(0,1,2,3) that was calculated using thresholds defined by SO badges.

### Languages

English

## Dataset Structure

title: string,
body: string,
label: int

### Data Splits

The split is 40/40/20, where classes have been balaned to be around the same size.

## Dataset Creation

The data set was extracted and labeled with the following query in BigQuery:

```
SELECT
  title,
  body,
  CASE
    WHEN score >= 100 OR favorite_count >= 100 OR view_count >= 10000 THEN 0
    WHEN score >= 25 OR favorite_count >= 25 OR view_count >= 2500  THEN 1
    WHEN score >= 10 OR favorite_count >= 10 OR view_count >= 1000 THEN 2
    ELSE 3
  END AS label
FROM `bigquery-public-data`.stackoverflow.posts_questions
```

### Source Data

The data was extracted from the Big Query public dataset: `bigquery-public-data.stackoverflow.posts_questions`

#### Initial Data Collection and Normalization

The original dataset contained high class imbalance:

label	count
0	977424
1	2401534
2	3418179
3	16222990
Grand Total	23020127

The data was sampled from each class to have around the same amount of records on every class.

### Contributions

Thanks to [@pacofvf](https://github.com/pacofvf) for adding this dataset.
