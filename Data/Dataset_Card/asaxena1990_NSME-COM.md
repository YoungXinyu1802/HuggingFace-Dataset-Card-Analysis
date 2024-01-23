---
annotations_creators:
- other
language_creators:
- other
language:
- en
expert-generated license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- n<1K 
source_datasets:
- original 
task_categories:
- question-answering
- text-retrieval
- text2text-generation
- other
- translation
- conversational
task_ids:
- extractive-qa
- closed-domain-qa
- utterance-retrieval
- document-retrieval
- closed-domain-qa
- open-book-qa
- closed-book-qa 
paperswithcode_id: acronym-identification
pretty_name: Massive E-commerce Dataset for Retail and Insurance domain.
train-eval-index:
- config: nsds
  task: token-classification 
  task_id: entity_extraction
  splits: 
    train_split: train
    eval_split: test
  col_mapping:
    sentence: text
    label: target
  metrics:
    - type: nsme-com
      name: NSME-COM
      config:
        nsds
tags:
- chatbots
- e-commerce
- retail
- insurance
- consumer
- consumer goods
configs:
- nsds
---
# Dataset Card for NSME-COM

## Table of Contents

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

- **Homepage**: [https://huggingface.co/asaxena1990)
- **Repository:** [https://huggingface.co/datasets/asaxena1990/NSME-COM)
- **Point of Contact:** (Ayushman Dash <ayushman@neuralspace.ai>, Ankur Saxena <ankursaxena@neuralspace.ai>)

- **Size of downloaded dataset files:** 10.86 KB

### Dataset Summary

NSME-COM, the NeuralSpace Massive E-commerce Dataset is a collection of resources for training, evaluating, and analyzing natural language understanding systems.

### Supported Tasks and Leaderboards

The leaderboard for the GLUE benchmark can be found [at this address](https://gluebenchmark.com/). It comprises the following tasks:

#### nsds

A manually-curated domain specific dataset by Data Engineers at NeuralSpace for rare E-commerce domains such as Insurance and Retail for NL researchers and practitioners to evaluate state of the art models [here](https://www.neuralspace.ai/) in 100+ languages. The dataset files are available in JSON format.

### Languages

The language data in NSME-COM is in English (BCP-47 `en`)

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 10.86 KB

An example of 'test' looks as follows.

``` {
  "text": "is it good to add roadside assistance?",
  "intent": "Add",
  "type": "Test"
 }
 ```

An example of 'train' looks as follows.

```{
  "text": "how can I add my spouse as a nominee?",
  "intent": "Add",
  "type": "Train"
 },
```

### Data Fields

The data fields are the same among all splits.

#### nsds

- `text`: a `string` feature.
- `intent`: a `string` feature.
- `type`: a classification label, with possible values including `train` or `test`.

### Data Splits

#### nsds
|    |train|test|
|----|----:|---:|
|nsds| 1725| 406|

### Contributions
Ankur Saxena (ankursaxena@neuralspace.ai)