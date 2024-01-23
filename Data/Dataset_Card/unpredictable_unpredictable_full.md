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
pretty_name: UnpredicTable-full
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


# Dataset Card for "UnpredicTable-full" - Dataset of Few-shot Tasks from Tables

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

- **Repository:** https://github.com/AnonCodeShare/few-shot-adaptation
- **Paper:** Few-shot Adaptation Works with UnpredicTable Data

### Dataset Summary

The UnpredicTable dataset consists of web tables formatted as few-shot tasks for fine-tuning language models to improve their few-shot performance.

There are several dataset versions available:

* [UnpredicTable-full](https://huggingface.co/datasets/unpredictable/unpredictable_full): Starting from the initial WTC corpus of 50M tables, we apply our tables-to-tasks procedure to produce our resulting dataset, [UnpredicTable-full](https://huggingface.co/datasets/unpredictable/unpredictable_full), which comprises 413,299 tasks from 23,744 unique websites.

* [UnpredicTable-unique](https://huggingface.co/datasets/unpredictable/unpredictable_unique): This is the same as [UnpredicTable-full](https://huggingface.co/datasets/unpredictable/unpredictable_full) but filtered to have a maximum of one task per website. [UnpredicTable-unique](https://huggingface.co/datasets/unpredictable/unpredictable_unique) contains exactly 23,744 tasks from 23,744 websites.

* [UnpredicTable-5k](https://huggingface.co/datasets/unpredictable/unpredictable_5k): This dataset contains 5k random tables from the full dataset.

* UnpredicTable data subsets based on the website of origin:
    * [UnpredicTable-support-google-com](https://huggingface.co/datasets/unpredictable/unpredictable_support-google-com)

### Supported Tasks and Leaderboards

Since the tables come from the web, the distribution of tasks and topics is very broad. The shape of our dataset is very wide, i.e., we have 1000's of tasks, while each task has only a few examples, compared to most current NLP datasets which are very deep, i.e., 10s of tasks with many examples. This implies that our dataset covers a broad range of potential tasks, e.g., multiple-choice, question-answering, table-question-answering, text-classification, etc.

The intended use of this dataset is to improve few-shot performance by fine-tuning/pre-training on our dataset.

### Languages

English

## Dataset Structure

### Data Instances

Each task is represented as a jsonline file and consists of several few-shot examples. Each example is a dictionary containing a field 'task', which identifies the task, followed by an 'input', 'options', and 'output' field. The 'input' field contains several column elements of the same row in the table, while the 'output' field is a target which represents an individual column of the same row. Each task contains several such examples which can be concatenated as a few-shot task. In the case of multiple choice classification, the 'options' field contains the possible classes that a model needs to choose from.

There are also additional meta-data fields such as 'pageTitle', 'title', 'outputColName', 'url', 'wdcFile'. 

### Data Fields

'task': task identifier

'input': column elements of a specific row in the table. 

'options': for multiple choice classification, it provides the options to choose from.

'output': target column element of the same row as input.

'pageTitle': the title of the page containing the table. 

'outputColName': output column name

'url': url to the website containing the table

'wdcFile': WDC Web Table Corpus file

### Data Splits

The UnpredicTable datasets do not come with additional data splits.

## Dataset Creation

### Curation Rationale

Few-shot training on multi-task datasets has been demonstrated to improve language models' few-shot learning (FSL) performance on new tasks, but it is unclear which training tasks lead to effective downstream task adaptation. Few-shot learning datasets are typically produced with expensive human curation, limiting the scale and diversity of the training tasks available to study. As an alternative source of few-shot data, we automatically extract 413,299 tasks from diverse internet tables. We provide this as a research resource to investigate the relationship between training data and few-shot learning.

### Source Data

#### Initial Data Collection and Normalization

We use internet tables from the English-language Relational Subset of the WDC Web Table Corpus 2015 (WTC). The WTC dataset tables were extracted from the July 2015 Common Crawl web corpus (http://webdatacommons.org/webtables/2015/EnglishStatistics.html). The dataset contains 50,820,165 tables from 323,160 web domains. We then convert the tables into few-shot learning tasks. Please see our publication for more details on the data collection and conversion pipeline.

#### Who are the source language producers?

The dataset is extracted from [WDC Web Table Corpora](http://webdatacommons.org/webtables/).

### Personal and Sensitive Information

The data was extracted from [WDC Web Table Corpora](http://webdatacommons.org/webtables/), which in turn extracted tables from the [Common Crawl](https://commoncrawl.org/). We did not filter the data in any way. Thus any user identities or otherwise sensitive information (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history, etc.) might be contained in our dataset.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is intended for use as a research resource to investigate the relationship between training data and few-shot learning. As such, it contains high- and low-quality data, as well as diverse content that may be untruthful or inappropriate. Without careful investigation, it should not be used for training models that will be deployed for use in decision-critical or user-facing situations.

### Discussion of Biases

Since our dataset contains tables that are scraped from the web, it will also contain many toxic, racist, sexist, and otherwise harmful biases and texts. We have not run any analysis on the biases prevalent in our datasets. Neither have we explicitly filtered the content. This implies that a model trained on our dataset may potentially reflect harmful biases and toxic text that exist in our dataset.

### Other Known Limitations

No additional known limitations.

## Additional Information

### Licensing Information
Apache 2.0