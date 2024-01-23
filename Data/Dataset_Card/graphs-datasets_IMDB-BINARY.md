---
license: unknown
task_categories:
- graph-ml
---

# Dataset Card for IMDB-BINARY (IMDb-B)

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

- **[Homepage](https://dl.acm.org/doi/10.1145/2783258.2783417)**
- **[Repository](https://www.chrsmrrs.com/graphkerneldatasets/IMDB-BINARY.zip):**: 
- **Paper:**: Deep Graph Kernels (see citation) 
- **Leaderboard:**: [Papers with code leaderboard](https://paperswithcode.com/sota/graph-classification-on-imdb-b)

### Dataset Summary

The `IMDb-B` dataset is "a movie collaboration dataset that consists of the ego-networks of 1,000 actors/actresses who played roles in movies in IMDB. In each graph, nodes represent actors/actress, and there is an edge between them if they appear in the same movie. These graphs are derived from the Action and Romance genres". 

### Supported Tasks and Leaderboards

`IMDb-B` should be used for graph classification (aiming to predict whether a movie graph is an action or romance movie), a binary classification task. The score used is accuracy, using a 10-fold cross-validation.


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

### Data Properties

| property | value |
|---|---|
| scale | medium |
| #graphs | 1000 |
| average #nodes | 19.79 |
| average #edges | 193.25 |

### Data Fields

Each row of a given file is a graph, with: 
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `y` (list: 1 x #labels): contains the number of labels available to predict (here 1, equal to zero or one)
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data comes from the PyGeometric version of the dataset.
This information can be found back using
```python
from torch_geometric.datasets import TUDataset
cur_dataset = TUDataset(root="../dataset/loaded/", 
                               name="IMDB-BINARY")
```

## Additional Information

### Licensing Information
The dataset has been released under unknown license, please open an issue if you have this information.

### Citation Information
```
@inproceedings{10.1145/2783258.2783417,
author = {Yanardag, Pinar and Vishwanathan, S.V.N.},
title = {Deep Graph Kernels},
year = {2015},
isbn = {9781450336642},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2783258.2783417},
doi = {10.1145/2783258.2783417},
abstract = {In this paper, we present Deep Graph Kernels, a unified framework to learn latent representations of sub-structures for graphs, inspired by latest advancements in language modeling and deep learning. Our framework leverages the dependency information between sub-structures by learning their latent representations. We demonstrate instances of our framework on three popular graph kernels, namely Graphlet kernels, Weisfeiler-Lehman subtree kernels, and Shortest-Path graph kernels. Our experiments on several benchmark datasets show that Deep Graph Kernels achieve significant improvements in classification accuracy over state-of-the-art graph kernels.},
booktitle = {Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
pages = {1365–1374},
numpages = {10},
keywords = {collaboration networks, bioinformatics, r-convolution kernels, graph kernels, structured data, deep learning, social networks, string kernels},
location = {Sydney, NSW, Australia},
series = {KDD '15}
}
```

### Contributions

Thanks to [@clefourrier](https://github.com/clefourrier) for adding this dataset.