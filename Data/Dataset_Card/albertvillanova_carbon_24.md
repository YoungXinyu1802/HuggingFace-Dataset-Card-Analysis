---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- cif
license:
- mit
multilinguality:
- other-crystallography
size_categories:
- unknown
source_datasets: []
task_categories:
- other
task_ids: []
pretty_name: Carbon-24
tags:
- material-property-optimization
- material-reconstruction
- material-generation
---

# Dataset Card for Carbon-24

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:**
- **Repository:** https://github.com/txie-93/cdvae/tree/main/data/carbon_24
- **Paper:** [Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)
- **Leaderboard:**
- **Point of Contact:** [Tian Xie](mailto:txie@csail.mit.edu)

### Dataset Summary

Carbon-24 contains 10k carbon materials, which share the same composition, but have different structures. There is 1 element and the materials have 6 - 24 atoms in the unit cells.

Carbon-24 includes various carbon structures obtained via ab initio random structure searching (AIRSS) (Pickard & Needs, 2006; 2011) performed at 10 GPa.

The original dataset includes 101529 carbon structures, and we selected the 10% of the carbon structure with the lowest energy per atom to create Carbon-24. All 10153 structures are at local energy minimum after DFT relaxation. The most stable structure is diamond at 10 GPa. All remaining structures are thermodynamically unstable but may be kinetically stable.

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

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

Please consider citing the following papers:

```
@article{xie2021crystal,
  title={Crystal Diffusion Variational Autoencoder for Periodic Material Generation},
  author={Tian Xie and Xiang Fu and Octavian-Eugen Ganea and Regina Barzilay and Tommi Jaakkola},
  year={2021},
  eprint={2110.06197},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```

and

```
@misc{carbon2020data,
  doi = {10.24435/MATERIALSCLOUD:2020.0026/V1},
  url = {https://archive.materialscloud.org/record/2020.0026/v1},
  author = {Pickard,  Chris J.},
  keywords = {DFT,  ab initio random structure searching,  carbon},
  language = {en},
  title = {AIRSS data for carbon at 10GPa and the C+N+H+O system at 1GPa},
  publisher = {Materials Cloud},
  year = {2020},
  copyright = {info:eu-repo/semantics/openAccess}
}
```


### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
