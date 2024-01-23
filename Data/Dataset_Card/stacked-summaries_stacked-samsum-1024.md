---
license: apache-2.0
source_datasets:
- samsum
task_categories:
- summarization
language:
- en
tags:
- stacked summaries
pretty_name: Stacked Samsum - 1024
size_categories:
- 10K<n<100K
---

# stacked samsum 1024

Created with the `stacked-booksum` repo version v0.25. It contains

- the original dataset
- stacked rows of the original dataset with criteria:
  - max input length 1024 longt5 tokens
  - max output length 1024 longt5 tokens


## dataset info

Default (train):

```python
[2022-12-04 13:19:32] INFO:root:{'num_columns': 4,
 'num_rows': 14732,
 'num_unique_target': 14730,
 'num_unique_text': 14265,
 'summary - average chars': 110.13,
 'summary - average tokens': 28.693727939180015,
 'text input - average chars': 511.22,
 'text input - average tokens': 148.88759163725223}

```

stacked (train)

```python
[2022-12-05 00:49:04] INFO:root:stacked 14730 rows, 2 rows were ineligible
[2022-12-05 00:49:04] INFO:root:dropped 20 duplicate rows, 29442 rows remain
[2022-12-05 00:49:04] INFO:root:shuffling output with seed 182
[2022-12-05 00:49:04] INFO:root:STACKED - basic stats - train
[2022-12-05 00:49:04] INFO:root:{'num_columns': 5,
 'num_rows': 29442,
 'num_unique_chapters': 28975,
 'num_unique_summaries': 29441,
 'summary - average chars': 452.8,
 'summary - average tokens': 106.46820868147545,
 'text input - average chars': 1814.09,
 'text input - average tokens': 528.665579783982}
```