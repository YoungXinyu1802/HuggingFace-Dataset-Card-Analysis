---
pretty_name: '`trec-cast/v0`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-cast/v0`

The `trec-cast/v0` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-cast#trec-cast/v0).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=47,696,605


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/trec-cast_v0', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Dalton2019Cast,
  title={CAsT 2019: The Conversational Assistance Track Overview},
  author={Jeffrey Dalton and Chenyan Xiong and Jamie Callan},
  booktitle={TREC},
  year={2019}
}
```
