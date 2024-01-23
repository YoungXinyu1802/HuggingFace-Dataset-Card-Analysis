---
pretty_name: '`aquaint`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `aquaint`

The `aquaint` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/aquaint#aquaint).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,033,461


This dataset is used by: [`aquaint_trec-robust-2005`](https://huggingface.co/datasets/irds/aquaint_trec-robust-2005)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/aquaint', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'marked_up_doc': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@misc{Graff2002Aquaint,
  title={The AQUAINT Corpus of English News Text},
  author={David Graff},
  year={2002},
  url={https://catalog.ldc.upenn.edu/LDC2002T31},
  publisher={Linguistic Data Consortium}
}
```
