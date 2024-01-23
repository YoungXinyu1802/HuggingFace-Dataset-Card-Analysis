---
annotations_creators: []
language: []
language_creators:
- expert-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: canonicalized ZINC
size_categories:
- 10M<n<100M
source_datasets:
- original
tags:
- ZINC
- chemical
- SMILES
task_categories: []
task_ids: []
---

### dataset description
We downloaded ZINC dataset from [here](https://zinc15.docking.org/) and canonicalized it.
We used the following function to canonicalize the data and removed some SMILES that cannot be read by RDKit.
    
```python:
from rdkit import Chem
def canonicalize(mol):
    mol = Chem.MolToSmiles(Chem.MolFromSmiles(mol),True)
    return mol 
```

We randomly split the preprocessed data into train and validation. The ratio is 9 : 1.