---
annotations_creators:
- crowdsourced
- machine-generated
language:
- en
language_creators:
- found
license:
- mit
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: SPICED
size_categories:
- 1K<n<10K
source_datasets:
- extended|s2orc
tags:
- scientific text
- scholarly text
- semantic text similarity
- fact checking
- misinformation
task_categories:
- text-classification
task_ids:
- text-scoring
- semantic-similarity-scoring
---

# Dataset Card for SPICED

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
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** http://www.copenlu.com/publication/2022_emnlp_wright/
- **Repository:** https://github.com/copenlu/scientific-information-change
- **Paper:**

### Dataset Summary

The Scientific Paraphrase and Information ChangE Dataset (SPICED) is a dataset of paired scientific findings from scientific papers, news media, and Twitter. The types of pairs are between <paper, news> and <paper, tweet>. Each pair is labeled for the degree of information similarity in the _findings_ described by each sentence, on a scale from 1-5. This is called the _Information Matching Score (IMS)_. The data was curated from S2ORC and matched news articles and Tweets using Altmetric. Instances are annotated by experts using the Prolific platform and Potato. Please use the following citation when using this dataset:

```
@article{modeling-information-change,
      title={{Modeling Information Change in Science Communication with Semantically Matched Paraphrases}},
      author={Wright, Dustin and Pei, Jiaxin and Jurgens, David and Augenstein, Isabelle},
      year={2022},
      booktitle = {Proceedings of EMNLP},
      publisher = {Association for Computational Linguistics},
      year = 2022
}
```

### Supported Tasks and Leaderboards

The task is to predict the IMS between two scientific sentences, which is a scalar between 1 and 5. Preferred metrics are mean-squared error and Pearson correlation.

### Languages

English

## Dataset Structure

### Data Fields

- DOI: The DOI of the original scientific article
- instance\_id: Unique instance ID for the sample. The ID contains the field, whether or not it is a tweet, and whether or not the sample was manually labeled or automatically using SBERT (marked as "easy")
- News Finding: Text of the news or tweet finding
- Paper Finding: Text of the paper finding
- News Context: For news instances, the surrounding two sentences for the news finding. For tweets, a copy of the tweet
- Paper Context: The surrounding two sentences for the paper finding
- scores: Annotator scores after removing low competence annotators
- field: The academic field of the paper ('Computer\_Science', 'Medicine', 'Biology', or 'Psychology')
- split: The dataset split ('train', 'val', or 'test')
- final\_score: The IMS of the instance
- source: Either "news" or "tweet"
- News Url: A URL to the source article if a news instance or the tweet ID of a tweet

### Data Splits

- train: 4721 instances
- validation: 664 instances
- test: 640 instances

## Dataset Creation

For the full details of how the dataset was created, please refer to our [EMNLP 2022 paper]().

### Curation Rationale

Science communication is a complex process of translation from highly technical scientific language to common language that lay people can understand. At the same time, the general public relies on good science communication in order to inform critical decisions about their health and behavior. SPICED was curated in order to provide a training dataset and benchmark for machine learning models to measure changes in scientific information at different stages of the science communication pipeline.

### Source Data

#### Initial Data Collection and Normalization

Scientific text: S2ORC

News articles and Tweets are collected through Altmetric.

#### Who are the source language producers?

Scientists, journalists, and Twitter users.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

Models trained on SPICED can be used to perform large scale analyses of science communication. They can be used to match the same finding discussed in different media, and reveal trends in differences in reporting at different stages of the science communication pipeline. It is hoped that this can help to build tools which will improve science communication.

### Discussion of Biases

The dataset is restricted to computer science, medicine, biology, and psychology, which may introduce some bias in the topics which models will perform well on.

### Other Known Limitations

While some context is available, we do not release the full text of news articles and scientific papers, which may contain further context to help with learning the task. We do however provide the paper DOIs and links to the original news articles in case full text is desired.

## Additional Information

### Dataset Curators

Dustin Wright, Jiaxin Pei, David Jurgens, and Isabelle Augenstein

### Licensing Information

MIT

### Contributions

Thanks to [@dwright37](https://github.com/dwright37) for adding this dataset.