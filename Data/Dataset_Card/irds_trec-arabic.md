---
pretty_name: '`trec-arabic`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-arabic`

The `trec-arabic` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-arabic#trec-arabic).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=383,872


This dataset is used by: [`trec-arabic_ar2001`](https://huggingface.co/datasets/irds/trec-arabic_ar2001), [`trec-arabic_ar2002`](https://huggingface.co/datasets/irds/trec-arabic_ar2002)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/trec-arabic', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'marked_up_doc': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@misc{Graff2001Arabic,
  title={Arabic Newswire Part 1 LDC2001T55},
  author={Graff, David, and Walker, Kevin},
  year={2001},
  url={https://catalog.ldc.upenn.edu/LDC2001T55},
  publisher={Linguistic Data Consortium}
}
```
