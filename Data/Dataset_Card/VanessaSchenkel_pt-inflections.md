---
annotations_creators:
- found
language:
- pt
language_creators:
- found
license: []
multilinguality:
- monolingual
pretty_name: "dicion\xE1rio de portugu\xEAs"
size_categories:
- 100K<n<1M
source_datasets:
- extended|wikipedia
tags: []
task_categories: []
task_ids: []
---

# Dataset Card for Dicionário Português
It is a list of 53138 portuguese words with its inflections.


How to use it: 
```
from datasets import load_dataset
remote_dataset = load_dataset("VanessaSchenkel/pt-inflections", field="data")
remote_dataset
```
Output:
```
DatasetDict({
    train: Dataset({
        features: ['word', 'pos', 'forms'],
        num_rows: 53138
    })
})
```
Exemple: 
```
remote_dataset["train"][42]
```
Output:
```
{'word': 'numeral',
 'pos': 'noun',
 'forms': [{'form': 'numerais', 'tags': ['plural']}]}
 ```
