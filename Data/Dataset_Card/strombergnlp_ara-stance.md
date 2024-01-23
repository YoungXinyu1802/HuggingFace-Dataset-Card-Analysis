---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- ar
license:
- cc-by-4.0
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
pretty_name: ara-stance
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
- **Repository:** [https://github.com/Tariq60/arastance](https://github.com/Tariq60/arastance)
- **Paper:** [https://arxiv.org/abs/2104.13559](https://arxiv.org/abs/2104.13559)
- **Point of Contact:** [Tariq Alhindi](tariq@cs.columbia.edu)

### Dataset Summary
The AraStance dataset contains true and false claims, where each claim is paired with one or more documents. Each claim–article pair has a stance label: agree, disagree, discuss, or unrelated.

### Languages
Arabic

## Dataset Structure

### Data Instances
An example of 'train' looks as follows:
```
{
    'id': '0', 
    'claim': 'تم رفع صورة السيسي في ملعب ليفربول', 
    'article': 'خطفت مكة محمد صلاح نجلة نجم ليفربول الإنجليزي الأنظار في ظهورها بملعب آنفيلد عقب مباراة والدها أمام برايتون في ختام الدوري الإنجليزي والتي انتهت بفوز الأول برباعية نظيفة. وأوضحت صحيفة "ميرور" البريطانية أن مكة محمد صلاح أضفت حالة من المرح في ملعب آنفيلد أثناء مداعبة الكرة بعد تتويج نجم منتخب مصر بجائزة هداف الدوري الإنجليزي. وأشارت إلى أن مكة أظهرت بعضًا من مهاراتها بمداعبة الكرة ونجحت في خطف قلوب مشجعي الريدز.', 
    'stance': 3

}
```

### Data Fields
- `id`: a 'string' feature.
- `claim`: a 'string' expressing a claim/topic.
- `article`: a 'string' to be classified for its stance to the source.
- `stance`: a class label representing the stance the article expresses towards the claim. Full tagset with indices:
```
                0: "Agree",
                1: "Disagree",
                2: "Discuss",
                3: "Unrelated",
```

### Data Splits
|name|instances|
|----|----:|
|train|2848|
|validation|569|
|test|646|

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
The authors distribute this data under Creative Commons attribution license, CC-BY 4.0

### Citation Information
```
@article{arastance,
  url = {https://arxiv.org/abs/2104.13559},
  author = {Alhindi, Tariq and Alabdulkarim, Amal and Alshehri, Ali and Abdul-Mageed, Muhammad and Nakov, Preslav},
  title = {AraStance: A Multi-Country and Multi-Domain Dataset of Arabic Stance Detection for Fact Checking},
  year = {2021},  
  copyright = {Creative Commons Attribution 4.0 International}
}
```

### Contributions
Thanks to [mkonxd](https://github.com/mkonxd) for adding this dataset.