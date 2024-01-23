---
pretty_name: '`argsme/1.0/touche-2020-task-1/uncorrected`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `argsme/1.0/touche-2020-task-1/uncorrected`

The `argsme/1.0/touche-2020-task-1/uncorrected` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/argsme#argsme/1.0/touche-2020-task-1/uncorrected).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=49
 - `qrels`: (relevance assessments); count=2,964


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/argsme_1.0_touche-2020-task-1_uncorrected', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/argsme_1.0_touche-2020-task-1_uncorrected', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Bondarenko2020Touche,
  address = {Berlin Heidelberg New York},
  author = {Alexander Bondarenko and Maik Fr{\"o}be and Meriem Beloucif and Lukas Gienapp and Yamen Ajjour and Alexander Panchenko and Chris Biemann and Benno Stein and Henning Wachsmuth and Martin Potthast and Matthias Hagen},
  booktitle = {Experimental IR Meets Multilinguality, Multimodality, and Interaction. 11th International Conference of the CLEF Association (CLEF 2020)},
  doi = {10.1007/978-3-030-58219-7\_26},
  editor = {Avi Arampatzis and Evangelos Kanoulas and Theodora Tsikrika and Stefanos Vrochidis and Hideo Joho and Christina Lioma and Carsten Eickhoff and Aur{\'e}lie N{\'e}v{\'e}ol and Linda Cappellato and Nicola Ferro},
  month = sep,
  pages = {384-395},
  publisher = {Springer},
  series = {Lecture Notes in Computer Science},
  site = {Thessaloniki, Greece},
  title = {{Overview of Touch{\'e} 2020: Argument Retrieval}},
  url = {https://link.springer.com/chapter/10.1007/978-3-030-58219-7_26},
  volume = 12260,
  year = 2020,
}
@inproceedings{Wachsmuth2017Quality,
  author = {Henning Wachsmuth and Nona Naderi and Yufang Hou and Yonatan Bilu and Vinodkumar Prabhakaran and Tim Alberdingk Thijm and Graeme Hirst and Benno Stein},
  booktitle = {15th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2017)},
  editor = {Phil Blunsom and Alexander Koller and Mirella Lapata},
  month = apr,
  pages = {176-187},
  site = {Valencia, Spain},
  title = {{Computational Argumentation Quality Assessment in Natural Language}},
  url = {http://aclweb.org/anthology/E17-1017},
  year = 2017
}
```
