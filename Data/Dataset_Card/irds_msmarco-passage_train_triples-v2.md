---
pretty_name: '`msmarco-passage/train/triples-v2`'
viewer: false
source_datasets: ['irds/msmarco-passage']
task_categories:
- text-retrieval
---

# Dataset Card for `msmarco-passage/train/triples-v2`

The `msmarco-passage/train/triples-v2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/msmarco-passage#msmarco-passage/train/triples-v2).

# Data

This dataset provides:
 - `docpairs`; count=397,768,673

 - For `docs`, use [`irds/msmarco-passage`](https://huggingface.co/datasets/irds/msmarco-passage)

## Usage

```python
from datasets import load_dataset

docpairs = load_dataset('irds/msmarco-passage_train_triples-v2', 'docpairs')
for record in docpairs:
    record # {'query_id': ..., 'doc_id_a': ..., 'doc_id_b': ...}

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
