---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- ca
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Catalan Textual Corpus
size_categories:
- 10M<n<100M
source_datasets:
- original
- extended|opus_dogc
- extended|cawac
- extended|oscar
- extended|open_subtitles
- extended|wikipedia
- extended|projecte-aina/catalan_general_crawling
- extended|projecte-aina/catalan_government_crawling
task_categories:
- fill-mask
task_ids: []
---

# Dataset Card for Catalan Textual Corpus

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

- **Homepage:** https://zenodo.org/record/4519349
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Point of Contact:** [ona.degibert@bsc.es](ona.degibert@bsc.es)

### Dataset Summary

The Catalan Textual Corpus is a 1760-million-token web corpus of Catalan built from several sources.

It consists of 1,758,388,896 tokens, 73,172,152 sentences, and 12,556,365 documents. Documents are separated by single new lines. These boundaries have been preserved as long as the license allowed it.

### Supported Tasks and Leaderboards

This corpus is mainly intended to pretrain language models and word representations.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{'text': "L'operatiu continuarà durant aquest divendres."}
```

### Data Fields

- `text` (str): Text.

### Data Splits

The dataset contains a single split: `train`.

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

The Catalan Textual Corpus is a 1760-million-token web corpus of Catalan built from several sources: existing corpora such as DOGC, CaWac (non-dedup version), Oscar (unshuffled version), Open Subtitles, Catalan Wikipedia, and three brand new crawlings: the Catalan General Crawling, obtained by crawling the 500 most popular .cat and .ad domains; the Catalan Government Crawling, obtained by crawling the .gencat domain and subdomains, belonging to the Catalan Government; and the ACN corpus with 220k news items from March 2015 until October 2020, crawled from the Catalan News Agency.
For preprocessing we used [Corpus-Cleaner](https://github.com/TeMU-BSC/corpus-cleaner-acl), a modular Python-based toolkit to clean raw text corpora through generator pipelines.

#### Who are the source language producers?

The original data comes from various sources: existing corpora and crawlings from public websites.

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

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that since the data comes from unreliable web pages and multilingual crawled corpora, some biases may be present in the dataset. Nonetheless, we have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Licensing Information

[Creative Commons Attribution Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/).

### Citation Information

```
@inproceedings{armengol-estape-etal-2021-multilingual,
    title = "Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? {A} Comprehensive Assessment for {C}atalan",
    author = "Armengol-Estap{\'e}, Jordi  and
      Carrino, Casimiro Pio  and
      Rodriguez-Penagos, Carlos  and
      de Gibert Bonet, Ona  and
      Armentano-Oller, Carme  and
      Gonzalez-Agirre, Aitor  and
      Melero, Maite  and
      Villegas, Marta",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.437",
    doi = "10.18653/v1/2021.findings-acl.437",
    pages = "4933--4946",
    eprint={2107.07903},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.