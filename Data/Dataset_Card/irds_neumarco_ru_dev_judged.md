---
pretty_name: '`neumarco/ru/dev/judged`'
viewer: false
source_datasets: ['irds/neumarco_ru', 'irds/neumarco_ru_dev']
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/ru/dev/judged`

The `neumarco/ru/dev/judged` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/ru/dev/judged).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=55,578

 - For `docs`, use [`irds/neumarco_ru`](https://huggingface.co/datasets/irds/neumarco_ru)
 - For `qrels`, use [`irds/neumarco_ru_dev`](https://huggingface.co/datasets/irds/neumarco_ru_dev)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/neumarco_ru_dev_judged', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
