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
pretty_name: IndicQuestionGeneration
size_categories:
- 98K<n<98K
source_datasets:
- we start with the SQuAD question answering dataset repurposed to serve as a question generation dataset. We translate this dataset into different Indic languages.
task_categories:
- conditional-text-generation
task_ids:
- conditional-text-generation-other-question-generation
---

# Dataset Card for "IndicQuestionGeneration"

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

IndicQuestionGeneration is the question generation dataset released as part of IndicNLG Suite. Each 
example has five fields: id, squad_id, answer, context and question. We create this dataset in eleven 
languages, including as, bn, gu, hi, kn, ml, mr, or, pa, ta, te. This is translated data. The examples in each language are exactly similar but in different languages. 
The number of examples in each language is 98,027.


### Supported Tasks and Leaderboards

**Tasks:** Question Generation

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
  {
  "id": 8, 
  "squad_id": "56be8e613aeaaa14008c90d3", 
  "answer": "अमेरिकी फुटबॉल सम्मेलन", 
  "context": "अमेरिकी फुटबॉल सम्मेलन (एएफसी) के चैंपियन डेनवर ब्रोंकोस ने नेशनल फुटबॉल कांफ्रेंस (एनएफसी) की चैंपियन कैरोलिना पैंथर्स को 24-10 से हराकर अपना तीसरा सुपर बाउल खिताब जीता।", 
  "question": "एएफसी का मतलब क्या है?"
  }
  ```

### Data Fields
-  `id (string)`: Unique identifier.
-  `squad_id (string)`: Unique identifier in Squad dataset.
-  `answer (strings)`: Answer as one of the two inputs.
-  `context (string)`: Context, the other input. 
-  `question (string)`: Question, the output.


### Data Splits

Here is the number of samples in each split for all the languages.




Language	|	ISO 639-1 Code	|	Train	|	Dev	|	Test	|
----------	|	----------	|	----------	|	----------	|	----------	|
Assamese	|	as	|	69,979	|	17,495	|	10,553	|
Bengali	|	bn	|	69,979	|	17,495	|	10,553	|
Gujarati	|	gu	|	69,979	|	17,495	|	10,553	|
Hindi	|	hi	|	69,979	|	17,495	|	10,553	|
Kannada	|	kn	|	69,979	|	17,495	|	10,553	|
Malayalam	|	ml	|	69,979	|	17,495	|	10,553	|
Marathi	|	mr 	|	69,979	|	17,495	|	10,553	|
Oriya	|	or	|	69,979	|	17,495	|	10,553	|
Punjabi	|	pa 	|	69,979	|	17,495	|	10,553	|
Tamil	|	ta 	|	69,979	|	17,495	|	10,553	|
Telugu	|	te 	|	69,979	|	17,495	|	10,553	|


## Dataset Creation

### Curation Rationale

[Detailed in the paper](https://arxiv.org/abs/2203.05437)

### Source Data

Squad Dataset(https://rajpurkar.github.io/SQuAD-explorer/)

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