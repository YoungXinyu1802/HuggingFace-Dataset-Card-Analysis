---
pretty_name: '`trec-spanish`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-spanish`

The `trec-spanish` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-spanish#trec-spanish).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=120,605


This dataset is used by: [`trec-spanish_trec3`](https://huggingface.co/datasets/irds/trec-spanish_trec3), [`trec-spanish_trec4`](https://huggingface.co/datasets/irds/trec-spanish_trec4)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/trec-spanish', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'marked_up_doc': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@misc{Rogers2000Spanish,
  title={TREC Spanish LDC2000T51},
  author={Rogers, Willie},
  year={2000},
  url={https://catalog.ldc.upenn.edu/LDC2000T51},
  publisher={Linguistic Data Consortium}
}
```
