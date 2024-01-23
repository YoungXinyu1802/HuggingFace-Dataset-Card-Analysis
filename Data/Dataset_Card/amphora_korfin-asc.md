---
annotations_creators:
- expert-generated
language:
- ko
language_creators:
- expert-generated
license: cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: KorFin-ABSA
size_categories:
- 1K<n<10K
source_datasets:
- klue
tags:
- sentiment analysis
- aspect based sentiment analysis
- finance
task_categories:
- text-classification
task_ids:
- topic-classification
- sentiment-classification
---

# Dataset Card for KorFin-ABSA

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
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description
### Dataset Summary

The KorFin-ASC is an extension of KorFin-ABSA including 8818 samples with (aspect, polarity) pairs annotated. 
The samples were collected from [KLUE-TC](https://klue-benchmark.com/tasks/66/overview/description) and 
analyst reports from [Naver Finance](https://finance.naver.com). 
Annotation of the dataset is described in the paper [Removing Non-Stationary Knowledge From Pre-Trained Language Models for Entity-Level Sentiment Classification in Finance](https://arxiv.org/abs/2301.03136).


### Supported Tasks and Leaderboards

This dataset supports the following tasks:

* Aspect-Based Sentiment Classification

### Languages

Korean

## Dataset Structure

### Data Instances

Each instance consists of a single sentence, aspect, and corresponding polarity (POSITIVE/NEGATIVE/NEUTRAL).

```
{
  "title": "LGU＋ 1분기 영업익 1천706억원…마케팅 비용 감소",
  "aspect": "LG U+",
  'sentiment': 'NEUTRAL', 
  'url': 'https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=105&sid2=227&oid=001&aid=0008363739', 
  'annotator_id': 'A_01', 
  'Type': 'single'
}

```

### Data Fields

* title: 
* aspect: 
* sentiment: 
* url: 
* annotator_id: 
* url: 


### Data Splits

The dataset currently does not contain standard data splits.

## Additional Information

You can download the data via:
```
from datasets import load_dataset
dataset = load_dataset("amphora/KorFin-ASC")
``` 
Please find more information about the code and how the data was collected in the paper [Removing Non-Stationary Knowledge From Pre-Trained Language Models for Entity-Level Sentiment Classification in Finance](https://arxiv.org/abs/2301.03136).
The best-performing model on this dataset can be found at [link](https://huggingface.co/amphora/KorFinASC-XLM-RoBERTa).

### Licensing Information

KorFin-ASC is licensed under the terms of the [cc-by-sa-4.0](https://creativecommons.org/licenses/by-sa/4.0/)

### Citation Information

Please cite this data using: 

```
@article{son2023removing,
  title={Removing Non-Stationary Knowledge From Pre-Trained Language Models for Entity-Level Sentiment Classification in Finance},
  author={Son, Guijin and Lee, Hanwool and Kang, Nahyeon and Hahm, Moonjeong},
  journal={arXiv preprint arXiv:2301.03136},
  year={2023}
}
```

### Contributions

Thanks to [@Albertmade](https://github.com/h-albert-lee), [@amphora](https://github.com/guijinSON) for making this dataset.