---
pretty_name: '`clueweb12/b13/clef-ehealth/sv`'
viewer: false
source_datasets: ['irds/clueweb12_b13']
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12/b13/clef-ehealth/sv`

The `clueweb12/b13/clef-ehealth/sv` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12/b13/clef-ehealth/sv).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=300
 - `qrels`: (relevance assessments); count=269,232

 - For `docs`, use [`irds/clueweb12_b13`](https://huggingface.co/datasets/irds/clueweb12_b13)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clueweb12_b13_clef-ehealth_sv', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/clueweb12_b13_clef-ehealth_sv', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'trustworthiness': ..., 'understandability': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Zuccon2016ClefEhealth,
  title={The IR Task at the CLEF eHealth Evaluation Lab 2016: User-centred Health Information Retrieval},
  author={Guido Zuccon and Joao Palotti and Lorraine Goeuriot and Liadh Kelly and Mihai Lupu and Pavel Pecina and Henning M{\"u}ller and Julie Budaher and Anthony Deacon},
  booktitle={CLEF},
  year={2016}
}
@inproceedings{Palotti2017ClefEhealth,
  title={CLEF 2017 Task Overview: The IR Task at the eHealth Evaluation Lab - Evaluating Retrieval Methods for Consumer Health Search},
  author={Joao Palotti and Guido Zuccon and Jimmy and Pavel Pecina and Mihai Lupu and Lorraine Goeuriot and Liadh Kelly and Allan Hanbury},
  booktitle={CLEF},
  year={2017}
}
```
