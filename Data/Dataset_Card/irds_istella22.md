---
pretty_name: '`istella22`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `istella22`

The `istella22` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/istella22#istella22).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=8,421,456


This dataset is used by: [`istella22_test`](https://huggingface.co/datasets/irds/istella22_test), [`istella22_test_fold1`](https://huggingface.co/datasets/irds/istella22_test_fold1), [`istella22_test_fold2`](https://huggingface.co/datasets/irds/istella22_test_fold2), [`istella22_test_fold3`](https://huggingface.co/datasets/irds/istella22_test_fold3), [`istella22_test_fold4`](https://huggingface.co/datasets/irds/istella22_test_fold4), [`istella22_test_fold5`](https://huggingface.co/datasets/irds/istella22_test_fold5)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/istella22', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'url': ..., 'text': ..., 'extra_text': ..., 'lang': ..., 'lang_pct': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Dato2022Istella,
  title={The Istella22 Dataset: Bridging Traditional and Neural Learning to Rank Evaluation},
  author={Domenico Dato, Sean MacAvaney, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto},
  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  year={2022}
}
```
