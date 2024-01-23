---
pretty_name: '`clueweb12/touche-2020-task-2`'
viewer: false
source_datasets: ['irds/clueweb12']
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12/touche-2020-task-2`

The `clueweb12/touche-2020-task-2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12/touche-2020-task-2).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=1,783

 - For `docs`, use [`irds/clueweb12`](https://huggingface.co/datasets/irds/clueweb12)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clueweb12_touche-2020-task-2', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/clueweb12_touche-2020-task-2', 'qrels')
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
@inproceedings{Braunstain2016Support,
  author = {Liora Braunstain and Oren Kurland and David Carmel and Idan Szpektor and Anna Shtok},
  editor = {Nicola Ferro and Fabio Crestani and Marie{-}Francine Moens and Josiane Mothe and Fabrizio Silvestri and Giorgio Maria Di Nunzio and Claudia Hauff and Gianmaria Silvello},
  title = {Supporting Human Answers for Advice-Seeking Questions in {CQA} Sites},
  booktitle = {Advances in Information Retrieval - 38th European Conference on {IR} Research, {ECIR} 2016, Padua, Italy, March 20-23, 2016. Proceedings},
  series = {Lecture Notes in Computer Science},
  volume = {9626},
  pages = {129--141},
  publisher = {Springer},
  year = {2016},
  doi = {10.1007/978-3-319-30671-1\_10},
}
@inproceedings{Rafalak2014Credibility,
  author    = {Maria Rafalak and Katarzyna Abramczuk and Adam Wierzbicki},
  editor = {Chin{-}Wan Chung and Andrei Z. Broder and Kyuseok Shim and Torsten Suel},
  title = {Incredible: is (almost) all web content trustworthy? analysis of psychological factors related to website credibility evaluation},
  booktitle = {23rd International World Wide Web Conference, {WWW} '14, Seoul, Republic of Korea, April 7-11, 2014, Companion Volume},
  pages = {1117--1122},
  publisher = {{ACM}},
  year = {2014},
  doi = {10.1145/2567948.2578997},
}
```
