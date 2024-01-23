---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: ConceptNet with High Confidence
---

# Dataset Card for "relbert/conceptnet_relation_similarity"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://home.ttic.edu/~kgimpel/commonsense.html](https://home.ttic.edu/~kgimpel/commonsense.html)
- **Dataset:** Relational similarity dataset based on the high-confidence subset of ConceptNet

### Dataset Summary
The selected subset of ConceptNet used in [this work](https://home.ttic.edu/~kgimpel/commonsense.html), which compiled 
to fine-tune [RelBERT](https://github.com/asahi417/relbert) model.
We removed `NotCapableOf` and `NotDesires` to keep the positive relation only.
We consider the original test set as test set, dev1 as the training set, and dev2 as the validation set.


## Dataset Structure
### Data Instances
An example of `train` looks as follows.
```shell
{
    "relation_type": "AtLocation",
    "positives": [["fish", "water"], ["cloud", "sky"], ["child", "school"], ... ],
    "negatives": [["pen", "write"], ["sex", "fun"], ["soccer", "sport"], ["fish", "school"], ... ]
}
```

### Data Splits

|   train |validation|      test|
|--------:|---------:|---------:|
|       15| 17       |        15|


### Citation Information
```
@InProceedings{P16-1137,
  author = 	"Li, Xiang
		and Taheri, Aynaz
		and Tu, Lifu
		and Gimpel, Kevin",
  title = 	"Commonsense Knowledge Base Completion",
  booktitle = 	"Proceedings of the 54th Annual Meeting of the Association for      Computational Linguistics (Volume 1: Long Papers)    ",
  year = 	"2016",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"1445--1455",
  location = 	"Berlin, Germany",
  doi = 	"10.18653/v1/P16-1137",
  url = 	"http://aclweb.org/anthology/P16-1137"
}
```