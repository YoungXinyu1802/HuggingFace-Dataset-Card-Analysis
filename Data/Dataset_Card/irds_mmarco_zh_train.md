---
pretty_name: '`mmarco/zh/train`'
viewer: false
source_datasets: ['irds/mmarco_zh']
task_categories:
- text-retrieval
---

# Dataset Card for `mmarco/zh/train`

The `mmarco/zh/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/mmarco#mmarco/zh/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=808,731
 - `qrels`: (relevance assessments); count=532,761
 - `docpairs`; count=39,780,811

 - For `docs`, use [`irds/mmarco_zh`](https://huggingface.co/datasets/irds/mmarco_zh)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/mmarco_zh_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/mmarco_zh_train', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

docpairs = load_dataset('irds/mmarco_zh_train', 'docpairs')
for record in docpairs:
    record # {'query_id': ..., 'doc_id_a': ..., 'doc_id_b': ...}

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
