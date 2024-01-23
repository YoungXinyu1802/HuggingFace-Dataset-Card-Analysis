## Overview
Original dataset available [here](https://people.ict.usc.edu/~gordon/copa.html).
Current dataset extracted from [this repo](https://github.com/felipessalvatore/NLI_datasets).

This is the "full" dataset.


# Curation
Same curation as the one applied in [this repo](https://github.com/felipessalvatore/NLI_datasets), that is

from the original COPA format:


|premise                                |       choice1       |          choice2            |        label |
|---|---|---|---|
|My body cast a shadow over the grass   |  The sun was rising |     The grass was cut       |          0 |


to the NLI format:


| premise                              |    hypothesis     |   label |
|---|---|---|
| My body cast a shadow over the grass | The sun was rising| entailment |
| My body cast a shadow over the grass | The grass was cut | not_entailment |

Also, the labels are encoded with the following mapping `{"not_entailment": 0, "entailment": 1}`


## Code to generate dataset
```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset, DatasetDict, load_dataset
from pathlib import Path


# read data
path = Path("./nli_datasets")
datasets = {}
for dataset_path in path.iterdir():
    datasets[dataset_path.name] = {}
    for name in dataset_path.iterdir():
        df = pd.read_csv(name)
        datasets[dataset_path.name][name.name.split(".")[0]] = df

# merge all splits
df = pd.concat(list(datasets["copa"].values()))

# encode labels
df["label"] = df["label"].map({"not_entailment": 0, "entailment": 1})

# cast to dataset
features = Features({
    "premise": Value(dtype="string", id=None),
    "hypothesis": Value(dtype="string", id=None),
    "label": ClassLabel(num_classes=2, names=["not_entailment", "entailment"]),
})
ds = Dataset.from_pandas(df, features=features)
ds.push_to_hub("copa_nli", token="<token>")
```