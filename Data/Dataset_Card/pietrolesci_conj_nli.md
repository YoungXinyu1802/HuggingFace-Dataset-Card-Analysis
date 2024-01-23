## Overview
The original dataset can be found [here](https://github.com/swarnaHub/ConjNLI). It has been
proposed in [ConjNLI: Natural Language Inference Over Conjunctive Sentences](https://aclanthology.org/2020.emnlp-main.661/).

This dataset is a stress test for natural language inference over conjunctive sentences, 
where the premise differs from the hypothesis by conjuncts removed, added, or replaced.


## Dataset curation
The label mapping is the usual `{"entailment": 0, "neutral": 1, "contradiction": 2}`
used in NLI datasets. Note that labels for `test` split are not available. 
Also, the `train` split is originally named `adversarial_train_15k`.

There are 2 instances (join on "premise", "hypothesis", "label") present both in `train` and `dev`.

The `test` split does not have labels.

Finally, in the `train` set there are a few instances without a label, they are removed.


## Code to create the dataset
```python
import pandas as pd
from datasets import Dataset, ClassLabel, Value, Features, DatasetDict

# download data from repo https://github.com/swarnaHub/ConjNLI
paths = {
    "train": "<path_to_folder>/ConjNLI-master/data/NLI/adversarial_train_15k.tsv",
    "dev": "<path_to_folder>/ConjNLI-master/data/NLI/conj_dev.tsv",
    "test": "<path_to_folder>/ConjNLI-master/data/NLI/conj_test.tsv",
}

dataset_splits = {}
for split, path in paths.items():

    # load data
    df = pd.read_csv(paths[split], sep="\t")

    # encode labels using the default mapping used by other nli datasets
    # i.e, entailment: 0, neutral: 1, contradiction: 2
    df.columns = df.columns.str.lower()

    if "test" in path:
        df["label"] = -1
    
    else:
        # remove empty labels
        df = df.loc[~df["label"].isna()]
        # encode labels
        df["label"] = df["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

    # cast to dataset
    features = Features({
        "premise": Value(dtype="string", id=None),
        "hypothesis": Value(dtype="string", id=None),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
    })
    dataset = Dataset.from_pandas(df, features=features)
    dataset_splits[split] = dataset

conj_nli = DatasetDict(dataset_splits)
conj_nli.push_to_hub("pietrolesci/conj_nli", token="<token>")


# check overlap between splits
from itertools import combinations
for i, j in combinations(conj_nli.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            conj_nli[i].to_pandas(), 
            conj_nli[j].to_pandas(), 
            on=["premise", "hypothesis", "label"], how="inner"
        ).shape[0],
    )
#> train - dev:  2
#> train - test:  0
#> dev - test:  0
```