---
annotations_creators:
- expert-generated
extended:
- original
language_creators:
- expert-generated
language:
- en-US
license:
- apache-2.0
multilinguality:
- monolingual
paperswithcode_id: prost
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- multiple-choice-qa
- open-domain-qa
---

# PROST: Physical Reasoning about Objects Through Space and Time

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

- **Homepage:** 
- **Repository:** https://github.com/nala-cub/prost
- **Paper:** https://arxiv.org/abs/2106.03634 
- **Leaderboard:**
- **Point of Contact:** [Stéphane Aroca-Ouellette](mailto:stephane.aroca-ouellette@colorado.edu)

### Dataset Summary
*Physical Reasoning about Objects Through Space and Time* (PROST) is a probing dataset to evaluate the ability of pretrained LMs to understand and reason about the physical world. PROST consists of 18,736 cloze-style multiple choice questions from 14 manually curated templates, covering 10 physical reasoning concepts:  direction, mass, height, circumference, stackable, rollable, graspable, breakable, slideable, and bounceable. 


### Supported Tasks and Leaderboards
The task is multiple choice question answering, but you can formulate it multiple ways. You can use `context` and `question` to form cloze style questions, or `context` and `ex_question` as multiple choice question answering. See the [GitHub](https://github.com/nala-cub/prost) repo for examples using GPT-1, GPT-2, BERT, RoBERTa, ALBERT, T5, and UnifiedQA.

### Languages
The text in the dataset is in English. The associated BCP-47 code is `en-US`.

## Dataset Structure

### Data Instances
An example looks like this:

```json
{
  "A": "glass", 
  "B": "pillow", 
  "C": "coin", 
  "D": "ball", 
  "context": "A person drops a glass, a pillow, a coin, and a ball from a balcony.", 
  "ex_question": "Which object is the most likely to break?", 
  "group": "breaking", 
  "label": 0, 
  "name": "breaking_1", 
  "question": "The [MASK] is the most likely to break."
}
```


### Data Fields

- `A`: Option A (0)
- `B`: Option B (1)
- `C`: Option C (2)
- `D`: Option D (3)
- `context`: Context for the question
- `question`: A cloze style continuation of the context.
- `ex_question`: A multiple-choice style question.
- `group`: The question group, e.g. *bouncing*
- `label`: A ClassLabel indication the correct option
- `name':` The template identifier.

### Data Splits

The dataset contains 18,736 examples for testing.

## Dataset Creation

### Curation Rationale

PROST is designed to avoid models succeeding in unintended ways. First, PROST provides no training data, so as to probe models in a zero-shot fashion. This prevents models from succeeding through spurious correlations between testing and training, and encourages success through a true understanding of and reasoning about the concepts at hand. Second, we manually write templates for all questions in an effort to prevent models from having seen the exact same sentences in their training data. Finally, it focuses on a small set of well defined, objective concepts that only require a small vocabulary. This allows researchers to focus more on the quality of training data rather than on size of it.

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

PROST is licensed under the Apache 2.0 license.

### Citation Information

```
@inproceedings{aroca-ouellette-etal-2021-prost,
    title = "{PROST}: {P}hysical Reasoning about Objects through Space and Time",
    author = "Aroca-Ouellette, St{\'e}phane  and
      Paik, Cory  and
      Roncone, Alessandro  and
      Kann, Katharina",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.404",
    pages = "4597--4608",
}
```

### Contributions

Thanks to [@corypaik](https://github.com/corypaik) for adding this dataset.
