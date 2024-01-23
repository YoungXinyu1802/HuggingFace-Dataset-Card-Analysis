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
pretty_name: BTC
---

# Dataset Card for "tner/btc"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/C16-1111/](https://aclanthology.org/C16-1111/)
- **Dataset:** Broad Twitter Corpus
- **Domain:** Twitter
- **Number of Entity:** 3


### Dataset Summary
Broad Twitter Corpus NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `LOC`, `ORG`, `PER`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tokens': ['I', 'hate', 'the', 'words', 'chunder', ',', 'vomit', 'and', 'puke', '.', 'BUUH', '.'],
    'tags': [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/btc/raw/main/dataset/label.json).
```python
{
    "B-LOC": 0,
    "B-ORG": 1,
    "B-PER": 2,
    "I-LOC": 3,
    "I-ORG": 4,
    "I-PER": 5,
    "O": 6
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|btc      | 6338|      1001|2000|

### Citation Information

```
@inproceedings{derczynski-etal-2016-broad,
    title = "Broad {T}witter Corpus: A Diverse Named Entity Recognition Resource",
    author = "Derczynski, Leon  and
      Bontcheva, Kalina  and
      Roberts, Ian",
    booktitle = "Proceedings of {COLING} 2016, the 26th International Conference on Computational Linguistics: Technical Papers",
    month = dec,
    year = "2016",
    address = "Osaka, Japan",
    publisher = "The COLING 2016 Organizing Committee",
    url = "https://aclanthology.org/C16-1111",
    pages = "1169--1179",
    abstract = "One of the main obstacles, hampering method development and comparative evaluation of named entity recognition in social media, is the lack of a sizeable, diverse, high quality annotated corpus, analogous to the CoNLL{'}2003 news dataset. For instance, the biggest Ritter tweet corpus is only 45,000 tokens {--} a mere 15{\%} the size of CoNLL{'}2003. Another major shortcoming is the lack of temporal, geographic, and author diversity. This paper introduces the Broad Twitter Corpus (BTC), which is not only significantly bigger, but sampled across different regions, temporal periods, and types of Twitter users. The gold-standard named entity annotations are made by a combination of NLP experts and crowd workers, which enables us to harness crowd recall while maintaining high quality. We also measure the entity drift observed in our dataset (i.e. how entity representation varies over time), and compare to newswire. The corpus is released openly, including source text and intermediate annotations.",
}
```