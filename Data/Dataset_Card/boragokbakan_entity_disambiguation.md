---
license: afl-3.0
language:
- en
tags:
- entity disambiguation
- disambiguation
- ned
- GENRE
- BLINK
pretty_name: Entity Disambiguation
task_categories:
- question-answering
---

Entity Disambiguation datasets as provided in the [GENRE](https://github.com/facebookresearch/GENRE/blob/main/scripts_genre/download_all_datasets.sh) repo. The dataset can be used to train and evaluate entity disambiguators.

The datasets can be imported easily as follows:

```
from datasets import load_dataset

ds = load_dataset("boragokbakan/entity_disambiguation", "aida")
```

Available dataset names are:
- `blink`
- `ace2004`
- `aida`
- `aquaint`
- `blink`
- `clueweb`
- `msnbc`
- `wiki`

**Note:** As the BLINK training set is very large in size (~10GB), it is advised to set `streaming=True` when calling `load_dataset`.