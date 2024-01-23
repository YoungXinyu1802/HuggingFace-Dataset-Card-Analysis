---
pretty_name: '`medline/2004`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `medline/2004`

The `medline/2004` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/medline#medline/2004).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=3,672,808


This dataset is used by: [`medline_2004_trec-genomics-2004`](https://huggingface.co/datasets/irds/medline_2004_trec-genomics-2004), [`medline_2004_trec-genomics-2005`](https://huggingface.co/datasets/irds/medline_2004_trec-genomics-2005)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/medline_2004', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'abstract': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
