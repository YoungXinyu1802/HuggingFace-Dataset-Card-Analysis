---
annotations_creators:
- other
language_creators:
- other
language:
- en
- es
language_bcp47:
- en-US
- es-ES
license:
- cc-by-nc-nd-4.0
multilinguality:
- translation
pretty_name: must-c_en-es_text-only
size_categories:
- unknown
source_datasets: []
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
---

# Dataset Card for kudo-research/mustc-en-es-text-only

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

- **Homepage:** [https://ict.fbk.eu/must-c-release-v1-2/](https://ict.fbk.eu/must-c-release-v1-2/)
- **Repository:** n/a
- **Paper:** [MuST-C: A multilingual corpus for end-to-end speech translation](https://www.sciencedirect.com/science/article/abs/pii/S0885230820300887)
- **Leaderboard:** n/a
- **Point of Contact:** Roldano Cattoni <cattoni@fbk.eu>; Marco Turchi <turchi@fbk.eu>

### Dataset Summary

This dataset is a selection of text only (English-Spanish) from the MuST-C corpus.

MuST-C is a multilingual speech translation corpus whose size and quality will facilitate the training of end-to-end systems for SLT from English into 14 languages (Arabic, Chinese, Czech, Dutch, French, German, Italian, Persian, Portuguese, Romanian, Russian, Spanish, Turkish and Vietnamese).
For each target language, MuST-C comprises several hundred hours of audio recordings from English TED Talks, which are automatically aligned at the sentence level with their manual transcriptions and translations.

### Supported Tasks and Leaderboards

- `machine-translation`: The dataset can be used to train a model for machine-translation.
  [More Information Needed]

### Languages

- en-US
- es-ES

## Dataset Structure

### Data Instances

Dataset example:

```
{
  "translation": {
    "en": "I'll tell you one quick story to illustrate what that's been like for me.", 
    "es": "Les diré una rápida historia para ilustrar lo que ha sido para mí."
  }
}
```

### Data Fields

The fields are:

- `translation`: an object containing two items, constructed as key-value pairs:
  - language code (key)
  - text (value)


### Data Splits

More Information Needed...

|                         | Tain    | Valid | Test |
|-------------------------|---------|-------|------|
| Input Sentences         | 265,625 | 1316  | 2502 |
| Average Sentence Length | n/a     | n/a   | n/a  |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

TED Talks

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

[More Information Needed]

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

FBK - Fondazione Bruno Kessler, Trento, Italy
 - Roldano Cattoni, Mattia Antonino Di Gangi, Luisa Bentivogli, Matteo Negri, Marco Turchi

### Licensing Information

- TED talks are copyrighted by TED Conference LLC and licensed under a
  Creative Commons Attribution-NonCommercial-NoDerivs 4.0
(cfr. https://www.ted.com/about/our-organization/our-policies-terms/ted-talks-usage-policy) 

- the MuST-C corpus is released under the same Creative Commons
  Attribution-NonCommercial-NoDerivs 4.0 License.
### Citation Information

Bibtex reference:
```
@article{CATTONI2021101155,
title = {MuST-C: A multilingual corpus for end-to-end speech translation},
journal = {Computer Speech & Language},
volume = {66},
pages = {101155},
year = {2021},
issn = {0885-2308},
doi = {https://doi.org/10.1016/j.csl.2020.101155},
url = {https://www.sciencedirect.com/science/article/pii/S0885230820300887},
author = {Roldano Cattoni and Mattia Antonino {Di Gangi} and Luisa Bentivogli and Matteo Negri and Marco Turchi},
keywords = {Spoken language translation, Multilingual corpus},
abstract = {End-to-end spoken language translation (SLT) has recently gained popularity thanks to the advancement of sequence to sequence learning in its two parent tasks: automatic speech recognition (ASR) and machine translation (MT). However, research in the field has to confront with the scarcity of publicly available corpora to train data-hungry neural networks. Indeed, while traditional cascade solutions can build on sizable ASR and MT training data for a variety of languages, the available SLT corpora suitable for end-to-end training are few, typically small and of limited language coverage. We contribute to fill this gap by presenting MuST-C, a large and freely available Multilingual Speech Translation Corpus built from English TED Talks. Its unique features include: i) language coverage and diversity (from English into 14 languages from different families), ii) size (at least 237 hours of transcribed recordings per language, 430 on average), iii) variety of topics and speakers, and iv) data quality. Besides describing the corpus creation methodology and discussing the outcomes of empirical and manual quality evaluations, we present baseline results computed with strong systems on each language direction covered by MuST-C.}
}```

[DOI available here](https://doi.org/10.1016/j.csl.2020.101155)

### Contributions

Thanks to [@dblandan](https://github.com/dblandan) for adding this dataset.
