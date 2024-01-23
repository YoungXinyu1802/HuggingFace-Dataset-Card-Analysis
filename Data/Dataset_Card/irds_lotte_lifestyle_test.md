---
pretty_name: '`lotte/lifestyle/test`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `lotte/lifestyle/test`

The `lotte/lifestyle/test` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/lotte#lotte/lifestyle/test).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=119,461


This dataset is used by: [`lotte_lifestyle_test_forum`](https://huggingface.co/datasets/irds/lotte_lifestyle_test_forum), [`lotte_lifestyle_test_search`](https://huggingface.co/datasets/irds/lotte_lifestyle_test_search)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/lotte_lifestyle_test', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Santhanam2021ColBERTv2,
  title = "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction",
  author = "Keshav Santhanam and Omar Khattab and Jon Saad-Falcon and Christopher Potts and Matei Zaharia", 
  journal= "arXiv preprint arXiv:2112.01488",
  year = "2021",
  url = "https://arxiv.org/abs/2112.01488"
}
```
