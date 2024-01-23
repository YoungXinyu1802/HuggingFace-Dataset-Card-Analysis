---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: Lexical Relation Classification
---

# Dataset Card for "relbert/lexical_relation_classification"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/P19-1169/](https://aclanthology.org/P19-1169/)
- **Dataset:** Lexical Relation Classification

### Dataset Summary
Five different datasets (`BLESS`, `CogALexV`, `EVALution`, `K&H+N`, `ROOT09`) for lexical relation classification used in [SphereRE](https://www.aclweb.org/anthology/P19-1169/).


### Dataset Summary
This dataset contains 5 different word analogy questions used in [Analogy Language Model](https://aclanthology.org/2021.acl-long.280/).

| name          | train | validation | test |
|---------------|------:|-------:|-----:|
| `BLESS`       | 18582 | 1327   | 6637 |
| `CogALexV`    | 3054  | -      | 4260 | 
| `EVALution`   | 5160  | 372    | 1846 |
| `K&H+N`       | 40256 | 2876   | 14377 |
| `ROOT09`      | 8933  | 638    | 3191 |


## Dataset Structure
### Data Instances
An example looks as follows.
```
{"head": "turtle", "tail": "live", "relation": "event"}
```
The `stem` and `tail` are the word pair and `relation` is the corresponding relation label.

### Citation Information
```
@inproceedings{wang-etal-2019-spherere,
    title = "{S}phere{RE}: Distinguishing Lexical Relations with Hyperspherical Relation Embeddings",
    author = "Wang, Chengyu  and
      He, Xiaofeng  and
      Zhou, Aoying",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P19-1169",
    doi = "10.18653/v1/P19-1169",
    pages = "1727--1737",
    abstract = "Lexical relations describe how meanings of terms relate to each other. Typical examples include hypernymy, synonymy, meronymy, etc. Automatic distinction of lexical relations is vital for NLP applications, and also challenging due to the lack of contextual signals to discriminate between such relations. In this work, we present a neural representation learning model to distinguish lexical relations among term pairs based on Hyperspherical Relation Embeddings (SphereRE). Rather than learning embeddings for individual terms, the model learns representations of relation triples by mapping them to the hyperspherical embedding space, where relation triples of different lexical relations are well separated. Experiments over several benchmarks confirm SphereRE outperforms state-of-the-arts.",
}
```

### LICENSE
The LICENSE of all the resources are under [CC-BY-NC-4.0](./LICENSE). Thus, they are freely available for academic purpose or individual research, but restricted for commercial use.

