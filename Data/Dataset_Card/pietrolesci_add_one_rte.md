## Overview

Original data available [here](http://www.seas.upenn.edu/~nlp/resources/AN-composition.tgz).


## Dataset curation

`premise` and `hypothesis` columns have been cleaned following common practices ([1](https://github.com/rabeehk/robust-nli/blob/c32ff958d4df68ac2fad9bf990f70d30eab9f297/data/scripts/add_one_rte.py#L51-L52), [2](https://github.com/azpoliak/hypothesis-only-NLI/blob/b045230437b5ba74b9928ca2bac5e21ae57876b9/data/convert_add_1_rte.py#L31-L32)), that is

- remove HTML tags `<b>`, `<u>`, `</b>`, `</u>`
- normalize repeated white spaces
- strip

`mean_human_score` has been transformed into class labels following common practices ([1](https://github.com/rabeehk/robust-nli/blob/c32ff958d4df68ac2fad9bf990f70d30eab9f297/data/scripts/add_one_rte.py#L20-L35), [2](https://github.com/azpoliak/hypothesis-only-NLI/blob/b045230437b5ba74b9928ca2bac5e21ae57876b9/data/convert_add_1_rte.py#L6-L17)), that is

- for test set: `mean_human_score <= 3 -> "not-entailed"` and `mean_human_score >= 4 -> "entailed"` (anything between 3 and 4 has been removed)
- for all other splits: `mean_human_score < 3.5 -> "not-entailed"` else `"entailed"`

more details below.


## Code to generate the dataset
```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict


def convert_label(score, is_test):
  if is_test:
    if score <= 3:
      return "not-entailed"
    elif score >= 4:
      return "entailed"
    return "REMOVE"

  if score < 3.5:
      return "not-entailed"
  return "entailed"


ds = {}
for split in ("dev", "test", "train"):

    # read data
    df = pd.read_csv(f"<path to folder>/AN-composition/addone-entailment/splits/data.{split}", sep="\t", header=None)
    df.columns = ["mean_human_score", "binary_label", "sentence_id", "adjective", "noun", "premise", "hypothesis"]

    # clean text from html tags and useless spaces
    for col in ("premise", "hypothesis"):
        df[col] = (
            df[col]
            .str.replace("(<b>)|(<u>)|(</b>)|(</u>)", " ", regex=True)
            .str.replace(" {2,}", " ", regex=True)
            .str.strip()
        )

    # encode labels
    if split == "test":
        df["label"] = df["mean_human_score"].map(lambda x: convert_label(x, True))
        df = df.loc[df["label"] != "REMOVE"]
    else:
        df["label"] = df["mean_human_score"].map(lambda x: convert_label(x, False))
    assert df["label"].isna().sum() == 0

    df["label"] = df["label"].map({"not-entailed": 0, "entailed": 1})

    # cast to dataset
    features = Features({
        "mean_human_score": Value(dtype="float32"), 
        "binary_label": Value(dtype="string"), 
        "sentence_id": Value(dtype="string"), 
        "adjective": Value(dtype="string"), 
        "noun": Value(dtype="string"), 
        "premise": Value(dtype="string"), 
        "hypothesis": Value(dtype="string"),
        "label": ClassLabel(num_classes=2, names=["not-entailed", "entailed"]),
    })    
    ds[split] = Dataset.from_pandas(df, features=features)

ds = DatasetDict(ds)
ds.push_to_hub("add_one_rte", token="<token>")


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