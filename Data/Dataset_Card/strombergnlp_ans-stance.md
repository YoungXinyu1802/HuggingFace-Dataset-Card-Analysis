---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- ar
license:
- apache-2.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- fact-checking
pretty_name: ans-stance
tags:
- stance-detection
---

# Dataset Card for AraStance
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
- **Repository:** [https://github.com/latynt/ans](https://github.com/latynt/ans)
- **Paper:** [https://arxiv.org/abs/2005.10410](https://arxiv.org/abs/2005.10410)
- **Point of Contact:** [Jude Khouja](jude@latynt.com)

### Dataset Summary
The dataset is a collection of news titles in arabic along with paraphrased and corrupted titles. The stance prediction version is a 3-class classification task. Data contains three columns: s1, s2, stance.

### Languages
Arabic

## Dataset Structure

### Data Instances
An example of 'train' looks as follows:
```
{
  'id': '0', 
  's1': 'هجوم صاروخي يستهدف مطار في طرابلس ويجبر ليبيا على تغيير مسار الرحلات الجوية', 
  's2': 'هدوء الاشتباكات فى طرابلس', 
  'stance': 0
}

```

### Data Fields
- `id`: a 'string' feature.
- `s1`: a 'string' expressing a claim/topic.
- `s2`: a 'string' to be classified for its stance to the source.
- `stance`: a class label representing the stance the article expresses towards the claim. Full tagset with indices:
```
                0: "disagree",
                1: "agree",
                2: "other",
```

### Data Splits
|name|instances|
|----|----:|
|train|2652|
|validation|755|
|test|379|

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
The dataset is curated by the paper's authors

### Licensing Information
The authors distribute this data under the Apache License, Version 2.0 

### Citation Information
```
@inproceedings{,
    title = "Stance Prediction and Claim Verification: An {A}rabic Perspective", 
    author = "Khouja, Jude",
    booktitle = "Proceedings of the Third Workshop on Fact Extraction and {VER}ification ({FEVER})",
    year = "2020",
    address = "Seattle, USA",
    publisher = "Association for Computational Linguistics",
}
```

### Contributions
Thanks to [mkonxd](https://github.com/mkonxd) for adding this dataset.