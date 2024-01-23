---
pretty_name: '`mr-tydi/id/dev`'
viewer: false
source_datasets: ['irds/mr-tydi_id']
task_categories:
- text-retrieval
---

# Dataset Card for `mr-tydi/id/dev`

The `mr-tydi/id/dev` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/mr-tydi#mr-tydi/id/dev).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=1,224
 - `qrels`: (relevance assessments); count=1,224

 - For `docs`, use [`irds/mr-tydi_id`](https://huggingface.co/datasets/irds/mr-tydi_id)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/mr-tydi_id_dev', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/mr-tydi_id_dev', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Zhang2021MrTyDi,
  title={{Mr. TyDi}: A Multi-lingual Benchmark for Dense Retrieval}, 
  author={Xinyu Zhang and Xueguang Ma and Peng Shi and Jimmy Lin},
  year={2021},
  journal={arXiv:2108.08787},
}
@article{Clark2020TyDiQa,
    title={{TyDi QA}: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
    author={Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki},
    year={2020},
    journal={Transactions of the Association for Computational Linguistics}
}
```
