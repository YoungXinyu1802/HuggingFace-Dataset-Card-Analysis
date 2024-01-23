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
# Dataset Card for "relbert/semeval2012_relational_similarity"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/S12-1047/](https://aclanthology.org/S12-1047/)
- **Dataset:** SemEval2012: Relational Similarity

### Dataset Summary
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
|semeval2012_relational_similarity| 89 |      89|


### Number of Positive/Negative Word-pairs in each Split

| relation_type   |   positive (train) |   negative (train) |   positive (validation) |   negative (validation) |
|:----------------|-------------------:|-------------------:|------------------------:|------------------------:|
| 1               |                 50 |                740 |                      63 |                     826 |
| 10              |                 60 |                730 |                      66 |                     823 |
| 10a             |                 10 |                799 |                      14 |                     894 |
| 10b             |                 10 |                797 |                      13 |                     893 |
| 10c             |                 10 |                800 |                      11 |                     898 |
| 10d             |                 10 |                799 |                      10 |                     898 |
| 10e             |                 10 |                795 |                       8 |                     896 |
| 10f             |                 10 |                799 |                      10 |                     898 |
| 1a              |                 10 |                797 |                      14 |                     892 |
| 1b              |                 10 |                797 |                      14 |                     892 |
| 1c              |                 10 |                800 |                      11 |                     898 |
| 1d              |                 10 |                797 |                      16 |                     890 |
| 1e              |                 10 |                794 |                       8 |                     895 |
| 2               |                100 |                690 |                     117 |                     772 |
| 2a              |                 10 |                799 |                      15 |                     893 |
| 2b              |                 10 |                796 |                      11 |                     894 |
| 2c              |                 10 |                798 |                      13 |                     894 |
| 2d              |                 10 |                798 |                      10 |                     897 |
| 2e              |                 10 |                799 |                      11 |                     897 |
| 2f              |                 10 |                802 |                      11 |                     900 |
| 2g              |                 10 |                796 |                      16 |                     889 |
| 2h              |                 10 |                799 |                      11 |                     897 |
| 2i              |                 10 |                800 |                       9 |                     900 |
| 2j              |                 10 |                801 |                      10 |                     900 |
| 3               |                 80 |                710 |                      80 |                     809 |
| 3a              |                 10 |                799 |                      11 |                     897 |
| 3b              |                 10 |                802 |                      11 |                     900 |
| 3c              |                 10 |                798 |                      12 |                     895 |
| 3d              |                 10 |                798 |                      14 |                     893 |
| 3e              |                 10 |                802 |                       5 |                     906 |
| 3f              |                 10 |                803 |                      11 |                     901 |
| 3g              |                 10 |                801 |                       6 |                     904 |
| 3h              |                 10 |                801 |                      10 |                     900 |
| 4               |                 80 |                710 |                      82 |                     807 |
| 4a              |                 10 |                802 |                      11 |                     900 |
| 4b              |                 10 |                797 |                       7 |                     899 |
| 4c              |                 10 |                800 |                      12 |                     897 |
| 4d              |                 10 |                796 |                       4 |                     901 |
| 4e              |                 10 |                802 |                      12 |                     899 |
| 4f              |                 10 |                802 |                       9 |                     902 |
| 4g              |                 10 |                798 |                      15 |                     892 |
| 4h              |                 10 |                801 |                      12 |                     898 |
| 5               |                 90 |                700 |                     105 |                     784 |
| 5a              |                 10 |                798 |                      14 |                     893 |
| 5b              |                 10 |                801 |                       8 |                     902 |
| 5c              |                 10 |                799 |                      11 |                     897 |
| 5d              |                 10 |                797 |                      15 |                     891 |
| 5e              |                 10 |                801 |                       8 |                     902 |
| 5f              |                 10 |                801 |                      11 |                     899 |
| 5g              |                 10 |                802 |                       9 |                     902 |
| 5h              |                 10 |                800 |                      15 |                     894 |
| 5i              |                 10 |                800 |                      14 |                     895 |
| 6               |                 80 |                710 |                      99 |                     790 |
| 6a              |                 10 |                798 |                      15 |                     892 |
| 6b              |                 10 |                801 |                      11 |                     899 |
| 6c              |                 10 |                801 |                      13 |                     897 |
| 6d              |                 10 |                804 |                      10 |                     903 |
| 6e              |                 10 |                801 |                      11 |                     899 |
| 6f              |                 10 |                799 |                      12 |                     896 |
| 6g              |                 10 |                798 |                      12 |                     895 |
| 6h              |                 10 |                799 |                      15 |                     893 |
| 7               |                 80 |                710 |                      91 |                     798 |
| 7a              |                 10 |                800 |                      14 |                     895 |
| 7b              |                 10 |                796 |                       7 |                     898 |
| 7c              |                 10 |                797 |                      11 |                     895 |
| 7d              |                 10 |                800 |                      14 |                     895 |
| 7e              |                 10 |                797 |                      10 |                     896 |
| 7f              |                 10 |                796 |                      12 |                     893 |
| 7g              |                 10 |                794 |                       9 |                     894 |
| 7h              |                 10 |                795 |                      14 |                     890 |
| 8               |                 80 |                710 |                      90 |                     799 |
| 8a              |                 10 |                797 |                      14 |                     892 |
| 8b              |                 10 |                801 |                       7 |                     903 |
| 8c              |                 10 |                796 |                      12 |                     893 |
| 8d              |                 10 |                796 |                      13 |                     892 |
| 8e              |                 10 |                796 |                      11 |                     894 |
| 8f              |                 10 |                797 |                      12 |                     894 |
| 8g              |                 10 |                793 |                       7 |                     895 |
| 8h              |                 10 |                798 |                      14 |                     893 |
| 9               |                 90 |                700 |                      96 |                     793 |
| 9a              |                 10 |                795 |                      14 |                     890 |
| 9b              |                 10 |                799 |                      12 |                     896 |
| 9c              |                 10 |                790 |                       7 |                     892 |
| 9d              |                 10 |                803 |                       9 |                     903 |
| 9e              |                 10 |                804 |                       8 |                     905 |
| 9f              |                 10 |                799 |                      10 |                     898 |
| 9g              |                 10 |                796 |                      14 |                     891 |
| 9h              |                 10 |                799 |                      13 |                     895 |
| 9i              |                 10 |                799 |                       9 |                     899 |
| SUM             |               1580 |              70207 |                    1778 |                   78820 |

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