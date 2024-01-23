---
annotations_creators:
- machine-generated
language_creators:
- expert-generated
language:
- ca
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets: []
task_categories:
- summarization
task_ids: []
pretty_name: casum
---

# Dataset Card for VilaSum

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

- **Paper:**[Sequence to Sequence Resources for Catalan](https://arxiv.org/pdf/2202.06871.pdf)
- **Point of Contact:** [Ona de Gibert Bonet](mailto:ona.degibert@bsc.es)

### Dataset Summary

VilaSum is a summarization dataset for evaluation. It is extracted from a newswire corpus crawled from the Catalan news portal [VilaWeb](https://www.vilaweb.cat/). The corpus consists of 13,843 instances that are composed by the headline and the body.
 
### Supported Tasks and Leaderboards

The dataset can be used to train a model for abstractive summarization. Success on this task is typically measured by achieving a high Rouge score. The [mbart-base-ca-casum](https://huggingface.co/projecte-aina/bart-base-ca-casum) model currently achieves a 35.04.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'summary': 'Un vídeo corrobora les agressions a dues animalistes en un correbou del Mas de Barberans',
  'text': 'Noves imatges, a les quals ha tingut accés l'ACN, certifiquen les agressions i la destrucció del material d'enregistrament que han denunciat dues activistes d'AnimaNaturalis en la celebració d'un acte de bous a la plaça al Mas de Barberans (Montsià). En el vídeo es veu com unes quantes persones s'abalancen sobre les noies que reben estirades i cops mentre els intenten prendre les càmeres. Membres de la comissió taurina intervenen per aturar els presumptes agressors però es pot escoltar com part del públic victoreja la situació. Els Mossos d'Esquadra presentaran aquest dilluns al migdia l'atestat dels fets al Jutjat d'Amposta. Dissabte ja es van detenir quatre persones que van quedar en llibertat a l'espera de ser cridats pel jutge. Es tracta de tres homes i una dona de Sant Carles de la Ràpita, tots ells membres de la mateixa família.'
}
```

### Data Fields

- `summary` (str): Summary of the piece of news
- `text` (str): The text of the piece of news

### Data Splits

Due to the reduced size of the dataset, we use it only for evaluation as a test set.

- test: 13,843 examples

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language. There exist few resources for summarization in Catalan.

### Source Data

#### Initial Data Collection and Normalization

We obtained each headline and its corresponding body of each news piece on [VilaWeb](https://www.vilaweb.cat/) and applied the following cleaning pipeline: deduplicating the documents, removing the documents with empty attributes, and deleting some boilerplate sentences. 

#### Who are the source language producers?

The news portal [VilaWeb](https://www.vilaweb.cat/).

### Annotations

The dataset is unannotated.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Since all data comes from public websites, no anonymization process was performed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of summarization models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that since the data comes from unreliable web pages, some biases may be present in the dataset. Nonetheless, we have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information
### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by MT4All CEF project and the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

If you use any of these resources (datasets or models) in your work, please cite our latest preprint:

```bibtex
@misc{degibert2022sequencetosequence,
      title={Sequence-to-Sequence Resources for Catalan}, 
      author={Ona de Gibert and Ksenia Kharitonova and Blanca Calvo Figueras and Jordi Armengol-Estapé and Maite Melero},
      year={2022},
      eprint={2202.06871},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

[N/A]
