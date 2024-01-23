---
licence: unknown
task_categories:
- graph-ml
---

# Dataset Card for benzene

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
- **[Homepage](http://www.sgdml.org/#datasets)**
- **Paper:**:  (see citation)


### Dataset Summary
The `benzene` dataset is molecular dynamics (MD) dataset. The total energy and force labels for each dataset were computed using the PBE+vdW-TS electronic structure method. All geometries are in Angstrom, energies and forces are given in kcal/mol and kcal/mol/A respectively.

### Supported Tasks and Leaderboards
`benzene` should be used for organic molecular property prediction, a regression task on 1 property. The score used is Mean absolute errors (in meV) for energy prediction.


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
| #graphs | 527983 |
| average #nodes | 12.0 |
| average #edges | 129.8848866632322 |

### Data Fields

Each row of a given file is a graph, with: 
- `node_feat` (list: #nodes x #node-features): nodes
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_attr` (list: #edges x #edge-features): for the aforementioned edges, contains their features
- `y` (list:  #labels): contains the number of labels available to predict
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data is not split, and should be used with cross validation. It comes from the PyGeometric version of the dataset.

## Additional Information

### Licensing Information
The dataset has been released under license unknown.

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

@article{Chmiela_2017,
	doi = {10.1126/sciadv.1603015},
	url = {https://doi.org/10.1126%2Fsciadv.1603015},
	year = 2017,
	month = {may},
	publisher = {American Association for the Advancement of Science ({AAAS})},
	volume = {3},
	number = {5},
	author = {Stefan Chmiela and Alexandre Tkatchenko and Huziel E. Sauceda and Igor Poltavsky and Kristof T. Schütt and Klaus-Robert Müller},
	title = {Machine learning of accurate energy-conserving molecular force fields},
	journal = {Science Advances}
}


```