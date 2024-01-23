## Overview
Original dataset available [here](https://github.com/jimmycode/gen-debiased-nli#training-with-our-datasets).

```latex
@inproceedings{gen-debiased-nli-2022,
    title = "Generating Data to Mitigate Spurious Correlations in Natural Language Inference Datasets",
    author = "Wu, Yuxiang  and
      Gardner, Matt  and
      Stenetorp, Pontus  and
      Dasigi, Pradeep",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics",
    month = may,
    year = "2022",
    publisher = "Association for Computational Linguistics",
}
```


## Dataset curation
No curation.

## Code to create the dataset
```python
import pandas as pd
from datasets import Dataset, ClassLabel, Value, Features, DatasetDict
import json
from pathlib import Path


# load data
path = Path("./")
ds = {}
for i in path.rglob("*.jsonl"): 
    print(i)
    name = str(i).split(".")[0].lower().replace("-", "_")
    
    with i.open("r") as fl:
        df = pd.DataFrame([json.loads(line) for line in fl])
    
    ds[name] = df

# cast to dataset
features = Features(
    {
        "premise": Value(dtype="string"),
        "hypothesis": Value(dtype="string"),
        "label": ClassLabel(num_classes=3, names=["entailment", "neutral", "contradiction"]),
        "type": Value(dtype="string"),
    }
)
ds = DatasetDict({k: Dataset.from_pandas(v, features=features) for k, v in ds.items()})
ds.push_to_hub("pietrolesci/gen_debiased_nli", token="<token>")

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
#> mnli_seq_z - snli_z_aug:  0
#> mnli_seq_z - mnli_par_z:  477149
#> mnli_seq_z - snli_seq_z:  0
#> mnli_seq_z - mnli_z_aug:  333840
#> mnli_seq_z - snli_par_z:  0
#> snli_z_aug - mnli_par_z:  0
#> snli_z_aug - snli_seq_z:  506624
#> snli_z_aug - mnli_z_aug:  0
#> snli_z_aug - snli_par_z:  504910
#> mnli_par_z - snli_seq_z:  0
#> mnli_par_z - mnli_z_aug:  334960
#> mnli_par_z - snli_par_z:  0
#> snli_seq_z - mnli_z_aug:  0
#> snli_seq_z - snli_par_z:  583107
#> mnli_z_aug - snli_par_z:  0
```