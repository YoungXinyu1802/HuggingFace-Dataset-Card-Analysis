---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- ca
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: ViquiQuAD
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# ViquiQuAD, An extractive QA dataset for Catalan, from the Wikipedia

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

- **Homepage:** https://zenodo.org/record/4562345#.YK41aqGxWUk
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Point of Contact:** [Carlos Rodríguez-Penagos](mailto:carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](mailto:carme.armentano@bsc.es)

### Dataset Summary

ViquiQuAD, An extractive QA dataset for Catalan, from the Wikipedia.

This dataset contains 3111 contexts extracted from a set of 597 high quality original (no translations) articles in the Catalan Wikipedia "[Viquipèdia](https://ca.wikipedia.org/wiki/Portada)", and 1 to 5 questions with their answer for each fragment.

Viquipedia articles are used under [CC-by-sa](https://creativecommons.org/licenses/by-sa/3.0/legalcode) licence. 

This dataset can be used to fine-tune and evaluate extractive-QA and Language Models. 

### Supported Tasks and Leaderboards

Extractive-QA, Language Model

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'id': 'P_66_C_391_Q1',
  'title': 'Xavier Miserachs i Ribalta',
  'context': "En aquesta època es va consolidar el concepte modern del reportatge fotogràfic, diferenciat del fotoperiodisme[n. 2] i de la fotografia documental,[n. 3] pel que fa a l'abast i el concepte. El reportatge fotogràfic implica més la idea de relat: un treball que vol més dedicació de temps, un esforç d'interpretació d'una situació i que culmina en un conjunt d'imatges. Això implica, d'una banda, la reivindicació del fotògraf per opinar, fet que li atorgarà estatus d'autor; l'autor proposa, doncs, una interpretació pròpia de la realitat. D'altra banda, el consens que s'estableix entre la majoria de fotògrafs és que el vehicle natural de la imatge fotogràfica és la pàgina impresa. Això suposà que revistes com Life, Paris-Match, Stern o Época assolissin la màxima esplendor en aquest període.",
  'question': 'De què es diferenciava el reportatge fotogràfic?',
  'answers': [{
    'text': 'del fotoperiodisme[n. 2] i de la fotografia documental',
    'answer_start': 92
  }]
}
```

### Data Fields

Follows [Rajpurkar, Pranav et al. (2016)](http://arxiv.org/abs/1606.05250) for SQuAD v1 datasets.

- `id` (str): Unique ID assigned to the question.
- `title` (str): Title of the Wikipedia article.
- `context` (str): Wikipedia section text.
- `question` (str): Question.
- `answers` (list): List of answers to the question, each containing:
  - `text` (str): Span text answering to the question.
  - `answer_start` Starting offset of the span text answering to the question.

### Data Splits

- train: 11259 examples
- developement: 1493 examples
- test: 1428 examples


## Dataset Creation

### Curation Rationale

We hope this dataset contributes to the development of language models in Catalan, a low-resource language.

### Source Data

- [Catalan Wikipedia](https://ca.wikipedia.org)

#### Initial Data Collection and Normalization

The source data are scraped articles from the [Catalan wikipedia](https://ca.wikipedia.org) site.

From a set of high quality, non-translation, articles in the Catalan Wikipedia, 597 were randomly chosen, and from them 3111, 5-8 sentence contexts were extracted. We commissioned creation of between 1 and 5 questions for each context, following an adaptation of the guidelines from SQuAD 1.0 ([Rajpurkar, Pranav et al. (2016)](http://arxiv.org/abs/1606.05250)). In total, 15153 pairs of a question and an extracted fragment that contains the answer were created.

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines.

#### Who are the source language producers?

Volunteers who collaborate with Catalan Wikipedia. 

### Annotations

#### Annotation process

We commissioned the creation of 1 to 5 questions for each context, following an adaptation of the guidelines from SQuAD 1.0 ([Rajpurkar, Pranav et al. (2016)](http://arxiv.org/abs/1606.05250)).

#### Who are the annotators?

Annotation was commissioned to an specialized company that hired a team of native language speakers.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this dataset contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International License</a>.

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
}
```


[DOI](https://doi.org/10.5281/zenodo.4562344)


### Contributions

[N/A]