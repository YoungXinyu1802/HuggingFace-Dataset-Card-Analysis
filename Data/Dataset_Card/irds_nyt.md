---
pretty_name: '`nyt`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `nyt`

The `nyt` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nyt#nyt).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,864,661


This dataset is used by: [`nyt_trec-core-2017`](https://huggingface.co/datasets/irds/nyt_trec-core-2017), [`nyt_wksup`](https://huggingface.co/datasets/irds/nyt_wksup), [`nyt_wksup_train`](https://huggingface.co/datasets/irds/nyt_wksup_train), [`nyt_wksup_valid`](https://huggingface.co/datasets/irds/nyt_wksup_valid)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/nyt', 'docs')
for record in docs:
    record # {'doc_id': ..., 'headline': ..., 'body': ..., 'source_xml': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Sandhaus2008Nyt,
  title={The new york times annotated corpus},
  author={Sandhaus, Evan},
  journal={Linguistic Data Consortium, Philadelphia},
  volume={6},
  number={12},
  pages={e26752},
  year={2008}
}
```
