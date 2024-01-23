---
license: apache-2.0
language:
- en
- de
- ru
- zh
tags:
- mt-evaluation
- WMT
size_categories:
- 100K<n<1M
---

# Dataset Summary

This dataset contains all MQM human annotations from previous [WMT Metrics shared tasks](https://wmt-metrics-task.github.io/) and the MQM annotations from [Experts, Errors, and Context](https://aclanthology.org/2021.tacl-1.87/).

The data is organised into 8 columns:
- lp: language pair
- src: input text
- mt: translation
- ref: reference translation
- score: MQM score
- system: MT Engine that produced the translation
- annotators: number of annotators
- domain: domain of the input text (e.g. news)
- year: collection year
  
You can also find the original data [here](https://github.com/google/wmt-mqm-human-evaluation). We recommend using the original repo if you are interested in annotation spans and not just the final score.


## Python usage:

```python
from datasets import load_dataset
dataset = load_dataset("RicardoRei/wmt-mqm-human-evaluation", split="train")
```

There is no standard train/test split for this dataset but you can easily split it according to year, language pair or domain. E.g. :

```python
# split by year
data = dataset.filter(lambda example: example["year"] == 2022)

# split by LP
data = dataset.filter(lambda example: example["lp"] == "en-de")

# split by domain
data = dataset.filter(lambda example: example["domain"] == "ted")
```

## Citation Information

If you use this data please cite the following works:
- [Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for Machine Translation](https://aclanthology.org/2021.tacl-1.87/)
- [Results of the WMT21 Metrics Shared Task: Evaluating Metrics with Expert-based Human Evaluations on TED and News Domain](https://aclanthology.org/2021.wmt-1.73/)
- [Results of WMT22 Metrics Shared Task: Stop Using BLEU – Neural Metrics Are Better and More Robust](https://aclanthology.org/2022.wmt-1.2/)