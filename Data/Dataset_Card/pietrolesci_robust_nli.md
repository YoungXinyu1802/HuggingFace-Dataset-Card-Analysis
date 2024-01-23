## Overview
Original dataset is available in the original [Github repo](https://github.com/tyliupku/nli-debiasing-datasets).

This dataset is a collection of NLI benchmarks constructed as described in the paper
[An Empirical Study on Model-agnostic Debiasing Strategies for Robust Natural Language Inference](https://aclanthology.org/2020.conll-1.48/)
published at CoNLL 2020.


## Dataset curation
No specific curation for this dataset. Label encoding follows exactly what is reported in the paper by the authors.
Also, from the paper:

> _all the following datasets are collected based on the public available resources proposed by their authors, thus the experimental results in this paper are comparable to the numbers reported in the original papers and the other papers that use these datasets_

Most of the datasets included follow the custom 3-class NLI convention `{"entailment": 0, "neutral": 1, "contradiction": 2}`.
However, the following datasets have a particular label mapping 

- `IS-SD`: `{"non-entailment": 0, "entailment": 1}`

- `LI_TS`: `{"non-contradiction": 0, "contradiction": 1}`


## Dataset structure
This benchmark dataset includes 10 adversarial datasets. To provide more insights on how the adversarial
datasets attack the models, the authors categorized them according to the bias(es) they test and they renamed
them accordingly. More details in section 2 of the paper. 
A mapping with the original dataset names is provided below

|    | Name   | Original Name | Original Paper | Original Curation |
|---:|:-------|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | PI-CD  | SNLI-Hard              | [Gururangan et al. (2018)](https://aclanthology.org/N18-2017/)                                                            | SNLI test sets instances that cannot be correctly classified by a neural classifier (fastText) trained on only the hypothesis sentences.                                                                                                                                            |
|  1 | PI-SP  | MNLI-Hard              | [Liu et al. (2020)](https://aclanthology.org/2020.lrec-1.846/)                                                            | MNLI-mismatched dev sets instances that cannot be correctly classified by surface patterns that are highly correlated with the labels.                                                                                                                                              |
|  2 | IS-SD  | HANS                   | [McCoy et al. (2019)](https://aclanthology.org/P19-1334/)                                                                 | Dataset that tests lexical overlap, subsequence, and constituent heuristics between the hypothesis and premises sentences.                                                                                                                                                          |
|  3 | IS-CS  | SoSwap-AddAMod         | [Nie et al. (2019)](https://dl.acm.org/doi/abs/10.1609/aaai.v33i01.33016867)                                              | Pairs of sentences whose logical relations cannot be extracted from lexical information alone. Premise are taken from SNLI dev set and modified. The original paper assigns a Lexically Misleading Scores (LMS) to each instance. Here, only the subset with LMS > 0.7 is reported. |
|  4 | LI-LI  | Stress tests (antonym) | [Naik et al. (2018)](https://aclanthology.org/C18-1198/) and [Glockner et al. (2018)](https://aclanthology.org/P18-2103/) | Merge of the 'antonym' category in Naik et al. (2018) (from MNLI matched and mismatched dev sets) and Glockner et al. (2018) (SNLI training set).                                                                                                                                   |
|  5 | LI-TS  | Created by the authors | Created by the authors                                                                                                    | Swap the two sentences in the original MultiNLI mismatched dev sets. If the gold label is 'contradiction', the corresponding label in the swapped instance remains unchanged, otherwise it becomes 'non-contradicted'.                                                              |
|  6 | ST-WO  | Word overlap           | [Naik et al. (2018)](https://aclanthology.org/C18-1198/)                                                                  | 'Word overlap' category in Naik et al. (2018).                                                                                                                                                                                                                                      |
|  7 | ST-NE  | Negation               | [Naik et al. (2018)](https://aclanthology.org/C18-1198/)                                                                  | 'Negation' category in Naik et al. (2018).                                                                                                                                                                                                                                          |
|  8 | ST-LM  | Length mismatch        | [Naik et al. (2018)](https://aclanthology.org/C18-1198/)                                                                  | 'Length mismatch' category in Naik et al. (2018).                                                                                                                                                                                                                                   |
|  9 | ST-SE  | Spelling errors        | [Naik et al. (2018)](https://aclanthology.org/C18-1198/)                                                                  | 'Spelling errors' category in Naik et al. (2018).                                                                                                                                                                                                                                   |

## Code to create the dataset

```python

import pandas as pd
from datasets import Dataset, ClassLabel, Value, Features, DatasetDict


Tri_dataset = ["IS_CS", "LI_LI", "PI_CD", "PI_SP", "ST_LM", "ST_NE", "ST_SE", "ST_WO"]
Ent_bin_dataset = ["IS_SD"]
Con_bin_dataset = ["LI_TS"]


# read data
with open("<path to file>/robust_nli.txt", encoding="utf-8", mode="r") as fl:
    f = fl.read().strip().split("\n")
    f = [eval(i) for i in f]
df = pd.DataFrame.from_dict(f)

# rename to map common names
df = df.rename(columns={"prem": "premise", "hypo": "hypothesis"})

# reorder columns
df = df.loc[:, ["idx", "split", "premise", "hypothesis", "label"]]

# create split-specific features
Tri_features = Features(
    {
        "idx": Value(dtype="int64"),
        "premise": Value(dtype="string"),
        "hypothesis": Value(dtype="string"),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
    }
)

Ent_features = Features(
    {
        "idx": Value(dtype="int64"),
        "premise": Value(dtype="string"),
        "hypothesis": Value(dtype="string"),
        "label": ClassLabel(num_classes=2, names=["non-entailment", "entailment"]),
    }
)

Con_features = Features(
    {
        "idx": Value(dtype="int64"),
        "premise": Value(dtype="string"),
        "hypothesis": Value(dtype="string"),
        "label": ClassLabel(num_classes=2, names=["non-contradiction", "contradiction"]),
    }
)

# convert to datasets
dataset_splits = {}

for split in df["split"].unique():
    print(split)
    df_split = df.loc[df["split"] == split].copy()
    
    if split in Tri_dataset:
        df_split["label"] = df_split["label"].map({"entailment": 0, "neutral": 1, "contradiction": 2})
        ds = Dataset.from_pandas(df_split, features=Tri_features)
    
    elif split in Ent_bin_dataset:
        df_split["label"] = df_split["label"].map({"non-entailment": 0, "entailment": 1})
        ds = Dataset.from_pandas(df_split, features=Ent_features)
    
    elif split in Con_bin_dataset:
        df_split["label"] = df_split["label"].map({"non-contradiction": 0, "contradiction": 1})
        ds = Dataset.from_pandas(df_split, features=Con_features)

    else:
        print("ERROR:", split)
    dataset_splits[split] = ds
datasets = DatasetDict(dataset_splits)    
datasets.push_to_hub("pietrolesci/robust_nli", token="<your token>")


# check overlap between splits
from itertools import combinations
for i, j in combinations(datasets.keys(), 2):
    print(
        f"{i} - {j}: ",
        pd.merge(
            datasets[i].to_pandas(), 
            datasets[j].to_pandas(), 
            on=["premise", "hypothesis", "label"], 
            how="inner",
        ).shape[0],
    )
#> PI_SP - ST_LM:  0
#> PI_SP - ST_NE:  0
#> PI_SP - IS_CS:  0
#> PI_SP - LI_TS:  1
#> PI_SP - LI_LI:  0
#> PI_SP - ST_SE:  0
#> PI_SP - PI_CD:  0
#> PI_SP - IS_SD:  0
#> PI_SP - ST_WO:  0
#> ST_LM - ST_NE:  0
#> ST_LM - IS_CS:  0
#> ST_LM - LI_TS:  0
#> ST_LM - LI_LI:  0
#> ST_LM - ST_SE:  0
#> ST_LM - PI_CD:  0
#> ST_LM - IS_SD:  0
#> ST_LM - ST_WO:  0
#> ST_NE - IS_CS:  0
#> ST_NE - LI_TS:  0
#> ST_NE - LI_LI:  0
#> ST_NE - ST_SE:  0
#> ST_NE - PI_CD:  0
#> ST_NE - IS_SD:  0
#> ST_NE - ST_WO:  0
#> IS_CS - LI_TS:  0
#> IS_CS - LI_LI:  0
#> IS_CS - ST_SE:  0
#> IS_CS - PI_CD:  0
#> IS_CS - IS_SD:  0
#> IS_CS - ST_WO:  0
#> LI_TS - LI_LI:  0
#> LI_TS - ST_SE:  0
#> LI_TS - PI_CD:  0
#> LI_TS - IS_SD:  0
#> LI_TS - ST_WO:  0
#> LI_LI - ST_SE:  0
#> LI_LI - PI_CD:  0
#> LI_LI - IS_SD:  0
#> LI_LI - ST_WO:  0
#> ST_SE - PI_CD:  0
#> ST_SE - IS_SD:  0
#> ST_SE - ST_WO:  0
#> PI_CD - IS_SD:  0
#> PI_CD - ST_WO:  0
#> IS_SD - ST_WO:  0
```