---
annotations_creators:
- crowdsourced
language_creators:
- expert-generated
- other
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
pretty_name: spolin
size_categories:
- 100K<n<1M
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
- text-generation
task_ids:
- text-scoring
- dialogue-modeling
---

# SPOLIN
[![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]


## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Available SPOLIN Versions](#available_spolin_versions)
  - [Relevant Links](#relevant-links)
- [Dataset Structure](#dataset-structure)
- [Dataset Statistics](#dataset-statistics)
- [Other Information](#other-information)
  - [ACL Presentation](#acl-presentation)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description 

### Dataset Summary 
This is the repo for the paper ["Grounding Conversations with Improvised Dialogues"](https://aclanthology.org/2020.acl-main.218/) (ACL2020). 
The _Selected Pairs of Learnable ImprovisatioN_ (SPOLIN) corpus is a collection of more than 68,000 "Yes, and" type dialogue pairs extracted from the Spontaneanation podcast by Paul F. Tompkins, the Cornell Movie-Dialogs Corpus, and the SubTle corpus. For more information, refer to our [paper](https://arxiv.org/abs/2004.09544) or our [project page](https://justin-cho.com/spolin).


### Available SPOLIN Versions:
The core dataset that was used for the experiments in the paper only includes _yes-ands_ and non-_yes-ands_ from Spontaneanation and most of what is provided in those extracted from the Cornell Movie-Dialogs Corpus. After the submitting the paper, we continued our iterative data augmentation process, repeating another iteration with the Cornell Movie-Dialogs Corpus and extracting from the SubTle corpus. This expanded version is also included in this repository [here](/data). This latest version of SPOLIN was used to train the model used in our [demo](https://spolin.isi.edu). 


In the `data` folder, we provide two versions of the SPOLIN training set: 
1. Version used for experiments in the ACL paper: `data/spolin-train-acl.csv` 
2. Expanded version: `data/spolin-train.csv`

### Relevant Links: 

* Project page: https://justin-cho.com/spolin
* Github repo: https://github.com/wise-east/spolin 
* SpolinBot Demo: https://spolin.isi.edu
* ACL2020 Paper: https://aclanthology.org/2020.acl-main.218/


## Dataset Structure
**Fields**
* `id`: unique identifier
* `prompt`: first utterance in utterance pair
* `response`: second utterance in utterance pair 
* `label`: yesand = 1, non-yesand = 0 
* `source`: the source for the sample 
* `split`: whether the sample belongs to the training set or the validation set 
  
## Dataset Statistics 

##### `spolin-train.csv`:  
|| yesands| non-yesands|
|--|---:|---:|
|Spontaneanation|10,459|5,587*|
|Cornell|16,426|18,310|
|SubTle|40,303|19,512|
|Total|67,188|43,409|


##### `spolin-train-acl.csv`: 

|| yesands| non-yesands|
|--|---:|---:|
|Spontaneanation|10,459|5,587*|
|Cornell|14,976|17,851|
|Total|25,435|23,438|

##### `spolin-valid.csv`: 

|| yesands| non-yesands|
|--|---:|---:|
|Spontaneanation|500|500*|
|Cornell|500|500|
|Total|1,000|1,000|

\*Artificially collected by mix & matching positive Spontaneanation samples to balance dataset for training classifier

## Other Information 

### ACL Presentation 

[Video recording](https://slideslive.com/38928948/grounding-conversations-with-improvised-dialogues)


### Citation Information

If you use our data for your work, please cite our ACL2020 paper: 
```
@inproceedings{cho2020spolin,
    title={Grounding Conversations with Improvised Dialogues},
    author={Cho, Hyundong and May, Jonathan},
    booktitle ={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
    publisher = {Association for Computational Linguistics}, 
    location =  {Seattle, Washington, USA},
    year={2020}
}  
```


### Licensing Information


This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: http://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg

