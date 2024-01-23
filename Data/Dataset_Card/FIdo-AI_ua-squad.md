annotations_creators:
- crowdsourced
language:
- uk
language_creators:
- crowdsourced
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
paperswithcode_id: squad
pretty_name: ''
size_categories:
- 100K<n<1M
source_datasets:
- extended|squad_v2
task_categories:
- question-answering
task_ids:
- open-domain-qa
- extractive-qa
train-eval-index:
- col_mapping:
    answers:
      answer_start: answer_start
      text: text
    context: context
    question: question
  config: squad_v2
  metrics:
  - name: SQuAD v2
    type: squad_v2
  splits:
    eval_split: validation
    train_split: train
  task: question-answering
  task_id: extractive_question_answering

# Dataset Card for ua-squad

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://github.com/fido-ai/ua-datasets
- **Repository:** https://huggingface.co/datasets/FIdo-AI/ua-squad
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Ukrainian translation of the Stanford Question Answering Dataset (SQuAD) 2.0

### Supported Tasks and Leaderboards

question-answering

### Languages

Ukrainian

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]