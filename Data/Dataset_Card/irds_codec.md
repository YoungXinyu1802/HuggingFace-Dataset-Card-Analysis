---
pretty_name: '`codec`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `codec`

The `codec` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/codec#codec).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=729,824
 - `queries` (i.e., topics); count=42
 - `qrels`: (relevance assessments); count=6,186


This dataset is used by: [`codec_economics`](https://huggingface.co/datasets/irds/codec_economics), [`codec_history`](https://huggingface.co/datasets/irds/codec_history), [`codec_politics`](https://huggingface.co/datasets/irds/codec_politics)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/codec', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'text': ..., 'url': ...}

queries = load_dataset('irds/codec', 'queries')
for record in queries:
    record # {'query_id': ..., 'query': ..., 'domain': ..., 'guidelines': ...}

qrels = load_dataset('irds/codec', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{mackie2022codec,
   title={CODEC: Complex Document and Entity Collection},
   author={Mackie, Iain and Owoicho, Paul and Gemmell, Carlos and Fischer, Sophie and MacAvaney, Sean and Dalton, Jeffery},
   booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
   year={2022}
}
```
