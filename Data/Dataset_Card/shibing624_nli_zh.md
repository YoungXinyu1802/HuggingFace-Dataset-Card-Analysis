---
annotations_creators:
- shibing624
language_creators:
- shibing624
language:
- zh
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<20M
source_datasets:
- https://github.com/shibing624/text2vec
- https://github.com/IceFlameWorm/NLP_Datasets/tree/master/ATEC
- http://icrc.hitsz.edu.cn/info/1037/1162.htm
- http://icrc.hitsz.edu.cn/Article/show/171.html
- https://arxiv.org/abs/1908.11828
- https://github.com/pluto-junzeng/CNSD
task_categories:
- text-classification
task_ids:
- natural-language-inference
- semantic-similarity-scoring
- text-scoring
paperswithcode_id: snli
pretty_name: Stanford Natural Language Inference
---
# Dataset Card for NLI_zh
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
- **Repository:** [Chinese NLI dataset](https://github.com/shibing624/text2vec)
- **Leaderboard:** [NLI_zh leaderboard](https://github.com/shibing624/text2vec) (located on the homepage)
- **Size of downloaded dataset files:** 16 MB
- **Total amount of disk used:** 42 MB
### Dataset Summary

常见中文语义匹配数据集，包含[ATEC](https://github.com/IceFlameWorm/NLP_Datasets/tree/master/ATEC)、[BQ](http://icrc.hitsz.edu.cn/info/1037/1162.htm)、[LCQMC](http://icrc.hitsz.edu.cn/Article/show/171.html)、[PAWSX](https://arxiv.org/abs/1908.11828)、[STS-B](https://github.com/pluto-junzeng/CNSD)共5个任务。

数据源：

- ATEC: https://github.com/IceFlameWorm/NLP_Datasets/tree/master/ATEC
- BQ: http://icrc.hitsz.edu.cn/info/1037/1162.htm
- LCQMC: http://icrc.hitsz.edu.cn/Article/show/171.html
- PAWSX: https://arxiv.org/abs/1908.11828
- STS-B: https://github.com/pluto-junzeng/CNSD


### Supported Tasks and Leaderboards

Supported Tasks: 支持中文文本匹配任务，文本相似度计算等相关任务。

中文匹配任务的结果目前在顶会paper上出现较少，我罗列一个我自己训练的结果：

**Leaderboard:** [NLI_zh leaderboard](https://github.com/shibing624/text2vec) 

### Languages

数据集均是简体中文文本。

## Dataset Structure
### Data Instances
An example of 'train' looks as follows.
```
{
  "sentence1": "刘诗诗杨幂谁漂亮",
  "sentence2": "刘诗诗和杨幂谁漂亮",
  "label": 1,
}
{
  "sentence1": "汇理财怎么样",
  "sentence2": "怎么样去理财",
  "label": 0,
}
```

### Data Fields
The data fields are the same among all splits.

- `sentence1`: a `string` feature.
- `sentence2`: a `string` feature.
- `label`: a classification label, with possible values including `similarity` (1), `dissimilarity` (0).

### Data Splits

#### ATEC

```shell
$ wc -l ATEC/*
   20000 ATEC/ATEC.test.data
   62477 ATEC/ATEC.train.data
   20000 ATEC/ATEC.valid.data
  102477 total
```

#### BQ

```shell
$ wc -l BQ/*
   10000 BQ/BQ.test.data
  100000 BQ/BQ.train.data
   10000 BQ/BQ.valid.data
  120000 total
```

#### LCQMC

```shell
$ wc -l LCQMC/*
   12500 LCQMC/LCQMC.test.data
  238766 LCQMC/LCQMC.train.data
    8802 LCQMC/LCQMC.valid.data
  260068 total
```

#### PAWSX

```shell
$ wc -l PAWSX/*
    2000 PAWSX/PAWSX.test.data
   49401 PAWSX/PAWSX.train.data
    2000 PAWSX/PAWSX.valid.data
   53401 total
```

#### STS-B

```shell
$ wc -l STS-B/*
    1361 STS-B/STS-B.test.data
    5231 STS-B/STS-B.train.data
    1458 STS-B/STS-B.valid.data
    8050 total
```

## Dataset Creation
### Curation Rationale
作为中文NLI(natural langauge inference)数据集，这里把这个数据集上传到huggingface的datasets，方便大家使用。
### Source Data
#### Initial Data Collection and Normalization
#### Who are the source language producers?
数据集的版权归原作者所有，使用各数据集时请尊重原数据集的版权。

BQ: Jing Chen, Qingcai Chen, Xin Liu, Haijun Yang, Daohe Lu, Buzhou Tang, The BQ Corpus: A Large-scale Domain-specific Chinese Corpus For Sentence Semantic Equivalence Identification EMNLP2018. 
### Annotations
#### Annotation process

#### Who are the annotators?
原作者。

### Personal and Sensitive Information

## Considerations for Using the Data
### Social Impact of Dataset
This dataset was developed as a benchmark for evaluating representational systems for text, especially including those induced by representation learning methods, in the task of predicting truth conditions in a given context. 

Systems that are successful at such a task may be more successful in modeling semantic representations.
### Discussion of Biases
### Other Known Limitations
## Additional Information
### Dataset Curators

- 苏剑林对文件名称有整理
- 我上传到huggingface的datasets

### Licensing Information

用于学术研究。

The BQ corpus is free to the public for academic research.


### Contributions

Thanks to [@shibing624](https://github.com/shibing624) add this dataset.
