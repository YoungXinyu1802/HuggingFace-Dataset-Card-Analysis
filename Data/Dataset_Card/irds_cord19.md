---
pretty_name: '`cord19`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `cord19`

The `cord19` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/cord19#cord19).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=192,509


This dataset is used by: [`cord19_trec-covid`](https://huggingface.co/datasets/irds/cord19_trec-covid), [`cord19_trec-covid_round5`](https://huggingface.co/datasets/irds/cord19_trec-covid_round5)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/cord19', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'doi': ..., 'date': ..., 'abstract': ...}

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
```
