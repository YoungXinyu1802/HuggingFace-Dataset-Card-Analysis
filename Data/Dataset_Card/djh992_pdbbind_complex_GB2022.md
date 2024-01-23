---
tags:
- molecules
- Chemistry
- SMILES
- Protein
- Ligand
- Complexes
---

### To generate the dataset

Register for an account at https://www.pdbbind.org.cn/, confirm the validation email, then login and download

the Index files (1)
the general protein-ligand complexes (2)
the refined protein-ligand complexes (3)
Extract those files in pdbbind_complex_GB2022/data

Run the script pdbbind.py in a compute job on an MPI-enabled cluster (e.g., mpirun -n 64 pdbbind.py).

Output will be tar files in `train/`, `val/` and `test/` folders, following the split direction which is from EquiBind manuscript. 