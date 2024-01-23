---
annotations_creators:
- crowdsourced
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: 'NewsMTSC'
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
language_bcp47:
- en-US
---
# NewsMTSC dataset

NewsMTSC is a high-quality dataset consisting of more than 11k manually labeled sentences sampled from English news articles. Each sentence was labeled by five human coders (the dataset contains only examples where the five coders assessed same or similar sentiment). The dataset is published as a [full paper at EACL 2021: *NewsMTSC: (Multi-)Target-dependent Sentiment Classification in News Articles*](https://aclanthology.org/2021.eacl-main.142.pdf).

## Subsets and splits
The dataset consists of two subsets (`rw` and `mt`), each consisting of three splits (train, validation, and test). We recommend to use the `rw` subset, which is also the default subset. Both subsets share the same train set, in which the three sentiment classes have similar frequency since we applied class boosting. The two subsets differ in their validation and test sets: `rw` contains validation and test sets that resemble real-world distribution of sentiment in news articles. In contrast, `mt`'s validation and test sets contain only sentences that each have two or more (different) targets, where each target's sentiment was labeled individually. 

More information on the subsets can be found in our [paper](https://aclanthology.org/2021.eacl-main.142.pdf).

## Format
Each split is stored in a JSONL file. In JSONL, each line represents one JSON object. In our dataset, each JSON object consists of the following attributes. When using the dataset, you most likely will need (only) the attributes highlighted in **bold**.

1. `mention`: text of the mention within `sentence`
2. **`polarity`: sentiment of the sentence concerning the target's mention (-1 = negative, 0 = neutral, 1 = positive)**
3. **`from`: character-based, 0-indexed position of the first character of the target's mention within `sentence`**
4. **`to`: last character of the target's mention**
5. **`sentence`: sentence**
6. `id`: identifier that is unique within NewsMTSC

## Contact

If you find an issue with the dataset or model or have a question concerning either, please open an issue in the repository.

* Repository: [https://github.com/fhamborg/NewsMTSC](https://github.com/fhamborg/NewsMTSC)
* Web: [https://felix.hamborg.eu/](https://felix.hamborg.eu/)

## How to cite

If you use the dataset or parts of it, please cite our paper:

```
@InProceedings{Hamborg2021b,
  author    = {Hamborg, Felix and Donnay, Karsten},
  title     = {NewsMTSC: (Multi-)Target-dependent Sentiment Classification in News Articles},
  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2021)},
  year      = {2021},
  month     = {Apr.},
  location  = {Virtual Event},
}
```
