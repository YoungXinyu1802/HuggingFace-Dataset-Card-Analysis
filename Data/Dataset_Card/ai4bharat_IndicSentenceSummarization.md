---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- as
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- ta
- te
license:
- cc-by-nc-4.0
multilinguality:
- multilingual
pretty_name: IndicSentenceSummarization
size_categories:
- 5K<n<112K
source_datasets:
- original for Hindi, and modified [IndicGLUE](https://indicnlp.ai4bharat.org/indic-glue/) for other languages.
task_categories:
- conditional-text-generation
task_ids:
- conditional-text-generation-other-sentence-summarization
---

# Dataset Card for "IndicSentenceSummarization"

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

IndicSentenceSummarization is the sentence summarization dataset released as part of IndicNLG Suite. Each 
input sentence is paired with an output as summary. We create this dataset in eleven 
languages including as, bn, gu, hi, kn, ml, mr, or, pa, ta, te. The total
size of the dataset is 431K. 


### Supported Tasks and Leaderboards

**Tasks:** Sentence Summarization

**Leaderboards:** Currently there is no Leaderboard for this dataset.

### Languages
-  `Assamese (as)`
-  `Bengali (bn)`
-  `Gujarati (gu)`
-  `Kannada (kn)`
-  `Hindi (hi)`
-  `Malayalam (ml)`
-  `Marathi (mr)`
-  `Oriya (or)`
-  `Punjabi (pa)`
-  `Tamil (ta)`
-  `Telugu (te)`

## Dataset Structure

### Data Instances

One random example from the `hi` dataset is given below in JSON format. 
  ```
  {'id': '5',
 'input': 'जम्मू एवं कश्मीर के अनंतनाग जिले में शनिवार को सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादियों को मार गिराया गया।',
 'target': 'जम्मू-कश्मीर : सुरक्षाबलों के साथ मुठभेड़ में 2 आतंकवादी ढेर',
 'url': 'https://www.indiatv.in/india/national-jammu-kashmir-two-millitant-killed-in-encounter-with-security-forces-574529'
}

  ```

### Data Fields
-  `id (string)`: Unique identifier.
-  `input (string)`: Input sentence.
-  `target (strings)`: Output summary.
-  `url (string)`: Source web link of the sentence. 


### Data Splits

Here is the number of samples in each split for all the languages.




Language	|	ISO 639-1 Code	|	Train	|	Dev	|	Test	|
----------	|	----------	|	----------	|	----------	|	----------	|
Assamese	|	as	|	10,812	|	5,232	|	5,452	|
Bengali	|	bn	|	17,035	|	2,355	|	2,384	|
Gujarati	|	gu	|	54,788	|	8,720	|	8,460	|
Hindi	|	hi	|	78,876	|	16,935	|	16,835	|
Kannada	|	kn	|	61,220	|	9,024	|	1,485	|
Malayalam	|	ml	|	2,855	|	1,520	|	1,580	|
Marathi	|	mr 	|	27,066	|	3,249	|	3,309	|
Oriya	|	or	|	12,065	|	1,539	|	1,440	|
Punjabi	|	pa 	|	31,630	|	4,004	|	3,967	|
Tamil	|	ta 	|	23,098	|	2,874	|	2,948	|
Telugu	|	te 	|	7,119	|	878	|	862	|

## Dataset Creation

### Curation Rationale

[Detailed in the paper](https://arxiv.org/abs/2203.05437)

### Source Data

It is a modified subset of [IndicHeadlineGeneration](https://huggingface.co/datasets/ai4bharat/IndicHeadlineGeneration) dataset.

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