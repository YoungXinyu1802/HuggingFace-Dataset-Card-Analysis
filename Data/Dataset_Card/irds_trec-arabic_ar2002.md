---
pretty_name: '`trec-arabic/ar2002`'
viewer: false
source_datasets: ['irds/trec-arabic']
task_categories:
- text-retrieval
---

# Dataset Card for `trec-arabic/ar2002`

The `trec-arabic/ar2002` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-arabic#trec-arabic/ar2002).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=38,432

 - For `docs`, use [`irds/trec-arabic`](https://huggingface.co/datasets/irds/trec-arabic)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-arabic_ar2002', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/trec-arabic_ar2002', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Gey2002Arabic,
  title={The TREC-2002 Arabic/English CLIR Track},
  author={Fredric Gey and Douglas Oard},
  booktitle={TREC},
  year={2002}
}
@misc{Graff2001Arabic,
  title={Arabic Newswire Part 1 LDC2001T55},
  author={Graff, David, and Walker, Kevin},
  year={2001},
  url={https://catalog.ldc.upenn.edu/LDC2001T55},
  publisher={Linguistic Data Consortium}
}
```
