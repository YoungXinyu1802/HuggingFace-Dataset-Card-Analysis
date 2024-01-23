## Overview

Original dataset available [here](https://github.com/sheng-z/JOCI/tree/master/data). 
This dataset is the "full" JOCI dataset, which is the file named `joci.csv.zip`.


# Dataset curation
The following processing is applied,

- `label` column renamed to `original_label`
- creation of the `label` column using the following mapping, using common practices ([1](https://github.com/rabeehk/robust-nli/blob/c32ff958d4df68ac2fad9bf990f70d30eab9f297/data/scripts/joci.py#L22-L27), [2](https://github.com/azpoliak/hypothesis-only-NLI/blob/b045230437b5ba74b9928ca2bac5e21ae57876b9/data/convert_joci.py#L7-L12))

```
{
    0: "contradiction", 
    1: "contradiction",  
    2: "neutral",
    3: "neutral",
    4: "neutral",
    5: "entailment",
}
```

- finally, converting this to the usual NLI classes, that is `{"entailment": 0, "neutral": 1, "contradiction": 2}`


## Code to create dataset
```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset


# read data
df = pd.read_csv("<path to folder>/joci.csv")

# column name to lower
df.columns = df.columns.str.lower()

# rename label column
df = df.rename(columns={"label": "original_label"})

# encode labels
df["label"] = df["original_label"].map({
    0: "contradiction", 
    1: "contradiction",  
    2: "neutral",
    3: "neutral",
    4: "neutral",
    5: "entailment",
})

# encode labels
df["label"] = df["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

# cast to dataset
features = Features({
    "context": Value(dtype="string"),
    "hypothesis": Value(dtype="string"),
    "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
    "original_label": Value(dtype="int32"),
    "context_from": Value(dtype="string"),
    "hypothesis_from": Value(dtype="string"),
    "subset": Value(dtype="string"),
})
ds = Dataset.from_pandas(df, features=features)
ds.push_to_hub("joci", token="<token>")
```
