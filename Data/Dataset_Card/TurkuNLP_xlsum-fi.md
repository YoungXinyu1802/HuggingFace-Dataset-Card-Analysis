---
annotations_creators:
- found
language_creators:
- machine translated
language:
- fi
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- xlsum
task_categories:
- summarization
- text2text-generation
task_ids: []
pretty_name: XL-Sum-FI
tags:
- conditional-text-generation
---

# Dataset Card for "XL-Sum-FI"

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
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

- **Repository:** https://github.com/TurkuNLP/xlsum-fi
- **Point of Contact:** [Filip Ginter](mailto:figint@utu.fi)

### Dataset Summary

This dataset is a DeepL -based machine translation of a part of the English section of the XLSum dataset:[https://github.com/csebuetnlp/xl-sum](https://github.com/csebuetnlp/xl-sum) In the present version, only examples where the full version is at most 10x the summary in length are included. We might translate more later.

### Supported Tasks and Leaderboards


### Languages

-  `finnish`


## Dataset Structure

### Data Instances

One example from the `Finnish` dataset is given below in JSON format. 
  ```
  {
    "id": "technology-17657859",
    "url": "https://www.bbc.com/news/technology-17657859",
    "title": "Walesin myrskytuulien vuoksi annettu säävaroitus",
    "summary": "Tuulet voivat yltyä Walesissa myrskytuuliin, ja myrskysää on luvassa koko maahan tällä viikolla.",
    "text": "Met Office on antanut Walesin ja Englannin kattavan keltaisen tuulivaroituksen keskiviikkoillasta kello 21.00 GMT alkaen. Matkustaminen ja sähkönjakelu todennäköisesti häiriintyvät, ja varoitus on voimassa torstaihin kello 15:00 asti. Puuskat ovat todennäköisesti nopeudeltaan 88 kilometriä tunnissa, ja rannikoilla ja kukkuloilla puuskat voivat nousta jopa 70 kilometriin tunnissa, ja lisäksi voi esiintyä rankkasateita ja myrskyisiä sadekuuroja."
  }
  ```

### Data Fields
-  'id': A string representing the article ID, matched to the XLSum dataset original
-  'url': A string representing the article URL as in the original XLSum dataset
-  'title': A string containing the article title, machine-translated to Finnish
-  'summary': A string containing the article summary, machine-translated to Finnish
-  'text' : A string containing the article text, machine-translated to Finnish


### Data Splits

Follows the XLSum dataset.

## Dataset Creation

### Curation Rationale

### Source Data

[BBC News](https://www.bbc.co.uk/ws/languages)

#### Initial Data Collection and Normalization

[Detailed in the paper](https://aclanthology.org/2021.findings-acl.413/) For this present dataset, only English was used as the source and only examples where the full text is at maximum 10x in length compared to the summary are preserved. This 10x cutoff is naturally measured on English.

#### Who are the source language producers?

[Detailed in the paper](https://aclanthology.org/2021.findings-acl.413/) 

### Annotations

[Detailed in the paper](https://aclanthology.org/2021.findings-acl.413/) DeepL was used to machine-translate from English to Finnish

#### Annotation process

[Detailed in the paper](https://aclanthology.org/2021.findings-acl.413/) 

#### Who are the annotators?

[Detailed in the paper](https://aclanthology.org/2021.findings-acl.413/) 

### Personal and Sensitive Information

[More information needed](https://github.com/csebuetnlp/xl-sum)

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

Due to DeepL terms and conditions, this dataset **must not be used for any machine translation work**, namely machine translation system development and evaluation of any kind. In general, we wish you do not pair the original English data with the translations except when working on research unrelated to machine translation, so as not to infringe on the terms and conditions.

## Additional Information

### Dataset Curators


### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.

### Citation Information

If you use any of the datasets, models or code modules, please cite the original XL-Sum paper below as well as acknowledge Filip Ginter and the TurkuNLP group for the Finnish machine translated version.

```
@inproceedings{hasan-etal-2021-xl,
    title = "{XL}-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Islam, Md. Saiful  and
      Mubasshir, Kazi  and
      Li, Yuan-Fang  and
      Kang, Yong-Bin  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.413",
    pages = "4693--4703",
}
```


### Contributions

Thanks to the creators of the XLSum dataset!