## Overview
Original dataset available [here](https://gluebenchmark.com/diagnostics).


## Dataset curation
Filled in the empty rows of columns "lexical semantics", "predicate-argument structure", 
"logic", "knowledge" with empty string `""`.
Labels are encoded as follows

```
{"entailment": 0, "neutral": 1, "contradiction": 2}
```

## Code to create dataset

```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset


df = pd.read_csv("<path to file>/diagnostic-full.tsv", sep="\t")

# column names to lower
df.columns = df.columns.str.lower()

# fill na
assert df["label"].isna().sum() == 0
df = df.fillna("")

# encode labels
df["label"] = df["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

# cast to dataset
features = Features({
    "lexical semantics": Value(dtype="string", id=None),
    "predicate-argument structure": Value(dtype="string", id=None),
    "logic": Value(dtype="string", id=None),
    "knowledge": Value(dtype="string", id=None),
    "domain": Value(dtype="string", id=None),
    "premise": Value(dtype="string", id=None),
    "hypothesis": Value(dtype="string", id=None),
    "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
})

dataset = Dataset.from_pandas(df, features=features)
dataset.push_to_hub("glue_diagnostics", token="<token>", split="test")
```



