---
pretty_name: '`mmarco/pt/dev`'
viewer: false
source_datasets: ['irds/mmarco_pt']
task_categories:
- text-retrieval
---

# Dataset Card for `mmarco/pt/dev`

The `mmarco/pt/dev` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/mmarco#mmarco/pt/dev).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=101,619
 - `qrels`: (relevance assessments); count=59,273

 - For `docs`, use [`irds/mmarco_pt`](https://huggingface.co/datasets/irds/mmarco_pt)

This dataset is used by: [`mmarco_pt_dev_v1.1`](https://huggingface.co/datasets/irds/mmarco_pt_dev_v1.1)


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/mmarco_pt_dev', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/mmarco_pt_dev', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Bonifacio2021MMarco,
    title={{mMARCO}: A Multilingual Version of {MS MARCO} Passage Ranking Dataset},
    author={Luiz Henrique Bonifacio and Israel Campiotti and Roberto Lotufo and Rodrigo Nogueira},
    year={2021},
    journal={arXiv:2108.13897}
}
```
