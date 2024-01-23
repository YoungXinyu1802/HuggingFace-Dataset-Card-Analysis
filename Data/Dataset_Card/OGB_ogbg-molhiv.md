---
license: mit
task_categories:
- graph-ml
---

# Dataset Card for ogbg-molhiv

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

- **[Homepage](https://ogb.stanford.edu/docs/graphprop/#ogbg-mol)**
- **[Repository](https://github.com/snap-stanford/ogb):**: 
- **Paper:**: Open Graph Benchmark: Datasets for Machine Learning on Graphs (see citation) 
- **Leaderboard:**: [OGB leaderboard](https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-molhiv) and [Papers with code leaderboard](https://paperswithcode.com/sota/graph-property-prediction-on-ogbg-molhiv)

### Dataset Summary

The `ogbg-molhiv` dataset is a small molecular property prediction dataset, adapted from MoleculeNet by teams at Stanford, to be a part of the Open Graph Benchmark. 

### Supported Tasks and Leaderboards

`ogbg-molhiv` should be used for molecular property prediction (aiming to predict whether molecules inhibit HIV or not), a binary classification task. The score used is ROC-AUC.

The associated leaderboards are here: [OGB leaderboard](https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-molhiv) and [Papers with code leaderboard](https://paperswithcode.com/sota/graph-property-prediction-on-ogbg-molhiv).

## External Use
### PyGeometric
To load in PyGeometric, do the following:

```python
from datasets import load_dataset

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

ogbg_molhiv = load_dataset("graphs-datasets/ogbg-molhiv")
# For the train set (replace by valid or test as needed)
ogbg_molhiv_pg_list = [Data(graph) for graph in ogbg_molhiv["train"]]
ogbg_molhiv_pg = DataLoader(ogbg_molhiv_pg_list)

```


## Dataset Structure

### Data Properties

| property | value |
|---|---|
| scale | small |
| #graphs | 41,127 |
| average #nodes | 25.5 |
| average #edges | 27.5 |
| average node degree | 2.2 | 
| average cluster coefficient | 0.002 | 
| MaxSCC ratio | 0.993 |
| graph diameter | 12.0 |

### Data Fields

Each row of a given file is a graph, with: 
- `node_feat` (list: #nodes x #node-features): nodes
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_attr` (list: #edges x #edge-features): for the aforementioned edges, contains their features
- `y` (list: 1 x #labels): contains the number of labels available to predict (here 1, equal to zero or one)
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data comes from the PyGeometric version of the dataset provided by OGB, and follows the provided data splits.
This information can be found back using
```python
from ogb.graphproppred import PygGraphPropPredDataset

dataset = PygGraphPropPredDataset(name = 'ogbg-molhiv')

split_idx = dataset.get_idx_split() 
train = dataset[split_idx['train']] # valid, test
```

## Additional Information

### Licensing Information
The dataset has been released under MIT license.

### Citation Information
```
@inproceedings{hu-etal-2020-open,
  author    = {Weihua Hu and
               Matthias Fey and
               Marinka Zitnik and
               Yuxiao Dong and
               Hongyu Ren and
               Bowen Liu and
               Michele Catasta and
               Jure Leskovec},
  editor    = {Hugo Larochelle and
               Marc Aurelio Ranzato and
               Raia Hadsell and
               Maria{-}Florina Balcan and
               Hsuan{-}Tien Lin},
  title     = {Open Graph Benchmark: Datasets for Machine Learning on Graphs},
  booktitle = {Advances in Neural Information Processing Systems 33: Annual Conference
               on Neural Information Processing Systems 2020, NeurIPS 2020, December
               6-12, 2020, virtual},
  year      = {2020},
  url       = {https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html},
}
```

### Contributions

Thanks to [@clefourrier](https://github.com/clefourrier) for adding this dataset.