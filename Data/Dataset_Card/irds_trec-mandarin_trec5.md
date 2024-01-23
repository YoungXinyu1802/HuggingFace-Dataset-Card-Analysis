---
pretty_name: '`trec-mandarin/trec5`'
viewer: false
source_datasets: ['irds/trec-mandarin']
task_categories:
- text-retrieval
---

# Dataset Card for `trec-mandarin/trec5`

The `trec-mandarin/trec5` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-mandarin#trec-mandarin/trec5).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=28
 - `qrels`: (relevance assessments); count=15,588

 - For `docs`, use [`irds/trec-mandarin`](https://huggingface.co/datasets/irds/trec-mandarin)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-mandarin_trec5', 'queries')
for record in queries:
    record # {'query_id': ..., 'title_en': ..., 'title_zh': ..., 'description_en': ..., 'description_zh': ..., 'narrative_en': ..., 'narrative_zh': ...}

qrels = load_dataset('irds/trec-mandarin_trec5', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Harman1997Chinese,
  title={Spanish and Chinese Document Retrieval in TREC-5},
  author={Alan Smeaton and Ross Wilkinson},
  booktitle={TREC},
  year={1996}
}
@misc{Rogers2000Mandarin,
  title={TREC Mandarin LDC2000T52},
  author={Rogers, Willie},
  year={2000},
  url={https://catalog.ldc.upenn.edu/LDC2000T52},
  publisher={Linguistic Data Consortium}
}
```
