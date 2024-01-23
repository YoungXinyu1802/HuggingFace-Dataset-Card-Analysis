---
tags:
- molecules
- chemistry
- SMILES
---

## How to use the data sets

This dataset contains more than 16,000 unique pairs of protein sequences and ligand SMILES with experimentally determined
binding affinities and protein-ligand contacts (ligand atom/SMILES token vs. Calpha within 5 Angstrom). These
are represented by a list that contains the positions of non-zero elements of the flattened, sparse
sequence x smiles tokens (2048x512) matrix. The first and last entries in both dimensions
are padded to zero, they correspond to [CLS] and [SEP].

It can be used for fine-tuning a language model.

The data solely uses data from PDBind-cn.

Contacts are calculated at four cut-off distances: 5, 8, 11A and 15A.

### Use the already preprocessed data

Load a test/train split using

```
from datasets import load_dataset
train = load_dataset("jglaser/protein_ligand_contacts",split='train[:90%]')
validation = load_dataset("jglaser/protein_ligand_contacts",split='train[90%:]')
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

Perform the steps in the notebook `pdbbind.ipynb`
