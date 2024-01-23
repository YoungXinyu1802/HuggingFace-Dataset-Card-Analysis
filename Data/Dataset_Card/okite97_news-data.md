---
annotations_creators:
- other
language:
- 'en'
language_creators:
- found
license:
- afl-3.0
multilinguality:
- monolingual
pretty_name: News Dataset
size_categories:
- 1K<n<10K
source_datasets:
- original
tags: []
task_categories:
- text-classification
task_ids:
- topic-classification
- multi-class-classification
---

# Dataset Card for news-data

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
 
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)

  - [Dataset Curators](#dataset-curators)
 

### Dataset Summary

The News Dataset is an English-language dataset containing just over 4k unique news articles scrapped from AriseTv- One of the most popular news television in Nigeria. 
### Supported Tasks and Leaderboards

It supports news article classification into different categories.

### Languages

English

## Dataset Structure

### Data Instances

'''
{'Title': 'Nigeria: APC Yet to Zone Party Positions Ahead of Convention'
 'Excerpt': 'The leadership of the All Progressives Congress (APC), has denied reports that it had zoned some party positions ahead of'
 'Category': 'politics'
 'labels': 2}
 '''

### Data Fields
* Title: a string containing the title of a news title as shown
* Excerpt: a string containing a short extract from the body of the news
* Category: a string that tells the category of an example (string label)
* labels: integer telling the class of an example (label)

### Data Splits

| Dataset Split      | Number of instances in split |
| -----------        | ----------- |
| Train              | 4,594      |
| Paragraph          | 811      |

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The code for the dataset creation at *https://github.com/chimaobi-okite/NLP-Projects-Competitions/blob/main/NewsCategorization/Data/NewsDataScraping.ipynb*. The examples were scrapped from
<https://www.arise.tv/>


### Annotations

#### Annotation process

The annotation is based on the news category in the [arisetv](https://www.arise.tv) website

#### Who are the annotators?

Journalists at arisetv

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop models that can classify news articles into categories.

This task is useful for efficiently presenting information given a large quantity of text. It should be made clear that any summarizations produced by models trained on this dataset are reflective of the language used in the articles, but are in fact automatically generated.

### Discussion of Biases
This data is biased towards news happenings in Nigeria but the model built using it can as well classify news from other parts of the world 
with a slight degradation in performance.


### Dataset Curators

The dataset is created by people at arise but was scrapped by [@github-chimaobi-okite](https://github.com/chimaobi-okite/)
