---
pretty_name: '`codesearchnet`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `codesearchnet`

The `codesearchnet` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/codesearchnet#codesearchnet).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=2,070,536


This dataset is used by: [`codesearchnet_challenge`](https://huggingface.co/datasets/irds/codesearchnet_challenge), [`codesearchnet_test`](https://huggingface.co/datasets/irds/codesearchnet_test), [`codesearchnet_train`](https://huggingface.co/datasets/irds/codesearchnet_train), [`codesearchnet_valid`](https://huggingface.co/datasets/irds/codesearchnet_valid)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/codesearchnet', 'docs')
for record in docs:
    record # {'doc_id': ..., 'repo': ..., 'path': ..., 'func_name': ..., 'code': ..., 'language': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Husain2019CodeSearchNet,
  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},
  author={Hamel Husain and Ho-Hsiang Wu and Tiferet Gazit and Miltiadis Allamanis and Marc Brockschmidt},
  journal={ArXiv},
  year={2019}
}
```
