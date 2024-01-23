---
tags:
- proteins
- molecules
- chemistry
- SMILES
- complex structures
---

## How to use the data sets

This dataset contains about 36,000 unique pairs of protein sequences and ligand SMILES, and the coordinates
of their complexes from the PDB.

SMILES are assumed to be tokenized by the regex from P. Schwaller.

## Ligand selection criteria

Only ligands

- that have at least 3 atoms,
- a molecular weight >= 100 Da,
- and which are not among the 280 most common ligands in the PDB (this includes common additives like PEG, ADP, ..)

are considered.

### Use the already preprocessed data

Load a test/train split using

```
import pandas as pd
train = pd.read_pickle('data/pdb_train.p')
test = pd.read_pickle('data/pdb_test.p')
```

Receptor features contain protein frames and side chain angles in OpenFold/AlphaFold format.
Ligand tokens which do not correspond to atoms have `nan` as their coordinates.

Documentation by example:

```
>>> import pandas as pd
>>> test = pd.read_pickle('data/pdb_test.p')
>>> test.head(5)
  pdb_id lig_id  ...                                      ligand_xyz_2d                                       ligand_bonds
0   7k38    VTY  ...  [(-2.031355975502858, -1.6316778784387098, 0.0...  [(0, 1), (1, 4), (4, 5), (5, 10), (10, 9), (9,...
1   6prt    OWA  ...  [(4.883261310160714, -0.37850716807626705, 0.0...  [(11, 18), (18, 20), (20, 8), (8, 7), (7, 2), ...
2   4lxx    FNF  ...  [(8.529427756002057, 2.2434809270065372, 0.0),...  [(51, 49), (49, 48), (48, 46), (46, 53), (53, ...
3   4lxx    FON  ...  [(-10.939694946697701, -1.1876214529096956, 0....  [(13, 1), (1, 0), (0, 3), (3, 4), (4, 7), (7, ...
4   7bp1    CAQ  ...  [(-1.9485571585149868, -1.499999999999999, 0.0...  [(4, 3), (3, 1), (1, 0), (0, 7), (7, 9), (7, 6...

[5 rows x 8 columns]
>>> test.columns
Index(['pdb_id', 'lig_id', 'seq', 'smiles', 'receptor_features', 'ligand_xyz',
       'ligand_xyz_2d', 'ligand_bonds'],
      dtype='object')
>>> test.iloc[0]['receptor_features']
{'rigidgroups_gt_frames': array([[[[-5.3122622e-01,  2.0922849e-01, -8.2098854e-01,
           1.7295000e+01],
         [-7.1005428e-01, -6.3858479e-01,  2.9670244e-01,
          -9.1399997e-01],
         [-4.6219218e-01,  7.4056256e-01,  4.8779655e-01,
           3.3284000e+01],
         [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,
           1.0000000e+00]],
...
         [[ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,
          -3.5030000e+00],
         [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,
           2.6764999e+01],
         [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,
           1.5136000e+01],
         [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,
           1.0000000e+00]]]], dtype=float32), 'torsion_angles_sin_cos': array([[[-1.90855725e-09,  3.58859784e-02],
        [ 1.55730803e-01,  9.87799530e-01],
        [ 6.05505241e-01, -7.95841312e-01],
        ...,
        [-2.92459433e-01, -9.56277928e-01],
        [ 9.96634814e-01, -8.19697779e-02],
        [ 0.00000000e+00,  0.00000000e+00]],
...

       [[ 2.96455977e-04, -9.99999953e-01],
        [-8.15660990e-01,  5.78530158e-01],
        [-3.17915569e-01,  9.48119024e-01],
        ...,
        [ 0.00000000e+00,  0.00000000e+00],
        [ 0.00000000e+00,  0.00000000e+00],
        [ 0.00000000e+00,  0.00000000e+00]]])}
>>> test.iloc[0]['receptor_features'].keys()
dict_keys(['rigidgroups_gt_frames', 'torsion_angles_sin_cos'])
>>> test.iloc[0]['ligand_xyz']
[(22.289, 11.985, 9.225), (21.426, 11.623, 7.959), (nan, nan, nan), (nan, nan, nan), (21.797, 11.427, 6.574), (20.556, 11.56, 5.792), (nan, nan, nan), (20.507, 11.113, 4.552), (nan, nan, nan), (19.581, 10.97, 6.639), (20.107, 10.946, 7.954), (nan, nan, nan), (nan, nan, nan), (19.645, 10.364, 8.804)]
```
### Manual update from PDB

```
# download the PDB archive into folder pdb/
sh rsync.sh 24 # number of parallel download processes

# extract sequences and coordinates in parallel
sbatch pdb.slurm
# or
mpirun -n 42 parse_complexes.py # desired number of tasks
```
