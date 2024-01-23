---
pretty_name: FaQuAD
annotations_creators:
- expert-generated
language_creators:
- found
language:
- pt
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- extended|wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
# paperswithcode_id: faquad
train-eval-index:
- config: plain_text
  task: question-answering
  task_id: extractive_question_answering
  splits:
    train_split: train
    eval_split: validation
  col_mapping:
    question: question
    context: context
    answers:
      text: text
      answer_start: answer_start
  metrics:
    - type: squad
      name: SQuAD
---

# Dataset Card for FaQuAD

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

- **Homepage:** https://github.com/liafacom/faquad
- **Repository:** https://github.com/liafacom/faquad
- **Paper:** https://ieeexplore.ieee.org/document/8923668/
<!-- - **Leaderboard:** -->
- **Point of Contact:** Eraldo R. Fernandes <eraldoluis@gmail.com>

### Dataset Summary

Academic secretaries and faculty members of higher education institutions face a common problem: 
  the abundance of questions sent by academics 
  whose answers are found in available institutional documents. 
The official documents produced by Brazilian public universities are vast and disperse, 
  which discourage students to further search for answers in such sources.
In order to lessen this problem, we present FaQuAD: 
  a novel machine reading comprehension dataset 
  in the domain of Brazilian higher education institutions. 
FaQuAD follows the format of SQuAD (Stanford Question Answering Dataset) [Rajpurkar et al. 2016]. 
It comprises 900 questions about 249 reading passages (paragraphs), 
  which were taken from 18 official documents of a computer science college 
  from a Brazilian federal university 
  and 21 Wikipedia articles related to Brazilian higher education system. 
As far as we know, this is the first Portuguese reading comprehension dataset in this format. 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

|  name   |train|validation|
|---------|----:|----:|
|faquad|837|63|

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

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

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
