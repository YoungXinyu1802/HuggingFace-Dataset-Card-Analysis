---
pretty_name: '`mmarco/zh/dev/v1.1`'
viewer: false
source_datasets: ['irds/mmarco_zh', 'irds/mmarco_zh_dev']
task_categories:
- text-retrieval
---

# Dataset Card for `mmarco/zh/dev/v1.1`

The `mmarco/zh/dev/v1.1` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/mmarco#mmarco/zh/dev/v1.1).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=101,093

 - For `docs`, use [`irds/mmarco_zh`](https://huggingface.co/datasets/irds/mmarco_zh)
 - For `qrels`, use [`irds/mmarco_zh_dev`](https://huggingface.co/datasets/irds/mmarco_zh_dev)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/mmarco_zh_dev_v1.1', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

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
