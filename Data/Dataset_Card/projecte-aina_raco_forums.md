---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- ca
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
pretty_name: Racó Forums
size_categories:
- ?
task_categories:
- fill-mask
task_ids: []
---

# Dataset Card for Racó Forums Corpus

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

- **Point of Contact:** [blanca.calvo@bsc.es](blanca.calvo@bsc.es)

### Dataset Summary

The Racó Forums Corpus is a 19-million-sentence corpus of Catalan user-generated text built from the forums of [Racó Català](https://www.racocatala.cat/forums).

Since the existing available corpora in Catalan lacked conversational data, we searched for a major source of such data for Catalan, and we found Racó Català, a popular multitopic online forum. We obtained a database dump and we transformed all the threads so that we obtained documents that traversed all the existing paths from the root (initial comment) to the leaves (last comment with no reply). In other words, if T is a tree such that T = {A,B,C,D} and the first comment is A that is replied by B and C independently, and, then, C is replied by D,  we obtain two different documents A,B and A,C,D in the fairseq language modeling format.

### Supported Tasks and Leaderboards

This corpus is mainly intended to pretrain language models and word representations.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

The sentences are ordered to preserve the forum structure of comments and answers. T is a tree such that T = {A,B,C,D} and the first comment is A that is replied by B and C independently, and, then, C is replied by D,  we obtain two different documents A,B and A,C,D in the fairseq language modeling format.

### Data Instances

```
Ni la Paloma, ni la Razz, ni Bikini, ni res: la cafeteria Slàvia, a Les borges Blanques. Quin concertàs el d'ahir de Pomada!!! Fuà!!! va ser tan tan tan tan tan tan tan bo!!! Flipant!!! Irrepetible!! 
És cert, l'Slàvia mola màxim. 
```

### Data Splits

The dataset contains two splits: `train` and `valid`.

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language. The data was structured to preserve the dialogue structure of forums.

### Source Data

#### Initial Data Collection and Normalization

The data was structured and anonymized by the BSC.

#### Who are the source language producers?

The data was provided by Racó Català. 

### Annotations

The dataset is unannotated.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

The data was annonymised to remove user names and emails, which were changed to random Catalan names. The mentions to the chat itself have also been changed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that, since the data comes from user-generated forums, this will contain biases, hate speech and toxic content. We have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es).

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

[Creative Commons Attribution Non-commercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/).

### Citation Information

```

```

### Contributions

Thanks to Racó Català for sharing their data.
