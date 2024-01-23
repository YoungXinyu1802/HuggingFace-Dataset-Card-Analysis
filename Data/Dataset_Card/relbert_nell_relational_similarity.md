---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: Relational similarity dataset based on the NELL-one
---

# Dataset Card for "relbert/nell_relation_similarity"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/D18-1223/](https://aclanthology.org/D18-1223/)
- **Dataset:** Relational similarity dataset based on the NELL-one

### Dataset Summary
[NELL-one](https://huggingface.co/datasets/relbert/nell) cleaned dataset compiled for relational similarity.

## Dataset Structure
### Data Instances
An example of `test` looks as follows.
```shell
{
  "relation_type": "concept:automobilemakerdealersincity",
  "positives": [["Lexus", "Dallas"], ["Buick", "Columbus"], ...,
  "negatives": []}
}
```

### Data Splits

|   train |validation|      test|
|--------:|---------:|---------:|
|       30| 3        |        5 |


### Citation Information
```
@inproceedings{xiong-etal-2018-one,
    title = "One-Shot Relational Learning for Knowledge Graphs",
    author = "Xiong, Wenhan  and
      Yu, Mo  and
      Chang, Shiyu  and
      Guo, Xiaoxiao  and
      Wang, William Yang",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1223",
    doi = "10.18653/v1/D18-1223",
    pages = "1980--1990",
    abstract = "Knowledge graphs (KG) are the key components of various natural language processing applications. To further expand KGs{'} coverage, previous studies on knowledge graph completion usually require a large number of positive examples for each relation. However, we observe long-tail relations are actually more common in KGs and those newly added relations often do not have many known triples for training. In this work, we aim at predicting new facts under a challenging setting where only one training instance is available. We propose a one-shot relational learning framework, which utilizes the knowledge distilled by embedding models and learns a matching metric by considering both the learned embeddings and one-hop graph structures. Empirically, our model yields considerable performance improvements over existing embedding models, and also eliminates the need of re-training the embedding models when dealing with newly added relations.",
}
```