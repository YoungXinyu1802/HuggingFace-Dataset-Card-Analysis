---
language: 
  - uk
license: cc-by-4.0
---

This repository contains transcriptions with other metadata for the VOA Ukrainian dataset (~398h).

Usage:

```python
from datasets import load_dataset

ds = load_dataset('Yehor/voa-uk-transcriptions', split='train')

for row in ds:
    print(row['text'])
```
