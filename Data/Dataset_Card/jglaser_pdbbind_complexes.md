---
tags:
- molecules
- chemistry
- SMILES
---

## How to use the data sets

This dataset contains more than 16,000 unique pairs of protein sequences and ligand SMILES, and the coordinates
of their complexes.

SMILES are assumed to be tokenized by the regex from P. Schwaller

Every (x,y,z) ligand coordinate maps onto a SMILES token, and is *nan* if the token does not represent an atom

Every receptor coordinate maps onto the Calpha coordinate of that residue.

The dataset can be used to fine-tune a language model, all data comes from PDBind-cn.

### Use the already preprocessed data

Load a test/train split using

```
from datasets import load_dataset
train = load_dataset("jglaser/pdbbind_complexes",split='train[:90%]')
validation = load_dataset("jglaser/pdbbind_complexes",split='train[90%:]')
```

### Pre-process yourself

To manually perform the preprocessing, download the data sets from P.DBBind-cn

Register for an account at <https://www.pdbbind.org.cn/>, confirm the validation
email, then login and download 

- the Index files (1)
- the general protein-ligand complexes (2)
- the refined protein-ligand complexes (3)

Extract those files in `pdbbind/data`

Run the script `pdbbind.py` in a compute job on an MPI-enabled cluster
(e.g., `mpirun -n 64 pdbbind.py`).
