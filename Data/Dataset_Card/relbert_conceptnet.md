---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: relbert/conceptnet
---
# Dataset Card for "relbert/conceptnet"

## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://home.ttic.edu/~kgimpel/commonsense.html](https://home.ttic.edu/~kgimpel/commonsense.html)
- **Dataset:** High Confidence Subset of ConceptNet for link prediction

### Dataset Summary
The selected subset of ConceptNet used in [this work](https://home.ttic.edu/~kgimpel/commonsense.html).
We removed `NotCapableOf` and `NotDesires` to keep the positive relation only.
We consider the original test set as test set, dev1 as the training set, and dev2 as the validation set.

- Number of instances

 |                                 |   train |   validation |   test |
|:--------------------------------|--------:|-------------:|-------:|
| number of pairs                 |     592 |          595 |   1189 |
| number of unique relation types |      18 |           22 |     21 |

- Number of pairs in each relation type

 |                  |   number of pairs (train) |   number of pairs (validation) |   number of pairs (test) |
|:-----------------|--------------------------:|-------------------------------:|-------------------------:|
| AtLocation       |                       133 |                             97 |                      250 |
| CapableOf        |                        51 |                             73 |                      144 |
| Causes           |                        26 |                             26 |                       45 |
| CausesDesire     |                         4 |                             11 |                        5 |
| Desires          |                         8 |                             12 |                        8 |
| HasA             |                        26 |                             17 |                       41 |
| HasFirstSubevent |                         1 |                              1 |                        1 |
| HasLastSubevent  |                         2 |                              3 |                        0 |
| HasPrerequisite  |                        59 |                             57 |                      109 |
| HasProperty      |                        24 |                             39 |                       70 |
| HasSubevent      |                        42 |                             40 |                       83 |
| IsA              |                        99 |                             98 |                      211 |
| MadeOf           |                         3 |                              7 |                       14 |
| MotivatedByGoal  |                         6 |                             11 |                        8 |
| NotMadeOf        |                         1 |                              0 |                        0 |
| PartOf           |                        12 |                              7 |                       22 |
| ReceivesAction   |                         7 |                              8 |                       11 |
| UsedFor          |                        88 |                             81 |                      161 |
| CreatedBy        |                         0 |                              1 |                        2 |
| DefinedAs        |                         0 |                              2 |                        1 |
| NotHasProperty   |                         0 |                              1 |                        1 |
| NotIsA           |                         0 |                              1 |                        1 |
| SymbolOf         |                         0 |                              2 |                        0 |
| RelatedTo        |                         0 |                              0 |                        1 |


## Dataset Structure
An example of `train` looks as follows.
```shell
{
  "relation": "IsA",
  "head": "baseball",
  "tail": "sport"
}
```


## Citation Information
```
@InProceedings{P16-1137,
  author = 	"Li, Xiang
		and Taheri, Aynaz
		and Tu, Lifu
		and Gimpel, Kevin",
  title = 	"Commonsense Knowledge Base Completion",
  booktitle = 	"Proceedings of the 54th Annual Meeting of the Association for      Computational Linguistics (Volume 1: Long Papers)    ",
  year = 	"2016",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"1445--1455",
  location = 	"Berlin, Germany",
  doi = 	"10.18653/v1/P16-1137",
  url = 	"http://aclweb.org/anthology/P16-1137"
}
```