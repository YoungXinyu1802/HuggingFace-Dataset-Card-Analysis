---
language: 
  - uk
license: cc-by-nc-sa-4.0
tags:
- uk
---

This dataset contains **5,242,391** samples of Ukrainian news headlines.

Usage:

```python
from datasets import load_dataset

ds = load_dataset('Yehor/ukrainian-news-headlines', split='train')

for row in ds:
    print(row['headline'])
```

Attribution to the dataset:

- Chaplynskyi, D. et al. (2021) lang-uk Ukrainian Ubercorpus [Data set]. https://lang.org.ua/uk/corpora/#anchor4
