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
pretty_name: BioNLP2004
---

# Dataset Card for "tner/bionlp2004"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/U15-1010.pdf](https://aclanthology.org/U15-1010.pdf)
- **Dataset:** BioNLP2004
- **Domain:** Biochemical
- **Number of Entity:** 5

### Dataset Summary
BioNLP2004 NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
BioNLP2004 dataset contains training and test only, so we randomly sample a half size of test instances from the training set to create validation set. 

- Entity Types: `DNA`, `protein`, `cell_type`, `cell_line`, `RNA`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tags': [0, 0, 0, 0, 3, 0, 9, 10, 0, 0, 0, 0, 0, 7, 8, 0, 3, 0, 0, 9, 10, 10, 0, 0],
    'tokens': ['In', 'the', 'presence', 'of', 'Epo', ',', 'c-myb', 'mRNA', 'declined', 'and', '20', '%', 'of', 'K562', 'cells', 'synthesized', 'Hb', 'regardless', 'of', 'antisense', 'myb', 'RNA', 'expression', '.']
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/fin/raw/main/dataset/label.json).
```python
{
    "O": 0,
    "B-DNA": 1,
    "I-DNA": 2,
    "B-protein": 3,
    "I-protein": 4,
    "B-cell_type": 5,
    "I-cell_type": 6,
    "B-cell_line": 7,
    "I-cell_line": 8,
    "B-RNA": 9,
    "I-RNA": 10
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|bionlp2004      |16619  |       1927| 3856|

### Citation Information

```
@inproceedings{collier-kim-2004-introduction,
    title = "Introduction to the Bio-entity Recognition Task at {JNLPBA}",
    author = "Collier, Nigel  and
      Kim, Jin-Dong",
    booktitle = "Proceedings of the International Joint Workshop on Natural Language Processing in Biomedicine and its Applications ({NLPBA}/{B}io{NLP})",
    month = aug # " 28th and 29th",
    year = "2004",
    address = "Geneva, Switzerland",
    publisher = "COLING",
    url = "https://aclanthology.org/W04-1213",
    pages = "73--78",
}
```