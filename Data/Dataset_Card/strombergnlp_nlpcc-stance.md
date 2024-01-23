---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- zh
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-analysis
pretty_name: NLPCC Stance
tags:
- stance-detection
---

# Dataset Card for "NLPCC 2016: Stance Detection in Chinese Microblogs"

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

- **Homepage:** [http://tcci.ccf.org.cn/conference/2016/pages/page05_evadata.html](http://tcci.ccf.org.cn/conference/2016/pages/page05_evadata.html)
- **Repository:** 
- **Paper:** [https://link.springer.com/chapter/10.1007/978-3-319-50496-4_85](https://link.springer.com/chapter/10.1007/978-3-319-50496-4_85)
- **Point of Contact:** [Mads Kongsback](https://github.com/mkonxd)
- **Size of downloaded dataset files:**
- **Size of the generated dataset:** 
- **Total amount of disk used:** 

### Dataset Summary

This is a stance prediction dataset in Chinese.
The data is that from a shared task, stance detection in Chinese microblogs, in NLPCC-ICCPOL 2016. It covers Task A, a mandatory supervised task which detects stance towards five targets of interest with given labeled data. 
Some instances of the dataset have been removed, as they were without label.

### Supported Tasks and Leaderboards

* Stance Detection in Chinese Microblogs

### Languages

Chinese, as spoken on the Weibo website  (`bcp47:zh`)

## Dataset Structure
 

### Data Instances

Example instance:

```
{
  'id': '0', 
  'target': 'IphoneSE', 
  'text': '3月31日，苹果iPhone SE正式开卖，然而这款小屏新机并未出现人们预想的疯抢局面。根据市场分析机构Localytics周一公布的数据，iPhone SE正式上市的这个周末，销量成绩并不算太好。', 
  'stance': 2
}
```

### Data Fields

* id: a `string` field with a unique id for the instance
* target: a `string` representing the target of the stance
* text: a `string` of the stance-bearing text
* stance: an `int` representing class label -- `0`: AGAINST; `1`: FAVOR; `2`: NONE.

### Data Splits

The training split has 2986 instances

## Dataset Creation

### Curation Rationale

The goal was to create a dataset of microblog text annotated for stance. Six stance targets were selected and data was collected from Sina Weibo for annotation.

### Source Data

#### Initial Data Collection and Normalization

Not specified

#### Who are the source language producers?

Sina Weibo users

### Annotations

#### Annotation process

The stance of each target-microblog pair is duplicated annotated by two students
individually. If these two students provide the same annotation, the stance of this
microblog-target pair is then labeled. If the different annotation is detected, the third
student will be assigned to annotate this pair. Their annotation results will be voted to
obtain the final label.

#### Who are the annotators?

Students in China

### Personal and Sensitive Information

No reflections


## Considerations for Using the Data

### Social Impact of Dataset

The data preserves social media utterances verbatim and so has obviated any right to be forgotten, though usernames and post IDs are not explicitly included in the data.


### Discussion of Biases

There'll be at least a temporal and regional bias to this data, as well as it only representing expressions of stance on six topics.

### Other Known Limitations


## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. 

### Citation Information

```
@incollection{xu2016overview,
  title={Overview of nlpcc shared task 4: Stance detection in chinese microblogs},
  author={Xu, Ruifeng and Zhou, Yu and Wu, Dongyin and Gui, Lin and Du, Jiachen and Xue, Yun},
  booktitle={Natural language understanding and intelligent applications},
  pages={907--916},
  year={2016},
  publisher={Springer}
}
```


### Contributions

Added by [@mkonxd](https://github.com/mkonxd), [@leondz](https://github.com/leondz) 
