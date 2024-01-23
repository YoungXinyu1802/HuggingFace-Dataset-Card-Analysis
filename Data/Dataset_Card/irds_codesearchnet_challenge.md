---
pretty_name: '`codesearchnet/challenge`'
viewer: false
source_datasets: ['irds/codesearchnet']
task_categories:
- text-retrieval
---

# Dataset Card for `codesearchnet/challenge`

The `codesearchnet/challenge` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/codesearchnet#codesearchnet/challenge).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=99
 - `qrels`: (relevance assessments); count=4,006

 - For `docs`, use [`irds/codesearchnet`](https://huggingface.co/datasets/irds/codesearchnet)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/codesearchnet_challenge', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/codesearchnet_challenge', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'note': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Husain2019CodeSearchNet,
  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},
  author={Hamel Husain and Ho-Hsiang Wu and Tiferet Gazit and Miltiadis Allamanis and Marc Brockschmidt},
  journal={ArXiv},
  year={2019}
}
```
