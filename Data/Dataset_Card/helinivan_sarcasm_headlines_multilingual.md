# Dataset Card for Multilingual Sarcasm Detection

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)

## Dataset Description

- Repository: https://github.com/helinivan/multilingual-sarcasm-detector

### Dataset Summary

Dataset consists of news article headlines in Dutch, English and Italian. The news article headlines are both from actual news sources and sarcastic/satirical newspapers. The news article is determined sarcastic/non-sarcastic based on the news article source.

The sources of news articles are:
- The Huffington Post (en, non-sarcastic)
- The Onion (en, sarcastic)
- NOS (nl, non-sarcastic)
- De Speld (nl, sarcastic)
- Il Giornale (it, non-sarcastic)
- Lercio (it, sarcastic)

### Languages

`en`, `nl`, `it`

## Dataset Structure

### Data Instances

- total_length: 67,480
- sarcastic: 25,609
- non_sarcastic: 41,817
- english: 22,837
- dutch: 20,771
- italian: 23,871

### Data Fields

- article_url: str
- article_title: str
- is_sarcastic: int
- lang: str
- title_length: int

## Dataset Creation

### Source Data

- Selected all English news article titles from this Kaggle dataset: https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection
- Randomly selected 15k Dutch non-sarcastic news article titles from this Kaggle dataset: https://www.kaggle.com/datasets/maxscheijen/dutch-news-articles

Rest of the data is scraped directly from the newspapers.