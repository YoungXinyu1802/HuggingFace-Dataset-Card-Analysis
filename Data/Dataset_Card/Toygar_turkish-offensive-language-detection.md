---
annotations_creators:
- crowdsourced
- expert-generated
language_creators:
- crowdsourced
language:
- tr
license:
- cc-by-2.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
- text-classification
task_ids: []
pretty_name: Turkish Offensive Language Detection Dataset
tags:
- offensive-language-classification
---

# Dataset Summary

This dataset is enhanced version of existing offensive language studies. Existing studies are highly imbalanced, and solving this problem is too costly. To solve this, we proposed contextual data mining method for dataset augmentation. Our method is basically prevent us from retrieving random tweets and label individually. We can directly access almost exact hate related tweets and label them directly without any further human interaction in order to solve imbalanced label problem.

In addition, existing studies *(can be found at Reference section)* are merged to create even more comprehensive and robust dataset for Turkish offensive language detection task. 

The file train.csv contains 42,398, test.csv contains 8,851, valid.csv contains 1,756 annotated tweets.

# Dataset Structure

A binary dataset with with (0) Not Offensive and (1) Offensive tweets.

### Task and Labels
Offensive language identification:
- (0) Not Offensive - Tweet does not contain offense or profanity.
- (1) Offensive - Tweet contains offensive language or a targeted (veiled or direct) offense

### Data Splits
| | train | test | dev |
|------:|:------|:-----|:-----|
| 0 (Not Offensive) | 22,589 | 4,436 | 1,402 |
| 1 (Offensive) | 19,809 | 4,415 | 354 |

 
### Citation Information
```
T. Tanyel, B. Alkurdi and S. Ayvaz, "Linguistic-based Data Augmentation Approach for Offensive Language Detection," 2022 7th International Conference on Computer Science and Engineering (UBMK), 2022, pp. 1-6, doi: 10.1109/UBMK55850.2022.9919562.
```

### Paper codes
https://github.com/toygarr/lingda

# References
We merged open-source offensive language dataset studies in Turkish to increase contextuality with existing data even more, before our method is applied.
- https://huggingface.co/datasets/offenseval2020_tr
- https://github.com/imayda/turkish-hate-speech-dataset-2
- https://www.kaggle.com/datasets/kbulutozler/5k-turkish-tweets-with-incivil-content

