---
pretty_name: '`trec-cast/v1/2020`'
viewer: false
source_datasets: ['irds/trec-cast_v1']
task_categories:
- text-retrieval
---

# Dataset Card for `trec-cast/v1/2020`

The `trec-cast/v1/2020` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-cast#trec-cast/v1/2020).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=216
 - `qrels`: (relevance assessments); count=40,451

 - For `docs`, use [`irds/trec-cast_v1`](https://huggingface.co/datasets/irds/trec-cast_v1)

This dataset is used by: [`trec-cast_v1_2020_judged`](https://huggingface.co/datasets/irds/trec-cast_v1_2020_judged)


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-cast_v1_2020', 'queries')
for record in queries:
    record # {'query_id': ..., 'raw_utterance': ..., 'automatic_rewritten_utterance': ..., 'manual_rewritten_utterance': ..., 'manual_canonical_result_id': ..., 'topic_number': ..., 'turn_number': ...}

qrels = load_dataset('irds/trec-cast_v1_2020', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

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
