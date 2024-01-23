---
pretty_name: '`msmarco-document`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `msmarco-document`

The `msmarco-document` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/msmarco-document#msmarco-document).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=3,213,835


This dataset is used by: [`msmarco-document_trec-dl-hard`](https://huggingface.co/datasets/irds/msmarco-document_trec-dl-hard), [`msmarco-document_trec-dl-hard_fold1`](https://huggingface.co/datasets/irds/msmarco-document_trec-dl-hard_fold1), [`msmarco-document_trec-dl-hard_fold2`](https://huggingface.co/datasets/irds/msmarco-document_trec-dl-hard_fold2), [`msmarco-document_trec-dl-hard_fold3`](https://huggingface.co/datasets/irds/msmarco-document_trec-dl-hard_fold3), [`msmarco-document_trec-dl-hard_fold4`](https://huggingface.co/datasets/irds/msmarco-document_trec-dl-hard_fold4), [`msmarco-document_trec-dl-hard_fold5`](https://huggingface.co/datasets/irds/msmarco-document_trec-dl-hard_fold5)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/msmarco-document', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'title': ..., 'body': ...}

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
