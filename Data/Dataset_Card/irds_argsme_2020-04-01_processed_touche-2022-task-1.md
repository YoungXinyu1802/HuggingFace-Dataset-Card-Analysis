---
pretty_name: '`argsme/2020-04-01/processed/touche-2022-task-1`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `argsme/2020-04-01/processed/touche-2022-task-1`

The `argsme/2020-04-01/processed/touche-2022-task-1` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/argsme#argsme/2020-04-01/processed/touche-2022-task-1).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=6,841


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/argsme_2020-04-01_processed_touche-2022-task-1', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/argsme_2020-04-01_processed_touche-2022-task-1', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'quality': ..., 'coherence': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Bondarenko2022Touche,
  address = {Berlin Heidelberg New York},
  author = {Alexander Bondarenko and Maik Fr{\"o}be and Johannes Kiesel and Shahbaz Syed and Timon Gurcke and Meriem Beloucif and Alexander Panchenko and Chris Biemann and Benno Stein and Henning Wachsmuth and Martin Potthast and Matthias Hagen},
  booktitle = {Experimental IR Meets Multilinguality, Multimodality, and Interaction. 13th International Conference of the CLEF Association (CLEF 2022)},
  editor = {Alberto Barr{\'o}n-Cede{\~n}o and Giovanni Da San Martino and Mirko Degli Esposti and Fabrizio Sebastiani and Craig Macdonald and Gabriella Pasi and Allan Hanbury and Martin Potthast and Guglielmo Faggioli and Nicola Ferro},
  month = sep,
  numpages = 29,
  publisher = {Springer},
  series = {Lecture Notes in Computer Science},
  site = {Bologna, Italy},
  title = {{Overview of Touch{\'e} 2022: Argument Retrieval}},
  year = 2022
}
```
