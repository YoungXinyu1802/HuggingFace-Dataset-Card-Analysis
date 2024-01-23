---
pretty_name: '`lotte/pooled/test/search`'
viewer: false
source_datasets: ['irds/lotte_pooled_test']
task_categories:
- text-retrieval
---

# Dataset Card for `lotte/pooled/test/search`

The `lotte/pooled/test/search` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/lotte#lotte/pooled/test/search).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=3,869
 - `qrels`: (relevance assessments); count=11,124

 - For `docs`, use [`irds/lotte_pooled_test`](https://huggingface.co/datasets/irds/lotte_pooled_test)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/lotte_pooled_test_search', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/lotte_pooled_test_search', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Santhanam2021ColBERTv2,
  title = "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction",
  author = "Keshav Santhanam and Omar Khattab and Jon Saad-Falcon and Christopher Potts and Matei Zaharia", 
  journal= "arXiv preprint arXiv:2112.01488",
  year = "2021",
  url = "https://arxiv.org/abs/2112.01488"
}
```