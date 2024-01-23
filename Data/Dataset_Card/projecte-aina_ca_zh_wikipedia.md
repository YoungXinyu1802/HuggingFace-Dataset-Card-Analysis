---
annotations_creators:
- no-annotation
language_creators:
- machine-generated
language:
- ca
- zh
- multilingual
license: 
- cc-by-4.0
multilinguality:
- translation
pretty_name: CA-ZH Wikipedia Parallel Corpus
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- translation
task_ids: []
---

# Dataset Card for CA-ZH Wikipedia datasets

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

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [cescolano3@gmail.com](cescolano3@gmail.com)

### Dataset Summary

The CA-ZH Parallel Corpus is a Catalan-Chinese dataset of mutual translations automatically crawled from Wikipedia. Two separate corpora are included, namely CA-ZH 1.05 Wikipedia and CA-ZH 1.10 Wikipedia, the latter has better general quality than the former. The dataset was created to support Catalan NLP tasks, e.g., Machine Translation.

### Supported Tasks and Leaderboards

The dataset can be used to train a model for Multilingual Machine Translation. Success on this task is typically measured by achieving a high BLEU score. The dataset can be used to finetune a large-scale multilingual MT system such as m2m-100.

### Languages

The texts in the dataset are in Catalan and Chinese.

## Dataset Structure

### Data Instances

A typical data point comprises a pair of translations in Catalan and Chinese. An example from the Ca-Zh Parallel Corpus looks as follows:

```
{ "ca": "1591è Batalló Separat d'Artilleria autorpopulsada", "zh": "第1591自走砲营" }
```

### Data Fields

- "ca": Text in Catalan.
- "zh": Text in Chinese.

### Data Splits

The dataset contains a single split: `train`.

## Dataset Creation

### Curation Rationale

The Ca-Zh Parallel Corpus was built to provide more language data for MT tasks dedicated to low-resource languages. The dataset was built by gathering texts on the same topic in Catalan and Chinese from Wikipedia.

### Source Data

#### Initial Data Collection and Normalization

The data was obtained by automatic crawling, a quality filter was applied to improve the data quality. The original Chinese data was mixed into Traditional Chinese and Simplified Chinese, a simplification process was conducted in order to guarantee the unification.

#### Who are the source language producers?

All the texts in this dataset come from the Wikipedia.

### Annotations

The dataset is unannotated.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

No anonymisation process was performed.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop Machines Translation tasks for low-resource languages such as Catalan.

### Discussion of Biases

We are aware that since the data comes from unreliable web pages and non-curated texts, some biases may be present in the dataset. Nonetheless, we have not applied any steps to reduce their impact.

### Other Known Limitations

Wikipedia provides data of a more general domain. Application of this dataset in more specific domains such as biomedical, legal etc. would be of limited use.

## Additional Information

### Dataset Curators

Carlos Escolano, Chenuye Zhou and Zixuan Liu, Barcelona Supercomputing Center (cescolano3 at gmail dot com)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

[Creative Commons Attribution Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/).

### Citation Information

```
@mastersthesis{MasterThesisChenuyeZhou,
  author  = "Chenuye Zhou",
  title   = "Building a Catalan-Chinese parallel corpus for use in MT",
  school  = "Universitat Pompeu Fabra",
  year    = 2022,
  address = "Barcelona",
  url = "https://repositori.upf.edu/handle/10230/54140"
}

@mastersthesis{MasterThesisZixuanLiu,
  author  = "Zixuan Liu",
  title   = "Improving Chinese-Catalan Machine Translation with Wikipedia Parallel",
  school  = "Universitat Pompeu Fabra",
  year    = 2022,
  address = "Barcelona",
  url= "https://repositori.upf.edu/handle/10230/54142"
}
```
