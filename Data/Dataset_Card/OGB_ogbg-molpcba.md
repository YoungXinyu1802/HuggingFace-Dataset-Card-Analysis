---
license: mit
task_categories:
- graph-ml
---

# Dataset Card for ogbg-molpcba

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

- **Homepage:** [Homepage](https://ogb.stanford.edu/docs/graphprop/#ogbg-mol)
- **Repository:** [Repo](https://github.com/snap-stanford/ogb)  
- **Paper:**: Open Graph Benchmark: Datasets for Machine Learning on Graphs 
- **Leaderboard:**: [OGB leaderboard](https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-molpcba) and [Papers with code leaderboard](https://paperswithcode.com/sota/graph-property-prediction-on-ogbg-molpcba)

### Dataset Summary

The `ogbg-molpcba` dataset is a small molecular property prediction dataset, adapted from MoleculeNet by teams at Stanford, to be a part of the Open Graph Benchmark. 

### Supported Tasks and Leaderboards

`ogbg-molpcba` should be used for molecular property prediction (with 128 properties to predict, not all present for all graphs), a binary classification task.
The score used is Average Precision (AP) averaged over the tasks.

The associated leaderboards are here: [OGB leaderboard](https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-molpcba) and [Papers with code leaderboard](https://paperswithcode.com/sota/graph-property-prediction-on-ogbg-molpcba).

## External Use
### PyGeometric
To load in PyGeometric, do the following:

```python
from datasets import load_dataset

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

dataset = load_dataset("graphs-datasets/ogbg-molpcba")
# For the train set (replace by valid or test as needed)
graphs_list_pygeometric = [Data(graph) for graph in dataset["train"]]
dataset_pygeometric = DataLoader(graphs_list_pygeometric)

```


## Dataset Structure

### Data Properties

| property | value |
|---|---|
| scale | medium |
| #graphs | 437,929 |
| average #nodes | 26.0 |
| average #edges | 28.1 |
| average node degree | 2.2 | 
| average cluster coefficient | 0.002 | 
| MaxSCC ratio | 0.999 |
| graph diameter | 13.6 |

### Data Fields

Each row of a given file is a graph, with: 
- `node_feat` (list: #nodes x #node-features): nodes
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_attr` (list: #edges x #edge-features): for the aforementioned edges, contains their features
- `y` (list: 1 x #labels): contains the number of labels available to predict (here 128 labels, equal to zero, one, or Nan if the property is not relevant for the graph)
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data comes from the PyGeometric version of the dataset provided by OGB, and follows the provided data splits.
This information can be found back using
```python
from ogb.graphproppred import PygGraphPropPredDataset

dataset = PygGraphPropPredDataset(name = 'ogbg-molpcba')

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