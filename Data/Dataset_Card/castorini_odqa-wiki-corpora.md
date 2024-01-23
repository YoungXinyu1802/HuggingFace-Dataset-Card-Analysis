---
annotations_creators:
- no-annotation
language:
- en
language_creators: []
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: Open-Domain Question Answering Wikipedia Corpora
size_categories: []
source_datasets: []
tags: []
task_categories:
- question-answering
- text-retrieval
task_ids:
- open-domain-qa
---

# Dataset Card for Open-Domain Question Answering Wikipedia Corpora

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)

## Dataset Description

### Dataset Summary

The Wikipedia corpus variants provided can serve as knowledge sources for question-answering systems based on a retriever–reader pipeline. These corpus variants and their corresponding experiments are described further in the paper entitled: 
> Pre-Processing Matters! Improved Wikipedia Corpora for Open-Domain Question Answering.


## Dataset Structure

### Data Fields

The dataset consists of passages that have been segmented from Wikipedia articles.
For each passage, the following fields are provided  
- ```docid```: The passage id in the format of (X#Y) where passages from the same article share the same X, but Y denotes the segment id within the article  
- ```title```: The title of the article from where the passage comes
- ```text```: The text content of the passage
  
### Data Splits

There are 6 corpus variants in total
- ```wiki-text-100w-karpukhin```: The original DPR Wikipedia corpus with non-overlapping passages, each 100 words long, from Karpukhin et al.,
> Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih. [Dense Passage Retrieval for Open-Domain Question Answering](https://www.aclweb.org/anthology/2020.emnlp-main.550/). _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)_, pages 6769-6781, 2020.
- ```wiki-text-100w-tamber```: Our replication of the above corpus
- ```wiki-text-6-3-tamber```:  A corpus similar to above i.e. without tables, infoboxes, and lists. Segmentation is done differently, with a passage size of 6 sentences and a stride of 3 sentences. Note, this means that passages are overlapped.
- ```wiki-text-8-4-tamber```:  Like wiki-text-6-3, but with a passage size of 8 sentences and a stride of 4 sentences.
- ```wiki-all-6-3-tamber```: A corpus with tables, infoboxes, and lists included with a passage size of 6 sentences and a stride of 3 sentences.
- ```wiki-all-8-4-tamber```:  Like wiki-all-6-3, but with a passage size of 8 sentences and a stride of 4 sentences.

## Dataset Creation
### Source Data

#### Initial Data Collection and Normalization

We start with downloading the full December 20, 2018 Wikipedia XML dump: ```enwiki-20181220-pages-articles.xml``` from the Internet Archive: https://archive.org/details/enwiki-20181220. This is then Pre-processed by WikiExtractor: https://github.com/attardi/wikiextractor (making sure to modify the code to include lists as desired and replacing any tables with the string "TABLETOREPLACE") and DrQA: https://github.com/facebookresearch/DrQA/tree/main/scripts/retriever (again making sure to modify the code to not remove lists as desired).

We then apply the [pre-processing script]((https://github.com/castorini/pyserini/blob/master/docs/experiments-wiki-corpora.md)) we make available in [Pyserini](https://github.com/castorini/pyserini) to generate the different corpus variants.
