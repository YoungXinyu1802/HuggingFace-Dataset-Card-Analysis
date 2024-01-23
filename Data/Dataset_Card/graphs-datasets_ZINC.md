---
license: unknown
dataset_info:
  features:
  - name: node_feat
    sequence:
      sequence: int64
  - name: edge_index
    sequence:
      sequence: int64
  - name: edge_attr
    sequence:
      sequence: int64
  - name: 'y'
    sequence: float64
  - name: num_nodes
    dtype: int64
  splits:
  - name: train
    num_bytes: 376796456
    num_examples: 220011
  - name: test
    num_bytes: 8538528
    num_examples: 5000
  - name: validation
    num_bytes: 41819628
    num_examples: 24445
  download_size: 20636253
  dataset_size: 427154612
task_categories:
- graph-ml
---

# Dataset Card for ZINC

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

- **[Homepage](https://zinc15.docking.org/)**
- **[Repository](https://www.dropbox.com/s/feo9qle74kg48gy/molecules.zip?dl=1):**: 
- **Paper:**: ZINC 15 – Ligand Discovery for Everyone (see citation) 
- **Leaderboard:**: [Papers with code leaderboard](https://paperswithcode.com/sota/)

### Dataset Summary

The `ZINC` dataset is a "curated collection of commercially available chemical compounds prepared especially for virtual screening" (Wikipedia). 

### Supported Tasks and Leaderboards

`ZINC` should be used for molecular property prediction (aiming to predict the constrained solubility of the molecules), a graph regression task. The score used is the MAE.

The associated leaderboard is here: [Papers with code leaderboard](https://paperswithcode.com/sota/graph-regression-on-zinc).

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
| #graphs | 220011 |
| average #nodes | 23.15 |
| average #edges | 49.81 |

### Data Fields

Each row of a given file is a graph, with: 
- `node_feat` (list: #nodes x #node-features): nodes
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_attr` (list: #edges x #edge-features): for the aforementioned edges, contains their features
- `y` (list: 1 x #labels): contains the number of labels available to predict (here 1, equal to zero or one)
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data comes from the PyGeometric version of the dataset, and follows the provided data splits.
This information can be found back using
```python
from torch_geometric.datasets import ZINC

dataset = ZINC(root = '', split='train') # valid, test
```

## Additional Information

### Licensing Information
The dataset has been released under unknown license. Please open an issue if you know what is the license of this dataset.

### Citation Information
```bibtex
@article{doi:10.1021/acs.jcim.5b00559,
  author = {Sterling, Teague and Irwin, John J.},
  title = {ZINC 15 – Ligand Discovery for Everyone},
  journal = {Journal of Chemical Information and Modeling},
  volume = {55},
  number = {11},
  pages = {2324-2337},
  year = {2015},
  doi = {10.1021/acs.jcim.5b00559},
      note ={PMID: 26479676},
  
  URL = { 
          https://doi.org/10.1021/acs.jcim.5b00559
      
  },
  eprint = { 
          https://doi.org/10.1021/acs.jcim.5b00559
      
  }
  
}


```

### Contributions

Thanks to [@clefourrier](https://github.com/clefourrier) for adding this dataset.