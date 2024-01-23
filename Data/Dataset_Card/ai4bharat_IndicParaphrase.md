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
pretty_name: IndicParaphrase
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- conditional-text-generation
task_ids:
- conditional-text-generation-other-paraphrase-generation
---

# Dataset Card for "IndicParaphrase"

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

IndicParaphrase is the paraphrasing dataset released as part of IndicNLG Suite. Each 
input is paired with up to 5 references. We create this dataset in eleven 
languages including as, bn, gu, hi, kn, ml, mr, or, pa, ta, te. The total
size of the dataset is 5.57M. 


### Supported Tasks and Leaderboards

**Tasks:** Paraphrase generation

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

One example from the `hi` dataset is given below in JSON format. 
  ```
  {
    'id': '1',
 'input': 'निजी क्षेत्र में प्रदेश की 75 प्रतिशत नौकरियां हरियाणा के युवाओं के लिए आरक्षित की जाएगी।',
 'references': ['प्रदेश के युवाओं को निजी उद्योगों में 75 प्रतिशत आरक्षण देंगे।',
  'युवाओं के लिए हरियाणा की सभी प्राइवेट नौकरियों में 75 प्रतिशत आरक्षण लागू किया जाएगा।',
  'निजी क्षेत्र में 75 प्रतिशत आरक्षित लागू कर प्रदेश के युवाओं का रोजगार सुनिश्चत किया जाएगा।',
  'प्राईवेट कम्पनियों में हरियाणा के नौजवानों को 75 प्रतिशत नौकरियां में आरक्षित की जाएगी।',
  'प्रदेश की प्राइवेट फैक्टरियों में 75 फीसदी रोजगार हरियाणा के युवाओं के लिए आरक्षित किए जाएंगे।'],
 'target': 'प्रदेश के युवाओं को निजी उद्योगों में 75 प्रतिशत आरक्षण देंगे।'
}
  ```

### Data Fields
-  `id (string)`: Unique identifier.
-  `pivot (string)`: English sentence used as the pivot 
-  `input (string)`: Input sentence 
-  `references (list of strings)`: Paraphrases of `input`, ordered according to the least n-gram overlap
-  `target (string)`: The first reference (most dissimilar paraphrase) 



### Data Splits

We first select 10K instances each for the validation and test and put remaining in the training dataset. `Assamese (as)`, due to its low-resource nature, could only be split into validation and test sets with 4,420 examples each.
Individual dataset with train-dev-test example counts are given below:


Language      | ISO 639-1 Code |Train | Dev | Test |
--------------|----------------|-------|-----|------|
Assamese | as | - | 4,420 | 4,420 |
Bengali | bn | 890,445 | 10,000 | 10,000 |
Gujarati | gu |  379,202 | 10,000 | 10,000 |
Hindi | hi | 929,507 | 10,000 | 10,000 |
Kannada | kn |  522,148 | 10,000 | 10,000 | 
Malayalam | ml |761,933  | 10,000 | 10,000 | 
Marathi | mr |406,003 | 10,000 | 10,000 | 
Oriya | or | 105,970 | 10,000 | 10,000 | 
Punjabi | pa |  266,704 | 10,000 | 10,000 | 
Tamil | ta | 497,798 | 10,000 | 10,000 | 
Telugu | te | 596,283 | 10,000 | 10,000 |


## Dataset Creation

### Curation Rationale

[More information needed]

### Source Data

[Samanantar dataset](https://indicnlp.ai4bharat.org/samanantar/)

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
  url = "https://arxiv.org/abs/2203.05437"
}  
```


### Contributions

