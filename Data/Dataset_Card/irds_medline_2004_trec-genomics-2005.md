---
pretty_name: '`medline/2004/trec-genomics-2005`'
viewer: false
source_datasets: ['irds/medline_2004']
task_categories:
- text-retrieval
---

# Dataset Card for `medline/2004/trec-genomics-2005`

The `medline/2004/trec-genomics-2005` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/medline#medline/2004/trec-genomics-2005).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=39,958

 - For `docs`, use [`irds/medline_2004`](https://huggingface.co/datasets/irds/medline_2004)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/medline_2004_trec-genomics-2005', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/medline_2004_trec-genomics-2005', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Hersh2005TrecGenomics,
  title={TREC 2005 Genomics Track Overview},
  author={William Hersh and Aaron Cohen and Jianji Yang and Ravi Teja Bhupatiraju and Phoebe Roberts and Marti Hearst},
  booktitle={TREC},
  year={2007}
}
```
