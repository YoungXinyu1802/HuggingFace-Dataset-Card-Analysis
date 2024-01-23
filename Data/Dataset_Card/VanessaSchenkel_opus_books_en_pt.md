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
pretty_name: VanessaSchenkel/opus_books_en_pt
size_categories:
- 1K<n<10K
source_datasets:
- extended|opus_books
tags: []
task_categories:
- translation
task_ids: []
---

How to use it: 
```
from datasets import load_dataset
remote_dataset = load_dataset("VanessaSchenkel/opus_books_en_pt", field="data")
remote_dataset
```
Output:
```
DatasetDict({
    train: Dataset({
        features: ['id', 'translation'],
        num_rows: 1404
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
 'translation': {'en': "There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, 'Oh dear!",
  'pt': 'Não havia nada de tão extraordinário nisso; nem Alice achou assim tão fora do normal ouvir o Coelho dizer para si mesmo: —"Oh, céus!'}}
```