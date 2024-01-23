---
annotations_creators: []
language: []
language_creators:
- expert-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: canonicalized PubChem-10m
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- PubChem
- chemical
- SMILES
task_categories: []
task_ids: []
---

### dataset description
We downloaded PubChem-10m dataset from [here](https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/pubchem_10m.txt.zip) and canonicalized it.
We used the following function to canonicalize the data and removed some SMILES that cannot be read by RDKit.
    
```python:
from rdkit import Chem
def canonicalize(mol):
    mol = Chem.MolToSmiles(Chem.MolFromSmiles(mol),True)
    return mol 
```

We randomly split the preprocessed data into train and validation. The ratio is 9 : 1.