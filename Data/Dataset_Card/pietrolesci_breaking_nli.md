## Overview

Proposed by
```latex
@InProceedings{glockner_acl18,
  author    = {Glockner, Max and Shwartz, Vered and Goldberg, Yoav},
  title     = {Breaking NLI Systems with Sentences that Require Simple Lexical Inferences},
  booktitle = {The 56th Annual Meeting of the Association for Computational Linguistics (ACL)},
  month     = {July},
  year      = {2018},
  address   = {Melbourne, Australia}
}
```

Original dataset available [here](https://github.com/BIU-NLP/Breaking_NLI).


## Dataset curation
Labels encoded with the following mapping `{"entailment": 0, "neutral": 1, "contradiction": 2}`
and made available in the `label` column.


## Code to create the dataset
```python
import pandas as pd
from datasets import Features, Value, ClassLabel, Dataset, Sequence


# load data
with open("<path to folder>/dataset.jsonl", "r") as fl:
    data = fl.read().split("\n")
df = pd.DataFrame([eval(i) for i in data if len(i) > 0])

# encode labels
df["label"] = df["gold_label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})

# cast to dataset
features = Features({
    "sentence1": Value(dtype="string", id=None),
    "category": Value(dtype="string", id=None),
    "gold_label": Value(dtype="string", id=None),
    "annotator_labels": Sequence(feature=Value(dtype="string", id=None), length=3),
    "pairID": Value(dtype="int32", id=None),
    "sentence2": Value(dtype="string", id=None),
    "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
})
ds = Dataset.from_pandas(df, features=features)
ds.push_to_hub("breaking_nli", token="<token>", split="all")
```