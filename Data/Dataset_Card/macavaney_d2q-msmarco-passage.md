---
annotations_creators:
- no-annotation
language: []
language_creators:
- machine-generated
license: []
pretty_name: Doc2Query Generated Queries for `msmarco-passage`
source_datasets: [msmarco-passage]
tags:
- document-expansion
- doc2query
task_categories:
- text-retrieval
task_ids:
- document-retrieval
viewer: false
---

# Doc2Query Generated Queries for `msmarco-passage`

This dataset provides the pre-computed generated queries for the [`msmarco-passage`](https://ir-datasets.com/msmarco-passage) dataset,
for use when indexing Doc2Query.

The generated queries from from the T5 Doc2Query model, released by the original authors [here](https://github.com/castorini/docTTTTTquery).

## Getting started

This artefact is meant to be used with the [`pyterrier_doc2query`](https://github.com/terrierteam/pyterrier_doc2query) pacakge. It can
be installed as:

```bash
pip install git+https://github.com/terrierteam/pyterrier_doc2query
```

Depending on what you are using this aretefact for, you may also need the following additional package:

```bash
pip install git+https://github.com/terrierteam/pyterrier_pisa # for indexing / retrieval
```

## Using this artefact

The main use case is to use this aretefact in a Doc2Query indexing pipeline:

```python
import pyterrier as pt ; pt.init()
from pyterrier_pisa import PisaIndex
from pyterrier_doc2query import Doc2QueryStore

store = Doc2QueryStore.from_repo('https://huggingface.co/datasets/macavaney/d2q-msmarco-passage')
index = PisaIndex('path/to/index')
pipeline = store.generator(limit_k=40) >> index

dataset = pt.get_dataset('irds:msmarco-passage')
pipeline.index(dataset.get_corpus_iter())
```

You can also use the store directly as a dataset to look up or iterate over the data:

```python
store.lookup('100')
# {'querygen': ...}
for record in store:
   pass
```

## Reproducing this aretefact

Due to the random nature of the Doc2Query generation process, this artefact cannot be reproduced verbatim.
This aretefact can be reproduced using the following pipeline:

The following runs Doc2Query inference over the MS MARCO dataset. It will not produce the artefact verbatim,
but should produce similar results when used for indexing/retrieval.

```python
import pyterrier as pt ; pt.init()
from pyterrier_doc2query import Doc2Query, Doc2QueryStore

doc2query = Doc2Query('macavaney/doc2query-t5-base-msmarco', num_samples=80)
store = Doc2QueryStore('path/to/store')
pipeline = doc2query >> store

dataset = pt.get_dataset('irds:msmarco-passage')
pipeline.index(dataset.get_corpus_iter())
```

Note that this process will take quite some time, since it generates 80 queries for every document in the dataset.

Alternatively, you could reproduce this artefact verbatim using the following script, but it doesn't perform
model inference; it just uses the pre-generated queries from the original authors.

```bash
wget https://git.uwaterloo.ca/jimmylin/doc2query-data/raw/master/T5-passage/predicted_queries_topk_sampling.zip
unzip predicted_queries_topk_sampling.zip
```

```python
from pyterrier_doc2query import Doc2QueryStore
import os
import ir_datasets

def iter_files(path):
  i = 0
  while os.path.exists(path.format(i)):
    with open(path.format(i), 'rt') as fin:
      for line in fin:
        yield line.strip()
    i += 1

def it():
  file_iters = [iter_files('predicted_queries_topk_sample{:03}'.format(i)+'.txt{:03}-1004000') for i in range(80)]
  for queries in enumerate(zip(*file_iters)):
    yield {'docno': str(i), 'querygen': '\n'.join(queries)}

store = Doc2QueryStore('path/to/store')

store.index(it())
```
