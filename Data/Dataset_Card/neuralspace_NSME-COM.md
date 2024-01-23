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
  - [Supported Tasks](#supported-tasks)
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

### Dataset Description

- **Homepage**: [NeuralSpace Homepage](https://huggingface.co/neuralspace)
- **Repository:** [NSME-COM Dataset](https://huggingface.co/datasets/neuralspace/NSME-COM)
- **Point of Contact:** [Ankur Saxena](mailto:ankursaxena@neuralspace.ai)
- **Point of Contact:** [Ayushman Dash](mailto:ayushman@neuralspace.ai)
- **Size of downloaded dataset files:** 10.86 KB

### Dataset Summary

In this digital age, the E-Commerce industry has increasingly become a vital component of business strategy and development. To streamline, enhance and take the customer experience to the highest level, NLP can help create surprisingly massive value in the E-Commerce industry.

One of the most popular NLP use-cases is a chatbot. With a chatbot you can automate your customer engagement saving yourself time and other resources. Offering an enhanced and simplified customer experience you can increase your sales and also offer your website visitors personalized recommendations.
The NSME-COM dataset (NeuralSpace Massive E-Comm) is a manually curated dataset by data engineers at [NeuralSpace](https://www.neuralspace.ai/) for the insurance and retail domain. The dataset contains intents (the action users want to execute) and examples (anything that a user sends to the chatbot) that can be used to build a chatbot. The files in this dataset are available in JSON format.



### Supported Tasks


#### nsme-com



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

#### nsme-com

- `text`: a `string` feature.
- `intent`: a `string` feature.
- `type`: a classification label, with possible values including `train` or `test`.

### Data Splits

#### nsme-com
|    |train|test|
|----|----:|---:|
|nsme-com| 1725| 406|

### Contributions
Ankur Saxena (ankursaxena@neuralspace.ai)