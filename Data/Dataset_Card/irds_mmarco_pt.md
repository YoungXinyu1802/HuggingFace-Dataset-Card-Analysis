---
pretty_name: '`mmarco/pt`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `mmarco/pt`

The `mmarco/pt` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/mmarco#mmarco/pt).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=8,841,823


This dataset is used by: [`mmarco_pt_dev`](https://huggingface.co/datasets/irds/mmarco_pt_dev), [`mmarco_pt_dev_small`](https://huggingface.co/datasets/irds/mmarco_pt_dev_small), [`mmarco_pt_dev_v1.1`](https://huggingface.co/datasets/irds/mmarco_pt_dev_v1.1), [`mmarco_pt_train`](https://huggingface.co/datasets/irds/mmarco_pt_train), [`mmarco_pt_train_v1.1`](https://huggingface.co/datasets/irds/mmarco_pt_train_v1.1)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/mmarco_pt', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

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
