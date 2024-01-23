---
pretty_name: '`trec-spanish/trec3`'
viewer: false
source_datasets: ['irds/trec-spanish']
task_categories:
- text-retrieval
---

# Dataset Card for `trec-spanish/trec3`

The `trec-spanish/trec3` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-spanish#trec-spanish/trec3).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=25
 - `qrels`: (relevance assessments); count=19,005

 - For `docs`, use [`irds/trec-spanish`](https://huggingface.co/datasets/irds/trec-spanish)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-spanish_trec3', 'queries')
for record in queries:
    record # {'query_id': ..., 'title_es': ..., 'title_en': ..., 'description_es': ..., 'description_en': ..., 'narrative_es': ..., 'narrative_en': ...}

qrels = load_dataset('irds/trec-spanish_trec3', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Harman1994Trec3,
  title={Overview of the Third Text REtrieval Conference (TREC-3)},
  author={Donna Harman},
  booktitle={TREC},
  year={1994}
}
@misc{Rogers2000Spanish,
  title={TREC Spanish LDC2000T51},
  author={Rogers, Willie},
  year={2000},
  url={https://catalog.ldc.upenn.edu/LDC2000T51},
  publisher={Linguistic Data Consortium}
}
```
