---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- found
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: Toxic Wikipedia Comments
size_categories:
- 100K<n<1M
source_datasets:
- extended|other
tags:
- wikipedia
- toxicity
- toxic comments
task_categories:
- text-classification
task_ids:
- hate-speech-detection
---
# Dataset Card for Wiki Toxic

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

The Wiki Toxic dataset is a modified, cleaned version of the dataset used in the [Kaggle Toxic Comment Classification challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/overview) from 2017/18. The dataset contains comments collected from Wikipedia forums and classifies them into two categories, `toxic` and `non-toxic`.

The Kaggle dataset was cleaned using the included `clean.py` file.

### Supported Tasks and Leaderboards

- Text Classification: the dataset can be used for training a model to recognise toxicity in sentences and classify them accordingly.

### Languages

The sole language used in the dataset is English.

## Dataset Structure

### Data Instances

For each data point, there is an id, the comment_text itself, and a label (0 for non-toxic, 1 for toxic).

```
{'id': 'a123a58f610cffbc',
 'comment_text': '"This article SUCKS. It may be poorly written, poorly formatted, or full of pointless crap that no one cares about, and probably all of the above.  If it can be rewritten into something less horrible, please, for the love of God, do so, before the vacuum caused by its utter lack of quality drags the rest of Wikipedia down into a bottomless pit of mediocrity."',
 'label': 1}
```

### Data Fields

- `id`: A unique identifier string for each comment
- `comment_text`: A string containing the text of the comment
- `label`: An integer, either 0 if the comment is non-toxic, or 1 if the comment is toxic

### Data Splits

The Wiki Toxic dataset has three splits: *train*, *validation*, and *test*. The statistics for each split are below:

| Dataset Split | Number of data points in split |
| ----------- | ----------- |
| Train | 127,656 |
| Validation | 31,915 |
| Test | 63,978 |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

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

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.