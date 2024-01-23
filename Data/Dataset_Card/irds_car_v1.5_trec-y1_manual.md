---
pretty_name: '`car/v1.5/trec-y1/manual`'
viewer: false
source_datasets: ['irds/car_v1.5']
task_categories:
- text-retrieval
---

# Dataset Card for `car/v1.5/trec-y1/manual`

The `car/v1.5/trec-y1/manual` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/car#car/v1.5/trec-y1/manual).

# Data

This dataset provides:
 - `qrels`: (relevance assessments); count=29,571

 - For `docs`, use [`irds/car_v1.5`](https://huggingface.co/datasets/irds/car_v1.5)

## Usage

```python
from datasets import load_dataset

qrels = load_dataset('irds/car_v1.5_trec-y1_manual', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Dietz2017TrecCar,
  title={TREC Complex Answer Retrieval Overview.},
  author={Dietz, Laura and Verma, Manisha and Radlinski, Filip and Craswell, Nick},
  booktitle={TREC},
  year={2017}
}
@article{Dietz2017Car,
  title={{TREC CAR}: A Data Set for Complex Answer Retrieval},
  author={Laura Dietz and Ben Gamari},
  year={2017},
  note={Version 1.5},
  url={http://trec-car.cs.unh.edu}
}
```
