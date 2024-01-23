## Overview

Original dataset page [here](https://abhilasharavichander.github.io/NLI_StressTest/) and dataset available [here](https://drive.google.com/open?id=1faGA5pHdu5Co8rFhnXn-6jbBYC2R1dhw).


## Dataset curation
Added new column `label` with encoded labels with the following mapping

```
{"entailment": 0, "neutral": 1, "contradiction": 2}
```

and the columns with parse information are dropped as they are not well formatted.

Also, the name of the file from which each instance comes is added in the column `dtype`.


## Code to create the dataset

```python
import pandas as pd
from datasets import Dataset, ClassLabel, Value, Features, DatasetDict
import json
from pathlib import Path


# load data
ds = {}
path = Path("<path to folder>")
for i in path.rglob("*.jsonl"): 
    print(i)
    name = str(i).split("/")[0].lower()
    dtype = str(i).split("/")[1].lower()
    
    # read data
    with i.open("r") as fl:
        df = pd.DataFrame([json.loads(line) for line in fl])
    
    # select columns
    df = df.loc[:, ["sentence1", "sentence2", "gold_label"]]
    
    # add file name as column
    df["dtype"] = dtype
    
    # encode labels
    df["label"] = df["gold_label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})
    ds[name] = df
        
# cast to dataset
features = Features(
    {
        "sentence1": Value(dtype="string"),
        "sentence2": Value(dtype="string"),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
        "dtype": Value(dtype="string"),
        "gold_label": Value(dtype="string"),
    }
)
ds = DatasetDict({k: Dataset.from_pandas(v, features=features) for k, v in ds.items()})
ds.push_to_hub("pietrolesci/stress_tests_nli", token="<token>")


# check overlap between splits
from itertools import combinations
for i, j in combinations(ds.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            ds[i].to_pandas(), 
            ds[j].to_pandas(), 
            on=["sentence1", "sentence2", "label"], 
            how="inner",
        ).shape[0],
    )
#> numerical_reasoning - negation:  0
#> numerical_reasoning - length_mismatch:  0
#> numerical_reasoning - spelling_error:  0
#> numerical_reasoning - word_overlap:  0
#> numerical_reasoning - antonym:  0
#> negation - length_mismatch:  0
#> negation - spelling_error:  0
#> negation - word_overlap:  0
#> negation - antonym:  0
#> length_mismatch - spelling_error:  0
#> length_mismatch - word_overlap:  0
#> length_mismatch - antonym:  0
#> spelling_error - word_overlap:  0
#> spelling_error - antonym:  0
#> word_overlap - antonym:  0
```