---
pretty_name: '`tripclick`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `tripclick`

The `tripclick` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/tripclick#tripclick).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,523,878


This dataset is used by: [`tripclick_train`](https://huggingface.co/datasets/irds/tripclick_train), [`tripclick_train_head`](https://huggingface.co/datasets/irds/tripclick_train_head), [`tripclick_train_head_dctr`](https://huggingface.co/datasets/irds/tripclick_train_head_dctr), [`tripclick_train_hofstaetter-triples`](https://huggingface.co/datasets/irds/tripclick_train_hofstaetter-triples), [`tripclick_train_tail`](https://huggingface.co/datasets/irds/tripclick_train_tail), [`tripclick_train_torso`](https://huggingface.co/datasets/irds/tripclick_train_torso), [`tripclick_val_head_dctr`](https://huggingface.co/datasets/irds/tripclick_val_head_dctr)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/tripclick', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'url': ..., 'text': ...}

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
