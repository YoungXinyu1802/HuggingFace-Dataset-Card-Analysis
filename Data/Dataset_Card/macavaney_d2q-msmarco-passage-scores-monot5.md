---
annotations_creators:
- no-annotation
language: []
language_creators:
- machine-generated
license: []
pretty_name: Doc2Query monoT5 Relevance Scores for `msmarco-passage`
source_datasets: [msmarco-passage]
tags:
- document-expansion
- doc2query--
task_categories:
- text-retrieval
task_ids:
- document-retrieval
viewer: false
---

# Doc2Query monoT5 Relevance Scores for `msmarco-passage`

This dataset provides the pre-computed query relevance scores for the [`msmarco-passage`](https://ir-datasets.com/msmarco-passage) dataset,
for use with Doc2Query--.

The generated queries come from [`macavaney/d2q-msmarco-passage`](https://huggingface.co/datasets/macavaney/d2q-msmarco-passage) and
were scored with [`castorini/monot5-base-msmarco`](https://huggingface.co/castorini/monot5-base-msmarco).

## Getting started

This artefact is meant to be used with the [`pyterrier_doc2query`](https://github.com/terrierteam/pyterrier_doc2query) pacakge. It can
be installed as:

```bash
pip install git+https://github.com/terrierteam/pyterrier_doc2query
```

Depending on what you are using this aretefact for, you may also need the following additional packages:

```bash
pip install git+https://github.com/terrierteam/pyterrier_pisa # for indexing / retrieval
pip install git+https://github.com/terrierteam/pyterrier_t5 # for reproducing this aretefact
```

## Using this artefact

The main use case is to use this aretefact in a Doc2Query&minus;&minus; indexing pipeline:

```python
import pyterrier as pt ; pt.init()
from pyterrier_pisa import PisaIndex
from pyterrier_doc2query import QueryScoreStore, QueryFilter

store = QueryScoreStore.from_repo('https://huggingface.co/datasets/macavaney/d2q-msmarco-passage-scores-monot5')
index = PisaIndex('path/to/index')
pipeline = store.query_scorer(limit_k=40) >> QueryFilter(t=store.percentile(70)) >> index

dataset = pt.get_dataset('irds:msmarco-passage')
pipeline.index(dataset.get_corpus_iter())
```

You can also use the store directly as a dataset to look up or iterate over the data:

```python
store.lookup('100')
# {'querygen': ..., 'querygen_store': ...}
for record in store:
   pass
```

## Reproducing this aretefact

This aretefact can be reproduced using the following pipeline:

```python
import pyterrier as pt ; pt.init()
from pyterrier_t5 import MonoT5ReRanker
from pyterrier_doc2query import Doc2QueryStore, QueryScoreStore, QueryScorer

doc2query_generator = Doc2QueryStore.from_repo('https://huggingface.co/datasets/macavaney/d2q-msmarco-passage').generator()
store = QueryScoreStore('path/to/store')
pipeline = doc2query_generator >> QueryScorer(MonoT5ReRanker()) >> store

dataset = pt.get_dataset('irds:msmarco-passage')
pipeline.index(dataset.get_corpus_iter())
```

Note that this process will take quite some time; it computes the relevance score for 80 generated queries
for every document in the dataset.
