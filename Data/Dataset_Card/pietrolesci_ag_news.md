---
YAML tags:

annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilingualism:
- monolingual
paperswithcode_id: ag-news
pretty_name: ag_news
size_categories:
- 100K<n<1M
source_datasets:
- ag_news
task_categories:
- text-classification
task_ids:
- topic-classification
---

# Dataset Card for [Dataset Name]

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
AG is a collection of more than 1 million news articles. News articles have been
gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of
activity. ComeToMyHead is an academic news search engine which has been running
since July, 2004. The dataset is provided by the academic comunity for research
purposes in data mining (clustering, classification, etc), information retrieval
(ranking, search, etc), xml, data compression, data streaming, and any other
non-commercial activity. For more information, please refer to the link
http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .
   
The AG's news topic classification dataset is constructed by Xiang Zhang
(xiang.zhang@nyu.edu) from the dataset above. It is used as a text
classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann
LeCun. Character-level Convolutional Networks for Text Classification. Advances
in Neural Information Processing Systems 28 (NIPS 2015).

### Supported Tasks and Leaderboards
Text classification.

### Languages
English.

## Dataset Structure
We show detailed information for the 2 available configurations of the dataset.

### Data Instances
The two configurations share the following information:
- **Size of downloaded dataset files**: 29.88 MB
- **Size of the generated dataset**: 30.23 MB
- **Total amount of disk used**: 60.10 MB

### Data Fields
**concat**
- text: a string feature.
- label: a classification label, with possible values including World (0), Sports (1), Business (2), Sci/Tech (3).
```
{
  'description': 'Putin Heads for Turkey in Landmark Visit Between Former Foes Russian President Vladimir Putin is making a two-day official visit to Turkey, the first by any Russian leader in 32 years. Mr. Putin is expected to sign several economic cooperation agreements ',
  'label': 0
}
```

**original**
- title: a string feature.
- description: a string feature.
- label: a string feature, with possible values including World, Sports, Business, Sci/Tech.
```
{
  'description': 'Russian President Vladimir Putin is making a two-day official visit to Turkey, the first by any Russian leader in 32 years. Mr. Putin is expected to sign several economic cooperation agreements ',
  'label': 1,
  'class': 'World',
  'title': 'Putin Heads for Turkey in Landmark Visit Between Former Foes'
}
```

### Data Splits
The two configurations share the following information:
- **train**: 120000
- **test**: 7600

## Dataset Creation

### Curation Rationale
This specific instance of the dataset contains two configurations:

1. `concat` that can be loaded using `load_dataset("pietrolesci/ag_news", name="concat")` and contains the original dataset as available [here](https://huggingface.co/datasets/ag_news). This configuration of the dataset concatenates the text fields ("title" and "description") and encodes the four classes numerically with the following mapping `{0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}`. Notably, in this specific instance, the `text` field is preprocessed by replacing `\\` with `" "` and stripping whitespaces.

1. `original` that can be loaded using `load_dataset("pietrolesci/ag_news", name="original")` and contains the original dataset as available from the [source](https://drive.google.com/drive/u/0/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M?resourcekey=0-TLwzfR2O-D2aPitmn5o9VQ). It is equal to [here](https://huggingface.co/datasets/ag_news) but the text fields are not concatenated, the `label` field is not zero-indexed (but is like the original), there is an additional `class` field reporting the original label. Also, the text fields are preprocessed by replacing `\\` with `" "` and stripping whitespaces.

### Source Data
The original data source for this dataset can be found [here](https://drive.google.com/drive/u/0/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M?resourcekey=0-TLwzfR2O-D2aPitmn5o9VQ).

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators
Original split curated by [Pietro Lesci](https://github.com/pietrolesci).

### Licensing Information

[More Information Needed]

### Citation Information
```
@inproceedings{Zhang2015CharacterlevelCN,
  title={Character-level Convolutional Networks for Text Classification},
  author={Xiang Zhang and Junbo Jake Zhao and Yann LeCun},
  booktitle={NIPS},
  year={2015}
}
```
