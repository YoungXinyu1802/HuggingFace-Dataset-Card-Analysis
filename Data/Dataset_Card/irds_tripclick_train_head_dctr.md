---
pretty_name: '`tripclick/train/head/dctr`'
viewer: false
source_datasets: ['irds/tripclick', 'irds/tripclick_train_head']
task_categories:
- text-retrieval
---

# Dataset Card for `tripclick/train/head/dctr`

The `tripclick/train/head/dctr` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/tripclick#tripclick/train/head/dctr).

# Data

This dataset provides:
 - `qrels`: (relevance assessments); count=128,420

 - For `docs`, use [`irds/tripclick`](https://huggingface.co/datasets/irds/tripclick)
 - For `queries`, use [`irds/tripclick_train_head`](https://huggingface.co/datasets/irds/tripclick_train_head)

## Usage

```python
from datasets import load_dataset

qrels = load_dataset('irds/tripclick_train_head_dctr', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Rekabsaz2021TripClick,
  title={TripClick: The Log Files of a Large Health Web Search Engine}, 
  author={Navid Rekabsaz and Oleg Lesota and Markus Schedl and Jon Brassey and Carsten Eickhoff},
  year={2021},
  booktitle={SIGIR}
}
```
