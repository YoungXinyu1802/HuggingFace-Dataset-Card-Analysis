---
pretty_name: '`clueweb12/touche-2022-task-2/expanded-doc-t5-query`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12/touche-2022-task-2/expanded-doc-t5-query`

The `clueweb12/touche-2022-task-2/expanded-doc-t5-query` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12/touche-2022-task-2/expanded-doc-t5-query).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=868,655


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clueweb12_touche-2022-task-2_expanded-doc-t5-query', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'chatnoir_url': ...}

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
