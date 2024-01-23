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
- text-classification
task_ids:
- natural-language-inference
language:
- bn
license:
- cc-by-nc-sa-4.0
---

# Dataset Card for `xnli_bn`

## Table of Contents
- [Dataset Card for `xnli_bn`](#dataset-card-for-xnli_bn)
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

This is a Natural Language Inference (NLI) dataset for Bengali, curated using the subset of
MNLI data used in XNLI and state-of-the-art English to Bengali translation model introduced **[here](https://aclanthology.org/2020.emnlp-main.207/).**


### Supported Tasks and Leaderboards

[More information needed](https://github.com/csebuetnlp/banglabert)

### Languages

* `Bengali`

### Usage
```python
from datasets import load_dataset
dataset = load_dataset("csebuetnlp/xnli_bn")
```
## Dataset Structure

### Data Instances

One example from the dataset is given below in JSON format. 
  ```
  {
    "sentence1": "আসলে, আমি এমনকি এই বিষয়ে চিন্তাও করিনি, কিন্তু আমি এত হতাশ হয়ে পড়েছিলাম যে, শেষ পর্যন্ত আমি আবার তার সঙ্গে কথা বলতে শুরু করেছিলাম",
    "sentence2": "আমি তার সাথে আবার কথা বলিনি।",
    "label": "contradiction"
}
  ```

### Data Fields

The data fields are as follows:

- `sentence1`: a `string` feature indicating the premise.
- `sentence2`: a `string` feature indicating the hypothesis.
- `label`: a classification label, where possible values are `contradiction` (0), `entailment` (1), `neutral` (2) .

### Data Splits
|   split   |count  |
|----------|--------|
|`train`|  381449 |
|`validation`| 2419  |
|`test`| 4895 |




## Dataset Creation

The dataset curation procedure was the same as the [XNLI](https://aclanthology.org/D18-1269/) dataset: we translated the [MultiNLI](https://aclanthology.org/N18-1101/) training data using the English to Bangla translation model introduced [here](https://aclanthology.org/2020.emnlp-main.207/). Due to the possibility of incursions of error during automatic translation, we used the [Language-Agnostic BERT Sentence Embeddings (LaBSE)](https://arxiv.org/abs/2007.01852) of the translations and original sentences to compute their similarity. All sentences below a similarity threshold of 0.70 were discarded.

### Curation Rationale

[More information needed](https://github.com/csebuetnlp/banglabert)

### Source Data

[XNLI](https://aclanthology.org/D18-1269/)

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