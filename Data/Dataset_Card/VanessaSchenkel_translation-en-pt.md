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
pretty_name: VanessaSchenkel/translation-en-pt
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- translation
task_ids: []
---
How to use it: 

```
from datasets import load_dataset

remote_dataset = load_dataset("VanessaSchenkel/translation-en-pt", field="data")

remote_dataset
```

Output:
```
DatasetDict({
    train: Dataset({
        features: ['id', 'translation'],
        num_rows: 260482
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
 'translation': {'english': 'I have to go to sleep.',
  'portuguese': 'Tenho de dormir.'}}
 ```