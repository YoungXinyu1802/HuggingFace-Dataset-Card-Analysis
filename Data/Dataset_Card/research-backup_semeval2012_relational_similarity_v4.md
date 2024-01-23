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
# Dataset Card for "relbert/semeval2012_relational_similarity_v4"
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
| ('1', 'parent', 'train')                    |          88 |         544 |
| ('1', 'parent', 'validation')               |          22 |         136 |
| ('10', 'parent', 'train')                   |          48 |         584 |
| ('10', 'parent', 'validation')              |          12 |         146 |
| ('10a', 'child', 'train')                   |           8 |        1324 |
| ('10a', 'child', 'validation')              |           2 |         331 |
| ('10a', 'child_prototypical', 'train')      |          97 |        1917 |
| ('10a', 'child_prototypical', 'validation') |          26 |         521 |
| ('10b', 'child', 'train')                   |           8 |        1325 |
| ('10b', 'child', 'validation')              |           2 |         331 |
| ('10b', 'child_prototypical', 'train')      |          90 |        1558 |
| ('10b', 'child_prototypical', 'validation') |          27 |         469 |
| ('10c', 'child', 'train')                   |           8 |        1327 |
| ('10c', 'child', 'validation')              |           2 |         331 |
| ('10c', 'child_prototypical', 'train')      |          85 |        1640 |
| ('10c', 'child_prototypical', 'validation') |          20 |         390 |
| ('10d', 'child', 'train')                   |           8 |        1328 |
| ('10d', 'child', 'validation')              |           2 |         331 |
| ('10d', 'child_prototypical', 'train')      |          77 |        1390 |
| ('10d', 'child_prototypical', 'validation') |          22 |         376 |
| ('10e', 'child', 'train')                   |           8 |        1329 |
| ('10e', 'child', 'validation')              |           2 |         332 |
| ('10e', 'child_prototypical', 'train')      |          67 |         884 |
| ('10e', 'child_prototypical', 'validation') |          20 |         234 |
| ('10f', 'child', 'train')                   |           8 |        1328 |
| ('10f', 'child', 'validation')              |           2 |         331 |
| ('10f', 'child_prototypical', 'train')      |          80 |        1460 |
| ('10f', 'child_prototypical', 'validation') |          19 |         306 |
| ('1a', 'child', 'train')                    |           8 |        1324 |
| ('1a', 'child', 'validation')               |           2 |         331 |
| ('1a', 'child_prototypical', 'train')       |         106 |        1854 |
| ('1a', 'child_prototypical', 'validation')  |          17 |         338 |
| ('1b', 'child', 'train')                    |           8 |        1324 |
| ('1b', 'child', 'validation')               |           2 |         331 |
| ('1b', 'child_prototypical', 'train')       |          95 |        1712 |
| ('1b', 'child_prototypical', 'validation')  |          28 |         480 |
| ('1c', 'child', 'train')                    |           8 |        1327 |
| ('1c', 'child', 'validation')               |           2 |         331 |
| ('1c', 'child_prototypical', 'train')       |          80 |        1528 |
| ('1c', 'child_prototypical', 'validation')  |          25 |         502 |
| ('1d', 'child', 'train')                    |           8 |        1323 |
| ('1d', 'child', 'validation')               |           2 |         330 |
| ('1d', 'child_prototypical', 'train')       |         112 |        2082 |
| ('1d', 'child_prototypical', 'validation')  |          23 |         458 |
| ('1e', 'child', 'train')                    |           8 |        1329 |
| ('1e', 'child', 'validation')               |           2 |         332 |
| ('1e', 'child_prototypical', 'train')       |          63 |         775 |
| ('1e', 'child_prototypical', 'validation')  |          24 |         256 |
| ('2', 'parent', 'train')                    |          80 |         552 |
| ('2', 'parent', 'validation')               |          20 |         138 |
| ('2a', 'child', 'train')                    |           8 |        1324 |
| ('2a', 'child', 'validation')               |           2 |         330 |
| ('2a', 'child_prototypical', 'train')       |          93 |        1885 |
| ('2a', 'child_prototypical', 'validation')  |          36 |         736 |
| ('2b', 'child', 'train')                    |           8 |        1327 |
| ('2b', 'child', 'validation')               |           2 |         331 |
| ('2b', 'child_prototypical', 'train')       |          86 |        1326 |
| ('2b', 'child_prototypical', 'validation')  |          19 |         284 |
| ('2c', 'child', 'train')                    |           8 |        1325 |
| ('2c', 'child', 'validation')               |           2 |         331 |
| ('2c', 'child_prototypical', 'train')       |          96 |        1773 |
| ('2c', 'child_prototypical', 'validation')  |          21 |         371 |
| ('2d', 'child', 'train')                    |           8 |        1328 |
| ('2d', 'child', 'validation')               |           2 |         331 |
| ('2d', 'child_prototypical', 'train')       |          79 |        1329 |
| ('2d', 'child_prototypical', 'validation')  |          20 |         338 |
| ('2e', 'child', 'train')                    |           8 |        1327 |
| ('2e', 'child', 'validation')               |           2 |         331 |
| ('2e', 'child_prototypical', 'train')       |          82 |        1462 |
| ('2e', 'child_prototypical', 'validation')  |          23 |         463 |
| ('2f', 'child', 'train')                    |           8 |        1327 |
| ('2f', 'child', 'validation')               |           2 |         331 |
| ('2f', 'child_prototypical', 'train')       |          88 |        1869 |
| ('2f', 'child_prototypical', 'validation')  |          17 |         371 |
| ('2g', 'child', 'train')                    |           8 |        1323 |
| ('2g', 'child', 'validation')               |           2 |         330 |
| ('2g', 'child_prototypical', 'train')       |         108 |        1925 |
| ('2g', 'child_prototypical', 'validation')  |          27 |         480 |
| ('2h', 'child', 'train')                    |           8 |        1327 |
| ('2h', 'child', 'validation')               |           2 |         331 |
| ('2h', 'child_prototypical', 'train')       |          84 |        1540 |
| ('2h', 'child_prototypical', 'validation')  |          21 |         385 |
| ('2i', 'child', 'train')                    |           8 |        1328 |
| ('2i', 'child', 'validation')               |           2 |         332 |
| ('2i', 'child_prototypical', 'train')       |          72 |        1335 |
| ('2i', 'child_prototypical', 'validation')  |          21 |         371 |
| ('2j', 'child', 'train')                    |           8 |        1328 |
| ('2j', 'child', 'validation')               |           2 |         331 |
| ('2j', 'child_prototypical', 'train')       |          80 |        1595 |
| ('2j', 'child_prototypical', 'validation')  |          19 |         369 |
| ('3', 'parent', 'train')                    |          64 |         568 |
| ('3', 'parent', 'validation')               |          16 |         142 |
| ('3a', 'child', 'train')                    |           8 |        1327 |
| ('3a', 'child', 'validation')               |           2 |         331 |
| ('3a', 'child_prototypical', 'train')       |          87 |        1597 |
| ('3a', 'child_prototypical', 'validation')  |          18 |         328 |
| ('3b', 'child', 'train')                    |           8 |        1327 |
| ('3b', 'child', 'validation')               |           2 |         331 |
| ('3b', 'child_prototypical', 'train')       |          87 |        1833 |
| ('3b', 'child_prototypical', 'validation')  |          18 |         407 |
| ('3c', 'child', 'train')                    |           8 |        1326 |
| ('3c', 'child', 'validation')               |           2 |         331 |
| ('3c', 'child_prototypical', 'train')       |          93 |        1664 |
| ('3c', 'child_prototypical', 'validation')  |          18 |         315 |
| ('3d', 'child', 'train')                    |           8 |        1324 |
| ('3d', 'child', 'validation')               |           2 |         331 |
| ('3d', 'child_prototypical', 'train')       |         101 |        1943 |
| ('3d', 'child_prototypical', 'validation')  |          22 |         372 |
| ('3e', 'child', 'train')                    |           8 |        1332 |
| ('3e', 'child', 'validation')               |           2 |         332 |
| ('3e', 'child_prototypical', 'train')       |          49 |         900 |
| ('3e', 'child_prototypical', 'validation')  |          20 |         368 |
| ('3f', 'child', 'train')                    |           8 |        1327 |
| ('3f', 'child', 'validation')               |           2 |         331 |
| ('3f', 'child_prototypical', 'train')       |          90 |        1983 |
| ('3f', 'child_prototypical', 'validation')  |          15 |         362 |
| ('3g', 'child', 'train')                    |           8 |        1331 |
| ('3g', 'child', 'validation')               |           2 |         332 |
| ('3g', 'child_prototypical', 'train')       |          61 |        1089 |
| ('3g', 'child_prototypical', 'validation')  |          14 |         251 |
| ('3h', 'child', 'train')                    |           8 |        1328 |
| ('3h', 'child', 'validation')               |           2 |         331 |
| ('3h', 'child_prototypical', 'train')       |          71 |        1399 |
| ('3h', 'child_prototypical', 'validation')  |          28 |         565 |
| ('4', 'parent', 'train')                    |          64 |         568 |
| ('4', 'parent', 'validation')               |          16 |         142 |
| ('4a', 'child', 'train')                    |           8 |        1327 |
| ('4a', 'child', 'validation')               |           2 |         331 |
| ('4a', 'child_prototypical', 'train')       |          85 |        1766 |
| ('4a', 'child_prototypical', 'validation')  |          20 |         474 |
| ('4b', 'child', 'train')                    |           8 |        1330 |
| ('4b', 'child', 'validation')               |           2 |         332 |
| ('4b', 'child_prototypical', 'train')       |          66 |         949 |
| ('4b', 'child_prototypical', 'validation')  |          15 |         214 |
| ('4c', 'child', 'train')                    |           8 |        1326 |
| ('4c', 'child', 'validation')               |           2 |         331 |
| ('4c', 'child_prototypical', 'train')       |          86 |        1755 |
| ('4c', 'child_prototypical', 'validation')  |          25 |         446 |
| ('4d', 'child', 'train')                    |           8 |        1332 |
| ('4d', 'child', 'validation')               |           2 |         333 |
| ('4d', 'child_prototypical', 'train')       |          46 |         531 |
| ('4d', 'child_prototypical', 'validation')  |          17 |         218 |
| ('4e', 'child', 'train')                    |           8 |        1326 |
| ('4e', 'child', 'validation')               |           2 |         331 |
| ('4e', 'child_prototypical', 'train')       |          92 |        2021 |
| ('4e', 'child_prototypical', 'validation')  |          19 |         402 |
| ('4f', 'child', 'train')                    |           8 |        1328 |
| ('4f', 'child', 'validation')               |           2 |         332 |
| ('4f', 'child_prototypical', 'train')       |          72 |        1464 |
| ('4f', 'child_prototypical', 'validation')  |          21 |         428 |
| ('4g', 'child', 'train')                    |           8 |        1324 |
| ('4g', 'child', 'validation')               |           2 |         330 |
| ('4g', 'child_prototypical', 'train')       |         106 |        2057 |
| ('4g', 'child_prototypical', 'validation')  |          23 |         435 |
| ('4h', 'child', 'train')                    |           8 |        1326 |
| ('4h', 'child', 'validation')               |           2 |         331 |
| ('4h', 'child_prototypical', 'train')       |          85 |        1787 |
| ('4h', 'child_prototypical', 'validation')  |          26 |         525 |
| ('5', 'parent', 'train')                    |          72 |         560 |
| ('5', 'parent', 'validation')               |          18 |         140 |
| ('5a', 'child', 'train')                    |           8 |        1324 |
| ('5a', 'child', 'validation')               |           2 |         331 |
| ('5a', 'child_prototypical', 'train')       |         101 |        1876 |
| ('5a', 'child_prototypical', 'validation')  |          22 |         439 |
| ('5b', 'child', 'train')                    |           8 |        1329 |
| ('5b', 'child', 'validation')               |           2 |         332 |
| ('5b', 'child_prototypical', 'train')       |          70 |        1310 |
| ('5b', 'child_prototypical', 'validation')  |          17 |         330 |
| ('5c', 'child', 'train')                    |           8 |        1327 |
| ('5c', 'child', 'validation')               |           2 |         331 |
| ('5c', 'child_prototypical', 'train')       |          85 |        1552 |
| ('5c', 'child_prototypical', 'validation')  |          20 |         373 |
| ('5d', 'child', 'train')                    |           8 |        1324 |
| ('5d', 'child', 'validation')               |           2 |         330 |
| ('5d', 'child_prototypical', 'train')       |         102 |        1783 |
| ('5d', 'child_prototypical', 'validation')  |          27 |         580 |
| ('5e', 'child', 'train')                    |           8 |        1329 |
| ('5e', 'child', 'validation')               |           2 |         332 |
| ('5e', 'child_prototypical', 'train')       |          68 |        1283 |
| ('5e', 'child_prototypical', 'validation')  |          19 |         357 |
| ('5f', 'child', 'train')                    |           8 |        1327 |
| ('5f', 'child', 'validation')               |           2 |         331 |
| ('5f', 'child_prototypical', 'train')       |          77 |        1568 |
| ('5f', 'child_prototypical', 'validation')  |          28 |         567 |
| ('5g', 'child', 'train')                    |           8 |        1328 |
| ('5g', 'child', 'validation')               |           2 |         332 |
| ('5g', 'child_prototypical', 'train')       |          79 |        1626 |
| ('5g', 'child_prototypical', 'validation')  |          14 |         266 |
| ('5h', 'child', 'train')                    |           8 |        1324 |
| ('5h', 'child', 'validation')               |           2 |         330 |
| ('5h', 'child_prototypical', 'train')       |         109 |        2348 |
| ('5h', 'child_prototypical', 'validation')  |          20 |         402 |
| ('5i', 'child', 'train')                    |           8 |        1324 |
| ('5i', 'child', 'validation')               |           2 |         331 |
| ('5i', 'child_prototypical', 'train')       |          96 |        2010 |
| ('5i', 'child_prototypical', 'validation')  |          27 |         551 |
| ('6', 'parent', 'train')                    |          64 |         568 |
| ('6', 'parent', 'validation')               |          16 |         142 |
| ('6a', 'child', 'train')                    |           8 |        1324 |
| ('6a', 'child', 'validation')               |           2 |         330 |
| ('6a', 'child_prototypical', 'train')       |         102 |        1962 |
| ('6a', 'child_prototypical', 'validation')  |          27 |         530 |
| ('6b', 'child', 'train')                    |           8 |        1327 |
| ('6b', 'child', 'validation')               |           2 |         331 |
| ('6b', 'child_prototypical', 'train')       |          90 |        1840 |
| ('6b', 'child_prototypical', 'validation')  |          15 |         295 |
| ('6c', 'child', 'train')                    |           8 |        1325 |
| ('6c', 'child', 'validation')               |           2 |         331 |
| ('6c', 'child_prototypical', 'train')       |          90 |        1968 |
| ('6c', 'child_prototypical', 'validation')  |          27 |         527 |
| ('6d', 'child', 'train')                    |           8 |        1328 |
| ('6d', 'child', 'validation')               |           2 |         331 |
| ('6d', 'child_prototypical', 'train')       |          82 |        1903 |
| ('6d', 'child_prototypical', 'validation')  |          17 |         358 |
| ('6e', 'child', 'train')                    |           8 |        1327 |
| ('6e', 'child', 'validation')               |           2 |         331 |
| ('6e', 'child_prototypical', 'train')       |          85 |        1737 |
| ('6e', 'child_prototypical', 'validation')  |          20 |         398 |
| ('6f', 'child', 'train')                    |           8 |        1326 |
| ('6f', 'child', 'validation')               |           2 |         331 |
| ('6f', 'child_prototypical', 'train')       |          87 |        1652 |
| ('6f', 'child_prototypical', 'validation')  |          24 |         438 |
| ('6g', 'child', 'train')                    |           8 |        1326 |
| ('6g', 'child', 'validation')               |           2 |         331 |
| ('6g', 'child_prototypical', 'train')       |          94 |        1740 |
| ('6g', 'child_prototypical', 'validation')  |          17 |         239 |
| ('6h', 'child', 'train')                    |           8 |        1324 |
| ('6h', 'child', 'validation')               |           2 |         330 |
| ('6h', 'child_prototypical', 'train')       |         115 |        2337 |
| ('6h', 'child_prototypical', 'validation')  |          14 |         284 |
| ('7', 'parent', 'train')                    |          64 |         568 |
| ('7', 'parent', 'validation')               |          16 |         142 |
| ('7a', 'child', 'train')                    |           8 |        1324 |
| ('7a', 'child', 'validation')               |           2 |         331 |
| ('7a', 'child_prototypical', 'train')       |          99 |        2045 |
| ('7a', 'child_prototypical', 'validation')  |          24 |         516 |
| ('7b', 'child', 'train')                    |           8 |        1330 |
| ('7b', 'child', 'validation')               |           2 |         332 |
| ('7b', 'child_prototypical', 'train')       |          69 |         905 |
| ('7b', 'child_prototypical', 'validation')  |          12 |         177 |
| ('7c', 'child', 'train')                    |           8 |        1327 |
| ('7c', 'child', 'validation')               |           2 |         331 |
| ('7c', 'child_prototypical', 'train')       |          85 |        1402 |
| ('7c', 'child_prototypical', 'validation')  |          20 |         313 |
| ('7d', 'child', 'train')                    |           8 |        1324 |
| ('7d', 'child', 'validation')               |           2 |         331 |
| ('7d', 'child_prototypical', 'train')       |          98 |        2064 |
| ('7d', 'child_prototypical', 'validation')  |          25 |         497 |
| ('7e', 'child', 'train')                    |           8 |        1328 |
| ('7e', 'child', 'validation')               |           2 |         331 |
| ('7e', 'child_prototypical', 'train')       |          78 |        1270 |
| ('7e', 'child_prototypical', 'validation')  |          21 |         298 |
| ('7f', 'child', 'train')                    |           8 |        1326 |
| ('7f', 'child', 'validation')               |           2 |         331 |
| ('7f', 'child_prototypical', 'train')       |          89 |        1377 |
| ('7f', 'child_prototypical', 'validation')  |          22 |         380 |
| ('7g', 'child', 'train')                    |           8 |        1328 |
| ('7g', 'child', 'validation')               |           2 |         332 |
| ('7g', 'child_prototypical', 'train')       |          72 |         885 |
| ('7g', 'child_prototypical', 'validation')  |          21 |         263 |
| ('7h', 'child', 'train')                    |           8 |        1324 |
| ('7h', 'child', 'validation')               |           2 |         331 |
| ('7h', 'child_prototypical', 'train')       |          94 |        1479 |
| ('7h', 'child_prototypical', 'validation')  |          29 |         467 |
| ('8', 'parent', 'train')                    |          64 |         568 |
| ('8', 'parent', 'validation')               |          16 |         142 |
| ('8a', 'child', 'train')                    |           8 |        1324 |
| ('8a', 'child', 'validation')               |           2 |         331 |
| ('8a', 'child_prototypical', 'train')       |          93 |        1640 |
| ('8a', 'child_prototypical', 'validation')  |          30 |         552 |
| ('8b', 'child', 'train')                    |           8 |        1330 |
| ('8b', 'child', 'validation')               |           2 |         332 |
| ('8b', 'child_prototypical', 'train')       |          61 |        1126 |
| ('8b', 'child_prototypical', 'validation')  |          20 |         361 |
| ('8c', 'child', 'train')                    |           8 |        1326 |
| ('8c', 'child', 'validation')               |           2 |         331 |
| ('8c', 'child_prototypical', 'train')       |          96 |        1547 |
| ('8c', 'child_prototypical', 'validation')  |          15 |         210 |
| ('8d', 'child', 'train')                    |           8 |        1325 |
| ('8d', 'child', 'validation')               |           2 |         331 |
| ('8d', 'child_prototypical', 'train')       |          92 |        1472 |
| ('8d', 'child_prototypical', 'validation')  |          25 |         438 |
| ('8e', 'child', 'train')                    |           8 |        1327 |
| ('8e', 'child', 'validation')               |           2 |         331 |
| ('8e', 'child_prototypical', 'train')       |          87 |        1340 |
| ('8e', 'child_prototypical', 'validation')  |          18 |         270 |
| ('8f', 'child', 'train')                    |           8 |        1326 |
| ('8f', 'child', 'validation')               |           2 |         331 |
| ('8f', 'child_prototypical', 'train')       |          83 |        1416 |
| ('8f', 'child_prototypical', 'validation')  |          28 |         452 |
| ('8g', 'child', 'train')                    |           8 |        1330 |
| ('8g', 'child', 'validation')               |           2 |         332 |
| ('8g', 'child_prototypical', 'train')       |          62 |         640 |
| ('8g', 'child_prototypical', 'validation')  |          19 |         199 |
| ('8h', 'child', 'train')                    |           8 |        1324 |
| ('8h', 'child', 'validation')               |           2 |         331 |
| ('8h', 'child_prototypical', 'train')       |         100 |        1816 |
| ('8h', 'child_prototypical', 'validation')  |          23 |         499 |
| ('9', 'parent', 'train')                    |          72 |         560 |
| ('9', 'parent', 'validation')               |          18 |         140 |
| ('9a', 'child', 'train')                    |           8 |        1324 |
| ('9a', 'child', 'validation')               |           2 |         331 |
| ('9a', 'child_prototypical', 'train')       |          96 |        1520 |
| ('9a', 'child_prototypical', 'validation')  |          27 |         426 |
| ('9b', 'child', 'train')                    |           8 |        1326 |
| ('9b', 'child', 'validation')               |           2 |         331 |
| ('9b', 'child_prototypical', 'train')       |          93 |        1783 |
| ('9b', 'child_prototypical', 'validation')  |          18 |         307 |
| ('9c', 'child', 'train')                    |           8 |        1330 |
| ('9c', 'child', 'validation')               |           2 |         332 |
| ('9c', 'child_prototypical', 'train')       |          59 |         433 |
| ('9c', 'child_prototypical', 'validation')  |          22 |         163 |
| ('9d', 'child', 'train')                    |           8 |        1328 |
| ('9d', 'child', 'validation')               |           2 |         332 |
| ('9d', 'child_prototypical', 'train')       |          78 |        1683 |
| ('9d', 'child_prototypical', 'validation')  |          15 |         302 |
| ('9e', 'child', 'train')                    |           8 |        1329 |
| ('9e', 'child', 'validation')               |           2 |         332 |
| ('9e', 'child_prototypical', 'train')       |          66 |        1426 |
| ('9e', 'child_prototypical', 'validation')  |          21 |         475 |
| ('9f', 'child', 'train')                    |           8 |        1328 |
| ('9f', 'child', 'validation')               |           2 |         331 |
| ('9f', 'child_prototypical', 'train')       |          79 |        1436 |
| ('9f', 'child_prototypical', 'validation')  |          20 |         330 |
| ('9g', 'child', 'train')                    |           8 |        1324 |
| ('9g', 'child', 'validation')               |           2 |         331 |
| ('9g', 'child_prototypical', 'train')       |         100 |        1685 |
| ('9g', 'child_prototypical', 'validation')  |          23 |         384 |
| ('9h', 'child', 'train')                    |           8 |        1325 |
| ('9h', 'child', 'validation')               |           2 |         331 |
| ('9h', 'child_prototypical', 'train')       |          95 |        1799 |
| ('9h', 'child_prototypical', 'validation')  |          22 |         462 |
| ('9i', 'child', 'train')                    |           8 |        1328 |
| ('9i', 'child', 'validation')               |           2 |         332 |
| ('9i', 'child_prototypical', 'train')       |          79 |        1361 |
| ('9i', 'child_prototypical', 'validation')  |          14 |         252 |

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