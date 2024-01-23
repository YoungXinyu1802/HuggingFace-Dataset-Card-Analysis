---
annotations_creators:
- machine-generated
language_creators:
- found
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- extended
task_categories:
- question-answering
task_ids:
- open-domain-qa
- extractive-qa
language:
- bn
license:
- cc-by-nc-sa-4.0
---

# Dataset Card for `squad_bn`

## Table of Contents
- [Dataset Card for `squad_bn`](#dataset-card-for-squad_bn)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
    - [Usage](#usage)
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

- **Repository:** [https://github.com/csebuetnlp/banglabert](https://github.com/csebuetnlp/banglabert)
- **Paper:** [**"BanglaBERT: Combating Embedding Barrier in Multilingual Models for Low-Resource Language Understanding"**](https://arxiv.org/abs/2101.00204)
- **Point of Contact:** [Tahmid Hasan](mailto:tahmidhasan@cse.buet.ac.bd)

### Dataset Summary

This is a Question Answering (QA) dataset for Bengali, curated from the [SQuAD 2.0](), [TyDI-QA]() datasets and using the state-of-the-art English to Bengali translation model introduced **[here](https://aclanthology.org/2020.emnlp-main.207/).**


### Supported Tasks and Leaderboards

[More information needed](https://github.com/csebuetnlp/banglabert)

### Languages

* `Bengali`

### Usage
```python
from datasets import load_dataset
dataset = load_dataset("csebuetnlp/squad_bn")
```
## Dataset Structure

### Data Instances

One example from the dataset is given below in JSON format. 
  ```
  {
    "title": "শেখ মুজিবুর রহমান",
    "paragraphs": [
        {
            "qas": [
                {
                    "answers": [
                        {
                            "answer_start": 19,
                            "text": "১৭ মার্চ ১৯২০"
                        }
                    ],
                    "id": "bengali--981248442377505718-0-2649",
                    "question": "শেখ মুজিবুর রহমান কবে জন্মগ্রহণ করেন ?"
                }
            ],
            "context": "শেখ মুজিবুর রহমান (১৭ মার্চ ১৯২০ - ১৫ আগস্ট ১৯৭৫) বাংলাদেশের প্রথম রাষ্ট্রপতি ও ভারতীয় উপমহাদেশের একজন অন্যতম প্রভাবশালী রাজনৈতিক ব্যক্তিত্ব যিনি বাঙালীর অধিকার রক্ষায় ব্রিটিশ ভারত থেকে ভারত বিভাজন আন্দোলন এবং পরবর্তীতে  পূর্ব পাকিস্তান থেকে বাংলাদেশ প্রতিষ্ঠার সংগ্রামে নেতৃত্ব প্রদান করেন। প্রাচীন বাঙ্গালি সভ্যতার আধুনিক স্থপতি হিসাবে শেখ মুজিবুর রহমানকে বাংলাদেশের জাতির জনক বা জাতির পিতা বলা হয়ে থাকে। তিনি মাওলানা আব্দুল হামিদ খান ভাসানী প্রতিষ্ঠিত আওয়ামী লীগের সভাপতি, বাংলাদেশের প্রথম রাষ্ট্রপতি এবং পরবর্তীতে এদেশের প্রধানমন্ত্রীর দায়িত্ব পালন করেন। জনসাধারণের কাছে তিনি শেখ মুজিব এবং শেখ সাহেব হিসাবে বেশি পরিচিত এবং তার উপাধি বঙ্গবন্ধু। তার কন্যা শেখ হাসিনা বাংলাদেশ আওয়ামী লীগের বর্তমান সভানেত্রী এবং বাংলাদেশের বর্তমান প্রধানমন্ত্রী।"
        }
    ]
}
  ```

### Data Fields

The data fields are as follows:

- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.


### Data Splits
|   split   |count  |
|----------|--------|
|`train`|  127771 |
|`validation`| 2502  |
|`test`| 2504 |




## Dataset Creation

For the training set, we translated the complete [SQuAD 2.0](https://aclanthology.org/N18-1101/) dataset using the English to Bangla translation model introduced [here](https://aclanthology.org/2020.emnlp-main.207/). Due to the possibility of incursions of error during automatic translation, we used the [Language-Agnostic BERT Sentence Embeddings (LaBSE)](https://arxiv.org/abs/2007.01852) of the translations and original sentences to compute their similarity. A datapoint was accepted if all of its constituent sentences had a similarity score over 0.7. 

 Since the TyDI-QA Gold Passage task guarantees that the given context contains the answer and we want to pose our QA task analogous to SQuAD 2.0, we also consider examples from the Passage selection task that don't have an answer for the given question. We distribute the resultant examples from the TyDI-QA training and validation sets (which are publicly available) evenly to our test and validation sets.
 
### Curation Rationale

[More information needed](https://github.com/csebuetnlp/banglabert)

### Source Data

[SQuAD 2.0](https://arxiv.org/abs/1606.05250), [TyDi-QA](https://arxiv.org/abs/2003.05002)

#### Initial Data Collection and Normalization

[More information needed](https://github.com/csebuetnlp/banglabert)


#### Who are the source language producers?

[More information needed](https://github.com/csebuetnlp/banglabert)


### Annotations

[More information needed](https://github.com/csebuetnlp/banglabert)


#### Annotation process

[More information needed](https://github.com/csebuetnlp/banglabert)

#### Who are the annotators?

[More information needed](https://github.com/csebuetnlp/banglabert)

### Personal and Sensitive Information

[More information needed](https://github.com/csebuetnlp/banglabert)

## Considerations for Using the Data

### Social Impact of Dataset

[More information needed](https://github.com/csebuetnlp/banglabert)

### Discussion of Biases

[More information needed](https://github.com/csebuetnlp/banglabert)

### Other Known Limitations

[More information needed](https://github.com/csebuetnlp/banglabert)

## Additional Information

### Dataset Curators

[More information needed](https://github.com/csebuetnlp/banglabert)

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.
### Citation Information

If you use the dataset, please cite the following paper:
```
@misc{bhattacharjee2021banglabert,
      title={BanglaBERT: Combating Embedding Barrier in Multilingual Models for Low-Resource Language Understanding},
      author={Abhik Bhattacharjee and Tahmid Hasan and Kazi Samin and Md Saiful Islam and M. Sohel Rahman and Anindya Iqbal and Rifat Shahriyar},
      year={2021},
      eprint={2101.00204},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


### Contributions

Thanks to [@abhik1505040](https://github.com/abhik1505040) and [@Tahmid](https://github.com/Tahmid04) for adding this dataset.