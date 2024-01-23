---
annotations_creators: []
language_creators: []
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: canonicalized ORD
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- ord
- chemical
- reaction
task_categories:
- text2text-generation
- translation
task_ids: []
---

### dataset description
We downloaded open-reaction-database(ORD) dataset from [here](https://github.com/open-reaction-database/ord-data). As a preprocess, we removed overlapping data and canonicalized them using RDKit.
We used the following function to canonicalize the data and removed some SMILES that cannot be read by RDKit.
    
```python:
from rdkit import Chem
def canonicalize(mol):
    mol = Chem.MolToSmiles(Chem.MolFromSmiles(mol),True)
    return mol 
```

We randomly split the preprocessed data into train, validation and test. The ratio is 8:1:1.