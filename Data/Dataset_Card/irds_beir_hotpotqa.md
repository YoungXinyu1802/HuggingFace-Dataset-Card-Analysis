---
pretty_name: '`beir/hotpotqa`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/hotpotqa`

The `beir/hotpotqa` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/hotpotqa).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=5,233,329
 - `queries` (i.e., topics); count=97,852


This dataset is used by: [`beir_hotpotqa_dev`](https://huggingface.co/datasets/irds/beir_hotpotqa_dev), [`beir_hotpotqa_test`](https://huggingface.co/datasets/irds/beir_hotpotqa_test), [`beir_hotpotqa_train`](https://huggingface.co/datasets/irds/beir_hotpotqa_train)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_hotpotqa', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ..., 'url': ...}

queries = load_dataset('irds/beir_hotpotqa', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Yang2018Hotpotqa,
    title = "{H}otpot{QA}: A Dataset for Diverse, Explainable Multi-hop Question Answering",
    author = "Yang, Zhilin  and
      Qi, Peng  and
      Zhang, Saizheng  and
      Bengio, Yoshua  and
      Cohen, William  and
      Salakhutdinov, Ruslan  and
      Manning, Christopher D.",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D18-1259",
    doi = "10.18653/v1/D18-1259",
    pages = "2369--2380"
}
@article{Thakur2021Beir,
  title = "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models",
  author = "Thakur, Nandan and Reimers, Nils and Rücklé, Andreas and Srivastava, Abhishek and Gurevych, Iryna", 
  journal= "arXiv preprint arXiv:2104.08663",
  month = "4",
  year = "2021",
  url = "https://arxiv.org/abs/2104.08663",
}
```
