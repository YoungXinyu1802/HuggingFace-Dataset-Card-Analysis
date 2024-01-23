---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- ca
- en
license:
- cc0-1.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
- text-classification
task_ids:
- semantic-similarity-scoring
- text-scoring
pretty_name: gencata
---

# Dataset Card for GEnCaTa
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
- **Paper:**[Quality versus Quantity: Building Catalan-English MT Resources](http://www.lrec-conf.org/proceedings/lrec2022/workshops/SIGUL/pdf/2022.sigul-1.8.pdf)
- **Point of Contact:** [Ona de Gibert Bonet](mailto:ona.degibert@bsc.es)

### Dataset Summary
GEnCaTa is a Catalan-English dataset annotated for Parallel Corpus Filtering for MT. It is extracted from a general domain corpus crawled from the Catalan Government domains and subdomains. The dataset consists of 51,908 instances that are composed by the a Catalan sentence, its English translation, and whether the pair is valid for MT or not.
 
### Supported Tasks and Leaderboards
The dataset can be used to train a model for parallel corpus filtering. This task consists in automatically filtering out bad aligned sentences or sentences that are not good enough for MT training.

### Languages
The dataset is in Catalan (`ca-CA`) and English (`en-GB`).

## Dataset Structure
### Data Instances
```
{
  'ca': '- El vostre vehicle quedi immobilitzat per l'aigua',
  'en': 'You must leave your car and head for higher ground when:',
  'label': '0'
}
```
### Data Fields
- `ca` (str): Catalan sentence
- `en` (str): English sentence
- 'label' (int): 0, if the sentences are not aligned, and 1, if they are aligned and valid for MT training.

### Data Splits
We split our dataset into train, dev and test splits (positive / negative samples):
- train: 23,897 / 8,011
- dev: 7,490 / 2,510 
- test: 7,489 / 2,511

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of the new research line of parallel corpus filtering. Previous synthetic datasets exists, but to our knowledge, this is the first manually curated dataset for parallel sentence alignment.

### Source Data

#### Initial Data Collection and Normalization

We crawled the domains and subdomains of .gencat.cat and obtained comparable documents. Then we used Vecalign to perform sentence alignment.

#### Who are the source language producers?

The data comes from the official Catalan Government websites.

### Annotations

#### Annotation process

Two annotators reviewed the automatically aligned segments provided by Vecalign and labeled each pair as valid or not valid for MT training. This involves labeling as negative misaligned sentences, truncated sentences, and non-linguistic sentences.

#### Who are the annotators?

Four native Catalan speakers with a good understanding of the English language.

### Personal and Sensitive Information

Since all data comes from public websites, no anonymization process was performed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of the field of Parallel Corpus Filtering and leads to higher-quality resources for Catalan Machine Translation systems.

### Discussion of Biases

We are aware that since the data comes from public web pages, some biases may be present in the dataset. Nonetheless, we have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by MT4All CEF project and the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

### Citation

If you use any of these resources (datasets or models) in your work, please cite our latest paper:
```
@inproceedings{degibertbonet-EtAl:2022:SIGUL,
abstract = {In this work, we make the case of quality over quantity when training a MT system for a medium-to-low-resource language pair, namely Catalan-English. We compile our training corpus out of existing resources of varying quality and a new high-quality corpus. We also provide new evaluation translation datasets in three different domains. In the process of building Catalan-English parallel resources, we evaluate the impact of drastically filtering alignments in the resulting MT engines. Our results show that even when resources are limited, as in this case, it is worth filtering for quality. We further explore the cross-lingual transfer learning capabilities of the proposed model for parallel corpus filtering by applying it to other languages. All resources generated in this work are released under open license to encourage the development of language technology in Catalan.},
address = {Marseille, France},
author = {{de Gibert Bonet}, Ona and Kharitonova, Ksenia and {Calvo Figueras}, Blanca and Armengol-Estap{\'{e}}, Jordi and Melero, Maite},
booktitle = {Proceedings of the the 1st Annual Meeting of the ELRA/ISCA Special Interest Group on Under-Resourced Languages},
pages = {59--69},
publisher = {European Language Resources Association},
title = {{Quality versus Quantity: Building Catalan-English MT Resources}},
url = {http://www.lrec-conf.org/proceedings/lrec2022/workshops/SIGUL/pdf/2022.sigul-1.8.pdf},
year = {2022}
}
```

### Contributions

[N/A]
