---
license: mit
dataset_info:
  features:
  - name: selfies
    dtype: string
  - name: smiles
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_bytes: 238295712864
    num_examples: 804925861
  - name: validation
    num_bytes: 26983481360
    num_examples: 100642661
  - name: test
    num_bytes: 29158755632
    num_examples: 101082073
  download_size: 40061255073
  dataset_size: 294437949856
tags:
- bio
- selfies
- smiles
- small_molecules
pretty_name: zinc20
size_categories:
- 1B<n<10B
---
# Dataset Card for Zinc20

## Dataset Description

- **Homepage:** https://zinc20.docking.org/
- **Paper:** https://pubs.acs.org/doi/10.1021/acs.jcim.0c00675

### Dataset Summary

ZINC is a publicly available database that aggregates commercially available and annotated compounds. 
ZINC provides downloadable 2D and 3D versions as well as a website that enables rapid molecule lookup and analog search.
ZINC has grown from fewer than 1 million compounds in 2005 to nearly 2 billion now.
This dataset includes ~1B molecules in total. We have filtered out any compounds that were not avaible to be converted from `smiles` to `seflies` representations.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

The dataset is split into an 80/10/10 train/valid/test random split across files (which roughly corresponds to the same percentages)

### Source Data

#### Initial Data Collection and Normalization

Initial data was released at https://zinc20.docking.org/. We have downloaded and added a `selfies` field and filtered out all molecules that did not contain molecules that could be converted to `selfies` representations.

### Citation Information

@article{Irwin2020,
  doi = {10.1021/acs.jcim.0c00675},
  url = {https://doi.org/10.1021/acs.jcim.0c00675},
  year = {2020},
  month = oct,
  publisher = {American Chemical Society ({ACS})},
  volume = {60},
  number = {12},
  pages = {6065--6073},
  author = {John J. Irwin and Khanh G. Tang and Jennifer Young and Chinzorig Dandarchuluun and Benjamin R. Wong and Munkhzul Khurelbaatar and Yurii S. Moroz and John Mayfield and Roger A. Sayle},
  title = {{ZINC}20{\textemdash}A Free Ultralarge-Scale Chemical Database for Ligand Discovery},
  journal = {Journal of Chemical Information and Modeling}
}

### Contributions

This dataset was curated and added by [@zanussbaum](https://github.com/zanussbaum).
