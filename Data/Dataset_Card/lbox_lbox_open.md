---
license: cc-by-nc-4.0
---
# Dataset Card for `lbox_open`

## Dataset Description

- **Homepage:** `https://lbox.kr`
- **Repository:** `https://github.com/lbox-kr/lbox_open`
- **Point of Contact:** [Wonseok Hwang](mailto:wonseok.hwang@lbox.kr)

### Dataset Summary

A Legal AI Benchmark Dataset from Korean Legal Cases.

### Languages

Korean

### How to use
```python
from datasets import load_dataset

# casename classficiation task
data_cn = load_dataset("lbox/lbox_open", "casename_classification")
data_cn_plus = load_dataset("lbox/lbox_open", "casename_classification_plus")

# statutes classification task
data_st = load_dataset("lbox/lbox_open", "statute_classification")
data_st_plus = load_dataset("lbox/lbox_open", "statute_classification_plus")

# Legal judgement prediction tasks
data_ljp_criminal = load_dataset("lbox/lbox_open", "ljp_criminal")
data_ljp_civil = load_dataset("lbox/lbox_open", "ljp_civil")

# case summarization task
data_summ = load_dataset("lbox/lbox_open", "summarization")
data_summ_plus = load_dataset("lbox/lbox_open", "summarization_plus")

# precedent corpus
data_corpus = load_dataset("lbox/lbox_open", "precedent_corpus")

```

For more information about the dataset, please visit <https://github.com/lbox-kr/lbox_open>.

## Licensing Information
Copyright 2022-present [LBox Co. Ltd.](https://lbox.kr/)

Licensed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)