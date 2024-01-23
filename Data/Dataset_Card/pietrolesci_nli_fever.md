## Overview
The original dataset can be found [here](https://www.dropbox.com/s/hylbuaovqwo2zav/nli_fever.zip?dl=0)
while the Github repo is [here](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md).

This dataset has been proposed in [Combining fact extraction and verification with neural semantic matching networks](https://dl.acm.org/doi/abs/10.1609/aaai.v33i01.33016859). This dataset has been created as a modification
of FEVER.

In the original FEVER setting, the input is a claim from Wikipedia and the expected output is a label. 
However, this is different from the standard NLI formalization which is basically a *pair-of-sequence to label* problem.
To facilitate NLI-related research to take advantage of the FEVER dataset, the authors pair the claims in the FEVER dataset
with the textual evidence and make it a *pair-of-sequence to label* formatted dataset.

## Dataset curation
The label mapping follows the paper and is the following 

```python
mapping = {
    "SUPPORTS": 0,  # entailment
    "NOT ENOUGH INFO": 1,  # neutral
    "REFUTES": 2,  # contradiction
}
```

Also, the "verifiable" column has been encoded as follows

```python
mapping = {"NOT VERIFIABLE": 0, "VERIFIABLE": 1}
```

Finally, a consistency check with the labels reported in the original FEVER dataset is performed.

NOTE: no label is available for the "test" split.
NOTE: there are 3 instances in common between `dev` and `train` splits.


## Code to generate the dataset
```python
import pandas as pd
from datasets import Dataset, ClassLabel, load_dataset, Value, Features, DatasetDict
import json


# download data from https://www.dropbox.com/s/hylbuaovqwo2zav/nli_fever.zip?dl=0
paths = {
    "train": "<some_path>/nli_fever/train_fitems.jsonl",
    "validation": "<some_path>/nli_fever/dev_fitems.jsonl",
    "test": "<some_path>/nli_fever/test_fitems.jsonl",
}


# parsing code from https://github.com/facebookresearch/anli/blob/main/src/utils/common.py
registered_jsonabl_classes = {}


def register_class(cls):
    global registered_jsonabl_classes
    if cls not in registered_jsonabl_classes:
        registered_jsonabl_classes.update({cls.__name__: cls})


def unserialize_JsonableObject(d):
    global registered_jsonabl_classes
    classname = d.pop("_jcls_", None)
    if classname:
        cls = registered_jsonabl_classes[classname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


def load_jsonl(filename, debug_num=None):
    d_list = []
    with open(filename, encoding="utf-8", mode="r") as in_f:
        print("Load Jsonl:", filename)
        for line in in_f:
            item = json.loads(line.strip(), object_hook=unserialize_JsonableObject)
            d_list.append(item)
            if debug_num is not None and 0 < debug_num == len(d_list):
                break

    return d_list


def get_original_fever() -> pd.DataFrame:
    """Get original fever datasets."""

    fever_v1 = load_dataset("fever", "v1.0")
    fever_v2 = load_dataset("fever", "v2.0")

    columns = ["id", "label"]
    splits = ["paper_test", "paper_dev", "labelled_dev", "train"]
    list_dfs = [fever_v1[split].to_pandas()[columns] for split in splits]
    list_dfs.append(fever_v2["validation"].to_pandas()[columns])

    dfs = pd.concat(list_dfs, ignore_index=False)
    dfs = dfs.drop_duplicates()

    dfs = dfs.rename(columns={"label": "fever_gold_label"})
    return dfs


def load_and_process(path: str, fever_df: pd.DataFrame) -> pd.DataFrame:
    """Load data split and merge with fever."""

    df = pd.DataFrame(load_jsonl(path))
    df = df.rename(columns={"query": "premise", "context": "hypothesis"})

    # adjust dtype
    df["cid"] = df["cid"].astype(int)

    # merge with original fever to get labels
    df = pd.merge(df, fever_df, left_on="cid", right_on="id", how="inner").drop_duplicates()

    return df


def encode_labels(df: pd.DataFrame) -> pd.DataFrame:
    """Encode labels using the mapping used in SNLI and MultiNLI"""
    mapping = {
        "SUPPORTS": 0,  # entailment
        "NOT ENOUGH INFO": 1,  # neutral
        "REFUTES": 2,  # contradiction
    }
    df["label"] = df["fever_gold_label"].map(mapping)

    # verifiable
    df["verifiable"] = df["verifiable"].map({"NOT VERIFIABLE": 0, "VERIFIABLE": 1})

    return df


if __name__ == "__main__":
    fever_df = get_original_fever()

    dataset_splits = {}

    for split, path in paths.items():

        # from json to dataframe and merge with fever
        df = load_and_process(path, fever_df)

        if not len(df) > 0:
            print(f"Split `{split}` has no matches")
            continue

        if split == "train":
            # train must have same labels
            assert sum(df["fever_gold_label"] != df["label"]) == 0

        # encode labels using the default mapping used by other nli datasets
        # i.e, entailment: 0, neutral: 1, contradiction: 2
        df = df.drop(columns=["label"])
        df = encode_labels(df)

        # cast to dataset
        features = Features(
            {
                "cid": Value(dtype="int64", id=None),
                "fid": Value(dtype="string", id=None),
                "id": Value(dtype="int32", id=None),
                "premise": Value(dtype="string", id=None),
                "hypothesis": Value(dtype="string", id=None),
                "verifiable": Value(dtype="int64", id=None),
                "fever_gold_label": Value(dtype="string", id=None),
                "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
            }
        )
        if "test" in path:
            # no features for test set
            df["label"] = -1
            df["verifiable"] = -1
            df["fever_gold_label"] = "not available"
        dataset = Dataset.from_pandas(df, features=features)
        dataset_splits[split] = dataset

    nli_fever = DatasetDict(dataset_splits)
    nli_fever.push_to_hub("pietrolesci/nli_fever", token="<your token>")
    
    # check overlap between splits
    from itertools import combinations
    for i, j in combinations(dataset_splits.keys(), 2):
        print(
            f"{i} - {j}: ",
            pd.merge(
                dataset_splits[i].to_pandas(), 
                dataset_splits[j].to_pandas(), 
                on=["premise", "hypothesis", "label"], 
                how="inner",
            ).shape[0],
        )
    #> train - dev:  3
    #> train - test:  0
    #> dev - test:  0
```