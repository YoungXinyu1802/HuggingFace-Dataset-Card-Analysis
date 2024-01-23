## Overview
Original dataset is available on the HuggingFace Hub [here](https://huggingface.co/datasets/scitail).


## Dataset curation
This is the same as the `snli_format` split of the SciTail dataset available on the HuggingFace Hub (i.e., same data, same splits, etc).
The only differences are the following:

- selecting only the columns `["sentence1", "sentence2", "gold_label", "label"]`
- renaming columns with the following mapping `{"sentence1": "premise", "sentence2": "hypothesis"}`
- creating a new column "label" from "gold_label" with the following mapping `{"entailment": "entailment", "neutral": "not_entailment"}`
- encoding labels with the following mapping `{"not_entailment": 0, "entailment": 1}`

Note that there are 10 overlapping instances (as found by merging on columns "label", "premise", and "hypothesis") between
`train` and `test` splits.


## Code to create the dataset
```python
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict, load_dataset

# load datasets from the Hub
dd = load_dataset("scitail", "snli_format")

ds = {}
for name, df_ in dd.items():
    df = df_.to_pandas()

    # select important columns
    df = df[["sentence1", "sentence2", "gold_label"]]

    # rename columns
    df = df.rename(columns={"sentence1": "premise", "sentence2": "hypothesis"})

    # encode labels
    df["label"] = df["gold_label"].map({"entailment": "entailment", "neutral": "not_entailment"})
    df["label"] = df["label"].map({"not_entailment": 0, "entailment": 1})

    # cast to dataset
    features = Features({
        "premise": Value(dtype="string", id=None),
        "hypothesis": Value(dtype="string", id=None),
        "label": ClassLabel(num_classes=2, names=["not_entailment", "entailment"]),
    })
    ds[name] = Dataset.from_pandas(df, features=features)

dataset = DatasetDict(ds)
dataset.push_to_hub("scitail", token="<token>")

# check overlap between splits
from itertools import combinations
for i, j in combinations(dataset.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            dataset[i].to_pandas(), 
            dataset[j].to_pandas(), 
            on=["label", "premise", "hypothesis"], 
            how="inner",
        ).shape[0],
    )
#> train - test:  10
#> train - validation:  0
#> test - validation:  0
```