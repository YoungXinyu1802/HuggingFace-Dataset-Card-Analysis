---
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: FIN
---

# Dataset Card for "tner/fin"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/U15-1010.pdf](https://aclanthology.org/U15-1010.pdf)
- **Dataset:** FIN
- **Domain:** Financial News
- **Number of Entity:** 4

### Dataset Summary
FIN NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
FIN dataset contains training (FIN5) and test (FIN3) only, so we randomly sample a half size of test instances from the training set to create validation set.


- Entity Types: `ORG`, `LOC`, `PER`, `MISC`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    "tags": [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "tokens": ["1", ".", "1", ".", "4", "Borrower", "engages", "in", "criminal", "conduct", "or", "is", "involved", "in", "criminal", "activities", ";"]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/fin/raw/main/dataset/label.json).
```python
{
  "O": 0,
  "B-PER": 1,
  "B-LOC": 2,
  "B-ORG": 3,
  "B-MISC": 4,
  "I-PER": 5,
  "I-LOC": 6,
  "I-ORG": 7,
  "I-MISC": 8
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|fin      |1014 |       303| 150|


### Citation Information

```
@inproceedings{salinas-alvarado-etal-2015-domain,
    title = "Domain Adaption of Named Entity Recognition to Support Credit Risk Assessment",
    author = "Salinas Alvarado, Julio Cesar  and
      Verspoor, Karin  and
      Baldwin, Timothy",
    booktitle = "Proceedings of the Australasian Language Technology Association Workshop 2015",
    month = dec,
    year = "2015",
    address = "Parramatta, Australia",
    url = "https://aclanthology.org/U15-1010",
    pages = "84--90",
}
```