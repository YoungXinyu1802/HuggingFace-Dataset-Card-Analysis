---
pretty_name: '`car/v1.5`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `car/v1.5`

The `car/v1.5` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/car#car/v1.5).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=29,678,367


This dataset is used by: [`car_v1.5_trec-y1_auto`](https://huggingface.co/datasets/irds/car_v1.5_trec-y1_auto), [`car_v1.5_trec-y1_manual`](https://huggingface.co/datasets/irds/car_v1.5_trec-y1_manual)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/car_v1.5', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Dietz2017Car,
  title={{TREC CAR}: A Data Set for Complex Answer Retrieval},
  author={Laura Dietz and Ben Gamari},
  year={2017},
  note={Version 1.5},
  url={http://trec-car.cs.unh.edu}
}
```
