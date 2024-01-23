---
pretty_name: '`beir/hotpotqa/train`'
viewer: false
source_datasets: ['irds/beir_hotpotqa']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/hotpotqa/train`

The `beir/hotpotqa/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/hotpotqa/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=85,000
 - `qrels`: (relevance assessments); count=170,000

 - For `docs`, use [`irds/beir_hotpotqa`](https://huggingface.co/datasets/irds/beir_hotpotqa)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_hotpotqa_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_hotpotqa_train', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

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
