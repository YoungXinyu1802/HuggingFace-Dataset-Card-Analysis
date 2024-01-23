---
annotations_creators:
- expert-generated
- found
language_creators:
- found
language:
- en
- yo
license:
- cc-by-nc-4.0
multilinguality:
- translation
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- translation
task_ids: []
paperswithcode_id: menyo-20k
pretty_name: MENYO-20k
dataset_info:
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - yo
  config_name: menyo20k_mt
  splits:
  - name: train
    num_bytes: 2551345
    num_examples: 10070
  - name: validation
    num_bytes: 870011
    num_examples: 3397
  - name: test
    num_bytes: 1905432
    num_examples: 6633
  download_size: 5206234
  dataset_size: 5326788
---

# Dataset Card for MENYO-20k

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
- **Repository:** https://github.com/uds-lsv/menyo-20k_MT/
- **Paper:** [The Effect of Domain and Diacritics in Yorùbá-English Neural Machine Translation](https://arxiv.org/abs/2103.08647)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

MENYO-20k is a multi-domain parallel dataset with texts obtained from news articles, ted talks, movie transcripts, radio transcripts, science and technology texts, and other short articles curated from the web and professional translators. The dataset has 20,100 parallel sentences split into 10,070 training sentences, 3,397 development sentences, and 6,633 test sentences (3,419 multi-domain, 1,714 news domain, and 1,500 ted talks speech transcript domain).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Languages are English and Yoruba.

## Dataset Structure

### Data Instances

An instance example:

```
{'translation':
  {'en': 'Unit 1: What is Creative Commons?',
  'yo': '﻿Ìdá 1: Kín ni Creative Commons?'
  }
}
```

### Data Fields

- `translation`:
  - `en`: English sentence.
  - `yo`: Yoruba sentence.


### Data Splits

Training, validation and test splits are available.

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

The dataset is open but for non-commercial use because some data sources like Ted talks and JW news require permission for commercial use.

The dataset is licensed under Creative Commons [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) License: https://github.com/uds-lsv/menyo-20k_MT/blob/master/LICENSE

### Citation Information

If you use this dataset, please cite this paper:
```
@inproceedings{adelani-etal-2021-effect,
    title = "The Effect of Domain and Diacritics in {Y}oruba{--}{E}nglish Neural Machine Translation",
    author = "Adelani, David  and
      Ruiter, Dana  and
      Alabi, Jesujoba  and
      Adebonojo, Damilola  and
      Ayeni, Adesina  and
      Adeyemi, Mofe  and
      Awokoya, Ayodele Esther  and
      Espa{\~n}a-Bonet, Cristina",
    booktitle = "Proceedings of the 18th Biennial Machine Translation Summit (Volume 1: Research Track)",
    month = aug,
    year = "2021",
    address = "Virtual",
    publisher = "Association for Machine Translation in the Americas",
    url = "https://aclanthology.org/2021.mtsummit-research.6",
    pages = "61--75",
    abstract = "Massively multilingual machine translation (MT) has shown impressive capabilities and including zero and few-shot translation between low-resource language pairs. However and these models are often evaluated on high-resource languages with the assumption that they generalize to low-resource ones. The difficulty of evaluating MT models on low-resource pairs is often due to lack of standardized evaluation datasets. In this paper and we present MENYO-20k and the first multi-domain parallel corpus with a especially curated orthography for Yoruba{--}English with standardized train-test splits for benchmarking. We provide several neural MT benchmarks and compare them to the performance of popular pre-trained (massively multilingual) MT models both for the heterogeneous test set and its subdomains. Since these pre-trained models use huge amounts of data with uncertain quality and we also analyze the effect of diacritics and a major characteristic of Yoruba and in the training data. We investigate how and when this training condition affects the final quality of a translation and its understandability.Our models outperform massively multilingual models such as Google ($+8.7$ BLEU) and Facebook M2M ($+9.1$) when translating to Yoruba and setting a high quality benchmark for future research.",
}
```
### Contributions

Thanks to [@yvonnegitau](https://github.com/yvonnegitau) for adding this dataset.
