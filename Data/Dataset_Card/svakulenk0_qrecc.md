---
pretty_name: QReCC
language_creators:
- expert-generated
- found
language:
- en
license:
- cc-by-3.0
multilinguality:
- monolingual
source_datasets:
- extended|natural_questions
- extended|quac
task_categories:
- question-answering
task_ids:
- open-domain-qa
---

# Dataset Card for QReCC: Question Rewriting in Conversational Context

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- [**Repository:**](https://github.com/apple/ml-qrecc)
- [**Paper:**](https://arxiv.org/pdf/2010.04898.pdf)
- [**Leaderboard:**](https://www.tira.io/task/scai-qrecc/dataset/scai-qrecc21-test-dataset-2021-07-20)

### Dataset Summary

QReCC (Question Rewriting in Conversational Context) is an end-to-end open-domain question answering dataset comprising of 14K conversations with 81K question-answer pairs. The goal of this dataset is to provide a challenging benchmark for end-to-end conversational question answering that includes the individual subtasks of question rewriting, passage retrieval and reading comprehension.

The task in QReCC is to find answers to conversational questions within a collection of 10M web pages split into 54M passages. Answers to questions in the same conversation may be distributed across several web pages.

The passage collection should be downloaded from [**Zenodo**](https://zenodo.org/record/5115890#.YaeD7C8RppR) (passages.zip)

### Supported Tasks and Leaderboards

`question-answering`

### Languages

English

## Dataset Structure
### Data Instances

An example from the data set looks as follows:
```
{
  "Context": [
    "What are the pros and cons of electric cars?",
    "Some pros are: They're easier on the environment. Electricity is cheaper than gasoline. Maintenance is less frequent and less expensive. They're very quiet. You'll get tax credits. They can shorten your commute time. Some cons are: Most EVs have pretty short ranges. Recharging can take a while."
  ],
  "Question": "Tell me more about Tesla",
  "Rewrite": "Tell me more about Tesla the car company.",
  "Answer": "Tesla Inc. is an American automotive and energy company based in Palo Alto, California. The company specializes in electric car manufacturing and, through its SolarCity subsidiary, solar panel manufacturing.",
  "Answer_URL": "https://en.wikipedia.org/wiki/Tesla,_Inc.",
  "Conversation_no": 74,
  "Turn_no": 2,
  "Conversation_source": "trec"
}
```


### Data Splits

- train: 63501
- test: 16451


## Dataset Creation

### Source Data

- QuAC
- TREC CAsT
- Natural Questions



## Additional Information

### Licensing Information

[CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)

### Citation Information
```
@inproceedings{ qrecc,
    title={Open-Domain Question Answering Goes Conversational via Question Rewriting},
    author={Anantha, Raviteja and Vakulenko, Svitlana and Tu, Zhucheng and Longpre, Shayne and Pulman, Stephen and Chappidi, Srinivas},
    booktitle={ NAACL },
    year={2021}
}
```