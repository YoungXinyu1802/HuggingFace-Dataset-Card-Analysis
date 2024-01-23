---
annotations_creators:
- found
language_creators:
- found
language:
- bn
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100k<n<1M
source_datasets:
- original
task_categories:
- text2text-generation
task_ids: []
pretty_name: BanglaParaphrase
tags:
- conditional-text-generation
- paraphrase-generation
---

# Dataset Card for "BanglaParaphrase"

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

- **Repository:** [https://github.com/csebuetnlp/banglaparaphrase](https://github.com/csebuetnlp/banglaparaphrase)
- **Paper:** [BanglaParaphrase: A High-Quality Bangla Paraphrase Dataset](https://arxiv.org/abs/2210.05109)
- **Point of Contact:** [Najrin Sultana](mailto:nazrinshukti@gmail.com)

### Dataset Summary

We present BanglaParaphrase, a high quality synthetic Bangla paraphrase dataset containing about 466k paraphrase pairs. 
The paraphrases ensures high quality by being semantically coherent and syntactically diverse.

### Supported Tasks and Leaderboards

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

### Languages

-  `bengali`


## Loading the dataset
```python
from datasets import load_dataset

from datasets import load_dataset

ds = load_dataset("csebuetnlp/BanglaParaphrase")
```

## Dataset Structure

### Data Instances

One example from the `train` part of the dataset is given below in JSON format. 
```
{
"source": "বেশিরভাগ সময় প্রকৃতির দয়ার ওপরেই বেঁচে থাকতেন উপজাতিরা।", 
"target": "বেশিরভাগ সময়ই উপজাতিরা প্রকৃতির দয়ার উপর নির্ভরশীল ছিল।"
}
  ```

### Data Fields
-  'source': A string representing the source sentence.
-  'target': A string representing the target sentence.

### Data Splits
Dataset  with  train-dev-test  example  counts  are  given  below:

Language       | ISO  639-1  Code | Train | Validation | Test |
-------------- | ---------------- | ------- | ----- | ------ |
Bengali | bn | 419, 967 | 233, 31 | 233, 32 |


## Dataset Creation

### Curation Rationale

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

### Source Data

[Roar Bangla](https://roar.media/bangla)

#### Initial Data Collection and Normalization

[Detailed in the paper](https://arxiv.org/abs/2210.05109) 


#### Who are the source language producers?

[Detailed in the paper](https://arxiv.org/abs/2210.05109) 


### Annotations

[Detailed in the paper](https://arxiv.org/abs/2210.05109) 


#### Annotation process

[Detailed in the paper](https://arxiv.org/abs/2210.05109) 

#### Who are the annotators?

[Detailed in the paper](https://arxiv.org/abs/2210.05109) 

### Personal and Sensitive Information

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

## Considerations for Using the Data

### Social Impact of Dataset

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

### Discussion of Biases

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

### Other Known Limitations

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

## Additional Information

### Dataset Curators

[More information needed](https://github.com/csebuetnlp/banglaparaphrase)

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.
### Citation Information
```
@article{akil2022banglaparaphrase,
  title={BanglaParaphrase: A High-Quality Bangla Paraphrase Dataset},
  author={Akil, Ajwad and Sultana, Najrin and Bhattacharjee, Abhik and Shahriyar, Rifat},
  journal={arXiv preprint arXiv:2210.05109},
  year={2022}
}
```

### Contributions
