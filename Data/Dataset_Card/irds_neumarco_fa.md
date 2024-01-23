---
pretty_name: '`neumarco/fa`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/fa`

The `neumarco/fa` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/fa).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=8,841,823


This dataset is used by: [`neumarco_fa_dev`](https://huggingface.co/datasets/irds/neumarco_fa_dev), [`neumarco_fa_dev_judged`](https://huggingface.co/datasets/irds/neumarco_fa_dev_judged), [`neumarco_fa_dev_small`](https://huggingface.co/datasets/irds/neumarco_fa_dev_small), [`neumarco_fa_train`](https://huggingface.co/datasets/irds/neumarco_fa_train), [`neumarco_fa_train_judged`](https://huggingface.co/datasets/irds/neumarco_fa_train_judged)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/neumarco_fa', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
