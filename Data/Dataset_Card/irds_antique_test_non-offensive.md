---
pretty_name: '`antique/test/non-offensive`'
viewer: false
source_datasets: ['irds/antique']
task_categories:
- text-retrieval
---

# Dataset Card for `antique/test/non-offensive`

The `antique/test/non-offensive` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/antique#antique/test/non-offensive).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=176
 - `qrels`: (relevance assessments); count=5,752

 - For `docs`, use [`irds/antique`](https://huggingface.co/datasets/irds/antique)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/antique_test_non-offensive', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/antique_test_non-offensive', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ...}

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
