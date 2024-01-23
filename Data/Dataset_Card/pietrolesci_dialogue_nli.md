## Overview
Original dataset available [here](https://wellecks.github.io/dialogue_nli/).


## Dataset curation
Original `label` column is renamed `original_label`. The original classes are renamed as follows

```
{"positive": "entailment", "negative": "contradiction", "neutral": "neutral"})
```

and encoded with the following mapping

```
{"entailment": 0, "neutral": 1, "contradiction": 2}
```

and stored in the newly created column `label`.


The following splits and the corresponding columns are present in the original files

```
train {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
dev {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
test {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
verified_test {'dtype', 'annotation3', 'sentence1', 'sentence2', 'annotation1', 'annotation2', 'original_label', 'label', 'triple2', 'triple1'}
extra_test {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
extra_dev {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
extra_train {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
valid_havenot {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
valid_attributes {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
valid_likedislike {'dtype', 'id', 'sentence1', 'sentence2', 'original_label', 'label', 'triple2', 'triple1'}
```

Note that I only keep the common columns, which means that I drop "annotation{1, 2, 3}" from `verified_test`.
Note that there are some splits with the same instances, as found by matching on "original_label", "sentence1", "sentence2".


## Code to create dataset
```python
import pandas as pd
from pathlib import Path
import json
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict, Sequence


# load data
ds = {}
for path in Path(".").rglob("<path to folder>/*.jsonl"):
    print(path, flush=True)
    with path.open("r") as fl:
        data = fl.read()
    try:
        d = json.loads(data, encoding="utf-8")
    except json.JSONDecodeError as error:
        print(error)
    
    df = pd.DataFrame(d)

    # encode labels
    df["original_label"] = df["label"]
    df["label"] = df["label"].map({"positive": "entailment", "negative": "contradiction", "neutral": "neutral"})
    df["label"] = df["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

    ds[path.name.split(".")[0]] = df
    
    
# prettify names of data splits
datasets = {
    k.replace("dialogue_nli_", "").replace("uu_", "").lower(): v
    for k, v in ds.items()
}
datasets.keys()
#> dict_keys(['train', 'dev', 'test', 'verified_test', 'extra_test', 'extra_dev', 'extra_train', 'valid_havenot', 'valid_attributes', 'valid_likedislike'])


# cast to datasets using only common columns
features = Features({
    "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
    "sentence1": Value(dtype="string", id=None),
    "sentence2": Value(dtype="string", id=None),
    "triple1": Sequence(feature=Value(dtype="string", id=None), length=3),
    "triple2": Sequence(feature=Value(dtype="string", id=None), length=3),
    "dtype": Value(dtype="string", id=None),
    "id": Value(dtype="string", id=None),
    "original_label": Value(dtype="string", id=None),
})

ds = {}
for name, df in datasets.items():
    if "id" not in df.columns:
        df["id"] = ""
    ds[name] = Dataset.from_pandas(df.loc[:, list(features.keys())], features=features)
ds = DatasetDict(ds)
ds.push_to_hub("dialogue_nli", token="<token>")


# check overlap between splits
from itertools import combinations
for i, j in combinations(ds.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            ds[i].to_pandas(), 
            ds[j].to_pandas(), 
            on=["original_label", "sentence1", "sentence2"], 
            how="inner",
        ).shape[0],
    )
#> train - dev:  58
#> train - test:  98
#> train - verified_test:  90
#> train - extra_test:  0
#> train - extra_dev:  0
#> train - extra_train:  0
#> train - valid_havenot:  0
#> train - valid_attributes:  0
#> train - valid_likedislike:  0
#> dev - test:  19
#> dev - verified_test:  19
#> dev - extra_test:  0
#> dev - extra_dev:  75
#> dev - extra_train:  75
#> dev - valid_havenot:  75
#> dev - valid_attributes:  75
#> dev - valid_likedislike:  75
#> test - verified_test:  12524
#> test - extra_test:  34
#> test - extra_dev:  0
#> test - extra_train:  0
#> test - valid_havenot:  0
#> test - valid_attributes:  0
#> test - valid_likedislike:  0
#> verified_test - extra_test:  29
#> verified_test - extra_dev:  0
#> verified_test - extra_train:  0
#> verified_test - valid_havenot:  0
#> verified_test - valid_attributes:  0
#> verified_test - valid_likedislike:  0
#> extra_test - extra_dev:  0
#> extra_test - extra_train:  0
#> extra_test - valid_havenot:  0
#> extra_test - valid_attributes:  0
#> extra_test - valid_likedislike:  0
#> extra_dev - extra_train:  250946
#> extra_dev - valid_havenot:  250946
#> extra_dev - valid_attributes:  250946
#> extra_dev - valid_likedislike:  250946
#> extra_train - valid_havenot:  250946
#> extra_train - valid_attributes:  250946
#> extra_train - valid_likedislike:  250946
#> valid_havenot - valid_attributes:  250946
#> valid_havenot - valid_likedislike:  250946
#> valid_attributes - valid_likedislike:  250946
```