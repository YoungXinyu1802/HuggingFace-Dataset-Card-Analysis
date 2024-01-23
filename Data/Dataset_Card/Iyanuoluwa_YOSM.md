---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- yo
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- movie reviews
- nollywood
task_categories:
- text-classification
task_ids:
- sentiment-analysis
---
# Dataset Card for YOSM

## Table of Contents
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
- **Repository:** [Iyanuoluwa/YOSM](https://github.com/IyanuSh/YOSM)
- **Paper:** [A new Yorùbá Sentiment Corpus for Nigerian/Nollywood Movie Reviews](https://arxiv.org/pdf/2204.09711.pdf)
- **Point of Contact:** [Iyanuoluwa Shode](mailto:shodei1@montclair.edu)

### Dataset Summary

YOSM is the first Yorùbá sentiment corpus for Nollywood movie reviews. The reviews were collected from movie reviews websites - IMDB, Rotten Tomatoes, LetterboxD, Cinemapointer, and Nollyrated. 

### Languages

Yorùbá (ISO 639-1: yo) - the third most spoken indigenous African language with over 50 million speakers.

## Dataset Structure

### Data Instances

An instance consists of a movie review and the corresponding class label.

### Data Fields

- `yo_review`: A movie review in Yorùbá
- `sentiment`: The label describing the sentiment of the movie review. 

### Data Splits

The YOSM dataset has 3 splits: _train_, _dev_, and _test_. Below are the statistics for Version 3.0.0 of the dataset.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 800                                    |
| Development   | 200                                     |
| Test          | 500                                      |

### Data Splits

[More Information Needed]

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
