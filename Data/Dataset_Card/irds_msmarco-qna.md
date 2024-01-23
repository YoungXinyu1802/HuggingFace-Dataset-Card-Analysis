---
pretty_name: '`msmarco-qna`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `msmarco-qna`

The `msmarco-qna` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/msmarco-qna#msmarco-qna).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=9,048,606


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/msmarco-qna', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'url': ..., 'msmarco_passage_id': ..., 'msmarco_document_id': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Bajaj2016Msmarco,
  title={MS MARCO: A Human Generated MAchine Reading COmprehension Dataset},
  author={Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xiaodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri Nguyen, Mir Rosenberg, Xia Song, Alina Stoica, Saurabh Tiwary, Tong Wang},
  booktitle={InCoCo@NIPS},
  year={2016}
}
```
