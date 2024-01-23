---
licence: mit
task_categories:
- graph-ml
---

# Dataset Card for alchemy

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
- **[Homepage](https://alchemy.tencent.com/)**
- **Paper:**:  (see citation)
- **Leaderboard:**: [Leaderboard](https://alchemy.tencent.com/)

### Dataset Summary
The `alchemy` dataset is a molecular dataset, called Alchemy, which lists 12 quantum mechanical properties of 130,000+ organic molecules comprising up to 12 heavy atoms (C, N, O, S, F and Cl), sampled from the GDBMedChem database.

 ### Supported Tasks and Leaderboards
`alchemy` should be used for organic quantum molecular property prediction, a regression task on 12 properties. The score used is MAE.


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
| scale | big |
| #graphs | 202578 |
| average #nodes | 10.101387606810183 |
| average #edges | 20.877326870011206 |

### Data Fields

Each row of a given file is a graph, with: 
- `node_feat` (list: #nodes x #node-features): nodes
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_attr` (list: #edges x #edge-features): for the aforementioned edges, contains their features
- `y` (list: 1 x #labels): contains the number of labels available to predict (here 1, equal to zero or one)
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data is not split, and should be used with cross validation. It comes from the PyGeometric version of the dataset.

## Additional Information

### Licensing Information
The dataset has been released under license mit.

### Citation Information
```
@inproceedings{Morris+2020,
    title={TUDataset: A collection of benchmark datasets for learning with graphs},
    author={Christopher Morris and Nils M. Kriege and Franka Bause and Kristian Kersting and Petra Mutzel and Marion Neumann},
    booktitle={ICML 2020 Workshop on Graph Representation Learning and Beyond (GRL+ 2020)},
    archivePrefix={arXiv},
    eprint={2007.08663},
    url={www.graphlearning.io},
    year={2020}
}
```

```

@article{DBLP:journals/corr/abs-1906-09427,
  author    = {Guangyong Chen and
               Pengfei Chen and
               Chang{-}Yu Hsieh and
               Chee{-}Kong Lee and
               Benben Liao and
               Renjie Liao and
               Weiwen Liu and
               Jiezhong Qiu and
               Qiming Sun and
               Jie Tang and
               Richard S. Zemel and
               Shengyu Zhang},
  title     = {Alchemy: {A} Quantum Chemistry Dataset for Benchmarking {AI} Models},
  journal   = {CoRR},
  volume    = {abs/1906.09427},
  year      = {2019},
  url       = {http://arxiv.org/abs/1906.09427},
  eprinttype = {arXiv},
  eprint    = {1906.09427},
  timestamp = {Mon, 11 Nov 2019 12:55:11 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1906-09427.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}


```