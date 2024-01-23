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
pretty_name: BioCreative V CDR
---

# Dataset Card for "tner/bc5cdr"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://academic.oup.com/database/article/doi/10.1093/database/baw032/2630271?login=true](https://academic.oup.com/database/article/doi/10.1093/database/baw032/2630271?login=true)
- **Dataset:** BioCreative V CDR
- **Domain:** Biomedical
- **Number of Entity:** 2

### Dataset Summary
BioCreative V CDR NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
The original dataset consists of long documents which cannot be fed on LM because of the length, so we split them into sentences to reduce their size.
- Entity Types: `Chemical`, `Disease`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tags': [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    'tokens': ['Fasciculations', 'in', 'six', 'areas', 'of', 'the', 'body', 'were', 'scored', 'from', '0', 'to', '3', 'and', 'summated', 'as', 'a', 'total', 'fasciculation', 'score', '.']
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/bc5cdr/raw/main/dataset/label.json).
```python
{
    "O": 0,
    "B-Chemical": 1,
    "B-Disease": 2,
    "I-Disease": 3,
    "I-Chemical": 4
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|bc5cdr|5228|      5330|5865|

### Citation Information

```
@article{wei2016assessing,
  title={Assessing the state of the art in biomedical relation extraction: overview of the BioCreative V chemical-disease relation (CDR) task},
  author={Wei, Chih-Hsuan and Peng, Yifan and Leaman, Robert and Davis, Allan Peter and Mattingly, Carolyn J and Li, Jiao and Wiegers, Thomas C and Lu, Zhiyong},
  journal={Database},
  volume={2016},
  year={2016},
  publisher={Oxford Academic}
}
```