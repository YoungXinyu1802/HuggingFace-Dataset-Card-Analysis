---
pretty_name: '`cord19/trec-covid/round5`'
viewer: false
source_datasets: ['irds/cord19', 'irds/cord19_trec-covid']
task_categories:
- text-retrieval
---

# Dataset Card for `cord19/trec-covid/round5`

The `cord19/trec-covid/round5` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/cord19#cord19/trec-covid/round5).

# Data

This dataset provides:
 - `qrels`: (relevance assessments); count=23,151

 - For `docs`, use [`irds/cord19`](https://huggingface.co/datasets/irds/cord19)
 - For `queries`, use [`irds/cord19_trec-covid`](https://huggingface.co/datasets/irds/cord19_trec-covid)

## Usage

```python
from datasets import load_dataset

qrels = load_dataset('irds/cord19_trec-covid_round5', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Voorhees2020TrecCovid,
  title={TREC-COVID: Constructing a Pandemic Information Retrieval Test Collection},
  author={E. Voorhees and Tasmeer Alam and Steven Bedrick and Dina Demner-Fushman and W. Hersh and Kyle Lo and Kirk Roberts and I. Soboroff and Lucy Lu Wang},
  journal={ArXiv},
  year={2020},
  volume={abs/2005.04474}
}
@article{Wang2020Cord19,
  title={CORD-19: The Covid-19 Open Research Dataset},
  author={Lucy Lu Wang and Kyle Lo and Yoganand Chandrasekhar and Russell Reas and Jiangjiang Yang and Darrin Eide and K. Funk and Rodney Michael Kinney and Ziyang Liu and W. Merrill and P. Mooney and D. Murdick and Devvret Rishi and Jerry Sheehan and Zhihong Shen and B. Stilson and A. Wade and K. Wang and Christopher Wilhelm and Boya Xie and D. Raymond and Daniel S. Weld and Oren Etzioni and Sebastian Kohlmeier},
  journal={ArXiv},
  year={2020}
}
```
