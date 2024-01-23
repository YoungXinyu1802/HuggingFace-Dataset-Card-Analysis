---
pretty_name: '`tripclick/train`'
viewer: false
source_datasets: ['irds/tripclick']
task_categories:
- text-retrieval
---

# Dataset Card for `tripclick/train`

The `tripclick/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/tripclick#tripclick/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=685,649
 - `qrels`: (relevance assessments); count=2,705,212
 - `docpairs`; count=23,221,224

 - For `docs`, use [`irds/tripclick`](https://huggingface.co/datasets/irds/tripclick)

This dataset is used by: [`tripclick_train_hofstaetter-triples`](https://huggingface.co/datasets/irds/tripclick_train_hofstaetter-triples)


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/tripclick_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/tripclick_train', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

docpairs = load_dataset('irds/tripclick_train', 'docpairs')
for record in docpairs:
    record # {'query_id': ..., 'doc_id_a': ..., 'doc_id_b': ...}

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
