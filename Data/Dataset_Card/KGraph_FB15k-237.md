---
annotations_creators:
- found
- crowdsourced
language:
- en
language_creators: []
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: FB15k-237
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- knowledge graph
- knowledge
- link prediction
- link
task_categories:
- other
task_ids: []
---

# Dataset Card for FB15k-237

## Table of Contents
- [Dataset Card for FB15k-237](#dataset-card-for-fb15k-237)
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

- **Homepage:** [https://deepai.org/dataset/fb15k-237](https://deepai.org/dataset/fb15k-237)
- **Repository:** 
- **Paper:** [More Information Needed](https://paperswithcode.com/dataset/fb15k-237)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

FB15k-237 is a link prediction dataset created from FB15k. While FB15k consists of 1,345 relations, 14,951 entities, and 592,213 triples, many triples are inverses that cause leakage from the training to testing and validation splits. FB15k-237 was created by Toutanova and Chen (2015) to ensure that the testing and evaluation datasets do not have inverse relation test leakage. In summary, FB15k-237 dataset contains 310,079 triples with 14,505 entities and 237 relation types.

### Supported Tasks and Leaderboards

Supported Tasks: link prediction task on knowledge graphs.

Leaderboads:
[More Information Needed](https://paperswithcode.com/sota/link-prediction-on-fb15k-237)

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

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

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@inproceedings{schlichtkrull2018modeling,
  title={Modeling relational data with graph convolutional networks},
  author={Schlichtkrull, Michael and Kipf, Thomas N and Bloem, Peter and Berg, Rianne van den and Titov, Ivan and Welling, Max},
  booktitle={European semantic web conference},
  pages={593--607},
  year={2018},
  organization={Springer}
}
```

### Contributions

Thanks to [@pp413](https://github.com/pp413) for adding this dataset.