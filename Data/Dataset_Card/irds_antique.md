---
pretty_name: '`antique`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `antique`

The `antique` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/antique#antique).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=403,666


This dataset is used by: [`antique_test`](https://huggingface.co/datasets/irds/antique_test), [`antique_test_non-offensive`](https://huggingface.co/datasets/irds/antique_test_non-offensive), [`antique_train`](https://huggingface.co/datasets/irds/antique_train), [`antique_train_split200-train`](https://huggingface.co/datasets/irds/antique_train_split200-train), [`antique_train_split200-valid`](https://huggingface.co/datasets/irds/antique_train_split200-valid)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/antique', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Hashemi2020Antique,
  title={ANTIQUE: A Non-Factoid Question Answering Benchmark},
  author={Helia Hashemi and Mohammad Aliannejadi and Hamed Zamani and Bruce Croft},
  booktitle={ECIR},
  year={2020}
}
```
