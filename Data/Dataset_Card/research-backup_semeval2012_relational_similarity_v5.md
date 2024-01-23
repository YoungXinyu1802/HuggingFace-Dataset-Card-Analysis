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
# Dataset Card for "relbert/semeval2012_relational_similarity_v5"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/S12-1047/](https://aclanthology.org/S12-1047/)
- **Dataset:** SemEval2012: Relational Similarity

### Dataset Summary

***IMPORTANT***: This is the same dataset as [relbert/semeval2012_relational_similarity](https://huggingface.co/datasets/relbert/semeval2012_relational_similarity),
but with a different dataset construction.

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

|                                           |   positives |   negatives |
|:------------------------------------------|------------:|------------:|
| ('1', 'parent', 'train')                  |         110 |         680 |
| ('10', 'parent', 'train')                 |          60 |         730 |
| ('10a', 'child', 'train')                 |          10 |        1655 |
| ('10a', 'child_prototypical', 'train')    |         123 |        2438 |
| ('10b', 'child', 'train')                 |          10 |        1656 |
| ('10b', 'child_prototypical', 'train')    |         117 |        2027 |
| ('10c', 'child', 'train')                 |          10 |        1658 |
| ('10c', 'child_prototypical', 'train')    |         105 |        2030 |
| ('10d', 'child', 'train')                 |          10 |        1659 |
| ('10d', 'child_prototypical', 'train')    |          99 |        1766 |
| ('10e', 'child', 'train')                 |          10 |        1661 |
| ('10e', 'child_prototypical', 'train')    |          87 |        1118 |
| ('10f', 'child', 'train')                 |          10 |        1659 |
| ('10f', 'child_prototypical', 'train')    |          99 |        1766 |
| ('1a', 'child', 'train')                  |          10 |        1655 |
| ('1a', 'child_prototypical', 'train')     |         123 |        2192 |
| ('1b', 'child', 'train')                  |          10 |        1655 |
| ('1b', 'child_prototypical', 'train')     |         123 |        2192 |
| ('1c', 'child', 'train')                  |          10 |        1658 |
| ('1c', 'child_prototypical', 'train')     |         105 |        2030 |
| ('1d', 'child', 'train')                  |          10 |        1653 |
| ('1d', 'child_prototypical', 'train')     |         135 |        2540 |
| ('1e', 'child', 'train')                  |          10 |        1661 |
| ('1e', 'child_prototypical', 'train')     |          87 |        1031 |
| ('2', 'parent', 'train')                  |         100 |         690 |
| ('2a', 'child', 'train')                  |          10 |        1654 |
| ('2a', 'child_prototypical', 'train')     |         129 |        2621 |
| ('2b', 'child', 'train')                  |          10 |        1658 |
| ('2b', 'child_prototypical', 'train')     |         105 |        1610 |
| ('2c', 'child', 'train')                  |          10 |        1656 |
| ('2c', 'child_prototypical', 'train')     |         117 |        2144 |
| ('2d', 'child', 'train')                  |          10 |        1659 |
| ('2d', 'child_prototypical', 'train')     |          99 |        1667 |
| ('2e', 'child', 'train')                  |          10 |        1658 |
| ('2e', 'child_prototypical', 'train')     |         105 |        1925 |
| ('2f', 'child', 'train')                  |          10 |        1658 |
| ('2f', 'child_prototypical', 'train')     |         105 |        2240 |
| ('2g', 'child', 'train')                  |          10 |        1653 |
| ('2g', 'child_prototypical', 'train')     |         135 |        2405 |
| ('2h', 'child', 'train')                  |          10 |        1658 |
| ('2h', 'child_prototypical', 'train')     |         105 |        1925 |
| ('2i', 'child', 'train')                  |          10 |        1660 |
| ('2i', 'child_prototypical', 'train')     |          93 |        1706 |
| ('2j', 'child', 'train')                  |          10 |        1659 |
| ('2j', 'child_prototypical', 'train')     |          99 |        1964 |
| ('3', 'parent', 'train')                  |          80 |         710 |
| ('3a', 'child', 'train')                  |          10 |        1658 |
| ('3a', 'child_prototypical', 'train')     |         105 |        1925 |
| ('3b', 'child', 'train')                  |          10 |        1658 |
| ('3b', 'child_prototypical', 'train')     |         105 |        2240 |
| ('3c', 'child', 'train')                  |          10 |        1657 |
| ('3c', 'child_prototypical', 'train')     |         111 |        1979 |
| ('3d', 'child', 'train')                  |          10 |        1655 |
| ('3d', 'child_prototypical', 'train')     |         123 |        2315 |
| ('3e', 'child', 'train')                  |          10 |        1664 |
| ('3e', 'child_prototypical', 'train')     |          69 |        1268 |
| ('3f', 'child', 'train')                  |          10 |        1658 |
| ('3f', 'child_prototypical', 'train')     |         105 |        2345 |
| ('3g', 'child', 'train')                  |          10 |        1663 |
| ('3g', 'child_prototypical', 'train')     |          75 |        1340 |
| ('3h', 'child', 'train')                  |          10 |        1659 |
| ('3h', 'child_prototypical', 'train')     |          99 |        1964 |
| ('4', 'parent', 'train')                  |          80 |         710 |
| ('4a', 'child', 'train')                  |          10 |        1658 |
| ('4a', 'child_prototypical', 'train')     |         105 |        2240 |
| ('4b', 'child', 'train')                  |          10 |        1662 |
| ('4b', 'child_prototypical', 'train')     |          81 |        1163 |
| ('4c', 'child', 'train')                  |          10 |        1657 |
| ('4c', 'child_prototypical', 'train')     |         111 |        2201 |
| ('4d', 'child', 'train')                  |          10 |        1665 |
| ('4d', 'child_prototypical', 'train')     |          63 |         749 |
| ('4e', 'child', 'train')                  |          10 |        1657 |
| ('4e', 'child_prototypical', 'train')     |         111 |        2423 |
| ('4f', 'child', 'train')                  |          10 |        1660 |
| ('4f', 'child_prototypical', 'train')     |          93 |        1892 |
| ('4g', 'child', 'train')                  |          10 |        1654 |
| ('4g', 'child_prototypical', 'train')     |         129 |        2492 |
| ('4h', 'child', 'train')                  |          10 |        1657 |
| ('4h', 'child_prototypical', 'train')     |         111 |        2312 |
| ('5', 'parent', 'train')                  |          90 |         700 |
| ('5a', 'child', 'train')                  |          10 |        1655 |
| ('5a', 'child_prototypical', 'train')     |         123 |        2315 |
| ('5b', 'child', 'train')                  |          10 |        1661 |
| ('5b', 'child_prototypical', 'train')     |          87 |        1640 |
| ('5c', 'child', 'train')                  |          10 |        1658 |
| ('5c', 'child_prototypical', 'train')     |         105 |        1925 |
| ('5d', 'child', 'train')                  |          10 |        1654 |
| ('5d', 'child_prototypical', 'train')     |         129 |        2363 |
| ('5e', 'child', 'train')                  |          10 |        1661 |
| ('5e', 'child_prototypical', 'train')     |          87 |        1640 |
| ('5f', 'child', 'train')                  |          10 |        1658 |
| ('5f', 'child_prototypical', 'train')     |         105 |        2135 |
| ('5g', 'child', 'train')                  |          10 |        1660 |
| ('5g', 'child_prototypical', 'train')     |          93 |        1892 |
| ('5h', 'child', 'train')                  |          10 |        1654 |
| ('5h', 'child_prototypical', 'train')     |         129 |        2750 |
| ('5i', 'child', 'train')                  |          10 |        1655 |
| ('5i', 'child_prototypical', 'train')     |         123 |        2561 |
| ('6', 'parent', 'train')                  |          80 |         710 |
| ('6a', 'child', 'train')                  |          10 |        1654 |
| ('6a', 'child_prototypical', 'train')     |         129 |        2492 |
| ('6b', 'child', 'train')                  |          10 |        1658 |
| ('6b', 'child_prototypical', 'train')     |         105 |        2135 |
| ('6c', 'child', 'train')                  |          10 |        1656 |
| ('6c', 'child_prototypical', 'train')     |         117 |        2495 |
| ('6d', 'child', 'train')                  |          10 |        1659 |
| ('6d', 'child_prototypical', 'train')     |          99 |        2261 |
| ('6e', 'child', 'train')                  |          10 |        1658 |
| ('6e', 'child_prototypical', 'train')     |         105 |        2135 |
| ('6f', 'child', 'train')                  |          10 |        1657 |
| ('6f', 'child_prototypical', 'train')     |         111 |        2090 |
| ('6g', 'child', 'train')                  |          10 |        1657 |
| ('6g', 'child_prototypical', 'train')     |         111 |        1979 |
| ('6h', 'child', 'train')                  |          10 |        1654 |
| ('6h', 'child_prototypical', 'train')     |         129 |        2621 |
| ('7', 'parent', 'train')                  |          80 |         710 |
| ('7a', 'child', 'train')                  |          10 |        1655 |
| ('7a', 'child_prototypical', 'train')     |         123 |        2561 |
| ('7b', 'child', 'train')                  |          10 |        1662 |
| ('7b', 'child_prototypical', 'train')     |          81 |        1082 |
| ('7c', 'child', 'train')                  |          10 |        1658 |
| ('7c', 'child_prototypical', 'train')     |         105 |        1715 |
| ('7d', 'child', 'train')                  |          10 |        1655 |
| ('7d', 'child_prototypical', 'train')     |         123 |        2561 |
| ('7e', 'child', 'train')                  |          10 |        1659 |
| ('7e', 'child_prototypical', 'train')     |          99 |        1568 |
| ('7f', 'child', 'train')                  |          10 |        1657 |
| ('7f', 'child_prototypical', 'train')     |         111 |        1757 |
| ('7g', 'child', 'train')                  |          10 |        1660 |
| ('7g', 'child_prototypical', 'train')     |          93 |        1148 |
| ('7h', 'child', 'train')                  |          10 |        1655 |
| ('7h', 'child_prototypical', 'train')     |         123 |        1946 |
| ('8', 'parent', 'train')                  |          80 |         710 |
| ('8a', 'child', 'train')                  |          10 |        1655 |
| ('8a', 'child_prototypical', 'train')     |         123 |        2192 |
| ('8b', 'child', 'train')                  |          10 |        1662 |
| ('8b', 'child_prototypical', 'train')     |          81 |        1487 |
| ('8c', 'child', 'train')                  |          10 |        1657 |
| ('8c', 'child_prototypical', 'train')     |         111 |        1757 |
| ('8d', 'child', 'train')                  |          10 |        1656 |
| ('8d', 'child_prototypical', 'train')     |         117 |        1910 |
| ('8e', 'child', 'train')                  |          10 |        1658 |
| ('8e', 'child_prototypical', 'train')     |         105 |        1610 |
| ('8f', 'child', 'train')                  |          10 |        1657 |
| ('8f', 'child_prototypical', 'train')     |         111 |        1868 |
| ('8g', 'child', 'train')                  |          10 |        1662 |
| ('8g', 'child_prototypical', 'train')     |          81 |         839 |
| ('8h', 'child', 'train')                  |          10 |        1655 |
| ('8h', 'child_prototypical', 'train')     |         123 |        2315 |
| ('9', 'parent', 'train')                  |          90 |         700 |
| ('9a', 'child', 'train')                  |          10 |        1655 |
| ('9a', 'child_prototypical', 'train')     |         123 |        1946 |
| ('9b', 'child', 'train')                  |          10 |        1657 |
| ('9b', 'child_prototypical', 'train')     |         111 |        2090 |
| ('9c', 'child', 'train')                  |          10 |        1662 |
| ('9c', 'child_prototypical', 'train')     |          81 |         596 |
| ('9d', 'child', 'train')                  |          10 |        1660 |
| ('9d', 'child_prototypical', 'train')     |          93 |        1985 |
| ('9e', 'child', 'train')                  |          10 |        1661 |
| ('9e', 'child_prototypical', 'train')     |          87 |        1901 |
| ('9f', 'child', 'train')                  |          10 |        1659 |
| ('9f', 'child_prototypical', 'train')     |          99 |        1766 |
| ('9g', 'child', 'train')                  |          10 |        1655 |
| ('9g', 'child_prototypical', 'train')     |         123 |        2069 |
| ('9h', 'child', 'train')                  |          10 |        1656 |
| ('9h', 'child_prototypical', 'train')     |         117 |        2261 |
| ('9i', 'child', 'train')                  |          10 |        1660 |
| ('9i', 'child_prototypical', 'train')     |          93 |        1613 |
| ('AtLocation', 'N/A', 'validation')       |         960 |        4646 |
| ('CapableOf', 'N/A', 'validation')        |         536 |        4734 |
| ('Causes', 'N/A', 'validation')           |         194 |        4738 |
| ('CausesDesire', 'N/A', 'validation')     |          40 |        4730 |
| ('CreatedBy', 'N/A', 'validation')        |           4 |        3554 |
| ('DefinedAs', 'N/A', 'validation')        |           4 |        1182 |
| ('Desires', 'N/A', 'validation')          |          56 |        4732 |
| ('HasA', 'N/A', 'validation')             |         168 |        4772 |
| ('HasFirstSubevent', 'N/A', 'validation') |           4 |        3554 |
| ('HasLastSubevent', 'N/A', 'validation')  |          10 |        4732 |
| ('HasPrerequisite', 'N/A', 'validation')  |         450 |        4744 |
| ('HasProperty', 'N/A', 'validation')      |         266 |        4766 |
| ('HasSubevent', 'N/A', 'validation')      |         330 |        4768 |
| ('IsA', 'N/A', 'validation')              |         816 |        4688 |
| ('MadeOf', 'N/A', 'validation')           |          48 |        4726 |
| ('MotivatedByGoal', 'N/A', 'validation')  |          50 |        4736 |
| ('PartOf', 'N/A', 'validation')           |          82 |        4742 |
| ('ReceivesAction', 'N/A', 'validation')   |          52 |        4726 |
| ('SymbolOf', 'N/A', 'validation')         |           4 |        1184 |
| ('UsedFor', 'N/A', 'validation')          |         660 |        4760 |


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