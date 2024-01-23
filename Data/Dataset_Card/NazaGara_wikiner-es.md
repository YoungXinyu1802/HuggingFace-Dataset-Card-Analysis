annotations_creators:
- automatic
language_creators:
- found
languages:
- es-AR
licenses:
- cc0-1.0
multilinguality:
- monolingual
paperswithcode_id:
pretty_name: wikiner
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition

---
license: cc
---

# Dataset Card for wikiner

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
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
- **Repository:** [Needs More Informatio]
- **Paper:** [Learning multilingual named entity recognition from Wikipedia](https://doi.org/10.1016/j.artint.2012.03.006)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [NazaGara](ngaragiola430@mi.unc.edu.ar)

### Dataset Summary

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities.

Example: [PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .


### Supported Tasks and Leaderboards


Named Entity Recognition (NER) is a subtask of Information Extraction. Different NER systems were evaluated as a part of the Sixth Message Understanding Conference in 1995 (MUC6). The target language was English. The participating systems performed well. However, many of them used language-specific resources for performing the task and it is unknown how they would have performed on another language than English.
After 1995 NER systems have been developed for some European languages and a few Asian languages. There have been at least two studies that have applied one NER system to different languages. Palmer and Day [PD97] have used statistical methods for finding named entities in newswire articles in Chinese, English, French, Japanese, Portuguese and Spanish. They found that the difficulty of the NER task was different for the six languages but that a large part of the task could be performed with simple methods. Cucerzan and Yarowsky [CY99] used both morphological and contextual clues for identifying named entities in English, Greek, Hindi, Rumanian and Turkish. With minimal supervision, they obtained overall F measures between 40 and 70, depending on the languages used.
- `named-entity-recognition`: The performance in this task is measured with [F1](https://huggingface.co/metrics/f1) (higher is better). A named entity is correct only if it is an exact match of the corresponding entity in the data.

This dataset was used in order to train a Spanish NER model using [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased).

### Languages

The only supported language is spanish (es).

## Dataset Structure

### Data Fields

The dictionary to map the id to the Label names is:
{
  0: 'O',
  1: 'B-PER',
  2: 'I-PER',
  3: 'B-ORG',
  4: 'I-ORG',
  5: 'B-LOC',
  6: 'I-LOC',
  7: 'B-MISC',
  8: 'I-MISC'
}

### Data Splits

The only split is the train split.
Number of examples = 128355

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

Created by Nothman et al. at 2013.

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]