---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- ca
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: Catalan Government Crawling
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- fill-mask
task_ids: []
---

# Dataset Card for Catalan Government Crawling

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

- **Homepage:** https://zenodo.org/record/5511667
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Point of Contact:** [ona.degibert@bsc.es](ona.degibert@bsc.es)

### Dataset Summary

The Catalan Government Crawling Corpus is a 39-million-token web corpus of Catalan built from the web. It has been obtained by crawling the .gencat domain and subdomains, belonging to the Catalan Government during September and October 2020. It consists of 39,117,909 tokens, 1,565,433 sentences and 71,043 documents. Documents are separated by single new lines. It is a subcorpus of the Catalan Textual Corpus.

### Supported Tasks and Leaderboards

This corpus is mainly intended to pretrain language models and word representations.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'text': 'Títol: Estudi de tres marededéus del bisbat de Solsona\nResponsables del projecte: Pep Paret conservador–restaurador de l\'Àrea de Pintura i Escultura sobre fusta del CRBMC\nL\'objecte d\'aquest est
udi és un millor coneixement de l\'estat de conservació del patrimoni moble català, en concret de tres escultures romàniques del bisbat de Solsona.\nEs du a terme un estudi científic de tres marededéus del bisb
at de Solsona: la Mare de Déu de Queralt, la Mare de Déu de Coaner i la Mare de Déu de la Quar.\nLes imatges originals són romàniques, però totes elles han patit modificacions estructurals...'
}
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

The corpus has been obtained by crawling the all the `.gencat.cat` domains during July 2020.
For preprocessing we used [Corpus-Cleaner](https://github.com/TeMU-BSC/corpus-cleaner-acl), a modular Python-based toolkit to clean raw text corpora through generator pipelines.

#### Who are the source language producers?

The data comes from the official Catalan Government websites.

### Annotations

The dataset is unannotated.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Since all data comes from public websites, no anonymisation process was performed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that since the data comes from public web pages, some biases may be present in the dataset. Nonetheless, we have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Licensing Information

[Creative Commons CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

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