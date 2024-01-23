---
pretty_name: '`medline/2004/trec-genomics-2004`'
viewer: false
source_datasets: ['irds/medline_2004']
task_categories:
- text-retrieval
---

# Dataset Card for `medline/2004/trec-genomics-2004`

The `medline/2004/trec-genomics-2004` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/medline#medline/2004/trec-genomics-2004).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=8,268

 - For `docs`, use [`irds/medline_2004`](https://huggingface.co/datasets/irds/medline_2004)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/medline_2004_trec-genomics-2004', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'need': ..., 'context': ...}

qrels = load_dataset('irds/medline_2004_trec-genomics-2004', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Hersh2004TrecGenomics,
  title={TREC 2004 Genomics Track Overview},
  author={William R. Hersh and Ravi Teja Bhuptiraju and Laura Ross and Phoebe Johnson and Aaron M. Cohen and Dale F. Kraemer},
  booktitle={TREC},
  year={2004}
}
```
