---
license: apache-2.0
source_datasets:
- xsum
task_categories:
- summarization
language:
- en
tags:
- stacked summaries
- xsum
pretty_name: 'Stacked XSUM: 1024 tokens max'
size_categories:
- 100K<n<1M
---

# stacked-xsum-1024


a "stacked" version of `xsum` 

## updates 

- dec 3: upload initial version
- dec 4: upload v2 with basic data quality fixes (i.e. the `is_stacked` column)
- dec 5 0500: upload v3 which has pre-randomised order and duplicate rows for document+summary dropped

## dataset details

see the repo `.log` file for more details.

train input

```python
[2022-12-05 01:05:17] INFO:root:INPUTS - basic stats - train
[2022-12-05 01:05:17] INFO:root:{'num_columns': 5,
 'num_rows': 204045,
 'num_unique_target': 203107,
 'num_unique_text': 203846,
 'summary - average chars': 125.46,
 'summary - average tokens': 30.383719277610332,
 'text input - average chars': 2202.42,
 'text input - average tokens': 523.9222230390355}

```

stacked train:

```python
[2022-12-05 04:47:01] INFO:root:stacked 181719 rows, 22326 rows were ineligible
[2022-12-05 04:47:02] INFO:root:dropped 64825 duplicate rows, 320939 rows remain
[2022-12-05 04:47:02] INFO:root:shuffling output with seed 323
[2022-12-05 04:47:03] INFO:root:STACKED - basic stats - train
[2022-12-05 04:47:04] INFO:root:{'num_columns': 6,
 'num_rows': 320939,
 'num_unique_chapters': 320840,
 'num_unique_summaries': 320101,
 'summary - average chars': 199.89,
 'summary - average tokens': 46.29925001324239,
 'text input - average chars': 2629.19,
 'text input - average tokens': 621.541532814647}
```

## Citation

If you find this useful in your work, please consider citing us.

```
@misc {stacked_summaries_2023,
	author       = { {Stacked Summaries: Karim Foda and Peter Szemraj} },
	title        = { stacked-xsum-1024 (Revision 2d47220) },
	year         = 2023,
	url          = { https://huggingface.co/datasets/stacked-summaries/stacked-xsum-1024 },
	doi          = { 10.57967/hf/0390 },
	publisher    = { Hugging Face }
}
```