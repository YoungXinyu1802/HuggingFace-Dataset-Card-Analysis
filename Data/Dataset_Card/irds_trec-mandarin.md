---
pretty_name: '`trec-mandarin`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-mandarin`

The `trec-mandarin` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-mandarin#trec-mandarin).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=164,789


This dataset is used by: [`trec-mandarin_trec5`](https://huggingface.co/datasets/irds/trec-mandarin_trec5), [`trec-mandarin_trec6`](https://huggingface.co/datasets/irds/trec-mandarin_trec6)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/trec-mandarin', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'marked_up_doc': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@misc{Rogers2000Mandarin,
  title={TREC Mandarin LDC2000T52},
  author={Rogers, Willie},
  year={2000},
  url={https://catalog.ldc.upenn.edu/LDC2000T52},
  publisher={Linguistic Data Consortium}
}
```
