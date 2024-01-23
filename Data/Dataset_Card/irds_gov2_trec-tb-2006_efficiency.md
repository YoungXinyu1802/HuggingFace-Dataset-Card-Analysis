---
pretty_name: '`gov2/trec-tb-2006/efficiency`'
viewer: false
source_datasets: ['irds/gov2']
task_categories:
- text-retrieval
---

# Dataset Card for `gov2/trec-tb-2006/efficiency`

The `gov2/trec-tb-2006/efficiency` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/gov2#gov2/trec-tb-2006/efficiency).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=100,000
 - `qrels`: (relevance assessments); count=31,984

 - For `docs`, use [`irds/gov2`](https://huggingface.co/datasets/irds/gov2)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/gov2_trec-tb-2006_efficiency', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/gov2_trec-tb-2006_efficiency', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Buttcher2006TrecTerabyte,
  title={The TREC 2006 Terabyte Track},
  author={Stefan B\"uttcher and Charles L. A. Clarke and Ian Soboroff},
  booktitle={TREC},
  year={2006}
}
```
