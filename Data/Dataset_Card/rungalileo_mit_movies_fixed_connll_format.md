---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: MIT_movies_fixed
---

# Dataset Card for MIT_movies_fixed

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Galileo Homepage:** [Galileo ML Data Intelligence Platform](https://www.rungalileo.io)
- **Repository:** [Needs More Information]
- **Dataset Blog:** [Improving Your ML Datasets With Galileo, Part 2](https://www.rungalileo.io/blog/improving-your-ml-datasets-part-2-ner)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]
- **MIT movies Homepage:** [newsgroups homepage](https://groups.csail.mit.edu/sls/downloads/)

### Dataset Summary

This dataset is a version of the [**MIT movies**](https://groups.csail.mit.edu/sls/downloads/)

### Curation Rationale

This dataset was created to showcase the power of Galileo as a Data Intelligence Platform. Through Galileo, we identify critical error patterns within the original MIT movies dataset - annotation errors, ill-formed samples etc. Moreover, we observe that these errors permeate throughout the test dataset. As a result of our analysis, we fix 4% of the dataset by re-annotating the samples, and provide the dataset for NER research. To learn more about the process of fixing this dataset, please refer to our [**Blog**](https://www.rungalileo.io/blog/improving-your-ml-datasets-part-2-ner).


## Dataset Structure

### Data Instances
Every sample is blank line separated, every row is tab separated, and contains the word and its corresponding NER tag. This dataset uses the BIOES tagging schema.  

An example from the dataset looks as follows:
```
show	O
me	O
a	O
movie	O
about	O
cars	B-PLOT
that	I-PLOT
talk	E-PLOT
```

### Data Splits

The data is split into a training and test split. The training data has ~9700 samples and the test data has ~2700 samples.

### Data Classes
The dataset contains the following 12 classes: ACTOR, YEAR, TITLE, GENRE, DIRECTOR, SONG, PLOT, REVIEW, CHARACTER, RATING, RATINGS_AVERAGE, TRAILER. Some of the classes have high semantic overlap (e.g. RATING/RATINGS_AVERAGE and ACTOR/DIRECTOR). 