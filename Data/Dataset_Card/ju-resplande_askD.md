---
annotations_creators:
- no-annotation
language_creators:
- found
- machine-generated
language:
- en
- pt
license:
- lgpl-3.0
multilinguality:
- multilingual
- translation
size_categories:
- 100K<n<1M
source_datasets:
- extended|eli5
task_categories:
- text2text-generation
task_ids:
- abstractive-qa
- closed-domain-qa
pretty_name: AskDocs
---

# Dataset Card for askD

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

- **Repository:** https://github.com/ju-resplande/askD
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

[ELI5 dataset](https://huggingface.co/datasets/eli5) adapted on [Medical Questions (AskDocs)](https://www.reddit.com/r/AskDocs/) subreddit.
We additionally translated to Portuguese and used <a href="https://github.com/LasseRegin/medical-question-answer-data"> external data from here<a>.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The language data in AskD is English (BCP-47 en) and Brazilian Portuguese (BCP-47 pt-BR) 

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

|                             | Train  | Valid | Test | External |
| -----                       | ------ | ----- | ---- | -------- |
| en                          | 24256  |  5198 | 5198 | 166804   |
| pt                          | 24256  |  5198 | 5198 | 166804   |
 

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

 The dataset questions and answers span a period from January 2013 to December 2019.

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

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```bibtex
@misc{Gomes20202,
  author = {GOMES, J. R. S.},
  title = {PLUE: Portuguese Language Understanding Evaluation},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ju-resplande/askD}},
  commit = {42060c4402c460e174cbb75a868b429c554ba2b7}
}
```

### Contributions

Thanks to [@ju-resplande](https://github.com/ju-resplande) for adding this dataset.