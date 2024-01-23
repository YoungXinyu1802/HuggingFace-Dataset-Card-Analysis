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
pretty_name: UnpredicTable-cluster07
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


# Dataset Card for "UnpredicTable-cluster07" - Dataset of Few-shot Tasks from Tables

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

- **Homepage:** https://ethanperez.net/unpredictable
- **Repository:** https://github.com/JunShern/few-shot-adaptation
- **Paper:** Few-shot Adaptation Works with UnpredicTable Data
- **Point of Contact:** junshern@nyu.edu, perez@nyu.edu

### Dataset Summary

The UnpredicTable dataset consists of web tables formatted as few-shot tasks for fine-tuning language models to improve their few-shot performance.

There are several dataset versions available:

* [UnpredicTable-full](https://huggingface.co/datasets/MicPie/unpredictable_full): Starting from the initial WTC corpus of 50M tables, we apply our tables-to-tasks procedure to produce our resulting dataset, [UnpredicTable-full](https://huggingface.co/datasets/MicPie/unpredictable_full), which comprises 413,299 tasks from 23,744 unique websites.

* [UnpredicTable-unique](https://huggingface.co/datasets/MicPie/unpredictable_unique): This is the same as [UnpredicTable-full](https://huggingface.co/datasets/MicPie/unpredictable_full) but filtered to have a maximum of one task per website. [UnpredicTable-unique](https://huggingface.co/datasets/MicPie/unpredictable_unique) contains exactly 23,744 tasks from 23,744 websites.

* [UnpredicTable-5k](https://huggingface.co/datasets/MicPie/unpredictable_5k): This dataset contains 5k random tables from the full dataset.

* UnpredicTable data subsets based on a manual human quality rating (please see our publication for details of the ratings):
    * [UnpredicTable-rated-low](https://huggingface.co/datasets/MicPie/unpredictable_rated-low)
    * [UnpredicTable-rated-medium](https://huggingface.co/datasets/MicPie/unpredictable_rated-medium)
    * [UnpredicTable-rated-high](https://huggingface.co/datasets/MicPie/unpredictable_rated-high)

* UnpredicTable data subsets based on the website of origin:
    * [UnpredicTable-baseball-fantasysports-yahoo-com](https://huggingface.co/datasets/MicPie/unpredictable_baseball-fantasysports-yahoo-com) 
    * [UnpredicTable-bulbapedia-bulbagarden-net](https://huggingface.co/datasets/MicPie/unpredictable_bulbapedia-bulbagarden-net)
    * [UnpredicTable-cappex-com](https://huggingface.co/datasets/MicPie/unpredictable_cappex-com) 
    * [UnpredicTable-cram-com](https://huggingface.co/datasets/MicPie/unpredictable_cram-com)
    * [UnpredicTable-dividend-com](https://huggingface.co/datasets/MicPie/unpredictable_dividend-com) 
    * [UnpredicTable-dummies-com](https://huggingface.co/datasets/MicPie/unpredictable_dummies-com)
    * [UnpredicTable-en-wikipedia-org](https://huggingface.co/datasets/MicPie/unpredictable_en-wikipedia-org)
    * [UnpredicTable-ensembl-org](https://huggingface.co/datasets/MicPie/unpredictable_ensembl-org)
    * [UnpredicTable-gamefaqs-com](https://huggingface.co/datasets/MicPie/unpredictable_gamefaqs-com)
    * [UnpredicTable-mgoblog-com](https://huggingface.co/datasets/MicPie/unpredictable_mgoblog-com)
    * [UnpredicTable-mmo-champion-com](https://huggingface.co/datasets/MicPie/unpredictable_mmo-champion-com)
    * [UnpredicTable-msdn-microsoft-com](https://huggingface.co/datasets/MicPie/unpredictable_msdn-microsoft-com)
    * [UnpredicTable-phonearena-com](https://huggingface.co/datasets/MicPie/unpredictable_phonearena-com)
    * [UnpredicTable-sittercity-com](https://huggingface.co/datasets/MicPie/unpredictable_sittercity-com)
    * [UnpredicTable-sporcle-com](https://huggingface.co/datasets/MicPie/unpredictable_sporcle-com)
    * [UnpredicTable-studystack-com](https://huggingface.co/datasets/MicPie/unpredictable_studystack-com)
    * [UnpredicTable-support-google-com](https://huggingface.co/datasets/MicPie/unpredictable_support-google-com)
    * [UnpredicTable-w3-org](https://huggingface.co/datasets/MicPie/unpredictable_w3-org)
    * [UnpredicTable-wiki-openmoko-org](https://huggingface.co/datasets/MicPie/unpredictable_wiki-openmoko-org)
    * [UnpredicTable-wkdu-org](https://huggingface.co/datasets/MicPie/unpredictable_wkdu-org)


* UnpredicTable data subsets based on clustering (for the clustering details please see our publication):
    * [UnpredicTable-cluster00](https://huggingface.co/datasets/MicPie/unpredictable_cluster00)
    * [UnpredicTable-cluster01](https://huggingface.co/datasets/MicPie/unpredictable_cluster01)
    * [UnpredicTable-cluster02](https://huggingface.co/datasets/MicPie/unpredictable_cluster02)
    * [UnpredicTable-cluster03](https://huggingface.co/datasets/MicPie/unpredictable_cluster03)
    * [UnpredicTable-cluster04](https://huggingface.co/datasets/MicPie/unpredictable_cluster04)
    * [UnpredicTable-cluster05](https://huggingface.co/datasets/MicPie/unpredictable_cluster05)
    * [UnpredicTable-cluster06](https://huggingface.co/datasets/MicPie/unpredictable_cluster06)
    * [UnpredicTable-cluster07](https://huggingface.co/datasets/MicPie/unpredictable_cluster07)
    * [UnpredicTable-cluster08](https://huggingface.co/datasets/MicPie/unpredictable_cluster08)
    * [UnpredicTable-cluster09](https://huggingface.co/datasets/MicPie/unpredictable_cluster09)
    * [UnpredicTable-cluster10](https://huggingface.co/datasets/MicPie/unpredictable_cluster10)
    * [UnpredicTable-cluster11](https://huggingface.co/datasets/MicPie/unpredictable_cluster11)
    * [UnpredicTable-cluster12](https://huggingface.co/datasets/MicPie/unpredictable_cluster12)
    * [UnpredicTable-cluster13](https://huggingface.co/datasets/MicPie/unpredictable_cluster13)
    * [UnpredicTable-cluster14](https://huggingface.co/datasets/MicPie/unpredictable_cluster14)
    * [UnpredicTable-cluster15](https://huggingface.co/datasets/MicPie/unpredictable_cluster15)
    * [UnpredicTable-cluster16](https://huggingface.co/datasets/MicPie/unpredictable_cluster16)
    * [UnpredicTable-cluster17](https://huggingface.co/datasets/MicPie/unpredictable_cluster17)
    * [UnpredicTable-cluster18](https://huggingface.co/datasets/MicPie/unpredictable_cluster18)
    * [UnpredicTable-cluster19](https://huggingface.co/datasets/MicPie/unpredictable_cluster19)
    * [UnpredicTable-cluster20](https://huggingface.co/datasets/MicPie/unpredictable_cluster20)
    * [UnpredicTable-cluster21](https://huggingface.co/datasets/MicPie/unpredictable_cluster21)
    * [UnpredicTable-cluster22](https://huggingface.co/datasets/MicPie/unpredictable_cluster22)
    * [UnpredicTable-cluster23](https://huggingface.co/datasets/MicPie/unpredictable_cluster23)
    * [UnpredicTable-cluster24](https://huggingface.co/datasets/MicPie/unpredictable_cluster24)
    * [UnpredicTable-cluster25](https://huggingface.co/datasets/MicPie/unpredictable_cluster25)
    * [UnpredicTable-cluster26](https://huggingface.co/datasets/MicPie/unpredictable_cluster26)
    * [UnpredicTable-cluster27](https://huggingface.co/datasets/MicPie/unpredictable_cluster27)
    * [UnpredicTable-cluster28](https://huggingface.co/datasets/MicPie/unpredictable_cluster28)
    * [UnpredicTable-cluster29](https://huggingface.co/datasets/MicPie/unpredictable_cluster29)
    * [UnpredicTable-cluster-noise](https://huggingface.co/datasets/MicPie/unpredictable_cluster-noise)

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

### Annotations

#### Annotation process

Manual annotation was only carried out for the [UnpredicTable-rated-low](https://huggingface.co/datasets/MicPie/unpredictable_rated-low),
[UnpredicTable-rated-medium](https://huggingface.co/datasets/MicPie/unpredictable_rated-medium), and [UnpredicTable-rated-high](https://huggingface.co/datasets/MicPie/unpredictable_rated-high) data subsets to rate task quality. Detailed instructions of the annotation instructions can be found in our publication.

#### Who are the annotators?

Annotations were carried out by a lab assistant.

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

### Dataset Curators
Jun Shern Chan, Michael Pieler, Jonathan Jao, Jérémy Scheurer, Ethan Perez

### Licensing Information
Apache 2.0

### Citation Information

```
@misc{chan2022few,
  author = {Chan, Jun Shern and Pieler, Michael and Jao, Jonathan and Scheurer, Jérémy and Perez, Ethan},
  title = {Few-shot Adaptation Works with UnpredicTable Data},
  publisher={arXiv},
  year = {2022},
  url = {https://arxiv.org/abs/2208.01009}
}
```
