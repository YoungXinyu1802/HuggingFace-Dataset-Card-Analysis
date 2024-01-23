---
annotations_creators:
- no-annotation
language:
- zh
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Book revies from DouBan Dushu.
size_categories:
- 10M<n<100M
source_datasets: []
tags: []
task_categories: []
task_ids: []
---

# Dataset Card for Douban Dushu (豆瓣读书).

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

This dataset contains book reviews from DouBan Dushu. 

DouBan DuShu is a Chinese website where users can share their reviews about various kinds of books. Most of the users in this website are unprofessional book reviewers. Therefore, the comments are usually spoken Chinese or even Internet slang.

- **Repository:** https://github.com/JaniceZhao/Douban-Dushu-Dataset
- **Paper:** LSICC: A Large Scale Informal Chinese Corpus

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Chinese

## Dataset Structure

### Data Instances

```
{
    'tag': '日本文学',
    'book_name': '厨房',
    'user_name': '林大东',
    'date': '2013-03-12',
    'comment': '满月没有另外两篇好看',
    'star': 5,
    'vote_count': 0
}
```

### Data Fields

```
{
    "tag": datasets.Value("string"),
    "book_name": datasets.Value("string"),
    "user_name": datasets.Value("string"),
    "date": datasets.Value("string"),
    "comment": datasets.Value("string"),
    "star": datasets.Value("int32"),
    "vote_count": datasets.Value("int32"),
}
```

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

https://drive.google.com/drive/folders/1Me0aswzCCMtJt3clWiA39J5i-tbREgze

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

@article{zhao2018lsicc,
  title={LSICC: A Large Scale Informal Chinese Corpus},
  author={Zhao, Jianyu and Ji, Zhuoran},
  journal={arXiv preprint arXiv:1811.10167},
  year={2018}
}

### Contributions

Thanks to [@larrylawl](https://github.com/larrylawl) for adding this dataset.