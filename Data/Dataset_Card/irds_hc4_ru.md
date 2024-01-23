---
pretty_name: '`hc4/ru`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `hc4/ru`

The `hc4/ru` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/hc4#hc4/ru).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=4,721,064


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/hc4_ru', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'text': ..., 'url': ..., 'time': ..., 'cc_file': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Lawrie2022HC4,
  author = {Dawn Lawrie and James Mayfield and Douglas W. Oard and Eugene Yang},
  title = {HC4: A New Suite of Test Collections for Ad Hoc CLIR},
  booktitle = {{Advances in Information Retrieval. 44th European Conference on IR Research (ECIR 2022)},
  year = {2022},
  month = apr,
  publisher = {Springer},
  series = {Lecture Notes in Computer Science},
  site = {Stavanger, Norway},
  url = {https://arxiv.org/abs/2201.09992}
}
```
