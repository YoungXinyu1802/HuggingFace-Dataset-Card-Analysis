---
pretty_name: '`msmarco-document-v2`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `msmarco-document-v2`

The `msmarco-document-v2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/msmarco-document-v2#msmarco-document-v2).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=11,959,635


This dataset is used by: [`msmarco-document-v2_trec-dl-2019`](https://huggingface.co/datasets/irds/msmarco-document-v2_trec-dl-2019), [`msmarco-document-v2_trec-dl-2019_judged`](https://huggingface.co/datasets/irds/msmarco-document-v2_trec-dl-2019_judged), [`msmarco-document-v2_trec-dl-2020`](https://huggingface.co/datasets/irds/msmarco-document-v2_trec-dl-2020), [`msmarco-document-v2_trec-dl-2020_judged`](https://huggingface.co/datasets/irds/msmarco-document-v2_trec-dl-2020_judged)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/msmarco-document-v2', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'title': ..., 'headings': ..., 'body': ...}

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
