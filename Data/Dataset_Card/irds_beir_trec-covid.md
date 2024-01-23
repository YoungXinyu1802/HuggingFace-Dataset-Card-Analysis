---
pretty_name: '`beir/trec-covid`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/trec-covid`

The `beir/trec-covid` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/trec-covid).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=171,332
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=66,336


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_trec-covid', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ..., 'url': ..., 'pubmed_id': ...}

queries = load_dataset('irds/beir_trec-covid', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ..., 'query': ..., 'narrative': ...}

qrels = load_dataset('irds/beir_trec-covid', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Wang2020Cord19,
  title={CORD-19: The Covid-19 Open Research Dataset},
  author={Lucy Lu Wang and Kyle Lo and Yoganand Chandrasekhar and Russell Reas and Jiangjiang Yang and Darrin Eide and K. Funk and Rodney Michael Kinney and Ziyang Liu and W. Merrill and P. Mooney and D. Murdick and Devvret Rishi and Jerry Sheehan and Zhihong Shen and B. Stilson and A. Wade and K. Wang and Christopher Wilhelm and Boya Xie and D. Raymond and Daniel S. Weld and Oren Etzioni and Sebastian Kohlmeier},
  journal={ArXiv},
  year={2020}
}
@article{Voorhees2020TrecCovid,
  title={TREC-COVID: Constructing a Pandemic Information Retrieval Test Collection},
  author={E. Voorhees and Tasmeer Alam and Steven Bedrick and Dina Demner-Fushman and W. Hersh and Kyle Lo and Kirk Roberts and I. Soboroff and Lucy Lu Wang},
  journal={ArXiv},
  year={2020},
  volume={abs/2005.04474}
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
