---
pretty_name: '`tweets2013-ia`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `tweets2013-ia`

The `tweets2013-ia` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/tweets2013-ia#tweets2013-ia).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=252,713,133


This dataset is used by: [`tweets2013-ia_trec-mb-2013`](https://huggingface.co/datasets/irds/tweets2013-ia_trec-mb-2013), [`tweets2013-ia_trec-mb-2014`](https://huggingface.co/datasets/irds/tweets2013-ia_trec-mb-2014)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/tweets2013-ia', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'user_id': ..., 'created_at': ..., 'lang': ..., 'reply_doc_id': ..., 'retweet_doc_id': ..., 'source': ..., 'source_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Sequiera2017TweetsIA,
  title={Finally, a Downloadable Test Collection of Tweets},
  author={Royal Sequiera and Jimmy Lin},
  booktitle={SIGIR},
  year={2017}
}
```
