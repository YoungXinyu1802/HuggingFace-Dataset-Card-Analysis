## Overview
Original dataset [here](https://github.com/felipessalvatore/NLI_datasets).

Below the original description reported for convenience.
```latex
@MISC{Fracas96, 
    author = {{The Fracas Consortium} and Robin Cooper and Dick Crouch and Jan Van Eijck and Chris Fox and Josef Van Genabith and Jan Jaspars and Hans Kamp and David Milward and Manfred Pinkal and Massimo Poesio and Steve Pulman and Ted Briscoe and Holger Maier and Karsten Konrad}, 
    title = {Using the Framework}, 
    year = {1996} 
}
```

Adapted from [https://nlp.stanford.edu/~wcmac/downloads/fracas.xml](https://nlp.stanford.edu/~wcmac/downloads/fracas.xml). We took `P1, ..., Pn` as premise and H as hypothesis. Labels have been mapped as follows `{'yes': "entailment", 'no': 'contradiction', 'undef': "neutral", 'unknown': "neutral"}`. And we randomly split 80/20 for train/dev.


## Dataset curation
One hypothesis in the dev set and three hypotheses in the train set are empty and have been
filled in with the empty string `""`. Labels are encoded with custom NLI mapping, that is

```
{"entailment": 0, "neutral": 1, "contradiction": 2}
```


## Code to create the dataset
```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict, load_dataset
from pathlib import Path


# load datasets
path = Path("<path to folder>/nli_datasets")
datasets = {}
for dataset_path in path.iterdir():
    datasets[dataset_path.name] = {}
    for name in dataset_path.iterdir():
        df = pd.read_csv(name)
        datasets[dataset_path.name][name.name.split(".")[0]] = df


ds = {}
for name, df_ in datasets["fracas"].items():

    df = df_.copy()
    assert df["label"].isna().sum() == 0

    # fill-in empty hypothesis
    df = df.fillna("")

    # encode labels
    df["label"] = df["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

    # cast to dataset
    features = Features({
        "premise": Value(dtype="string", id=None),
        "hypothesis": Value(dtype="string", id=None),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
    })
    ds[name] = Dataset.from_pandas(df, features=features)

dataset = DatasetDict(ds)
dataset.push_to_hub("fracas", token="<token>")

# check overlap between splits
from itertools import combinations
for i, j in combinations(ds.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            ds[i].to_pandas(), 
            ds[j].to_pandas(), 
            on=["label", "premise", "hypothesis"], 
            how="inner",
        ).shape[0],
    )
#> train - dev: 0
```