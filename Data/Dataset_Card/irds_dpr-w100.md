---
pretty_name: '`dpr-w100`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `dpr-w100`

The `dpr-w100` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/dpr-w100#dpr-w100).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=21,015,324


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/dpr-w100', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@misc{Karpukhin2020Dpr,
  title={Dense Passage Retrieval for Open-Domain Question Answering},
  author={Vladimir Karpukhin and Barlas Oğuz and Sewon Min and Patrick Lewis and Ledell Wu and Sergey Edunov and Danqi Chen and Wen-tau Yih},
  year={2020},
  eprint={2004.04906},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```
