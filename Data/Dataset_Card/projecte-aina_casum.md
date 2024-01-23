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

# Dataset Card for CaSum

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

- **Paper:** [Sequence to Sequence Resources for Catalan](https://arxiv.org/pdf/2202.06871.pdf)
- **Point of Contact:** [Ona de Gibert Bonet](mailto:ona.degibert@bsc.es)


### Dataset Summary

CaSum is a summarization dataset. It is extracted from a newswire corpus crawled from the Catalan News Agency ([Agència Catalana de Notícies; ACN](https://www.acn.cat/)). The corpus consists of 217,735 instances that are composed by the headline and the body.
 
### Supported Tasks and Leaderboards

The dataset can be used to train a model for abstractive summarization. Success on this task is typically measured by achieving a high Rouge score. The [mbart-base-ca-casum](https://huggingface.co/projecte-aina/bart-base-ca-casum) model currently achieves a 41.39.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'summary': 'Mapfre preveu ingressar 31.000 milions d’euros al tancament de 2018',
  'text': 'L’asseguradora llançarà la seva filial Verti al mercat dels EUA a partir de 2017 ACN Madrid.-Mapfre preveu assolir uns ingressos de 31.000 milions d'euros al tancament de 2018 i destinarà a retribuir els seus accionistes com a mínim el 50% dels beneficis del grup durant el període 2016-2018, amb una rendibilitat mitjana a l’entorn del 5%, segons ha anunciat la companyia asseguradora durant la celebració aquest divendres de la seva junta general d’accionistes. La firma asseguradora també ha avançat que llançarà la seva filial d’automoció i llar al mercat dels EUA a partir de 2017. Mapfre ha recordat durant la junta que va pagar més de 540 milions d'euros en impostos el 2015, amb una taxa impositiva efectiva del 30,4 per cent. La companyia també ha posat en marxa el Pla de Sostenibilitat 2016-2018 i el Pla de Transparència Activa, “que han de contribuir a afermar la visió de Mapfre com a asseguradora global de confiança”, segons ha informat en un comunicat.'
}
```

### Data Fields

- `summary` (str): Summary of the piece of news
- `text` (str): The text of the piece of news

### Data Splits

We split our dataset into train, dev and test splits

- train: 197,735 examples
- validation: 10,000 examples
- test: 10,000 examples

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language. There exist few resources for summarization in Catalan.

### Source Data

#### Initial Data Collection and Normalization

We obtained each headline and its corresponding body of each news piece on the Catalan News Agency ([Agència Catalana de Notícies; ACN](https://www.acn.cat/)) website and applied the following cleaning pipeline: deduplicating the documents, removing the documents with empty attributes, and deleting some boilerplate sentences. 

#### Who are the source language producers?

The news portal Catalan News Agency ([Agència Catalana de Notícies; ACN](https://www.acn.cat/)).

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

This work was funded by MT4All CEF project and [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

### BibTeX  citation

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