---
pretty_name: '`msmarco-passage/dev/judged`'
viewer: false
source_datasets: ['irds/msmarco-passage', 'irds/msmarco-passage_dev']
task_categories:
- text-retrieval
---

# Dataset Card for `msmarco-passage/dev/judged`

The `msmarco-passage/dev/judged` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/msmarco-passage#msmarco-passage/dev/judged).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=55,578

 - For `docs`, use [`irds/msmarco-passage`](https://huggingface.co/datasets/irds/msmarco-passage)
 - For `qrels`, use [`irds/msmarco-passage_dev`](https://huggingface.co/datasets/irds/msmarco-passage_dev)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/msmarco-passage_dev_judged', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

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
