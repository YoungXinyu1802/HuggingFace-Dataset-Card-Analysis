---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- zu
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- fact-checking
- sentiment-classification
paperswithcode_id: zulu-stance
pretty_name: ZUstance
tags:
- stance-detection
---

# Dataset Card for "zulu-stance"

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

- **Homepage:** [https://arxiv.org/abs/2205.03153](https://arxiv.org/abs/2205.03153)
- **Repository:** 
- **Paper:** [https://arxiv.org/pdf/2205.03153](https://arxiv.org/pdf/2205.03153)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 212.54 KiB
- **Size of the generated dataset:** 186.76 KiB
- **Total amount of disk used:**  399.30KiB

### Dataset Summary

This is a stance detection dataset in the Zulu language. The data is translated to Zulu by Zulu native speakers, from English source texts.

Our paper aims at utilizing this progress made for English to transfers that knowledge into other languages, which is a non-trivial task due to the domain gap between English and the target languages. We propose a black-box non-intrusive method that utilizes techniques from Domain Adaptation to reduce the domain gap, without requiring any human expertise in the target language, by leveraging low-quality data in both a supervised and unsupervised manner. This allows us to rapidly achieve similar results for stance detection for the Zulu language, the target language in this work, as are found for English. A natively-translated dataset is used for evaluation of domain transfer.

### Supported Tasks and Leaderboards

* 

### Languages

Zulu (`bcp47:zu`)

## Dataset Structure

### Data Instances

#### zulu_stance

- **Size of downloaded dataset files:** 212.54 KiB
- **Size of the generated dataset:** 186.76 KiB
- **Total amount of disk used:**  399.30KiB

An example of 'train' looks as follows.

```
{
  'id': '0', 
  'text': 'ubukhulu be-islam buba sobala lapho i-smartphone ifaka i-ramayana njengo-ramadan. #semst', 
  'target': 'Atheism', 
  'stance': 1}

```


### Data Fields

- `id`: a `string` feature.
- `text`: a `string` expressing a stance.
- `target`: a `string` of the target/topic annotated here.
- `stance`: a class label representing the stance the text expresses towards the target. Full tagset with indices:

```
                            0: "FAVOR",
                            1: "AGAINST",
                            2: "NONE",
```

### Data Splits

|  name   |train|
|---------|----:|
|zulu_stance|1343 sentences|

## Dataset Creation

### Curation Rationale

To enable stance detection in Zulu and also to measure domain transfer in translation

### Source Data

#### Initial Data Collection and Normalization

The original data is taken from [Semeval2016 task 6: Detecting stance in tweets.](https://aclanthology.org/S16-1003/),
and then translated manually to Zulu.

#### Who are the source language producers?

English-speaking Twitter users.

### Annotations

#### Annotation process

See [Semeval2016 task 6: Detecting stance in tweets.](https://aclanthology.org/S16-1003/); the annotations are taken from there.

#### Who are the annotators?

See [Semeval2016 task 6: Detecting stance in tweets.](https://aclanthology.org/S16-1003/); the annotations are taken from there.

### Personal and Sensitive Information

The data was public at the time of collection. User names are preserved.

## Considerations for Using the Data

### Social Impact of Dataset

There's a risk of user-deleted content being in this data. The data has NOT been vetted for any content, so there's a risk of harmful text.

### Discussion of Biases

While the data is in Zulu, the source text is not from or about Zulu-speakers, and so still expresses the social biases and topics found in English-speaking Twitter users. Further, some of the topics are USA-specific. The sentiments and ideas in this dataset do not represent Zulu speakers.

### Other Known Limitations

The above limitations apply.

## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. 

### Citation Information

```
@inproceedings{dlamini_zulu_stance,
  title={Bridging the Domain Gap for Stance Detection for the Zulu language},
  author={Dlamini, Gcinizwe and Bekkouch, Imad Eddine Ibrahim and Khan, Adil and Derczynski, Leon},
  booktitle={Proceedings of IEEE IntelliSys},
  year={2022}
}
```


### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
