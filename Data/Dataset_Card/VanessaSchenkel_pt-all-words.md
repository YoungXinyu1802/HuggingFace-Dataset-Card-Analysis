---
annotations_creators:
- no-annotation
language:
- pt
language_creators:
- expert-generated
license: []
multilinguality:
- monolingual
paperswithcode_id: sbwce
pretty_name: "Dicion\xE1rio em Portugu\xEAs"
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- other
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---

# Dataset Card for Dicionário Português
It is a list of portuguese words with its inflections
How to use it: 
```
from datasets import load_dataset
remote_dataset = load_dataset("VanessaSchenkel/pt-all-words")
remote_dataset
```
