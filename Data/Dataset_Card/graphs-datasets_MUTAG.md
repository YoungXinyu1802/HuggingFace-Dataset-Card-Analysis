---
license: unknown
task_categories:
- graph-ml
---

# Dataset Card for MUTAG

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

- **[Homepage](https://pubs.acs.org/doi/abs/10.1021/jm00106a046)**
- **[Repository](https://www.chrsmrrs.com/graphkerneldatasets/MUTAG.zip):**: 
- **Paper:**: Structure-activity relationship of mutagenic aromatic and heteroaromatic nitro compounds. Correlation with molecular orbital energies and hydrophobicity (see citation) 
- **Leaderboard:**: [Papers with code leaderboard](https://paperswithcode.com/sota/graph-classification-on-mutag)

### Dataset Summary

The `MUTAG` dataset is 'a collection of nitroaromatic compounds and the goal is to predict their mutagenicity on Salmonella typhimurium'. 

### Supported Tasks and Leaderboards

`MUTAG` should be used for molecular property prediction (aiming to predict whether molecules have a mutagenic effect on a given bacterium or not), a binary classification task. The score used is accuracy, using a 10-fold cross-validation.

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
| scale | small |
| #graphs | 187 |
| average #nodes | 18.03 |
| average #edges | 39.80 |

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
from torch_geometric.datasets import TUDataset

cur_dataset = TUDataset(root="../dataset/loaded/", 
                               name="MUTAG")
 ```

## Additional Information

### Licensing Information
The dataset has been released under unknown license, please open an issue if you have information.

### Citation Information
```
@article{doi:10.1021/jm00106a046,
  author = {Debnath, Asim Kumar and Lopez de Compadre, Rosa L. and Debnath, Gargi and Shusterman, Alan J. and Hansch, Corwin},
  title = {Structure-activity relationship of mutagenic aromatic and heteroaromatic nitro compounds. Correlation with molecular orbital energies and hydrophobicity},
  journal = {Journal of Medicinal Chemistry},
  volume = {34},
  number = {2},
  pages = {786-797},
  year = {1991},
  doi = {10.1021/jm00106a046},
  URL = { 
          https://doi.org/10.1021/jm00106a046
  },
  eprint = { 
          https://doi.org/10.1021/jm00106a046 
  }
  
}
```

### Contributions

Thanks to [@clefourrier](https://github.com/clefourrier) for adding this dataset.