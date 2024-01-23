---
pretty_name: '`touche-image/2022-06-13/touche-2022-task-3`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `touche-image/2022-06-13/touche-2022-task-3`

The `touche-image/2022-06-13/touche-2022-task-3` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/touche-image#touche-image/2022-06-13/touche-2022-task-3).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=19,821


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/touche-image_2022-06-13_touche-2022-task-3', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/touche-image_2022-06-13_touche-2022-task-3', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

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
@inproceedings{Kiesel2021Image,
  author = {Johannes Kiesel and Nico Reichenbach and Benno Stein and Martin Potthast},
  booktitle = {8th Workshop on Argument Mining (ArgMining 2021) at EMNLP},
  doi = {10.18653/v1/2021.argmining-1.4},
  editor = {Khalid Al-Khatib and Yufang Hou and Manfred Stede},
  month = nov,
  pages = {36-45},
  publisher = {Association for Computational Linguistics},
  site = {Punta Cana, Dominican Republic},
  title = {{Image Retrieval for Arguments Using Stance-Aware Query Expansion}},
  url = {https://aclanthology.org/2021.argmining-1.4/},
  year = 2021
}
@inproceedings{Dimitrov2021SemEval,
  author = {Dimitar Dimitrov and Bishr Bin Ali and Shaden Shaar and Firoj Alam and Fabrizio Silvestri and Hamed Firooz and Preslav Nakov and Giovanni Da San Martino},
  editor = {Alexis Palmer and Nathan Schneider and Natalie Schluter and Guy Emerson and Aur{\'{e}}lie Herbelot and Xiaodan Zhu},
  title = {SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images},
  booktitle = {Proceedings of the 15th International Workshop on Semantic Evaluation, SemEval@ACL/IJCNLP 2021, Virtual Event / Bangkok, Thailand, August 5-6, 2021},
  pages = {70--98},
  publisher = {Association for Computational Linguistics},
  year = {2021},
  doi = {10.18653/v1/2021.semeval-1.7},
}
@inproceedings{Yanai2007Image,
  author = {Keiji Yanai},
  editor = {Carey L. Williamson and Mary Ellen Zurko and Peter F. Patel{-}Schneider and Prashant J. Shenoy},
  title = {Image collector {III:} a web image-gathering system with bag-of-keypoints},
  booktitle = {Proceedings of the 16th International Conference on World Wide Web, {WWW} 2007, Banff, Alberta, Canada, May 8-12, 2007},
  pages = {1295--1296},
  publisher = {{ACM}},
  year = {2007},
  doi = {10.1145/1242572.1242816},
}
```
