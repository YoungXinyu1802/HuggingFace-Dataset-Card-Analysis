---
pretty_name: '`trec-cast/v1`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-cast/v1`

The `trec-cast/v1` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-cast#trec-cast/v1).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=38,622,444


This dataset is used by: [`trec-cast_v1_2020`](https://huggingface.co/datasets/irds/trec-cast_v1_2020), [`trec-cast_v1_2020_judged`](https://huggingface.co/datasets/irds/trec-cast_v1_2020_judged)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/trec-cast_v1', 'docs')
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
