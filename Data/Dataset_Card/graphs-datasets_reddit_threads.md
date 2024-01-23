---
license: gpl-3.0
task_categories:
- graph-ml
---

# Dataset Card for Reddit threads

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [External Use](#external-use)
  - [PyGeometric](#pygeometric)
- [Dataset Structure](#dataset-structure)
  - [Data Properties](#data-properties)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description
- **[Homepage](https://snap.stanford.edu/data/reddit_threads.html)**
- **Paper:**:  (see citation)


### Dataset Summary
The `Reddit threads` dataset contains 'discussion and non-discussion based threads from Reddit which we collected in May 2018. Nodes are Reddit users who participate in a discussion and links are replies between them' (doc).

### Supported Tasks and Leaderboards
The related task is the binary classification to predict whether a thread is discussion based or not.

## External Use
### PyGeometric
To load in PyGeometric, do the following:

```python
from datasets import load_dataset

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

dataset_hf = load_dataset("graphs-datasets/<mydataset>")
# For the train set (replace by valid or test as needed)
dataset_pg_list = [Data(graph) for graph in dataset_hf["train"]]
dataset_pg = DataLoader(dataset_pg_list)
```

## Dataset Structure
### Dataset information
- 203,088 graphs

### Data Fields

Each row of a given file is a graph, with: 
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `y` (list:  #labels): contains the number of labels available to predict
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data is not split, and should be used with cross validation. It comes from the PyGeometric version of the dataset.

## Additional Information

### Licensing Information
The dataset has been released under GPL-3.0 license.

### Citation Information
See also [github](https://github.com/benedekrozemberczki/karateclub).

```
 @inproceedings{karateclub,
    title = {{Karate Club: An API Oriented Open-source Python Framework for Unsupervised Learning on Graphs}},
    author = {Benedek Rozemberczki and Oliver Kiss and Rik Sarkar},
    year = {2020},
    pages = {3125–3132},
    booktitle = {Proceedings of the 29th ACM International Conference on Information and Knowledge Management (CIKM '20)},
    organization = {ACM},
}
```