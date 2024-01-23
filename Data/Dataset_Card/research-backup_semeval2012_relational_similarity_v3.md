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
# Dataset Card for "relbert/semeval2012_relational_similarity_v3"
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

|                                             |   positives |   negatives |
|:--------------------------------------------|------------:|------------:|
| ('1', 'parent', 'train')                    |         110 |         680 |
| ('1', 'parent', 'validation')               |         129 |         760 |
| ('10', 'parent', 'train')                   |          60 |         730 |
| ('10', 'parent', 'validation')              |          66 |         823 |
| ('10a', 'child', 'train')                   |          10 |         780 |
| ('10a', 'child', 'validation')              |          14 |         875 |
| ('10a', 'child_prototypical', 'train')      |          39 |         506 |
| ('10a', 'child_prototypical', 'validation') |          63 |         938 |
| ('10b', 'child', 'train')                   |          10 |         780 |
| ('10b', 'child', 'validation')              |          13 |         876 |
| ('10b', 'child_prototypical', 'train')      |          39 |         428 |
| ('10b', 'child_prototypical', 'validation') |          57 |         707 |
| ('10c', 'child', 'train')                   |          10 |         780 |
| ('10c', 'child', 'validation')              |          11 |         878 |
| ('10c', 'child_prototypical', 'train')      |          39 |         545 |
| ('10c', 'child_prototypical', 'validation') |          45 |         650 |
| ('10d', 'child', 'train')                   |          10 |         780 |
| ('10d', 'child', 'validation')              |          10 |         879 |
| ('10d', 'child_prototypical', 'train')      |          39 |         506 |
| ('10d', 'child_prototypical', 'validation') |          39 |         506 |
| ('10e', 'child', 'train')                   |          10 |         780 |
| ('10e', 'child', 'validation')              |           8 |         881 |
| ('10e', 'child_prototypical', 'train')      |          39 |         350 |
| ('10e', 'child_prototypical', 'validation') |          27 |         218 |
| ('10f', 'child', 'train')                   |          10 |         780 |
| ('10f', 'child', 'validation')              |          10 |         879 |
| ('10f', 'child_prototypical', 'train')      |          39 |         506 |
| ('10f', 'child_prototypical', 'validation') |          39 |         506 |
| ('1a', 'child', 'train')                    |          10 |         780 |
| ('1a', 'child', 'validation')               |          14 |         875 |
| ('1a', 'child_prototypical', 'train')       |          39 |         428 |
| ('1a', 'child_prototypical', 'validation')  |          63 |         812 |
| ('1b', 'child', 'train')                    |          10 |         780 |
| ('1b', 'child', 'validation')               |          14 |         875 |
| ('1b', 'child_prototypical', 'train')       |          39 |         428 |
| ('1b', 'child_prototypical', 'validation')  |          63 |         812 |
| ('1c', 'child', 'train')                    |          10 |         780 |
| ('1c', 'child', 'validation')               |          11 |         878 |
| ('1c', 'child_prototypical', 'train')       |          39 |         545 |
| ('1c', 'child_prototypical', 'validation')  |          45 |         650 |
| ('1d', 'child', 'train')                    |          10 |         780 |
| ('1d', 'child', 'validation')               |          16 |         873 |
| ('1d', 'child_prototypical', 'train')       |          39 |         428 |
| ('1d', 'child_prototypical', 'validation')  |          75 |        1040 |
| ('1e', 'child', 'train')                    |          10 |         780 |
| ('1e', 'child', 'validation')               |           8 |         881 |
| ('1e', 'child_prototypical', 'train')       |          39 |         311 |
| ('1e', 'child_prototypical', 'validation')  |          27 |         191 |
| ('2', 'parent', 'train')                    |         100 |         690 |
| ('2', 'parent', 'validation')               |         117 |         772 |
| ('2a', 'child', 'train')                    |          10 |         780 |
| ('2a', 'child', 'validation')               |          15 |         874 |
| ('2a', 'child_prototypical', 'train')       |          39 |         506 |
| ('2a', 'child_prototypical', 'validation')  |          69 |        1061 |
| ('2b', 'child', 'train')                    |          10 |         780 |
| ('2b', 'child', 'validation')               |          11 |         878 |
| ('2b', 'child_prototypical', 'train')       |          39 |         389 |
| ('2b', 'child_prototypical', 'validation')  |          45 |         470 |
| ('2c', 'child', 'train')                    |          10 |         780 |
| ('2c', 'child', 'validation')               |          13 |         876 |
| ('2c', 'child_prototypical', 'train')       |          39 |         467 |
| ('2c', 'child_prototypical', 'validation')  |          57 |         764 |
| ('2d', 'child', 'train')                    |          10 |         780 |
| ('2d', 'child', 'validation')               |          10 |         879 |
| ('2d', 'child_prototypical', 'train')       |          39 |         467 |
| ('2d', 'child_prototypical', 'validation')  |          39 |         467 |
| ('2e', 'child', 'train')                    |          10 |         780 |
| ('2e', 'child', 'validation')               |          11 |         878 |
| ('2e', 'child_prototypical', 'train')       |          39 |         506 |
| ('2e', 'child_prototypical', 'validation')  |          45 |         605 |
| ('2f', 'child', 'train')                    |          10 |         780 |
| ('2f', 'child', 'validation')               |          11 |         878 |
| ('2f', 'child_prototypical', 'train')       |          39 |         623 |
| ('2f', 'child_prototypical', 'validation')  |          45 |         740 |
| ('2g', 'child', 'train')                    |          10 |         780 |
| ('2g', 'child', 'validation')               |          16 |         873 |
| ('2g', 'child_prototypical', 'train')       |          39 |         389 |
| ('2g', 'child_prototypical', 'validation')  |          75 |         965 |
| ('2h', 'child', 'train')                    |          10 |         780 |
| ('2h', 'child', 'validation')               |          11 |         878 |
| ('2h', 'child_prototypical', 'train')       |          39 |         506 |
| ('2h', 'child_prototypical', 'validation')  |          45 |         605 |
| ('2i', 'child', 'train')                    |          10 |         780 |
| ('2i', 'child', 'validation')               |           9 |         880 |
| ('2i', 'child_prototypical', 'train')       |          39 |         545 |
| ('2i', 'child_prototypical', 'validation')  |          33 |         446 |
| ('2j', 'child', 'train')                    |          10 |         780 |
| ('2j', 'child', 'validation')               |          10 |         879 |
| ('2j', 'child_prototypical', 'train')       |          39 |         584 |
| ('2j', 'child_prototypical', 'validation')  |          39 |         584 |
| ('3', 'parent', 'train')                    |          80 |         710 |
| ('3', 'parent', 'validation')               |          80 |         809 |
| ('3a', 'child', 'train')                    |          10 |         780 |
| ('3a', 'child', 'validation')               |          11 |         878 |
| ('3a', 'child_prototypical', 'train')       |          39 |         506 |
| ('3a', 'child_prototypical', 'validation')  |          45 |         605 |
| ('3b', 'child', 'train')                    |          10 |         780 |
| ('3b', 'child', 'validation')               |          11 |         878 |
| ('3b', 'child_prototypical', 'train')       |          39 |         623 |
| ('3b', 'child_prototypical', 'validation')  |          45 |         740 |
| ('3c', 'child', 'train')                    |          10 |         780 |
| ('3c', 'child', 'validation')               |          12 |         877 |
| ('3c', 'child_prototypical', 'train')       |          39 |         467 |
| ('3c', 'child_prototypical', 'validation')  |          51 |         659 |
| ('3d', 'child', 'train')                    |          10 |         780 |
| ('3d', 'child', 'validation')               |          14 |         875 |
| ('3d', 'child_prototypical', 'train')       |          39 |         467 |
| ('3d', 'child_prototypical', 'validation')  |          63 |         875 |
| ('3e', 'child', 'train')                    |          10 |         780 |
| ('3e', 'child', 'validation')               |           5 |         884 |
| ('3e', 'child_prototypical', 'train')       |          39 |         623 |
| ('3e', 'child_prototypical', 'validation')  |          10 |         140 |
| ('3f', 'child', 'train')                    |          10 |         780 |
| ('3f', 'child', 'validation')               |          11 |         878 |
| ('3f', 'child_prototypical', 'train')       |          39 |         662 |
| ('3f', 'child_prototypical', 'validation')  |          45 |         785 |
| ('3g', 'child', 'train')                    |          10 |         780 |
| ('3g', 'child', 'validation')               |           6 |         883 |
| ('3g', 'child_prototypical', 'train')       |          39 |         584 |
| ('3g', 'child_prototypical', 'validation')  |          15 |         200 |
| ('3h', 'child', 'train')                    |          10 |         780 |
| ('3h', 'child', 'validation')               |          10 |         879 |
| ('3h', 'child_prototypical', 'train')       |          39 |         584 |
| ('3h', 'child_prototypical', 'validation')  |          39 |         584 |
| ('4', 'parent', 'train')                    |          80 |         710 |
| ('4', 'parent', 'validation')               |          82 |         807 |
| ('4a', 'child', 'train')                    |          10 |         780 |
| ('4a', 'child', 'validation')               |          11 |         878 |
| ('4a', 'child_prototypical', 'train')       |          39 |         623 |
| ('4a', 'child_prototypical', 'validation')  |          45 |         740 |
| ('4b', 'child', 'train')                    |          10 |         780 |
| ('4b', 'child', 'validation')               |           7 |         882 |
| ('4b', 'child_prototypical', 'train')       |          39 |         428 |
| ('4b', 'child_prototypical', 'validation')  |          21 |         203 |
| ('4c', 'child', 'train')                    |          10 |         780 |
| ('4c', 'child', 'validation')               |          12 |         877 |
| ('4c', 'child_prototypical', 'train')       |          39 |         545 |
| ('4c', 'child_prototypical', 'validation')  |          51 |         761 |
| ('4d', 'child', 'train')                    |          10 |         780 |
| ('4d', 'child', 'validation')               |           4 |         885 |
| ('4d', 'child_prototypical', 'train')       |          39 |         389 |
| ('4d', 'child_prototypical', 'validation')  |           6 |          46 |
| ('4e', 'child', 'train')                    |          10 |         780 |
| ('4e', 'child', 'validation')               |          12 |         877 |
| ('4e', 'child_prototypical', 'train')       |          39 |         623 |
| ('4e', 'child_prototypical', 'validation')  |          51 |         863 |
| ('4f', 'child', 'train')                    |          10 |         780 |
| ('4f', 'child', 'validation')               |           9 |         880 |
| ('4f', 'child_prototypical', 'train')       |          39 |         623 |
| ('4f', 'child_prototypical', 'validation')  |          33 |         512 |
| ('4g', 'child', 'train')                    |          10 |         780 |
| ('4g', 'child', 'validation')               |          15 |         874 |
| ('4g', 'child_prototypical', 'train')       |          39 |         467 |
| ('4g', 'child_prototypical', 'validation')  |          69 |         992 |
| ('4h', 'child', 'train')                    |          10 |         780 |
| ('4h', 'child', 'validation')               |          12 |         877 |
| ('4h', 'child_prototypical', 'train')       |          39 |         584 |
| ('4h', 'child_prototypical', 'validation')  |          51 |         812 |
| ('5', 'parent', 'train')                    |          90 |         700 |
| ('5', 'parent', 'validation')               |         105 |         784 |
| ('5a', 'child', 'train')                    |          10 |         780 |
| ('5a', 'child', 'validation')               |          14 |         875 |
| ('5a', 'child_prototypical', 'train')       |          39 |         467 |
| ('5a', 'child_prototypical', 'validation')  |          63 |         875 |
| ('5b', 'child', 'train')                    |          10 |         780 |
| ('5b', 'child', 'validation')               |           8 |         881 |
| ('5b', 'child_prototypical', 'train')       |          39 |         584 |
| ('5b', 'child_prototypical', 'validation')  |          27 |         380 |
| ('5c', 'child', 'train')                    |          10 |         780 |
| ('5c', 'child', 'validation')               |          11 |         878 |
| ('5c', 'child_prototypical', 'train')       |          39 |         506 |
| ('5c', 'child_prototypical', 'validation')  |          45 |         605 |
| ('5d', 'child', 'train')                    |          10 |         780 |
| ('5d', 'child', 'validation')               |          15 |         874 |
| ('5d', 'child_prototypical', 'train')       |          39 |         428 |
| ('5d', 'child_prototypical', 'validation')  |          69 |         923 |
| ('5e', 'child', 'train')                    |          10 |         780 |
| ('5e', 'child', 'validation')               |           8 |         881 |
| ('5e', 'child_prototypical', 'train')       |          39 |         584 |
| ('5e', 'child_prototypical', 'validation')  |          27 |         380 |
| ('5f', 'child', 'train')                    |          10 |         780 |
| ('5f', 'child', 'validation')               |          11 |         878 |
| ('5f', 'child_prototypical', 'train')       |          39 |         584 |
| ('5f', 'child_prototypical', 'validation')  |          45 |         695 |
| ('5g', 'child', 'train')                    |          10 |         780 |
| ('5g', 'child', 'validation')               |           9 |         880 |
| ('5g', 'child_prototypical', 'train')       |          39 |         623 |
| ('5g', 'child_prototypical', 'validation')  |          33 |         512 |
| ('5h', 'child', 'train')                    |          10 |         780 |
| ('5h', 'child', 'validation')               |          15 |         874 |
| ('5h', 'child_prototypical', 'train')       |          39 |         545 |
| ('5h', 'child_prototypical', 'validation')  |          69 |        1130 |
| ('5i', 'child', 'train')                    |          10 |         780 |
| ('5i', 'child', 'validation')               |          14 |         875 |
| ('5i', 'child_prototypical', 'train')       |          39 |         545 |
| ('5i', 'child_prototypical', 'validation')  |          63 |        1001 |
| ('6', 'parent', 'train')                    |          80 |         710 |
| ('6', 'parent', 'validation')               |          99 |         790 |
| ('6a', 'child', 'train')                    |          10 |         780 |
| ('6a', 'child', 'validation')               |          15 |         874 |
| ('6a', 'child_prototypical', 'train')       |          39 |         467 |
| ('6a', 'child_prototypical', 'validation')  |          69 |         992 |
| ('6b', 'child', 'train')                    |          10 |         780 |
| ('6b', 'child', 'validation')               |          11 |         878 |
| ('6b', 'child_prototypical', 'train')       |          39 |         584 |
| ('6b', 'child_prototypical', 'validation')  |          45 |         695 |
| ('6c', 'child', 'train')                    |          10 |         780 |
| ('6c', 'child', 'validation')               |          13 |         876 |
| ('6c', 'child_prototypical', 'train')       |          39 |         584 |
| ('6c', 'child_prototypical', 'validation')  |          57 |         935 |
| ('6d', 'child', 'train')                    |          10 |         780 |
| ('6d', 'child', 'validation')               |          10 |         879 |
| ('6d', 'child_prototypical', 'train')       |          39 |         701 |
| ('6d', 'child_prototypical', 'validation')  |          39 |         701 |
| ('6e', 'child', 'train')                    |          10 |         780 |
| ('6e', 'child', 'validation')               |          11 |         878 |
| ('6e', 'child_prototypical', 'train')       |          39 |         584 |
| ('6e', 'child_prototypical', 'validation')  |          45 |         695 |
| ('6f', 'child', 'train')                    |          10 |         780 |
| ('6f', 'child', 'validation')               |          12 |         877 |
| ('6f', 'child_prototypical', 'train')       |          39 |         506 |
| ('6f', 'child_prototypical', 'validation')  |          51 |         710 |
| ('6g', 'child', 'train')                    |          10 |         780 |
| ('6g', 'child', 'validation')               |          12 |         877 |
| ('6g', 'child_prototypical', 'train')       |          39 |         467 |
| ('6g', 'child_prototypical', 'validation')  |          51 |         659 |
| ('6h', 'child', 'train')                    |          10 |         780 |
| ('6h', 'child', 'validation')               |          15 |         874 |
| ('6h', 'child_prototypical', 'train')       |          39 |         506 |
| ('6h', 'child_prototypical', 'validation')  |          69 |        1061 |
| ('7', 'parent', 'train')                    |          80 |         710 |
| ('7', 'parent', 'validation')               |          91 |         798 |
| ('7a', 'child', 'train')                    |          10 |         780 |
| ('7a', 'child', 'validation')               |          14 |         875 |
| ('7a', 'child_prototypical', 'train')       |          39 |         545 |
| ('7a', 'child_prototypical', 'validation')  |          63 |        1001 |
| ('7b', 'child', 'train')                    |          10 |         780 |
| ('7b', 'child', 'validation')               |           7 |         882 |
| ('7b', 'child_prototypical', 'train')       |          39 |         389 |
| ('7b', 'child_prototypical', 'validation')  |          21 |         182 |
| ('7c', 'child', 'train')                    |          10 |         780 |
| ('7c', 'child', 'validation')               |          11 |         878 |
| ('7c', 'child_prototypical', 'train')       |          39 |         428 |
| ('7c', 'child_prototypical', 'validation')  |          45 |         515 |
| ('7d', 'child', 'train')                    |          10 |         780 |
| ('7d', 'child', 'validation')               |          14 |         875 |
| ('7d', 'child_prototypical', 'train')       |          39 |         545 |
| ('7d', 'child_prototypical', 'validation')  |          63 |        1001 |
| ('7e', 'child', 'train')                    |          10 |         780 |
| ('7e', 'child', 'validation')               |          10 |         879 |
| ('7e', 'child_prototypical', 'train')       |          39 |         428 |
| ('7e', 'child_prototypical', 'validation')  |          39 |         428 |
| ('7f', 'child', 'train')                    |          10 |         780 |
| ('7f', 'child', 'validation')               |          12 |         877 |
| ('7f', 'child_prototypical', 'train')       |          39 |         389 |
| ('7f', 'child_prototypical', 'validation')  |          51 |         557 |
| ('7g', 'child', 'train')                    |          10 |         780 |
| ('7g', 'child', 'validation')               |           9 |         880 |
| ('7g', 'child_prototypical', 'train')       |          39 |         311 |
| ('7g', 'child_prototypical', 'validation')  |          33 |         248 |
| ('7h', 'child', 'train')                    |          10 |         780 |
| ('7h', 'child', 'validation')               |          14 |         875 |
| ('7h', 'child_prototypical', 'train')       |          39 |         350 |
| ('7h', 'child_prototypical', 'validation')  |          63 |         686 |
| ('8', 'parent', 'train')                    |          80 |         710 |
| ('8', 'parent', 'validation')               |          90 |         799 |
| ('8a', 'child', 'train')                    |          10 |         780 |
| ('8a', 'child', 'validation')               |          14 |         875 |
| ('8a', 'child_prototypical', 'train')       |          39 |         428 |
| ('8a', 'child_prototypical', 'validation')  |          63 |         812 |
| ('8b', 'child', 'train')                    |          10 |         780 |
| ('8b', 'child', 'validation')               |           7 |         882 |
| ('8b', 'child_prototypical', 'train')       |          39 |         584 |
| ('8b', 'child_prototypical', 'validation')  |          21 |         287 |
| ('8c', 'child', 'train')                    |          10 |         780 |
| ('8c', 'child', 'validation')               |          12 |         877 |
| ('8c', 'child_prototypical', 'train')       |          39 |         389 |
| ('8c', 'child_prototypical', 'validation')  |          51 |         557 |
| ('8d', 'child', 'train')                    |          10 |         780 |
| ('8d', 'child', 'validation')               |          13 |         876 |
| ('8d', 'child_prototypical', 'train')       |          39 |         389 |
| ('8d', 'child_prototypical', 'validation')  |          57 |         650 |
| ('8e', 'child', 'train')                    |          10 |         780 |
| ('8e', 'child', 'validation')               |          11 |         878 |
| ('8e', 'child_prototypical', 'train')       |          39 |         389 |
| ('8e', 'child_prototypical', 'validation')  |          45 |         470 |
| ('8f', 'child', 'train')                    |          10 |         780 |
| ('8f', 'child', 'validation')               |          12 |         877 |
| ('8f', 'child_prototypical', 'train')       |          39 |         428 |
| ('8f', 'child_prototypical', 'validation')  |          51 |         608 |
| ('8g', 'child', 'train')                    |          10 |         780 |
| ('8g', 'child', 'validation')               |           7 |         882 |
| ('8g', 'child_prototypical', 'train')       |          39 |         272 |
| ('8g', 'child_prototypical', 'validation')  |          21 |         119 |
| ('8h', 'child', 'train')                    |          10 |         780 |
| ('8h', 'child', 'validation')               |          14 |         875 |
| ('8h', 'child_prototypical', 'train')       |          39 |         467 |
| ('8h', 'child_prototypical', 'validation')  |          63 |         875 |
| ('9', 'parent', 'train')                    |          90 |         700 |
| ('9', 'parent', 'validation')               |          96 |         793 |
| ('9a', 'child', 'train')                    |          10 |         780 |
| ('9a', 'child', 'validation')               |          14 |         875 |
| ('9a', 'child_prototypical', 'train')       |          39 |         350 |
| ('9a', 'child_prototypical', 'validation')  |          63 |         686 |
| ('9b', 'child', 'train')                    |          10 |         780 |
| ('9b', 'child', 'validation')               |          12 |         877 |
| ('9b', 'child_prototypical', 'train')       |          39 |         506 |
| ('9b', 'child_prototypical', 'validation')  |          51 |         710 |
| ('9c', 'child', 'train')                    |          10 |         780 |
| ('9c', 'child', 'validation')               |           7 |         882 |
| ('9c', 'child_prototypical', 'train')       |          39 |         155 |
| ('9c', 'child_prototypical', 'validation')  |          21 |          56 |
| ('9d', 'child', 'train')                    |          10 |         780 |
| ('9d', 'child', 'validation')               |           9 |         880 |
| ('9d', 'child_prototypical', 'train')       |          39 |         662 |
| ('9d', 'child_prototypical', 'validation')  |          33 |         545 |
| ('9e', 'child', 'train')                    |          10 |         780 |
| ('9e', 'child', 'validation')               |           8 |         881 |
| ('9e', 'child_prototypical', 'train')       |          39 |         701 |
| ('9e', 'child_prototypical', 'validation')  |          27 |         461 |
| ('9f', 'child', 'train')                    |          10 |         780 |
| ('9f', 'child', 'validation')               |          10 |         879 |
| ('9f', 'child_prototypical', 'train')       |          39 |         506 |
| ('9f', 'child_prototypical', 'validation')  |          39 |         506 |
| ('9g', 'child', 'train')                    |          10 |         780 |
| ('9g', 'child', 'validation')               |          14 |         875 |
| ('9g', 'child_prototypical', 'train')       |          39 |         389 |
| ('9g', 'child_prototypical', 'validation')  |          63 |         749 |
| ('9h', 'child', 'train')                    |          10 |         780 |
| ('9h', 'child', 'validation')               |          13 |         876 |
| ('9h', 'child_prototypical', 'train')       |          39 |         506 |
| ('9h', 'child_prototypical', 'validation')  |          57 |         821 |
| ('9i', 'child', 'train')                    |          10 |         780 |
| ('9i', 'child', 'validation')               |           9 |         880 |
| ('9i', 'child_prototypical', 'train')       |          39 |         506 |
| ('9i', 'child_prototypical', 'validation')  |          33 |         413 |

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