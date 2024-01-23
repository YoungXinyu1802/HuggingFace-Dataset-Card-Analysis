---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1k<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: WNUT 2017
---

# Dataset Card for "tner/wnut2017"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/W17-4418/](https://aclanthology.org/W17-4418/)
- **Dataset:** WNUT 2017
- **Domain:** Twitter, Reddit, YouTube, and StackExchange
- **Number of Entity:** 6


### Dataset Summary
WNUT 2017 NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `creative-work`, `corporation`, `group`, `location`, `person`, `product`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tokens': ['@paulwalk', 'It', "'s", 'the', 'view', 'from', 'where', 'I', "'m", 'living', 'for', 'two', 'weeks', '.', 'Empire', 'State', 'Building', '=', 'ESB', '.', 'Pretty', 'bad', 'storm', 'here', 'last', 'evening', '.'],
    'tags': [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 3, 9, 9, 12, 3, 12, 12, 12, 12, 12, 12, 12, 12]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/wnut2017/raw/main/dataset/label.json).
```python
{
    "B-corporation": 0,
    "B-creative-work": 1,
    "B-group": 2,
    "B-location": 3,
    "B-person": 4,
    "B-product": 5,
    "I-corporation": 6,
    "I-creative-work": 7,
    "I-group": 8,
    "I-location": 9,
    "I-person": 10,
    "I-product": 11,
    "O": 12
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|wnut2017 | 2395|      1009|1287|

### Citation Information

```
@inproceedings{derczynski-etal-2017-results,
    title = "Results of the {WNUT}2017 Shared Task on Novel and Emerging Entity Recognition",
    author = "Derczynski, Leon  and
      Nichols, Eric  and
      van Erp, Marieke  and
      Limsopatham, Nut",
    booktitle = "Proceedings of the 3rd Workshop on Noisy User-generated Text",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-4418",
    doi = "10.18653/v1/W17-4418",
    pages = "140--147",
    abstract = "This shared task focuses on identifying unusual, previously-unseen entities in the context of emerging discussions. Named entities form the basis of many modern approaches to other tasks (like event clustering and summarization), but recall on them is a real problem in noisy text - even among annotators. This drop tends to be due to novel entities and surface forms. Take for example the tweet {``}so.. kktny in 30 mins?!{''} {--} even human experts find the entity {`}kktny{'} hard to detect and resolve. The goal of this task is to provide a definition of emerging and of rare entities, and based on that, also datasets for detecting these entities. The task as described in this paper evaluated the ability of participating entries to detect and classify novel and emerging named entities in noisy text.",
}
```