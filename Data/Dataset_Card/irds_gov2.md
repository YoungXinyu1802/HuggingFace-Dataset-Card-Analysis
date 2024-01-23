---
pretty_name: '`gov2`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `gov2`

The `gov2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/gov2#gov2).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=25,205,179


This dataset is used by: [`gov2_trec-tb-2004`](https://huggingface.co/datasets/irds/gov2_trec-tb-2004), [`gov2_trec-tb-2005`](https://huggingface.co/datasets/irds/gov2_trec-tb-2005), [`gov2_trec-tb-2005_efficiency`](https://huggingface.co/datasets/irds/gov2_trec-tb-2005_efficiency), [`gov2_trec-tb-2005_named-page`](https://huggingface.co/datasets/irds/gov2_trec-tb-2005_named-page), [`gov2_trec-tb-2006`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006), [`gov2_trec-tb-2006_efficiency`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_efficiency), [`gov2_trec-tb-2006_efficiency_10k`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_efficiency_10k), [`gov2_trec-tb-2006_efficiency_stream1`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_efficiency_stream1), [`gov2_trec-tb-2006_efficiency_stream2`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_efficiency_stream2), [`gov2_trec-tb-2006_efficiency_stream3`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_efficiency_stream3), [`gov2_trec-tb-2006_efficiency_stream4`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_efficiency_stream4), [`gov2_trec-tb-2006_named-page`](https://huggingface.co/datasets/irds/gov2_trec-tb-2006_named-page)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/gov2', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'http_headers': ..., 'body': ..., 'body_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
