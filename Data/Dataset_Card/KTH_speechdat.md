# Speechdat
Speechdat dataset

## Loading the dataset
You need to download the dataset from another folder. We assume the wav files are located inside a /wav folder inside speechdat.

```
from datasets import load_dataset
speechdat = load_dataset("./speechdat", split="train", data_dir="./speechdat/wav")
```

