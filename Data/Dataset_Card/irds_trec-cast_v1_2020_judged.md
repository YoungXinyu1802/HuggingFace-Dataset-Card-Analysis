---
pretty_name: '`trec-cast/v1/2020/judged`'
viewer: false
source_datasets: ['irds/trec-cast_v1', 'irds/trec-cast_v1_2020']
task_categories:
- text-retrieval
---

# Dataset Card for `trec-cast/v1/2020/judged`

The `trec-cast/v1/2020/judged` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-cast#trec-cast/v1/2020/judged).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=208

 - For `docs`, use [`irds/trec-cast_v1`](https://huggingface.co/datasets/irds/trec-cast_v1)
 - For `qrels`, use [`irds/trec-cast_v1_2020`](https://huggingface.co/datasets/irds/trec-cast_v1_2020)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-cast_v1_2020_judged', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Dalton2020Cast,
  title={CAsT 2020: The Conversational Assistance Track Overview},
  author={Jeffrey Dalton and Chenyan Xiong and Jamie Callan},
  booktitle={TREC},
  year={2020}
}
```
