---
pretty_name: '`neumarco/zh/dev`'
viewer: false
source_datasets: ['irds/neumarco_zh']
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/zh/dev`

The `neumarco/zh/dev` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/zh/dev).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=101,093
 - `qrels`: (relevance assessments); count=59,273

 - For `docs`, use [`irds/neumarco_zh`](https://huggingface.co/datasets/irds/neumarco_zh)

This dataset is used by: [`neumarco_zh_dev_judged`](https://huggingface.co/datasets/irds/neumarco_zh_dev_judged)


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/neumarco_zh_dev', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/neumarco_zh_dev', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
