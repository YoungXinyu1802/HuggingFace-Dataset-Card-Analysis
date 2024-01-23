---
license: other
tags:
- automatic claim verification
- claims
---


# multiFC

- a dataset for the task of **automatic claim verification**
- License is currently unknown, please refer to the original paper/[dataset site](http://www.copenlu.com/publication/2019_emnlp_augenstein/):

- https://arxiv.org/abs/1909.03242 

## Dataset contents

- **IMPORTANT:** the `label` column in the `test` set has dummy values as these were not provided (see original readme section for explanation)

```
DatasetDict({
    train: Dataset({
        features: ['claimID', 'claim', 'label', 'claimURL', 'reason', 'categories', 'speaker', 'checker', 'tags', 'article title', 'publish date', 'climate', 'entities'],
        num_rows: 27871
    })
    test: Dataset({
        features: ['claimID', 'claim', 'label', 'claimURL', 'reason', 'categories', 'speaker', 'checker', 'tags', 'article title', 'publish date', 'climate', 'entities'],
        num_rows: 3487
    })
    validation: Dataset({
        features: ['claimID', 'claim', 'label', 'claimURL', 'reason', 'categories', 'speaker', 'checker', 'tags', 'article title', 'publish date', 'climate', 'entities'],
        num_rows: 3484
    })
})
```
## Paper Abstract / Citation
> We contribute the largest publicly available dataset of naturally occurring factual claims for the purpose of automatic claim verification. It is collected from 26 fact checking websites in English, paired with textual sources and rich metadata, and labelled for veracity by human expert journalists. We present an in-depth analysis of the dataset, highlighting characteristics and challenges. Further, we present results for automatic veracity prediction, both with established baselines and with a novel method for joint ranking of evidence pages and predicting veracity that outperforms all baselines. Significant performance increases are achieved by encoding evidence, and by modelling metadata. Our best-performing model achieves a Macro F1 of 49.2%, showing that this is a challenging testbed for claim veracity prediction.

```
@inproceedings{conf/emnlp2019/Augenstein,
added-at = {2019-10-27T00:00:00.000+0200},
author = {Augenstein, Isabelle and Lioma, Christina and Wang, Dongsheng and Chaves Lima, Lucas and Hansen, Casper and Hansen, Christian and Grue Simonsen, Jakob},
booktitle = {EMNLP},
crossref = {conf/emnlp/2019},
publisher = {Association for Computational Linguistics},
title = {MultiFC: A Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims},
year = 2019
}
```

## Original README
Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims

The MultiFC is the largest publicly available dataset of naturally occurring factual claims for automatic claim verification.
It is collected from 26 English fact-checking websites paired with textual sources and rich metadata and labeled for veracity by human expert journalists.


###### TRAIN and DEV #######
The train and dev files are (tab-separated) and contain the following metadata:
claimID, claim, label, claimURL, reason, categories, speaker, checker, tags, article title, publish date, climate, entities

Fields that could not be crawled were set as "None." Please refer to Table 11 of our paper to see the summary statistics.


###### TEST #######
The test file follows the same structure. However, we have removed the label. Thus, it only presents 12 metadata.
claimID, claim, claim, reason, categories, speaker, checker, tags, article title, publish date, climate, entities

Fields that could not be crawled were set as "None." Please refer to Table 11 of our paper to see the summary statistics.


###### Snippets ######
The text of each claim is submitted verbatim as a query to the Google Search API (without quotes).
In the folder snippet, we provide the top 10 snippets retrieved. In some cases, fewer snippets are provided
since we have excluded the claimURL from the snippets.
Each file in the snippets folder is named after the claimID of the claim submitted as a query.
Snippets file is (tab-separated) and contains the following metadata:
rank_position, title, snippet, snippet_url


For more information, please refer to our paper:
References:
Isabelle Augenstein, Christina Lioma, Dongsheng Wang, Lucas Chaves Lima, Casper Hansen, Christian Hansen, and Jakob Grue Simonsen. 2019. 
MultiFC: A Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims. In EMNLP. Association for Computational Linguistics.

https://copenlu.github.io/publication/2019_emnlp_augenstein/

