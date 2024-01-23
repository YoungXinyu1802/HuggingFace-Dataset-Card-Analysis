---
license: unknown
task_categories:
- graph-ml
---

# Dataset Card for PROTEINS

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

- **[Homepage](https://academic.oup.com/bioinformatics/article/21/suppl_1/i47/202991)**
- **[Repository](https://www.chrsmrrs.com/graphkerneldatasets/PROTEINS.zip):**: 
- **Paper:**:  Protein function prediction via graph kernels (see citation) 
- **Leaderboard:**: [Papers with code leaderboard](https://paperswithcode.com/sota/graph-classification-on-proteins)

### Dataset Summary

The `PROTEINS` dataset is a medium molecular property prediction dataset. 

### Supported Tasks and Leaderboards

`PROTEINS` should be used for molecular property prediction (aiming to predict whether molecules are enzymes or not), a binary classification task. The score used is accuracy, using a 10-fold cross-validation.

## External Use
### PyGeometric
To load in PyGeometric, do the following:

```python
from datasets import load_dataset

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

dataset_hf = load_dataset("graphs-datasets/<mydataset>")
dataset_pg_list = [Data(graph) for graph in dataset_hf["train"]]
dataset_pg = DataLoader(dataset_pg_list)

```


## Dataset Structure

### Data Properties

| property | value |
|---|---|
| scale | medium |
| #graphs | 1113 |
| average #nodes | 39.06 |
| average #edges | 72.82 |

### Data Fields

Each row of a given file is a graph, with: 
- `node_feat` (list: #nodes x #node-features): nodes
- `edge_index` (list: 2 x #edges): pairs of nodes constituting edges
- `edge_attr` (list: #edges x #edge-features): for the aforementioned edges, contains their features
- `y` (list: 1 x #labels): contains the number of labels available to predict (here 1, equal to zero or one)
- `num_nodes` (int): number of nodes of the graph

### Data Splits

This data comes from the PyGeometric version of the dataset provided by TUDataset.
This information can be found back using
```python
from torch_geometric.datasets import TUDataset

dataset = TUDataset(root='', name = 'PROTEINS')
```

## Additional Information

### Licensing Information
The dataset has been released under unknown license, please open an issue if you have info about it.

### Citation Information
```
@article{10.1093/bioinformatics/bti1007,
    author = {Borgwardt, Karsten M. and Ong, Cheng Soon and Schönauer, Stefan and Vishwanathan, S. V. N. and Smola, Alex J. and Kriegel, Hans-Peter},
    title = "{Protein function prediction via graph kernels}",
    journal = {Bioinformatics},
    volume = {21},
    number = {suppl_1},
    pages = {i47-i56},
    year = {2005},
    month = {06},
    abstract = "{Motivation: Computational approaches to protein function prediction infer protein function by finding proteins with similar sequence, structure, surface clefts, chemical properties, amino acid motifs, interaction partners or phylogenetic profiles. We present a new approach that combines sequential, structural and chemical information into one graph model of proteins. We predict functional class membership of enzymes and non-enzymes using graph kernels and support vector machine classification on these protein graphs.Results: Our graph model, derivable from protein sequence and structure only, is competitive with vector models that require additional protein information, such as the size of surface pockets. If we include this extra information into our graph model, our classifier yields significantly higher accuracy levels than the vector models. Hyperkernels allow us to select and to optimally combine the most relevant node attributes in our protein graphs. We have laid the foundation for a protein function prediction system that integrates protein information from various sources efficiently and effectively.Availability: More information available via www.dbs.ifi.lmu.de/Mitarbeiter/borgwardt.html.Contact:borgwardt@dbs.ifi.lmu.de}",
    issn = {1367-4803},
    doi = {10.1093/bioinformatics/bti1007},
    url = {https://doi.org/10.1093/bioinformatics/bti1007},
    eprint = {https://academic.oup.com/bioinformatics/article-pdf/21/suppl\_1/i47/524364/bti1007.pdf},
}



```

### Contributions

Thanks to [@clefourrier](https://github.com/clefourrier) for adding this dataset.