---
tags:
- augmented-indonli
license: bigscience-openrail-m
datasets:
- indonli
---

On this repository, I just downloaded and processed the `translate_train.tar.gz` file with `train.jsonl` & `dev.jsonl` here: `https://github.com/ir-nlp-csui/indonli/tree/main/data`

How to use? As simple as this:

```python
!wget https://huggingface.co/datasets/muhammadravi251001/augmented-indo-nli/raw/main/dev_augmented.jsonl
!wget https://huggingface.co/datasets/muhammadravi251001/augmented-indo-nli/resolve/main/train_augmented.jsonl

import pandas as pd
data_train_augmented_indonli = pd.read_json(path_or_buf='train.jsonl', lines=True)
data_dev_augmented_indonli = pd.read_json(path_or_buf='dev.jsonl', lines=True)
```
Voila~!

## Reference

The dataset I used is by IndoNLI.

```
@inproceedings{indonli,
    title = "IndoNLI: A Natural Language Inference Dataset for Indonesian",
    author = "Mahendra, Rahmad and Aji, Alham Fikri and Louvan, Samuel and Rahman, Fahrurrozi and Vania, Clara",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    publisher = "Association for Computational Linguistics",
}
```