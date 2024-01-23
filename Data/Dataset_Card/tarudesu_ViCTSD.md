---
task_categories:
- text-classification
language:
- vi
size_categories:
- 10K<n<100K
---

# Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese
This is the official repository for the UIT-ViCTSD dataset from the paper [Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese](https://arxiv.org/pdf/2103.10069.pdf), which was accepted at the [IEA/AIE 2021](https://ieaaie2021.wordpress.com/list-of-accepted-papers/).

```
@InProceedings{nguyen2021victsd,
author="Nguyen, Luan Thanh and Van Nguyen, Kiet and Nguyen, Ngan Luu-Thuy",
title="Constructive and Toxic Speech Detection for Open-Domain Social Media Comments in Vietnamese",
booktitle="Advances and Trends in Artificial Intelligence. Artificial Intelligence Practices",
year="2021",
publisher="Springer International Publishing",
address="Cham",
pages="572--583"
}
```

## Introduction

The rise of social media has led to the increasing of comments on online forums. However, there still exists invalid comments which are not informative for users. Moreover, those comments are also quite toxic and harmful to people. In this paper, we create a dataset for constructive and toxic speech detection, named UIT-ViCTSD (Vietnamese Constructive and Toxic Speech Detection dataset) with 10,000 human-annotated comments. For these tasks, we propose a system for constructive and toxic speech detection with the state-of-the-art transfer learning model in Vietnamese NLP as PhoBERT. With this system, we obtain F1-scores of 78.59% and 59.40% for classifying constructive and toxic comments, respectively. Besides, we implement various baseline models as traditional Machine Learning and Deep Neural Network-Based models to evaluate the dataset. With the results, we can solve several tasks on the online discussions and develop the framework for identifying constructiveness and toxicity of Vietnamese social media comments automatically.

## Dataset
The ViCTSD dataset is consist of 10,000 human-annotated comments on 10 domains from Vietnamese users' comments on social media.

The dataset is divided into three parts as below:
1. Train set: 7,000 comments
2. Valid set: 2,000 comments
3. Test set: 1,000 comments

Please feel free to contact us by email luannt@uit.edu.vn if you have any further information!