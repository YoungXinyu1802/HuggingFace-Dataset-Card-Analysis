---
pretty_name: '`neumarco/zh/train/judged`'
viewer: false
source_datasets: ['irds/neumarco_zh', 'irds/neumarco_zh_train']
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/zh/train/judged`

The `neumarco/zh/train/judged` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/zh/train/judged).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=502,939

 - For `docs`, use [`irds/neumarco_zh`](https://huggingface.co/datasets/irds/neumarco_zh)
 - For `qrels`, use [`irds/neumarco_zh_train`](https://huggingface.co/datasets/irds/neumarco_zh_train)
 - For `docpairs`, use [`irds/neumarco_zh_train`](https://huggingface.co/datasets/irds/neumarco_zh_train)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/neumarco_zh_train_judged', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
