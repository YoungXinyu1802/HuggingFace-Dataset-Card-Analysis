---
tags:
- molecules
- chemistry
- SMILES
---

## How to use the data sets

This dataset contains 1.9M unique pairs of protein sequences and ligand SMILES with experimentally determined
binding affinities. It can be used for fine-tuning a language model.

The data comes from the following sources:
- BindingDB
- PDBbind-cn
- BioLIP
- BindingMOAD

### Use the already preprocessed data

Load a test/train split using

```
from datasets import load_dataset
train = load_dataset("jglaser/binding_affinity",split='train[:90%]')
validation = load_dataset("jglaser/binding_affinity",split='train[90%:]')
```

Optionally, datasets with certain protein sequences removed are available.
These can be used to test the predictive power for specific proteins even when
these are not part of the training data.

- `train_no_kras` (no KRAS proteins)

**Loading the data manually**

The file `data/all.parquet` contains the preprocessed data. To extract it,
you need download and install [git LFS support] https://git-lfs.github.com/].

### Pre-process yourself

To manually perform the preprocessing, download the data sets from

1. BindingDB

In `bindingdb`, download the database as tab separated values
<https://bindingdb.org> > Download > BindingDB_All_2021m4.tsv.zip
and extract the zip archive into `bindingdb/data`

Run the steps in `bindingdb.ipynb`

2. PDBBind-cn

Register for an account at <https://www.pdbbind.org.cn/>, confirm the validation
email, then login and download 

- the Index files (1)
- the general protein-ligand complexes (2)
- the refined protein-ligand complexes (3)

Extract those files in `pdbbind/data`

Run the script `pdbbind.py` in a compute job on an MPI-enabled cluster
(e.g., `mpirun -n 64 pdbbind.py`).

Perform the steps in the notebook `pdbbind.ipynb`

3. BindingMOAD

Go to <https://bindingmoad.org> and download the files `every.csv`
(All of Binding MOAD, Binding Data) and the non-redundant biounits
(`nr_bind.zip`). Place and extract those files into `binding_moad`.

Run the script `moad.py` in a compute job on an MPI-enabled cluster
(e.g., `mpirun -n 64 moad.py`).

Perform the steps in the notebook `moad.ipynb`

4. BioLIP

Download from <https://zhanglab.ccmb.med.umich.edu/BioLiP/> the files
- receptor1.tar.bz2 (Receptor1, Non-redudant set)
- ligand_2013-03-6.tar.bz2 (Ligands)
- BioLiP.tar.bz2 (Annotations)
and extract them in `biolip/data`.

The following steps are **optional**, they **do not** result in additional binding affinity data.

Download the script
- download_all_sets.pl
from the Weekly update subpage.

Update the 2013 database to its current state

`perl download_all-sets.pl`

Run the script `biolip.py` in a compute job on an MPI-enabled cluster
(e.g., `mpirun -n 64 biolip.py`).

Perform the steps in the notebook `biolip.ipynb`

5. Final concatenation and filtering

Run the steps in the notebook `combine_dbs.ipynb`
