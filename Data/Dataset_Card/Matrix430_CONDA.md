---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- afl-3.0
multilinguality:
- monolingual
pretty_name: CONDA
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- CONDA
task_categories:
- text-classification
- token-classification
task_ids:
- intent-classification
---

# Dataset Card for CONDA
## Table of Contents
- [Dataset Description](#dataset-description)
- [Abstract](#dataset-summary)
- [Leaderboards](#leaderboards)
  - [Evaluation Metrics](#evaluation-metrics)
- [Languages](#languages)
- [Video](#video)
- [Citation Information](#citation-information)



## Dataset Description

- **Homepage:** [CONDA](https://github.com/usydnlp/CONDA)
- **Paper:** [CONDA: a CONtextual Dual-Annotated dataset for in-game toxicity understanding and detection](https://arxiv.org/abs/2106.06213)
- **Point of Contact:** [Caren Han](caren.han@sydney.edu.au)


## Dataset Summary

Traditional toxicity detection models have focused on the single utterance level without deeper understanding of context. We introduce CONDA, a new dataset for in-game toxic language detection enabling joint intent classification and slot filling analysis, which is the core task of Natural Language Understanding (NLU). The dataset consists of 45K utterances from 12K conversations from the chat logs of 1.9K completed Dota 2 matches. We propose a robust dual semantic-level toxicity framework, which handles utterance and token-level patterns, and rich contextual chatting history. Accompanying the dataset is a thorough in-game toxicity analysis, which provides comprehensive understanding of context at utterance, token, and dual levels. Inspired by NLU, we also apply its metrics to the toxicity detection tasks for assessing toxicity and game-specific aspects. We evaluate strong NLU models on CONDA, providing fine-grained results for different intent classes and slot classes. Furthermore, we examine the coverage of toxicity nature in our dataset by comparing it with other toxicity datasets.

## Leaderboards
The Codalab leaderboard can be found at: https://codalab.lisn.upsaclay.fr/competitions/7827

### Evaluation Metrics
**JSA**(Joint Semantic Accuracy) is used for ranking. An utterance is deemed correctly analysed only if both utterance-level and all the token-level labels including Os are correctly predicted.

Besides, the f1 score of **utterance-level** E(xplicit) and I(mplicit) classes, **token-level** T(oxicity), D(ota-specific), S(game Slang) classes will be shown on the leaderboard (but not used as the ranking metric).

## Languages

English

## Video
Please enjoy a video presentation covering the main points from our paper:

<p align="centre">

[![ACL_video](https://img.youtube.com/vi/qRCPSSUuf18/0.jpg)](https://www.youtube.com/watch?v=qRCPSSUuf18)
      
</p>      

## Citation Information
```
@inproceedings{weld-etal-2021-conda,
    title = "{CONDA}: a {CON}textual Dual-Annotated dataset for in-game toxicity understanding and detection",
    author = "Weld, Henry  and
      Huang, Guanghao  and
      Lee, Jean  and
      Zhang, Tongshu  and
      Wang, Kunze  and
      Guo, Xinghong  and
      Long, Siqu  and
      Poon, Josiah  and
      Han, Caren",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.213",
    doi = "10.18653/v1/2021.findings-acl.213",
    pages = "2406--2416",
}
```

