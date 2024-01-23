---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- fa
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- extended|quora|google
task_categories:
- query-paraphrasing
task_ids:
- query-paraphrasing
---

# Dataset Card for PersiNLU (Query Paraphrasing)

## Table of Contents
- [Dataset Card for PersiNLU (Query Paraphrasing)](#dataset-card-for-persi_nlu_query_paraphrasing)
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

- **Homepage:** [Github](https://github.com/persiannlp/parsinlu/)
- **Repository:** [Github](https://github.com/persiannlp/parsinlu/)
- **Paper:** [Arxiv](https://arxiv.org/abs/2012.06154)
- **Leaderboard:** 
- **Point of Contact:** d.khashabi@gmail.com

### Dataset Summary

A Persian query paraphrasng task (deciding whether two questions are paraphrases of each other). 
The questions are partially generated from Google auto-complete, and partially translated from the Quora paraphrasing dataset. 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The text dataset is in Persian (`fa`).

## Dataset Structure

### Data Instances

Here is an example from the dataset: 
```json 
{
  "q1": "اعمال حج تمتع از چه روزی شروع میشود؟",
  "q2": "ویار از چه روزی شروع میشود؟",
  "label": "0",
  "category": "natural"
}
```

### Data Fields

- `q1`: the first question.
- `q2`: the second question. 
- `category`: whether the questions are mined from Quora (`qqp`) or they're extracted from Google auto-complete (`natural`).   
- `label`: `1` if the questions are paraphrases; `0` otherwise.   

### Data Splits

The train/dev/test splits contains 1830/898/1916 samples.

## Dataset Creation

### Curation Rationale

For details, check [the corresponding draft](https://arxiv.org/abs/2012.06154).

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

[More Information Needed]

### Licensing Information

CC BY-NC-SA 4.0 License 

### Citation Information
```bibtex 
@article{huggingface:dataset,
    title = {ParsiNLU: A Suite of Language Understanding Challenges for Persian},
    authors = {Khashabi, Daniel and Cohan, Arman and Shakeri, Siamak and Hosseini, Pedram and Pezeshkpour, Pouya and Alikhani, Malihe and Aminnaseri, Moin and Bitaab, Marzieh and Brahman, Faeze and Ghazarian, Sarik and others},
    year={2020}
    journal = {arXiv e-prints},
    eprint = {2012.06154},    
}
```

### Contributions

Thanks to [@danyaljj](https://github.com/danyaljj) for adding this dataset.
