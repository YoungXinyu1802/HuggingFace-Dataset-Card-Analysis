---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11818583
    num_examples: 15083
  - name: test
    num_bytes: 1152954
    num_examples: 1676
  download_size: 7404260
  dataset_size: 12971537
task_categories:
- text-generation
language:
- de
tags:
- german-gpt2
pretty_name: German Articles about the War in Ukraine
---
# Dataset Card

## Table of Contents
- [Dataset Card](#dataset-card)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** --
- **Repository:** [github.com/pstuerner/ukraine-liveblog-data](https://github.com/pstuerner/ukraine-liveblog-data)
- **Paper:** --
- **Leaderboard:** --
- **Point of Contact:** philipp.stuerner@web.de

### Dataset Summary

The "ukraine-liveblog" dataset contains a collection of news articles published on the liveblog of the popular German news website, tagesschau.de. The dataset covers the period from February 2022 to February 2023, and includes every news feed published during this time that covers the ongoing war in Ukraine.

### Supported Tasks and Leaderboards

--

### Languages

The language of the dataset is German.

## Dataset Structure

### Data Instances

Here is a JSON-formatted example of a typical instance in the "German Articles about the War in Ukraine" dataset:

This example consists of a headline and the corresponding text separated by a colon. The headline reads "Warum Waffenlieferungen in Ostdeutschland skeptisch gesehen werden" (Why Weapons Deliveries are Viewed Skeptically in East Germany), and the text provides additional details and analysis about the topic. This format is consistent across the dataset and allows for easy identification and extraction of key information.

```
{
  "text": "Warum Waffenlieferungen in Ostdeutschland skeptisch gesehen werden: Die Debatten um Waffenlieferungen für die Ukraine stoßen in Ostdeutschland meist auf Ablehnung. Das lässt sich aber nicht allein mit Russlandfreundlichkeit erklären, sagt Politikwissenschaftlerin Sarah Pagung."
  ...
}
```

### Data Fields

The "ukraine-liveblog" dataset includes the following fields:

- `text`: The main body of the article, written in German. (string)

### Data Splits

The dataset has been split into two sets: a training set and a validation set. The training set contains 90% of the data, or 15,083 instances, and the validation set contains the remaining 10%, or 1,676 instances.

|                         | train | validation | test |
|-------------------------|------:|-----------:|-----:|
| Input Sentences         | 15083 | 1676       |      |
| Average Sentence Length | 768   | 674        |      |

## Dataset Creation

### Curation Rationale

The creation of the dataset was motivated by a number of factors, such as the need to collect and analyze information about the conflict in Ukraine, understand how the conflict is being reported in German media, and provide a resource for NLP enthusiasts to fine-tune GPT2 on additional German data.

### Source Data

The liveblog on tagesschau.de about the war in Ukraine.

#### Initial Data Collection and Normalization

The dataset was built using a custom Python script that leverages the newspaper and beautifulsoup4 libraries. The script was designed to scrape data from the liveblog about the war in Ukraine on tagesschau.de, starting from the latest day of the liveblog and working backwards until it reaches the first day of the liveblog.

#### Who are the source language producers?

The articles were written by Tagesschau reporters.

### Annotations

--

#### Annotation process

--

#### Who are the annotators?

--

### Personal and Sensitive Information

All information is publicly available and doesn't include any personal or sensitive information.

## Considerations for Using the Data

### Social Impact of Dataset

--

### Discussion of Biases

--

### Other Known Limitations

--

## Additional Information

### Dataset Curators

--

### Licensing Information

--

### Citation Information

--

### Contributions

--