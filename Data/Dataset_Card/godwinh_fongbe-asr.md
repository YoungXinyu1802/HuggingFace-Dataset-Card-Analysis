---
license: apache-2.0
---

Original dataset at [this repo](https://github.com/laleye/pyFongbe)

We transformed the original repo to take into account the waveform values directly in the csv.
Using `IPython.diplay` module, you can load an audio by doing: 

```python
import pandas as pd
from IPython.display import Audio, display

train = pd.read_csv("train.csv")
sample = train.sample(1).values[0]
print(f"Text: {sample[2]}")
display(Audio(sample[3], rate=16000, autoplay=True))
```

```
Text: alin ɔ ɖo xwe tεntin
Audio : 
```
