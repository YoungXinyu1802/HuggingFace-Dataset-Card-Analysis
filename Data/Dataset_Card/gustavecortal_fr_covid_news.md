---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- fr
language_bcp47:
- fr-FR
license:
- unknown
multilinguality:
- monolingual
pretty_name: COVID-19 French News dataset
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
- sequence-modeling
- conditional-text-generation
task_ids:
- topic-classification
- multi-label-classification
- multi-class-classification
- language-modeling
- summarization
- other-stuctured-to-text
---

# Dataset Card for COVID-19 French News dataset

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
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The COVID-19 French News dataset is a French-language dataset containing just over 40k unique news articles from more than 50 different French-speaking online newspapers. The dataset has been prepared using [news-please](https://github.com/fhamborg/news-please) - an integrated web crawler and information extractor for news. The current version supports abstractive summarization and topic classification. Dataset Card not finished yet.

### Languages

The text in the dataset is in French.

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- `title`: title of the article
- `description`: description or a summary of the article
- `text`: the actual article text in raw form
- `domain`: source domain of the article (i.e. lemonde.fr)
- `url`: article URL, the original URL where it was scraped
- `labels`: classification labels

## Data Splits

COVID-19 French News dataset has only the training set, i.e. it has to be loaded with train split specified: fr_covid_news = load_dataset('gustavecortal/fr_covid_news', split="train")

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?


### Annotations

#### Annotation process

[More Information Needed]

### Personal and Sensitive Information

As one can imagine, data contains contemporary public figures or individuals who appeared in the news.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help researchers develop better French topic classification and abstractive summarization models for news related to COVID-19.

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The data was originally collected by Gustave Cortal (gustavecortal@gmail.com)

### Licensing Information

Usage of the dataset is restricted to non-commercial research purposes only.

### Citation Information

```
@dataset{fr_covid_news,
  author = {Gustave Cortal},
  year = {2022},
  title = {COVID-19 - French News Dataset},
  url = {https://www.gustavecortal.com}
}
```

### Contributions

[@gustavecortal](https://github.com/gustavecortal)