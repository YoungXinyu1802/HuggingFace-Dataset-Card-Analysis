---
license: cc-by-sa-4.0
annotations_creators:
- expert-generated
- found
language:
- en
language_creators:
- expert-generated
- found
multilinguality:
- monolingual
paperswithcode_id: scienceqa
pretty_name: ScienceQA
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- multi-modal-qa
- science
- chemistry
- biology
- physics
- earth-science
- engineering
- geography
- history
- world-history
- civics
- economics
- global-studies
- grammar
- writing
- vocabulary
- natural-science
- language-science
- social-science
task_categories:
- multiple-choice
- question-answering
- other
- visual-question-answering
- text-classification
task_ids:
- multiple-choice-qa
- closed-domain-qa
- open-domain-qa
- visual-question-answering
- multi-class-classification
dataset_info:
  features:
  - name: image
    dtype: image
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: int8
  - name: hint
    dtype: string
  - name: task
    dtype: string
  - name: grade
    dtype: string
  - name: subject
    dtype: string
  - name: topic
    dtype: string
  - name: category
    dtype: string
  - name: skill
    dtype: string
  - name: lecture
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: train
    num_bytes: 16416902
    num_examples: 12726
  - name: validation
    num_bytes: 5404896
    num_examples: 4241
  - name: test
    num_bytes: 5441676
    num_examples: 4241
  download_size: 0
  dataset_size: 27263474
---

# Dataset Card Creation Guide

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

- **Homepage:** [https://scienceqa.github.io/index.html#home](https://scienceqa.github.io/index.html#home)
- **Repository:** [https://github.com/lupantech/ScienceQA](https://github.com/lupantech/ScienceQA)
- **Paper:** [https://arxiv.org/abs/2209.09513](https://arxiv.org/abs/2209.09513)
- **Leaderboard:** [https://paperswithcode.com/dataset/scienceqa](https://paperswithcode.com/dataset/scienceqa)
- **Point of Contact:** [Pan Lu](https://lupantech.github.io/) or file an issue on [Github](https://github.com/lupantech/ScienceQA/issues)

### Dataset Summary

Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering

### Supported Tasks and Leaderboards

Multi-modal Multiple Choice

### Languages

English

## Dataset Structure

### Data Instances

Explore more samples [here](https://scienceqa.github.io/explore.html).

``` json
{'image': Image,
 'question': 'Which of these states is farthest north?',
 'choices': ['West Virginia', 'Louisiana', 'Arizona', 'Oklahoma'],
 'answer': 0,
 'hint': '',
 'task': 'closed choice',
 'grade': 'grade2',
 'subject': 'social science',
 'topic': 'geography',
 'category': 'Geography',
 'skill': 'Read a map: cardinal directions',
 'lecture': 'Maps have four cardinal directions, or main directions. Those directions are north, south, east, and west.\nA compass rose is a set of arrows that point to the cardinal directions. A compass rose usually shows only the first letter of each cardinal direction.\nThe north arrow points to the North Pole. On most maps, north is at the top of the map.',
 'solution': 'To find the answer, look at the compass rose. Look at which way the north arrow is pointing. West Virginia is farthest north.'}
```

Some records might be missing any or all of image, lecture, solution. 

### Data Fields

- `image` : Contextual image
- `question` : Prompt relating to the `lecture`
- `choices` : Multiple choice answer with 1 correct to the `question`
- `answer` : Index of choices corresponding to the correct answer
- `hint` : Hint to help answer the `question`
- `task` : Task description
- `grade` : Grade level from K-12
- `subject` : High level 
- `topic` : natural-sciences, social-science, or language-science
- `category` : A subcategory of `topic`
- `skill` : A description of the task required
- `lecture` : A relevant lecture that a `question` is generated from
- `solution` : Instructions on how to solve the `question`


Note that the descriptions can be initialized with the **Show Markdown Data Fields** output of the [Datasets Tagging app](https://huggingface.co/spaces/huggingface/datasets-tagging), you will then only need to refine the generated descriptions.

### Data Splits
- name: train
    - num_bytes: 16416902
    - num_examples: 12726
- name: validation
    - num_bytes: 5404896
    - num_examples: 4241
- name: test
    - num_bytes: 5441676
    - num_examples: 4241

## Dataset Creation

### Curation Rationale

When answering a question, humans utilize the information available across different modalities to synthesize a consistent and complete chain of thought (CoT). This process is normally a black box in the case of deep learning models like large-scale language models. Recently, science question benchmarks have been used to diagnose the multi-hop reasoning ability and interpretability of an AI system. However, existing datasets fail to provide annotations for the answers, or are restricted to the textual-only modality, small scales, and limited domain diversity. To this end, we present Science Question Answering (ScienceQA).

### Source Data

ScienceQA is collected from elementary and high school science curricula.

#### Initial Data Collection and Normalization

See Below

#### Who are the source language producers?

See Below

### Annotations

Questions in the ScienceQA dataset are sourced from open resources managed by IXL Learning,
an online learning platform curated by experts in the field of K-12 education. The dataset includes
problems that align with California Common Core Content Standards. To construct ScienceQA, we
downloaded the original science problems and then extracted individual components (e.g. questions,
hints, images, options, answers, lectures, and solutions) from them based on heuristic rules.
We manually removed invalid questions, such as questions that have only one choice, questions that
contain faulty data, and questions that are duplicated, to comply with fair use and transformative
use of the law. If there were multiple correct answers that applied, we kept only one correct answer.
Also, we shuffled the answer options of each question to ensure the choices do not follow any
specific pattern. To make the dataset easy to use, we then used semi-automated scripts to reformat
the lectures and solutions. Therefore, special structures in the texts, such as tables and lists, are
easily distinguishable from simple text passages. Similar to ImageNet, ReClor, and PMR datasets,
ScienceQA is available for non-commercial research purposes only and the copyright belongs to
the original authors. To ensure data quality, we developed a data exploration tool to review examples
in the collected dataset, and incorrect annotations were further manually revised by experts. The tool
can be accessed at https://scienceqa.github.io/explore.html.

#### Annotation process

See above

#### Who are the annotators?

See above

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

- Pan Lu1,3
- Swaroop Mishra2,3
- Tony Xia1
- Liang Qiu1
- Kai-Wei Chang1
- Song-Chun Zhu1
- Oyvind Tafjord3
- Peter Clark3
- Ashwin Kalyan3
 
From: 
1. University of California, Los Angeles    
2. Arizona State University    
3. Allen Institute for AI   



### Licensing Information

[Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
](https://creativecommons.org/licenses/by-nc-sa/4.0/)

### Citation Information

Provide the [BibTex](http://www.bibtex.org/)-formatted reference for the dataset. For example:
```
@inproceedings{lu2022learn,
    title={Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering},
    author={Lu, Pan and Mishra, Swaroop and Xia, Tony and Qiu, Liang and Chang, Kai-Wei and Zhu, Song-Chun and Tafjord, Oyvind and Clark, Peter and Ashwin Kalyan},
    booktitle={The 36th Conference on Neural Information Processing Systems (NeurIPS)},
    year={2022}
}
```
### Contributions

Thanks to [Derek Thomas](https://huggingface.co/derek-thomas) [@datavistics](https://github.com/datavistics) for adding this dataset.