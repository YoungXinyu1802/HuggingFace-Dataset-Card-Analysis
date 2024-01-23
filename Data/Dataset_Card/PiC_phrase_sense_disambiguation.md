---
annotations_creators:
- expert-generated
language_creators:
- found
- expert-generated
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
paperswithcode_id: phrase-in-context
pretty_name: 'PiC: Phrase Sense Disambiguation'
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-retrieval
task_ids: []
---

# Dataset Card for "PiC: Phrase Sense Disambiguation"

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

- **Homepage:** [https://phrase-in-context.github.io/](https://phrase-in-context.github.io/)
- **Repository:** [https://github.com/phrase-in-context](https://github.com/phrase-in-context)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [Thang Pham](<thangpham@auburn.edu>)
- **Size of downloaded dataset files:** 49.95 MB
- **Size of the generated dataset:** 43.26 MB
- **Total amount of disk used:** 93.20 MB

### Dataset Summary

PSD is a phrase retrieval task like PR-pass and PR-page but more challenging since each example contains two short paragraphs (~11 sentences each) which trigger different senses of the same phrase.
The goal is to find the instance of the target phrase **t** that is semantically similar to a paraphrase **q**.
The dataset is split into 5,150/3,000/20,002 for test/dev/train, respectively.

<p align="center">
<img src="https://auburn.edu/~tmp0038/PiC/psd_sample.png" alt="PSD sample" style="width:100%; border:0;">
</p>

Given document D, trained Longformer-large model correctly retrieves <span style="background-color: #ef8783">massive figure</span> in the second paragraph for the query Q<sub>2</sub> "giant number" but **fails** to retrieve the answer when the query Q<sub>1</sub> is "huge model".
The correct answer for Q<sub>1</sub> should be <span style="background-color: #a1fb8e">massive figure</span> in the first passage since this phrase relates to a model rather than a number.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English.

## Dataset Structure

### Data Instances

**PSD**
* Size of downloaded dataset files: 49.95 MB
* Size of the generated dataset: 43.26 MB
* Total amount of disk used: 93.20 MB

An example of 'test' looks as follows.

```
{
  "id": "297-1",
  "title": "https://en.wikipedia.org/wiki?curid=2226019,https://en.wikipedia.org/wiki?curid=1191780",
  "context": "In addition, the results from the study did not support the idea of females preferring complexity over simplicity in song sequences. These findings differ from past examinations, like the 2008 Morisake et al. study that suggested evidence of female Bengalese finches preferring complex songs over simple ones. Evolutionary adaptations of specifically complex song production in relation to female preference in Bengalese finches continues to be a topic worth examining. Comparison with zebra finches. Bengalese finches and zebra finches are members of the estrildiae family and are age-limited learners when it comes to song learning and the acoustic characteristics of their songs (Peng et al., 2012). Both of these species have been widely used in song learning based animal behavior research and although they share many characteristics researchers have been able to determine stark differences between the two. Previous to research done in 1987, it was thought that song learning in Bengalese finches was similar to zebra finches but there was no research to support this idea. Both species require learning from an adult during a sensitive juvenile phase in order to learn the species specific and sexually dimorphic songs. This tutor can be the father of the young or other adult males that are present around the juvenile. Clayton aimed to directly compare the song learning ability of both of these species to determine if they have separate learning behaviors. Many students find they can not possibly complete all the work assigned them; they learn to neglect some of it. Some student groups maintain files of past examinations which only worsen this situation. The difference between the formal and real requirements produced considerable dissonance among the students and resulted in cynicism, scorn, and hypocrisy among students, and particular difficulty for minority students. No part of the university community, writes Snyder, neither the professors, the administration nor the students, desires the end result created by this process. The \"Saturday Review\" said the book \"will gain recognition as one of the more cogent 'college unrest' books\" and that it presents a \"most provocative thesis.\" The book has been cited many times in studies. References. [[Category:Curricula]] [[Category:Philosophy of education]] [[Category:Massachusetts Institute of Technology]] [[Category:Books about social psychology]] [[Category:Student culture]] [[Category:Books about education]] [[Category:1970 non-fiction books]]",
  "query": "previous exams",
  "answers": {
    "text": ["past examinations"], 
    "answer_start": [1621] 
  }
}
```

### Data Fields

The data fields are the same among all subsets and splits.

* id: a string feature.
* title: a string feature.
* context: a string feature.
* question: a string feature.
* answers: a dictionary feature containing:
  * text: a list of string features.
  * answer_start: a list of int32 features.

### Data Splits

|        name        |train|validation|test|
|--------------------|----:|---------:|---:|
|PSD                 |20002|      3000|5000|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The source passages + answers are from Wikipedia and the source of queries were produced by our hired linguistic experts from [Upwork.com](https://upwork.com).

#### Who are the source language producers?

We hired 13 linguistic experts from [Upwork.com](https://upwork.com) for annotation and more than 1000 human annotators on Mechanical Turk along with another set of 5 Upwork experts for 2-round verification.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

13 linguistic experts from [Upwork.com](https://upwork.com).

### Personal and Sensitive Information

No annotator identifying details are provided.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset is a joint work between Adobe Research and Auburn University.
Creators: [Thang M. Pham](https://scholar.google.com/citations?user=eNrX3mYAAAAJ), [David Seunghyun Yoon](https://david-yoon.github.io/), [Trung Bui](https://sites.google.com/site/trungbuistanford/), and [Anh Nguyen](https://anhnguyen.me).

[@PMThangXAI](https://twitter.com/pmthangxai) added this dataset to HuggingFace.

### Licensing Information

This dataset is distributed under [Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

### Citation Information

```
@article{pham2022PiC,
  title={PiC: A Phrase-in-Context Dataset for Phrase Understanding and Semantic Search},
  author={Pham, Thang M and Yoon, Seunghyun and Bui, Trung and Nguyen, Anh},
  journal={arXiv preprint arXiv:2207.09068},
  year={2022}
}
```