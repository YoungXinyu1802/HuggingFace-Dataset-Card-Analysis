## Overview
Original dataset available [here](https://github.com/krandiash/gpt3-nli). Debiased dataset generated with GPT-3.


## Dataset curation
All string columns are stripped. Labels are encoded with the following mapping

```
{"entailment": 0, "neutral": 1, "contradiction": 2}
```


## Code to create the dataset
```python
import pandas as pd
from datasets import Dataset, ClassLabel, Value, Features
import json

# load data
with open("data/dataset.jsonl", "r") as fl:
    df = pd.DataFrame([json.loads(line) for line in fl])

df.columns = df.columns.str.strip()

# fix dtypes
df["guid"] = df["guid"].astype(int)
for col in df.select_dtypes(object):
    df[col] = df[col].str.strip()

# encode labels
df["label"] = df["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

# cast to dataset
features = Features(
    {
        "text_a": Value(dtype="string"),
        "text_b": Value(dtype="string"),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
        "guid": Value(dtype="int64"),
    }
)
ds = Dataset.from_pandas(df, features=features)
ds.push_to_hub("pietrolesci/gpt3_nli", token="<token>")
```