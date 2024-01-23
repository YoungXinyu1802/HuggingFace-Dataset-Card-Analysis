---
language: en
license: other
---

# Snares 

FSD50K subset of just snares.

```
wget -nc https://huggingface.co/datasets/nateraw/snares/resolve/main/snares.csv
wget -nc https://huggingface.co/datasets/nateraw/snares/resolve/main/snares.zip
unzip snares.zip
```

If you unpack as described above, `snares.csv` will have correct filepath to audio file when loaded in as CSV. Here we show with pandas...

```python
import pandas as pd

df = pd.read_csv('snares.csv')
```