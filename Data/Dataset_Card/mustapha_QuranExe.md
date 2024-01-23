---
annotations_creators:
  - no-annotation
language_creators:
  - expert-generated
language:
  - ar
license:
  - mit
multilinguality:
  - multilingual
paperswithcode_id: null
pretty_name: QuranExe
size_categories:
  - 10K<n<100K
source_datasets:
  - original
task_categories:
  - text-generation
  - fill-mask
  - sentence-similarity
task_ids:
  - language-modeling
  - masked-language-modeling
---
## Dataset Description

- **Size of downloaded dataset files:** 126 MB


This dataset contains the exegeses/tafsirs (تفسير القرآن) of the holy Quran in arabic by 8 exegetes.

This is a non Official dataset. It have been scrapped from the `Quran.com Api`

This dataset contains `49888` records with `+14` Million words. `8` records per Quranic verse

Usage Example :
```python
from datasets import load_dataset

tafsirs = load_dataset("mustapha/QuranExe")
```