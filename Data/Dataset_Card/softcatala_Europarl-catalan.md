---
annotations_creators:
- no-annotation
language_creators:
- machine-generated
language:
- ca
- de
- en
license:
- cc-by-4.0
multilinguality:
- translation
size_categories:
- 1M<n<10M
source_datasets:
- extended|europarl_bilingual
task_categories:
- translation
task_ids: []
pretty_name: Catalan-English and Catalan-German aligned corpora to train NMT systems.
---


# Dataset Card for Tilde-MODEL-Catalan

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

- **Homepage:** https://www.softcatala.org/
- **Repository:** https://github.com/Softcatala/Europarl-catalan
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

This dataset contains two dataset pairs corresponding to the Europarl corpus. Both the English and the German version are aligned with the Catalan translation, which has been obtained using Apertium's RBMT system from the Spanish version of the Spanish-English alignment. Catalan-German alignment has been obtained using this [alignment finder](https://github.com/davidcanovas/alignment-finder-with-pivot-language) from de-en and ca-en.
- Catalan-English: 1 965 735 segments.
- Catalan-German: 1 734 644 segments.

### Supported Tasks and Leaderboards

This dataset can be used to train NMT and SMT systems.
It has been used as a training corpus for the [Softcatalà machine translation engine](https://www.softcatala.org/traductor/).

### Languages

Catalan (`ca`).
German (`de`).
English (`en`).

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

Raw text.

### Data Splits

One file for language.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

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

[@softcatala](https://github.com/Softcatala)
[@jordimas](https://github.com/jordimas)
[@davidcanovas](https://github.com/davidcanovas)

### Licensing Information

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]
