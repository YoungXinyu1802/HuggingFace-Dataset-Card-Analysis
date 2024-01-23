---
pretty_name: '`aquaint/trec-robust-2005`'
viewer: false
source_datasets: ['irds/aquaint']
task_categories:
- text-retrieval
---

# Dataset Card for `aquaint/trec-robust-2005`

The `aquaint/trec-robust-2005` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/aquaint#aquaint/trec-robust-2005).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=37,798

 - For `docs`, use [`irds/aquaint`](https://huggingface.co/datasets/irds/aquaint)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/aquaint_trec-robust-2005', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/aquaint_trec-robust-2005', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Voorhees2005Robust,
  title={Overview of the TREC 2005 Robust Retrieval Track},
  author={Ellen M. Voorhees},
  booktitle={TREC},
  year={2005}
}
@misc{Graff2002Aquaint,
  title={The AQUAINT Corpus of English News Text},
  author={David Graff},
  year={2002},
  url={https://catalog.ldc.upenn.edu/LDC2002T31},
  publisher={Linguistic Data Consortium}
}
```
