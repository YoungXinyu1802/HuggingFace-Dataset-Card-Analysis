## Overview

This dataset has been introduced by "Inference is Everything: Recasting Semantic Resources into a Unified Evaluation Framework", Aaron Steven White, Pushpendre Rastogi, Kevin Duh, Benjamin Van Durme. IJCNLP, 2017. Original data available [here](https://github.com/decompositional-semantics-initiative/DNC/raw/master/inference_is_everything.zip).


## Dataset curation
The following processing is applied

- `hypothesis_grammatical` and `judgement_valid` columns are filled with `""` when empty
- all columns are stripped
- the `entailed` column is renamed `label`
- `label` column is encoded with the following mapping `{"not-entailed": 0, "entailed": 1}`
- columns `rating` and `good_word` are dropped from `fnplus` dataset

## Code to generate the dataset

```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict


ds = {}
for name in ("fnplus", "sprl", "dpr"):

    # read data
    with open(f"<path to files>/{name}_data.txt", "r") as f:
        data = f.read()
    data = data.split("\n\n")
    data = [lines.split("\n") for lines in data]
    data = [dict([col.split(":", maxsplit=1) for col in line if len(col) > 0]) for line in data]
    df = pd.DataFrame(data)

    # fill empty hypothesis_grammatical and judgement_valid
    df["hypothesis_grammatical"] = df["hypothesis_grammatical"].fillna("")
    df["judgement_valid"] = df["judgement_valid"].fillna("")

    # fix dtype
    df["index"] = df["index"].astype(int)

    # strip
    for col in df.select_dtypes(object).columns:
        df[col] = df[col].str.strip()

    # rename columns
    df = df.rename(columns={"entailed": "label"})

    # encode labels
    df["label"] = df["label"].map({"not-entailed": 0, "entailed": 1})

    # cast to dataset
    features = Features({
        "provenance": Value(dtype="string", id=None),
        "index": Value(dtype="int64", id=None),
        "text": Value(dtype="string", id=None),
        "hypothesis": Value(dtype="string", id=None),
        "partof": Value(dtype="string", id=None),
        "hypothesis_grammatical": Value(dtype="string", id=None),
        "judgement_valid": Value(dtype="string", id=None),
        "label": ClassLabel(num_classes=2, names=["not-entailed", "entailed"]),
    })

    # select common columns
    df = df.loc[:, list(features.keys())]
    ds[name] = Dataset.from_pandas(df, features=features)

ds = DatasetDict(ds)
ds.push_to_hub("recast_white", token="<token>")
```