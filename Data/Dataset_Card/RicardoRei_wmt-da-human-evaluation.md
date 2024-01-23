---
license: apache-2.0
size_categories:
- 1M<n<10M
language:
- bn
- cs
- de
- en
- et
- fi
- fr
- gu
- ha
- hi
- is
- ja
- kk
- km
- lt
- lv
- pl
- ps
- ru
- ta
- tr
- uk
- xh
- zh
- zu
tags:
- mt-evaluation
- WMT
- 41-lang-pairs
---

# Dataset Summary

This dataset contains all DA human annotations from previous WMT News Translation shared tasks.

The data is organised into 8 columns:
- lp: language pair
- src: input text
- mt: translation
- ref: reference translation
- score: z score
- raw: direct assessment
- annotators: number of annotators
- domain: domain of the input text (e.g. news)
- year: collection year
  
You can also find the original data for each year in the results section https://www.statmt.org/wmt{YEAR}/results.html e.g: for 2020 data: [https://www.statmt.org/wmt20/results.html](https://www.statmt.org/wmt20/results.html)

## Python usage:

```python
from datasets import load_dataset
dataset = load_dataset("RicardoRei/wmt-da-human-evaluation", split="train")
```

There is no standard train/test split for this dataset but you can easily split it according to year, language pair or domain. E.g. :

```python
# split by year
data = dataset.filter(lambda example: example["year"] == 2022)

# split by LP
data = dataset.filter(lambda example: example["lp"] == "en-de")

# split by domain
data = dataset.filter(lambda example: example["domain"] == "news")
```

Note that most data is from News domain.


## Citation Information

If you use this data please cite the WMT findings from previous years:
- [Findings of the 2017 Conference on Machine Translation (WMT17)](https://aclanthology.org/W17-4717.pdf)
- [Findings of the 2018 Conference on Machine Translation (WMT18)](https://aclanthology.org/W18-6401.pdf)
- [Findings of the 2019 Conference on Machine Translation (WMT19)](https://aclanthology.org/W19-5301.pdf)
- [Findings of the 2020 Conference on Machine Translation (WMT20)](https://aclanthology.org/2020.wmt-1.1.pdf)
- [Findings of the 2021 Conference on Machine Translation (WMT21)](https://aclanthology.org/2021.wmt-1.1.pdf)
- [Findings of the 2022 Conference on Machine Translation (WMT22)](https://aclanthology.org/2022.wmt-1.1.pdf)