---
pretty_name: '`msmarco-document/trec-dl-hard/fold2`'
viewer: false
source_datasets: ['irds/msmarco-document']
task_categories:
- text-retrieval
---

# Dataset Card for `msmarco-document/trec-dl-hard/fold2`

The `msmarco-document/trec-dl-hard/fold2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/msmarco-document#msmarco-document/trec-dl-hard/fold2).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=10
 - `qrels`: (relevance assessments); count=1,345

 - For `docs`, use [`irds/msmarco-document`](https://huggingface.co/datasets/irds/msmarco-document)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/msmarco-document_trec-dl-hard_fold2', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/msmarco-document_trec-dl-hard_fold2', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Mackie2021DlHard,
  title={How Deep is your Learning: the DL-HARD Annotated Deep Learning Dataset},
  author={Iain Mackie and Jeffrey Dalton and Andrew Yates},
  journal={ArXiv},
  year={2021},
  volume={abs/2105.07975}
}
@inproceedings{Bajaj2016Msmarco,
  title={MS MARCO: A Human Generated MAchine Reading COmprehension Dataset},
  author={Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xiaodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri Nguyen, Mir Rosenberg, Xia Song, Alina Stoica, Saurabh Tiwary, Tong Wang},
  booktitle={InCoCo@NIPS},
  year={2016}
}
```
