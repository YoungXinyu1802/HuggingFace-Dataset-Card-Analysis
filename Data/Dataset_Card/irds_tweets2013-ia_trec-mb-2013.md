---
pretty_name: '`tweets2013-ia/trec-mb-2013`'
viewer: false
source_datasets: ['irds/tweets2013-ia']
task_categories:
- text-retrieval
---

# Dataset Card for `tweets2013-ia/trec-mb-2013`

The `tweets2013-ia/trec-mb-2013` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/tweets2013-ia#tweets2013-ia/trec-mb-2013).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=60
 - `qrels`: (relevance assessments); count=71,279

 - For `docs`, use [`irds/tweets2013-ia`](https://huggingface.co/datasets/irds/tweets2013-ia)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/tweets2013-ia_trec-mb-2013', 'queries')
for record in queries:
    record # {'query_id': ..., 'query': ..., 'time': ..., 'tweet_time': ...}

qrels = load_dataset('irds/tweets2013-ia_trec-mb-2013', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Lin2013Microblog,
  title={Overview of the TREC-2013 Microblog Track},
  author={Jimmy Lin and Miles Efron},
  booktitle={TREC},
  year={2013}
}
@inproceedings{Sequiera2017TweetsIA,
  title={Finally, a Downloadable Test Collection of Tweets},
  author={Royal Sequiera and Jimmy Lin},
  booktitle={SIGIR},
  year={2017}
}
```
