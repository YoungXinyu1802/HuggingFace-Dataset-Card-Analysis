---
pretty_name: '`clueweb12/touche-2021-task-2`'
viewer: false
source_datasets: ['irds/clueweb12']
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12/touche-2021-task-2`

The `clueweb12/touche-2021-task-2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12/touche-2021-task-2).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=2,076

 - For `docs`, use [`irds/clueweb12`](https://huggingface.co/datasets/irds/clueweb12)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clueweb12_touche-2021-task-2', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/clueweb12_touche-2021-task-2', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'quality': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Bondarenko2021Touche,
  address = {Berlin Heidelberg New York},
  author = {Alexander Bondarenko and Lukas Gienapp and Maik Fr{\"o}be and Meriem Beloucif and Yamen Ajjour and Alexander Panchenko and Chris Biemann and Benno Stein and Henning Wachsmuth and Martin Potthast and Matthias Hagen},
  booktitle = {Experimental IR Meets Multilinguality, Multimodality, and Interaction. 12th International Conference of the CLEF Association (CLEF 2021)},
  doi = {10.1007/978-3-030-85251-1\_28},
  editor = {{K. Sel{\c{c}}uk} Candan and Bogdan Ionescu and Lorraine Goeuriot and Henning M{\"u}ller and Alexis Joly and Maria Maistro and Florina Piroi and Guglielmo Faggioli and Nicola Ferro},
  month = sep,
  pages = {450-467},
  publisher = {Springer},
  series = {Lecture Notes in Computer Science},
  site = {Bucharest, Romania},
  title = {{Overview of Touch{\'e} 2021: Argument Retrieval}},
  url = {https://link.springer.com/chapter/10.1007/978-3-030-85251-1_28},
  volume = 12880,
  year = 2021,
}
```
