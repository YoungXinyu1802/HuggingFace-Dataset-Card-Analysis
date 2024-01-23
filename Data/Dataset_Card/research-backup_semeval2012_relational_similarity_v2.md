---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
pretty_name: SemEval2012 task 2 Relational Similarity
---
# Dataset Card for "relbert/semeval2012_relational_similarity_v2"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/S12-1047/](https://aclanthology.org/S12-1047/)
- **Dataset:** SemEval2012: Relational Similarity

### Dataset Summary

***IMPORTANT***: This is the same dataset as [relbert/semeval2012_relational_similarity](https://huggingface.co/datasets/relbert/semeval2012_relational_similarity),
but with a different train/validation split.

Relational similarity dataset from [SemEval2012 task 2](https://aclanthology.org/S12-1047/), compiled to fine-tune [RelBERT](https://github.com/asahi417/relbert) model.
The dataset contains a list of positive and negative word pair from 89 pre-defined relations.
The relation types are constructed on top of following 10 parent relation types.  
```shell
{
    1: "Class Inclusion",  # Hypernym
    2: "Part-Whole",  # Meronym, Substance Meronym
    3: "Similar",  # Synonym, Co-hypornym
    4: "Contrast",  # Antonym
    5: "Attribute",  # Attribute, Event
    6: "Non Attribute",
    7: "Case Relation",
    8: "Cause-Purpose",
    9: "Space-Time",
    10: "Representation"
}
```
Each of the parent relation is further grouped into child relation types where the definition can be found [here](https://drive.google.com/file/d/0BzcZKTSeYL8VenY0QkVpZVpxYnc/view?resourcekey=0-ZP-UARfJj39PcLroibHPHw).


## Dataset Structure
### Data Instances
An example of `train` looks as follows.
```
{
  'relation_type': '8d',
  'positives': [ [ "breathe", "live" ], [ "study", "learn" ], [ "speak", "communicate" ], ... ]
  'negatives': [ [ "starving", "hungry" ], [ "clean", "bathe" ], [ "hungry", "starving" ], ... ] 
}
```

### Data Splits
|  name   |train|validation|
|---------|----:|---------:|
|semeval2012_relational_similarity_v2| 89 |      89|


### Number of Positive/Negative Word-pairs in each Split

| relation_type   |   positive (train) |   negative (train) |   positive (validation) |   negative (validation) |
|:----------------|-------------------:|-------------------:|------------------------:|------------------------:|
| 1               |                 40 |                592 |                      10 |                     148 |
| 10              |                 48 |                584 |                      12 |                     146 |
| 10a             |                  8 |                640 |                       2 |                     159 |
| 10b             |                  8 |                638 |                       2 |                     159 |
| 10c             |                  8 |                640 |                       2 |                     160 |
| 10d             |                  8 |                640 |                       2 |                     159 |
| 10e             |                  8 |                636 |                       2 |                     159 |
| 10f             |                  8 |                640 |                       2 |                     159 |
| 1a              |                  8 |                638 |                       2 |                     159 |
| 1b              |                  8 |                638 |                       2 |                     159 |
| 1c              |                  8 |                640 |                       2 |                     160 |
| 1d              |                  8 |                638 |                       2 |                     159 |
| 1e              |                  8 |                636 |                       2 |                     158 |
| 2               |                 80 |                552 |                      20 |                     138 |
| 2a              |                  8 |                640 |                       2 |                     159 |
| 2b              |                  8 |                637 |                       2 |                     159 |
| 2c              |                  8 |                639 |                       2 |                     159 |
| 2d              |                  8 |                639 |                       2 |                     159 |
| 2e              |                  8 |                640 |                       2 |                     159 |
| 2f              |                  8 |                642 |                       2 |                     160 |
| 2g              |                  8 |                637 |                       2 |                     159 |
| 2h              |                  8 |                640 |                       2 |                     159 |
| 2i              |                  8 |                640 |                       2 |                     160 |
| 2j              |                  8 |                641 |                       2 |                     160 |
| 3               |                 64 |                568 |                      16 |                     142 |
| 3a              |                  8 |                640 |                       2 |                     159 |
| 3b              |                  8 |                642 |                       2 |                     160 |
| 3c              |                  8 |                639 |                       2 |                     159 |
| 3d              |                  8 |                639 |                       2 |                     159 |
| 3e              |                  8 |                642 |                       2 |                     160 |
| 3f              |                  8 |                643 |                       2 |                     160 |
| 3g              |                  8 |                641 |                       2 |                     160 |
| 3h              |                  8 |                641 |                       2 |                     160 |
| 4               |                 64 |                568 |                      16 |                     142 |
| 4a              |                  8 |                642 |                       2 |                     160 |
| 4b              |                  8 |                638 |                       2 |                     159 |
| 4c              |                  8 |                640 |                       2 |                     160 |
| 4d              |                  8 |                637 |                       2 |                     159 |
| 4e              |                  8 |                642 |                       2 |                     160 |
| 4f              |                  8 |                642 |                       2 |                     160 |
| 4g              |                  8 |                639 |                       2 |                     159 |
| 4h              |                  8 |                641 |                       2 |                     160 |
| 5               |                 72 |                560 |                      18 |                     140 |
| 5a              |                  8 |                639 |                       2 |                     159 |
| 5b              |                  8 |                641 |                       2 |                     160 |
| 5c              |                  8 |                640 |                       2 |                     159 |
| 5d              |                  8 |                638 |                       2 |                     159 |
| 5e              |                  8 |                641 |                       2 |                     160 |
| 5f              |                  8 |                641 |                       2 |                     160 |
| 5g              |                  8 |                642 |                       2 |                     160 |
| 5h              |                  8 |                640 |                       2 |                     160 |
| 5i              |                  8 |                640 |                       2 |                     160 |
| 6               |                 64 |                568 |                      16 |                     142 |
| 6a              |                  8 |                639 |                       2 |                     159 |
| 6b              |                  8 |                641 |                       2 |                     160 |
| 6c              |                  8 |                641 |                       2 |                     160 |
| 6d              |                  8 |                644 |                       2 |                     160 |
| 6e              |                  8 |                641 |                       2 |                     160 |
| 6f              |                  8 |                640 |                       2 |                     159 |
| 6g              |                  8 |                639 |                       2 |                     159 |
| 6h              |                  8 |                640 |                       2 |                     159 |
| 7               |                 64 |                568 |                      16 |                     142 |
| 7a              |                  8 |                640 |                       2 |                     160 |
| 7b              |                  8 |                637 |                       2 |                     159 |
| 7c              |                  8 |                638 |                       2 |                     159 |
| 7d              |                  8 |                640 |                       2 |                     160 |
| 7e              |                  8 |                638 |                       2 |                     159 |
| 7f              |                  8 |                637 |                       2 |                     159 |
| 7g              |                  8 |                636 |                       2 |                     158 |
| 7h              |                  8 |                636 |                       2 |                     159 |
| 8               |                 64 |                568 |                      16 |                     142 |
| 8a              |                  8 |                638 |                       2 |                     159 |
| 8b              |                  8 |                641 |                       2 |                     160 |
| 8c              |                  8 |                637 |                       2 |                     159 |
| 8d              |                  8 |                637 |                       2 |                     159 |
| 8e              |                  8 |                637 |                       2 |                     159 |
| 8f              |                  8 |                638 |                       2 |                     159 |
| 8g              |                  8 |                635 |                       2 |                     158 |
| 8h              |                  8 |                639 |                       2 |                     159 |
| 9               |                 72 |                560 |                      18 |                     140 |
| 9a              |                  8 |                636 |                       2 |                     159 |
| 9b              |                  8 |                640 |                       2 |                     159 |
| 9c              |                  8 |                632 |                       2 |                     158 |
| 9d              |                  8 |                643 |                       2 |                     160 |
| 9e              |                  8 |                644 |                       2 |                     160 |
| 9f              |                  8 |                640 |                       2 |                     159 |
| 9g              |                  8 |                637 |                       2 |                     159 |
| 9h              |                  8 |                640 |                       2 |                     159 |
| 9i              |                  8 |                640 |                       2 |                     159 |
| SUM             |               1264 |              56198 |                     316 |                   14009 |

### Citation Information
```
@inproceedings{jurgens-etal-2012-semeval,
    title = "{S}em{E}val-2012 Task 2: Measuring Degrees of Relational Similarity",
    author = "Jurgens, David  and
      Mohammad, Saif  and
      Turney, Peter  and
      Holyoak, Keith",
    booktitle = "*{SEM} 2012: The First Joint Conference on Lexical and Computational Semantics {--} Volume 1: Proceedings of the main conference and the shared task, and Volume 2: Proceedings of the Sixth International Workshop on Semantic Evaluation ({S}em{E}val 2012)",
    month = "7-8 " # jun,
    year = "2012",
    address = "Montr{\'e}al, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/S12-1047",
    pages = "356--364",
}
```