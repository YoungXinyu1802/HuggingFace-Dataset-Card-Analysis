---
annotations_creators:
- found
language:
- en
- pt
language_creators:
- found
license:
- afl-3.0
multilinguality:
- translation
pretty_name: VanessaSchenkel/handmade-dataset
size_categories:
- n<1K
source_datasets:
- original
tags: []
task_categories:
- translation
task_ids: []
---
Dataset with sentences regarding professions, half of the translations are to feminine and half for masculine sentences.

How to use it: 
```
from datasets import load_dataset
remote_dataset = load_dataset("VanessaSchenkel/handmade-dataset", field="data")
remote_dataset
```
Output:
```
DatasetDict({
    train: Dataset({
        features: ['id', 'translation'],
        num_rows: 388
    })
})
```
Exemple: 
```
remote_dataset["train"][5]
```
Output:
```
{'id': '5',
 'translation': {'english': 'the postman finished her work .',
  'portuguese': 'A carteira terminou seu trabalho .'}} 
```