---
license: mit
task_categories:
- graph-ml
---

# Dataset Card for ogbg-code2

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

- **[Homepage](https://ogb.stanford.edu/docs/graphprop/#ogbg-code2)**
- **[Repository](https://github.com/snap-stanford/ogb):**: 
- **Paper:**: Open Graph Benchmark: Datasets for Machine Learning on Graphs (see citation) 
- **Leaderboard:**: [OGB leaderboard](https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-code2) and [Papers with code leaderboard](https://paperswithcode.com/sota/graph-property-prediction-on-ogbg-code2)

### Dataset Summary

The `ogbg-code2` dataset contains Abstract Syntax Trees (ASTs) obtained from 450 thousands Python method definitions, from GitHub CodeSearchNet. "Methods are extracted from a total of 13,587 different repositories across the most popular projects on GitHub.", by teams at Stanford, to be a part of the Open Graph Benchmark. See their website or paper for dataset postprocessing.

### Supported Tasks and Leaderboards

"The task is to predict the sub-tokens forming the method name, given the Python method body represented by AST and its node features. This task is often referred to as “code summarization”, because the model is trained to find succinct and precise description for a complete logical unit." 

The score is the F1 score of sub-token prediction. 

## External Use
### PyGeometric
To load in PyGeometric, do the following:

```python
from datasets import load_dataset

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

graphs_dataset = load_dataset("graphs-datasets/ogbg-code2)
# For the train set (replace by valid or test as needed)
graphs_list = [Data(graph) for graph in graphs_dataset["train"]]
graphs_pygeometric = DataLoader(graph_list)

```


## Dataset Structure

### Data Properties

| property | value |
|---|---|
| scale | medium |
| #graphs | 452,741 |
| average #nodes | 125.2 |
| average #edges | 124.2 |
| average node degree | 2.0 | 
| average cluster coefficient | 0.0 | 
| MaxSCC ratio | 1.000 |
| graph diameter | 13.5 |

### Data Fields

Each row of a given file is a graph, with: 
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_feat` (list: #edges x #edge-features): features of edges
- `node_feat` (list: #nodes x #node-features): the nodes features, embedded
- `node_feat_expanded` (list: #nodes x #node-features): the nodes features, as code
- `node_is_attributed` (list: 1 x #nodes): ?
- `node_dfs_order` (list: #nodes x #1): the nodes order in the abstract tree, if parsed using a depth first search
- `node_depth` (list: #nodes x #1): the nodes depth in the abstract tree
- `y` (list: 1 x #tokens): contains the tokens to predict as method name
- `num_nodes` (int): number of nodes of the graph
- `ptr` (list: 2): index of first and last node of the graph
- `batch` (list: 1 x #nodes): ?

### Data Splits

This data comes from the PyGeometric version of the dataset provided by OGB, and follows the provided data splits.
This information can be found back using
```python
from ogb.graphproppred import PygGraphPropPredDataset

dataset = PygGraphPropPredDataset(name = 'ogbg-code2')

split_idx = dataset.get_idx_split() 
train = dataset[split_idx['train']] # valid, test
```

More information (`node_feat_expanded`) has been added through the typeidx2type and attridx2attr csv files of the repo.

## Additional Information

### Licensing Information
The dataset has been released under MIT license license.

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