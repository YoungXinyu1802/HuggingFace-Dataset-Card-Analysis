---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: Fewshot Table Dataset
size_categories:
- 100K<n<1M
source_datasets: []
task_categories:
- multiple-choice
- question-answering
- zero-shot-classification
- text2text-generation
- table-question-answering
- text-generation
- text-classification
- tabular-classification
task_ids:
- multiple-choice-qa
- extractive-qa
- open-domain-qa
- closed-domain-qa
- closed-book-qa
- open-book-qa
- language-modeling
- multi-class-classification
- natural-language-inference
- topic-classification
- multi-label-classification
- tabular-multi-class-classification
- tabular-multi-label-classification
---


# Dataset Card for Fewshot Table Dataset

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

- **Homepage:** [Needs More Information]
- **Repository:** https://github.com/JunShern/few-shot-pretraining
- **Paper:** Paper-Title
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** junshern@nyu.edu, perez@nyu.edu

### Dataset Summary

The Fewshot Table dataset consists of tables that naturally occur on the web, that are formatted as few-shot tasks for fine-tuning language models to improve their few-shot performance. The dataset consists of approximately 413K tables that are extracted from the [WDC Web Table Corpora](http://webdatacommons.org/webtables/) 2015, which is released under the Apache-2.0 license. The WDC Web Table Corpora "contains vast amounts of HTML tables. [...] The Web Data Commons project extracts relational Web tables from the [Common Crawl](https://commoncrawl.org/), the largest and most up-to-date Web corpus that is currently available to the public."

### Supported Tasks and Leaderboards

Since the tables come from the web, the distribution of tasks and topics is very broad. The shape of our dataset is very wide i.e. we have 1000's tasks, while each task has only a few examples, compared to most current NLP datasets which are very deep, i.e. 10s of tasks with many examples. This implies that our dataset covers a broad range of potential tasks, e.g. multiple-choice, question-answering, table-question-answering, text-classification, etc.

The intended use of this dataset is to improve few-shot performance by finetuning/pretraining onour dataset.

### Languages

English

## Dataset Structure

### Data Instances

Each table, i.e. task is represented as a json-lines file and consists of several few-shot examples. Each example is a dictionary containing a field 'task', which identifies the task, followed by an 'input', 'options', and 'output' field. The 'input' field contains several column elements of the same row in the table, while the 'output' field is a target which represents an individual column of the same row. Each task contains several such examples which can be concatenated as a few-shot task. In the case of multiple choice classification, the 'options' field contains the possible classes that a model needs to choose from. 

There are also additional meta-data fields such as 'pageTitle', 'title', 'outputColName', 'url', 'wdcFile'. 

### Data Fields

'task': task identifier

'input': column elements of a specific row in table. 

'options': for multiple choice classification, it provides the options to choose from.

'output': target column element of same row as input.

'pageTitle': the title of the page containing the table. 

'outputColName': ?? (potentially remove this from data)

'url': url to the website containing the table

'wdcFile': ? (potentially remove this from data)

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

How do we convert tables to few-shot tasks?
Unlike unstructured text, structured data in the form of tables lends itself easily to the few-shot task format. Given a table where each row is an instance of a similar class and the columns describe the attributes of each instance, we can turn each row into a task example to predict one attribute given the others. When the table has more than one row, we instantly have multiple examples of this task by using each row as a single example, and thus each table becomes a few-shot dataset for a particular task. 

The few-shot setting in this setting is significant: Tables often do not come with clear instructions for each field, so tasks may be underspecified if prompted in a zero-shot manner, but the intended task becomes clearer when examples are provided. This makes a good two-way match: The few-shot format is a perfect setup for table learning, and tables provide a natural dataset for few-shot training. 

### Source Data

#### Initial Data Collection and Normalization

We downloaded the [WDC Web Table Corpora](http://webdatacommons.org/webtables/) 2015 dataset and focus on relational tables. In the following, we describe the steps we executed to filter the WDC Web Table Corpora and create our task dataset. Given a set of relation tables, we apply defined preprocessing steps to ensure all the tables can be handled consistently. Each table can then spawn one or more tasks using a simple predict-one-column approach. Finally, all tasks produced in this manner undergo simple rule-based checks, i.e. any candidates that do not meet some defined minimum requirements for a well-formed task are rejected. Following this approach, we start with 50 million tables in the initial corpus and produce a longlist of 400K tasks. 

1. We select only relational tables. 
2. We make sure all tables are vertical (horizontal tables are simply transposed) and remove duplicate rows. 
3. To create task we use what in the literature is referred to as verbalizers. For example, a table with 3 columns may be cast as three different tasks: predict column A given B and C, predict column B given A and C, and predict column C given A and B. 
4. Rule-based-checks to reject tables: 
a) We reject 25M tables that have fewer than 6 rows (so we can do at least k=5-shot learning)
b) We reject tables with > 20% non-English text as measured by [SpaCy](https://spacy.io/)
c) Given 2 Million passing tables we consider each table column as a potential output column, and concatenate all other columns to form the input (which produces 5.6 M candidate tasks)
5. Rule-based-checks to reject tasks
a) We reject a task if it has less than 6 rows. Note that tasks may have fewer rows than their origin tables since we remove rows where the output column is empty. 
b) We reject tasks if any input maps to multiple outputs. 
c) We reject tasks if it has fewer than 2 output classes. 
d) We reject a task if the output column alone has >20% non-English text. 
e) We reject a task if the classes are heavily imbalanced.

6. Lastly we apply domain-level filtering. Initial iterations of our dataset found a significant imbalance in terms of the website of origin for our generated tasks. In particular, we found that the mos-frequent domain in the WDC corpus, Cappex.com, was emphasized by our export criteria such that this website alone represented 41% of our total tasks. Since we want our dataset to represent the diversity of all the tables available on the web, we apply a hard fix for this imbalance by limiting the number of tasks per domain. Starting from the initial corpus of 50M tables from 323160 web domains, our resulting longlist of tasks comprises more than X  for a total of 413350 tasks. 

#### Who are the source language producers?

The dataset is extracted from [WDC Web Table Corpora](http://webdatacommons.org/webtables/).

### Annotations

#### Annotation process

No annotation Process

#### Who are the annotators?

-

### Personal and Sensitive Information

The data was extracted from [WDC Web Table Corpora](http://webdatacommons.org/webtables/), which in turn extracted tables from the [Common Crawl](https://commoncrawl.org/). We did not filter the data in any way. Thus any user identities or otherwise sensitive information (e.g. data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history, etc.) might be contained in our dataset. 

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop models that are better at few-shot learning and have higher few-shot performance by fine-tuning few-shot tasks extracted from tables.

While tables have a similar structure to few-shot tasks and we do see an improved performance on few-shot tasks in our paper, we want to make clear that finetuning on tables also has its risks. First of all, since the tables are extracted from the web, they may contain user identities or otherwise sensitive information which a model might reveal at inference, or which could influence the learning process of a model in a negative way. Second, since tables are very diverse in nature, the model also trains on low-quality data or data with an unusual structure. While it is interesting that training on such data improves few-shot performance on downstream tasks, this could also imply that the model learns concepts that are very dissimilar to human concepts that would be useful for a certain downstream task. In other words, it is possible that the model learns weird things that are helpful on the evaluated downstream tasks, but might lead to bad out-of-distribution behavior.

### Discussion of Biases

Since our dataset contains tables that are scraped from the web, it will also contain many toxic, racist, sexist, and otherwise harmful biases and texts. We have not run any analysis on the biases prevalent in our datasets. Neither have we explicitly filtered the content for toxic content. 
This implies that a model trained on our dataset will reinforce harmful biases and toxic text that exist in our dataset.


### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators
Mention all authors 

### Licensing Information
Apache 2.0

### Citation Information

[Needs More Information]