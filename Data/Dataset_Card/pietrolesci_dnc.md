## Overview
Original dataset [here](https://github.com/decompositional-semantics-initiative/DNC).

This dataset has been proposed in [Collecting Diverse Natural Language Inference Problems for Sentence Representation Evaluation](https://www.aclweb.org/anthology/D18-1007/).


## Dataset curation
This version of the dataset does not include the `type-of-inference` "KG" as its label set is 
`[1, 2, 3, 4, 5]` while here we focus on NLI-related label sets, i.e. `[entailed, not-entailed]`.
For this reason, I named the dataset DNLI for _Diverse_ NLI, as in [Liu et al 2020](https://aclanthology.org/2020.conll-1.48/), instead of DNC.

This version of the dataset contains columns from the `*_data.json` and the `*_metadata.json` files available in the repo.
In the original repo, each data file has the following keys and values:

- `context`: The context sentence for the NLI pair. The context is already tokenized.
- `hypothesis`: The hypothesis sentence for the NLI pair. The hypothesis is already tokenized.
- `label`: The label for the NLI pair
- `label-set`: The set of possible labels for the specific NLI pair
- `binary-label`: A `True` or `False` label. See the paper for details on how we convert the `label` into a binary label.
- `split`: This can be `train`, `dev`, or `test`.
- `type-of-inference`: A string indicating what type of inference is tested in this example.
- `pair-id`: A unique integer id for the NLI pair. The `pair-id` is used to find the corresponding metadata for any given NLI pair

while each metadata file has the following columns

- `pair-id`: A unique integer id for the NLI pair. 
- `corpus`: The original corpus where this example came from.
- `corpus-sent-id`: The id of the sentence (or example) in the original dataset that we recast.
- `corpus-license`: The license for the data from the original dataset.
- `creation-approach`: Determines the method used to recast this example. Options are `automatic`, `manual`, or `human-labeled`.
- `misc`: A dictionary of other relevant information. This is an optional field.

The files are merged on the `pair-id` key. I **do not** include the `misc` column as it is not essential for NLI.

NOTE: the label mapping is **not** the custom (i.e., 3 class) for NLI tasks. They used a binary target and I encoded them
with the following mapping `{"not-entailed": 0, "entailed": 1}`.

NOTE: some instances are present in multiple splits (matching performed by exact matching on "context", "hypothesis", and "label").

## Code to create the dataset
```python
import pandas as pd
from datasets import Dataset, ClassLabel, Value, Features, DatasetDict, Sequence
from pathlib import Path


paths = {
    "train": "<path_to_folder>/DNC-master/train",
    "dev": "<path_to_folder>/DNC-master/dev",
    "test": "<path_to_folder>/DNC-master/test",
}

# read all data files
dfs = []
for split, path in paths.items():
    for f_name in Path(path).rglob("*_data.json"):
        df = pd.read_json(str(f_name))
        df["file_split_data"] = split
        dfs.append(df)
data = pd.concat(dfs, ignore_index=False, axis=0)

# read all metadata files
meta_dfs = []
for split, path in paths.items():
    for f_name in Path(path).rglob("*_metadata.json"):
        df = pd.read_json(str(f_name))
        meta_dfs.append(df)
metadata = pd.concat(meta_dfs, ignore_index=False, axis=0)

# merge
dataset = pd.merge(data, metadata, on="pair-id", how="left")

# check that the split column reflects file splits
assert sum(dataset["split"] != dataset["file_split_data"]) == 0
dataset = dataset.drop(columns=["file_split_data"])

# fix `binary-label` column
dataset.loc[~dataset["label"].isin(["entailed", "not-entailed"]), "binary-label"] = False
dataset.loc[dataset["label"].isin(["entailed", "not-entailed"]), "binary-label"] = True

# fix datatype
dataset["corpus-sent-id"] = dataset["corpus-sent-id"].astype(str)

# order columns as shown in the README.md
columns = [
    "context",
    "hypothesis",
    "label",
    "label-set",
    "binary-label",
    "split",
    "type-of-inference",
    "pair-id",
    "corpus",
    "corpus-sent-id",
    "corpus-license",
    "creation-approach",
    "misc",
]
dataset = dataset.loc[:, columns]

# remove misc column
dataset = dataset.drop(columns=["misc"])

# remove KG for NLI
dataset.loc[(dataset["label"].isin([1, 2, 3, 4, 5])), "type-of-inference"].value_counts()
# > the only split with label-set [1, 2, 3, 4, 5], so remove as we focus on NLI
dataset = dataset.loc[~(dataset["type-of-inference"] == "KG")]

# encode labels
dataset["label"] = dataset["label"].map({"not-entailed": 0, "entailed": 1})

# fill NA in label-set
dataset["label-set"] = dataset["label-set"].ffill()

features = Features(
    {
        "context": Value(dtype="string"),
        "hypothesis": Value(dtype="string"),
        "label": ClassLabel(num_classes=2, names=["not-entailed", "entailed"]),
        "label-set": Sequence(length=2, feature=Value(dtype="string")),
        "binary-label": Value(dtype="bool"),
        "split": Value(dtype="string"),
        "type-of-inference": Value(dtype="string"),
        "pair-id": Value(dtype="int64"),
        "corpus": Value(dtype="string"),
        "corpus-sent-id": Value(dtype="string"),
        "corpus-license": Value(dtype="string"),
        "creation-approach": Value(dtype="string"),
    }
)

dataset_splits = {}
for split in ("train", "dev", "test"):
    df_split = dataset.loc[dataset["split"] == split]
    dataset_splits[split] = Dataset.from_pandas(df_split, features=features)

dataset_splits = DatasetDict(dataset_splits)
dataset_splits.push_to_hub("pietrolesci/dnli", token="<your token>")

# check overlap between splits
from itertools import combinations
for i, j in combinations(dataset_splits.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            dataset_splits[i].to_pandas(), 
            dataset_splits[j].to_pandas(), 
            on=["context", "hypothesis", "label"], 
            how="inner",
        ).shape[0],
    )
#> train - dev:  127
#> train - test:  55
#> dev - test:  54
```
