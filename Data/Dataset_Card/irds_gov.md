---
pretty_name: '`gov`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `gov`

The `gov` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/gov#gov).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,247,753


This dataset is used by: [`gov_trec-web-2002`](https://huggingface.co/datasets/irds/gov_trec-web-2002), [`gov_trec-web-2002_named-page`](https://huggingface.co/datasets/irds/gov_trec-web-2002_named-page), [`gov_trec-web-2003`](https://huggingface.co/datasets/irds/gov_trec-web-2003), [`gov_trec-web-2003_named-page`](https://huggingface.co/datasets/irds/gov_trec-web-2003_named-page), [`gov_trec-web-2004`](https://huggingface.co/datasets/irds/gov_trec-web-2004)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/gov', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'http_headers': ..., 'body': ..., 'body_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
