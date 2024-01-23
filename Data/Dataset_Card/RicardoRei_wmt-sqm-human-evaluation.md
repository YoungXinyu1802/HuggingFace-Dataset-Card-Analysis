---
license: apache-2.0
size_categories:
- 1M<n<10M
language:
 - cs 
 - de 
 - en 
 - hr 
 - ja 
 - liv 
 - ru 
 - sah 
 - uk 
 - zh
tags:
- mt-evaluation
- WMT
- 12-lang-pairs
---

# Dataset Summary

In 2022, several changes were made to the annotation procedure used in the WMT Translation task. In contrast to the standard DA (sliding scale from 0-100) used in previous years, in 2022 annotators performed DA+SQM (Direct Assessment + Scalar Quality Metric). In DA+SQM, the annotators still provide a raw score between 0 and 100, but also are presented with seven labeled tick marks. DA+SQM helps to stabilize scores across annotators (as compared to DA).

The data is organised into 8 columns:
- lp: language pair
- src: input text
- mt: translation
- ref: reference translation
- score: direct assessment
- system: MT engine that produced the `mt`
- annotators: number of annotators
- domain: domain of the input text (e.g. news)
- year: collection year
  
You can also find the original data [here](https://www.statmt.org/wmt22/results.html)

## Python usage:

```python
from datasets import load_dataset
dataset = load_dataset("RicardoRei/wmt-sqm-human-evaluation", split="train")
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

Note that, so far, all data is from [2022 General Translation task](https://www.statmt.org/wmt22/translation-task.html)

## Citation Information

If you use this data please cite the WMT findings:
- [Findings of the 2022 Conference on Machine Translation (WMT22)](https://aclanthology.org/2022.wmt-1.1.pdf)
  