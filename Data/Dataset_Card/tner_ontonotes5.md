---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: Ontonotes5
---

# Dataset Card for "tner/ontonotes5"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/N06-2015/](https://aclanthology.org/N06-2015/)
- **Dataset:** Ontonotes5
- **Domain:** News
- **Number of Entity:** 8

### Dataset Summary
Ontonotes5 NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `CARDINAL`, `DATE`, `PERSON`, `NORP`, `GPE`, `LAW`, `PERCENT`, `ORDINAL`, `MONEY`, `WORK_OF_ART`, `FAC`, `TIME`, `QUANTITY`, `PRODUCT`, `LANGUAGE`, `ORG`, `LOC`, `EVENT`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tags': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 11, 12, 12, 12, 12, 0, 0, 7, 0, 0, 0, 0, 0],
    'tokens': ['``', 'It', "'s", 'very', 'costly', 'and', 'time', '-', 'consuming', ',', "''", 'says', 'Phil', 'Rosen', ',', 'a', 'partner', 'in', 'Fleet', '&', 'Leasing', 'Management', 'Inc.', ',', 'a', 'Boston', 'car', '-', 'leasing', 'company', '.']
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/onotonotes5/raw/main/dataset/label.json).
```python
{
    "O": 0,
    "B-CARDINAL": 1,
    "B-DATE": 2,
    "I-DATE": 3,
    "B-PERSON": 4,
    "I-PERSON": 5,
    "B-NORP": 6,
    "B-GPE": 7,
    "I-GPE": 8,
    "B-LAW": 9,
    "I-LAW": 10,
    "B-ORG": 11,
    "I-ORG": 12, 
    "B-PERCENT": 13,
    "I-PERCENT": 14, 
    "B-ORDINAL": 15, 
    "B-MONEY": 16, 
    "I-MONEY": 17, 
    "B-WORK_OF_ART": 18, 
    "I-WORK_OF_ART": 19, 
    "B-FAC": 20, 
    "B-TIME": 21, 
    "I-CARDINAL": 22, 
    "B-LOC": 23, 
    "B-QUANTITY": 24, 
    "I-QUANTITY": 25, 
    "I-NORP": 26, 
    "I-LOC": 27, 
    "B-PRODUCT": 28, 
    "I-TIME": 29, 
    "B-EVENT": 30,
    "I-EVENT": 31,
    "I-FAC": 32,
    "B-LANGUAGE": 33,
    "I-PRODUCT": 34,
    "I-ORDINAL": 35,
    "I-LANGUAGE": 36
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|ontonotes5|59924|      8528|8262|

### Citation Information

```
@inproceedings{hovy-etal-2006-ontonotes,
    title = "{O}nto{N}otes: The 90{\%} Solution",
    author = "Hovy, Eduard  and
      Marcus, Mitchell  and
      Palmer, Martha  and
      Ramshaw, Lance  and
      Weischedel, Ralph",
    booktitle = "Proceedings of the Human Language Technology Conference of the {NAACL}, Companion Volume: Short Papers",
    month = jun,
    year = "2006",
    address = "New York City, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N06-2015",
    pages = "57--60",
}
```