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
pretty_name: TweeBank NER
---

# Dataset Card for "tner/tweebank_ner"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://arxiv.org/abs/2201.07281](https://arxiv.org/abs/2201.07281)
- **Dataset:** TweeBank NER
- **Domain:** Twitter
- **Number of Entity:** 4


### Dataset Summary
TweeBank NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `LOC`, `MISC`, `PER`, `ORG`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tokens': ['RT', '@USER2362', ':', 'Farmall', 'Heart', 'Of', 'The', 'Holidays', 'Tabletop', 'Christmas', 'Tree', 'With', 'Lights', 'And', 'Motion', 'URL1087', '#Holiday', '#Gifts'],
    'tags': [8, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/tweebank_ner/raw/main/dataset/label.json).
```python
{
    "B-LOC": 0,
    "B-MISC": 1,
    "B-ORG": 2,
    "B-PER": 3,
    "I-LOC": 4,
    "I-MISC": 5,
    "I-ORG": 6,
    "I-PER": 7,
    "O": 8
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|tweebank_ner | 1639|      710 |1201|

### Citation Information

```
@article{DBLP:journals/corr/abs-2201-07281,
  author    = {Hang Jiang and
               Yining Hua and
               Doug Beeferman and
               Deb Roy},
  title     = {Annotating the Tweebank Corpus on Named Entity Recognition and Building
               {NLP} Models for Social Media Analysis},
  journal   = {CoRR},
  volume    = {abs/2201.07281},
  year      = {2022},
  url       = {https://arxiv.org/abs/2201.07281},
  eprinttype = {arXiv},
  eprint    = {2201.07281},
  timestamp = {Fri, 21 Jan 2022 13:57:15 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2201-07281.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```