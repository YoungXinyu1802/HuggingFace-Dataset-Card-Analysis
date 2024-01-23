---
pretty_name: '`clueweb12/b13`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12/b13`

The `clueweb12/b13` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12/b13).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=52,343,021


This dataset is used by: [`clueweb12_b13_clef-ehealth`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth), [`clueweb12_b13_clef-ehealth_cs`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth_cs), [`clueweb12_b13_clef-ehealth_de`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth_de), [`clueweb12_b13_clef-ehealth_fr`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth_fr), [`clueweb12_b13_clef-ehealth_hu`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth_hu), [`clueweb12_b13_clef-ehealth_pl`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth_pl), [`clueweb12_b13_clef-ehealth_sv`](https://huggingface.co/datasets/irds/clueweb12_b13_clef-ehealth_sv), [`clueweb12_b13_ntcir-www-1`](https://huggingface.co/datasets/irds/clueweb12_b13_ntcir-www-1), [`clueweb12_b13_ntcir-www-2`](https://huggingface.co/datasets/irds/clueweb12_b13_ntcir-www-2), [`clueweb12_b13_ntcir-www-3`](https://huggingface.co/datasets/irds/clueweb12_b13_ntcir-www-3), [`clueweb12_b13_trec-misinfo-2019`](https://huggingface.co/datasets/irds/clueweb12_b13_trec-misinfo-2019)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clueweb12_b13', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'date': ..., 'http_headers': ..., 'body': ..., 'body_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
