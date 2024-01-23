## Overview

Original dataset [here](https://github.com/aylai/MultiPremiseEntailment).


## Dataset curation
Same data and splits as the original. The following columns have been added:

- `premise`: concatenation of `premise1`, `premise2`, `premise3`, and `premise4`
- `label`: encoded `gold_label` with the following mapping `{"entailment": 0, "neutral": 1, "contradiction": 2}`


## Code to create the dataset

```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict
from pathlib import Path


# read data
path = Path("<path to files>")
datasets = {}
for dataset_path in path.rglob("*.txt"):
    df = pd.read_csv(dataset_path, sep="\t")
    datasets[dataset_path.name.split("_")[1].split(".")[0]] = df
    

ds = {}
for name, df_ in datasets.items():
    df = df_.copy()
    
    # fix parsing error for dev split
    if name == "dev":
        # fix parsing error
        df.loc[df["contradiction_judgments"] == "3   contradiction", "contradiction_judgments"] = 3
        df.loc[df["gold_label"].isna(), "gold_label"] = "contradiction"
    
    # check no nan
    assert df.isna().sum().sum() == 0

    # fix dtypes
    for col in ("entailment_judgments", "neutral_judgments", "contradiction_judgments"):
        df[col] = df[col].astype(int)
    
    # fix premise column
    for i in range(1, 4 + 1):
        df[f"premise{i}"] = df[f"premise{i}"].str.split("/", expand=True)[1]
    df["premise"] = df[[f"premise{i}" for i in range(1, 4 + 1)]].agg(" ".join, axis=1)

    # encode labels
    df["label"] = df["gold_label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

    # cast to dataset
    features = Features({
        "premise1": Value(dtype="string", id=None),
        "premise2": Value(dtype="string", id=None),
        "premise3": Value(dtype="string", id=None),
        "premise4": Value(dtype="string", id=None),
        "premise": Value(dtype="string", id=None),
        "hypothesis": Value(dtype="string", id=None),
        "entailment_judgments": Value(dtype="int32"),
        "neutral_judgments": Value(dtype="int32"),
        "contradiction_judgments": Value(dtype="int32"),
        "gold_label": Value(dtype="string"),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
    })

    ds[name] = Dataset.from_pandas(df, features=features)
    
# push to hub
ds = DatasetDict(ds)
ds.push_to_hub("mpe", token="<token>")

# check overlap between splits
from itertools import combinations
for i, j in combinations(ds.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            ds[i].to_pandas(), 
            ds[j].to_pandas(), 
            on=["premise", "hypothesis", "label"], 
            how="inner",
        ).shape[0],
    )
#> dev - test:  0
#> dev - train:  0
#> test - train:  0
```