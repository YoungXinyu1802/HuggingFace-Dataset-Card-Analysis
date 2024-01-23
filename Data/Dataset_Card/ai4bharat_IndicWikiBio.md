---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- as
- bn
- hi
- kn
- ml
- or
- pa
- ta
- te
license:
- cc-by-nc-4.0
multilinguality:
- multilingual
pretty_name: IndicWikiBio
size_categories:
- 1960<n<11,502
source_datasets:
- none. Originally generated from www.wikimedia.org.
task_categories:
- conditional-text-generation
task_ids:
- conditional-text-generation-other-wikibio
---

# Dataset Card for "IndicWikiBio"

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
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

- **Homepage:** https://indicnlp.ai4bharat.org/indicnlg-suite
- **Paper:** [IndicNLG Suite: Multilingual Datasets for Diverse NLG Tasks in Indic Languages](https://arxiv.org/abs/2203.05437)
- **Point of Contact:** 

### Dataset Summary

The WikiBio dataset released as part of IndicNLG Suite. Each 
example has four fields: id, infobox, serialized infobox and summary. We create this dataset in nine 
languages including as, bn, hi, kn, ml, or, pa, ta, te. The total
size of the dataset is 57,426. 


### Supported Tasks and Leaderboards

**Tasks:** WikiBio

**Leaderboards:** Currently there is no Leaderboard for this dataset.

### Languages
-  `Assamese (as)`
-  `Bengali (bn)`
-  `Kannada (kn)`
-  `Hindi (hi)`
-  `Malayalam (ml)`
-  `Oriya (or)`
-  `Punjabi (pa)`
-  `Tamil (ta)`
-  `Telugu (te)`

## Dataset Structure

### Data Instances

One random example from the `hi` dataset is given below in JSON format. 
  ```
  {
  "id": 26, 
  "infobox": "name_1:सी॰\tname_2:एल॰\tname_3:रुआला\toffice_1:सांसद\toffice_2:-\toffice_3:मिजोरम\toffice_4:लोक\toffice_5:सभा\toffice_6:निर्वाचन\toffice_7:क्षेत्र\toffice_8:।\toffice_9:मिजोरम\tterm_1:2014\tterm_2:से\tterm_3:2019\tnationality_1:भारतीय", 
  "serialized_infobox": "<TAG> name </TAG> सी॰ एल॰ रुआला <TAG> office </TAG> सांसद - मिजोरम लोक सभा निर्वाचन क्षेत्र । मिजोरम <TAG> term </TAG> 2014 से 2019 <TAG> nationality </TAG> भारतीय", 
  "summary": "सी॰ एल॰ रुआला भारत की सोलहवीं लोक सभा के सांसद हैं।"
  }

  ```

### Data Fields
-  `id (string)`: Unique identifier.
-  `infobox (string)`: Raw Infobox.
-  `serialized_infobox (string)`: Serialized Infobox as input.
-  `summary (string)`: Summary of Infobox/First line of Wikipedia page. 


### Data Splits

Here is the number of samples in each split for all the languages.




Language	|	ISO 639-1 Code	|	Train	|	Test  |	Val  |
----------	|	----------	|	----------	|	----------	|	----------	|
Assamese	|	as  |	1,300	|	391	|	381	|
Bengali	|	bn	|	4,615	|	1,521	|	1,567	|
Hindi	|	hi	|	5,684	|	1,919	|	1,853	|
Kannada	|	kn	|	1,188	|	389	|	383	|
Malayalam	|	ml	|	5,620	|	1,835	|	1,896	|
Oriya	|	or	|	1,687	|	558	|	515	|
Punjabi	|	pa 	|	3,796	|	1,227	|	1,331	|
Tamil	|	ta 	|	8,169	|	2,701	|	2,632	|
Telugu	|	te 	|	2,594	|	854	|	820	|


## Dataset Creation

### Curation Rationale

[Detailed in the paper](https://arxiv.org/abs/2203.05437)

### Source Data

None

#### Initial Data Collection and Normalization

[Detailed in the paper](https://arxiv.org/abs/2203.05437)


#### Who are the source language producers?

[Detailed in the paper](https://arxiv.org/abs/2203.05437)


### Annotations
[More information needed]
#### Annotation process
[More information needed]

#### Who are the annotators?

[More information needed]

### Personal and Sensitive Information

[More information needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More information needed]

### Discussion of Biases

[More information needed]

### Other Known Limitations

[More information needed]

## Additional Information

### Dataset Curators

[More information needed]

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). Copyright of the dataset contents belongs to the original copyright holders.
### Citation Information

If you use any of the datasets, models or code modules, please cite the following paper:
```
@inproceedings{Kumar2022IndicNLGSM,
  title={IndicNLG Suite: Multilingual Datasets for Diverse NLG Tasks in Indic Languages},
  author={Aman Kumar and Himani Shrotriya and Prachi Sahu and Raj Dabre and Ratish Puduppully and Anoop Kunchukuttan and Amogh Mishra and Mitesh M. Khapra and Pratyush Kumar},
  year={2022},
  url = "https://arxiv.org/abs/2203.05437",     
```


### Contributions

[Detailed in the paper](https://arxiv.org/abs/2203.05437)
