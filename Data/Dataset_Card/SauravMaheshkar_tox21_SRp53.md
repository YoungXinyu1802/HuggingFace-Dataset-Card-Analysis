---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
pretty_name: tox21_SRp53
tags:
- bio
- bio-chem
- molnet
- molecule-net
- biophysics
task_categories:
- other
- graph-ml
task_ids: []
---
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
# Dataset Description
- **Homepage: https://moleculenet.org/**
- **Repository: https://github.com/deepchem/deepchem/tree/master**
- **Paper: https://arxiv.org/abs/1703.00564**
## Dataset Summary
`tox21_SRp53` is a dataset included in [MoleculeNet](https://moleculenet.org/). The "Toxicology in the 21st Century" (Tox21) initiative created a public database measuring toxicity of compounds, which has been used in the 2014 Tox21 Data Challenge. This dataset contains qualitative toxicity measurements for 8k compounds on 12 different targets, including nuclear receptors and stress response pathways.

# Dataset Structure

## Data Fields
Each split contains
* `smiles`: the [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) representation of a molecule
* `selfies`: the [SELFIES](https://github.com/aspuru-guzik-group/selfies) representation of a molecule
* `target`: Measured results (Active/Inactive) for bioassays
  
## Data Splits
The dataset is split into an 80/10/10 train/valid/test split using random split. 

# Additional Information

## Citation Information
```
@misc{https://doi.org/10.48550/arxiv.1703.00564,
  doi = {10.48550/ARXIV.1703.00564},
  
  url = {https://arxiv.org/abs/1703.00564},
  
  author = {Wu, Zhenqin and Ramsundar, Bharath and Feinberg, Evan N. and Gomes, Joseph and Geniesse, Caleb and Pappu, Aneesh S. and Leswing, Karl and Pande, Vijay},
  
  keywords = {Machine Learning (cs.LG), Chemical Physics (physics.chem-ph), Machine Learning (stat.ML), FOS: Computer and information sciences, FOS: Computer and information sciences, FOS: Physical sciences, FOS: Physical sciences},
  
  title = {MoleculeNet: A Benchmark for Molecular Machine Learning},
  
  publisher = {arXiv},
  
  year = {2017},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```
## Contributions
Thanks to [@SauravMaheshkar](https://github.com/SauravMaheshkar) and [@zanussbaum](https://github.com/zanussbaum) for adding this dataset