---
pretty_name: '`tripclick/train/hofstaetter-triples`'
viewer: false
source_datasets: ['irds/tripclick', 'irds/tripclick_train']
task_categories:
- text-retrieval
---

# Dataset Card for `tripclick/train/hofstaetter-triples`

The `tripclick/train/hofstaetter-triples` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/tripclick#tripclick/train/hofstaetter-triples).

# Data

This dataset provides:
 - `docpairs`; count=10,000,000

 - For `docs`, use [`irds/tripclick`](https://huggingface.co/datasets/irds/tripclick)
 - For `queries`, use [`irds/tripclick_train`](https://huggingface.co/datasets/irds/tripclick_train)
 - For `qrels`, use [`irds/tripclick_train`](https://huggingface.co/datasets/irds/tripclick_train)

## Usage

```python
from datasets import load_dataset

docpairs = load_dataset('irds/tripclick_train_hofstaetter-triples', 'docpairs')
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
@inproceedings{Hofstaetter2022TripClick,
  title={Establishing Strong Baselines for TripClick Health Retrieval},
  author={Sebastian Hofst\"atter and Sophia Althammer and Mete Sertkan and Allan Hanbury},
  year={2022},
  booktitle={ECIR}
}
```
