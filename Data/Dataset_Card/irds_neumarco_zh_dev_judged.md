---
pretty_name: '`neumarco/zh/dev/judged`'
viewer: false
source_datasets: ['irds/neumarco_zh', 'irds/neumarco_zh_dev']
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/zh/dev/judged`

The `neumarco/zh/dev/judged` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/zh/dev/judged).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=55,578

 - For `docs`, use [`irds/neumarco_zh`](https://huggingface.co/datasets/irds/neumarco_zh)
 - For `qrels`, use [`irds/neumarco_zh_dev`](https://huggingface.co/datasets/irds/neumarco_zh_dev)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/neumarco_zh_dev_judged', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
