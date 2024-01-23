---
license: apache-2.0
language:
- en
tags:
- stacked summaries
pretty_name: Stacked XSUM 16384
size_categories:
- 100K<n<1M
task_categories:
- summarization
source_datasets:
- xsum
---

# xsum-stacked

The current version (corresponding to the `stacked-booksum` release): `v0.3`. See the Stacked Summaries [org page](https://huggingface.co/stacked-summaries) for _what_ this is and why it exists.

The maximum input length is 16384 tokens, and the maximum output length is 1024 tokens (measured with the Long-T5 tokenizer). 

## stats


```python
[2023-01-09 19:36:25] INFO:root:INPUTS - basic stats - train
[2023-01-09 19:36:26] INFO:root:{'num_columns': 5,
 'num_rows': 204045,
 'num_unique_target': 203107,
 'num_unique_text': 203846,
 'summary - average chars': 125.46,
 'summary - average tokens': 30.383719277610332,
 'text input - average chars': 2202.42,
 'text input - average tokens': 523.9222230390355}
[2023-01-10 02:34:29] INFO:root:stacked 204040 rows, 5 rows were ineligible
[2023-01-10 02:37:17] INFO:root:dropped 106 duplicate rows, 407979 rows remain
[2023-01-10 02:37:17] INFO:root:shuffling output with seed 1017
[2023-01-10 02:37:19] INFO:root:STACKED - basic stats - train
[2023-01-10 02:37:24] INFO:root:{'num_columns': 6,
 'num_rows': 407979,
 'num_unique_chapters': 407880,
 'num_unique_summaries': 407141,
 'summary - average chars': 2189.41,
 'summary - average tokens': 473.4450547699759,
 'text input - average chars': 33855.06,
 'text input - average tokens': 8039.657793660948}
```


## Citation

If you find this useful in your work, please consider citing us.

```
@misc {stacked_summaries_2023,
	author       = { {Stacked Summaries: Karim Foda and Peter Szemraj} },
	title        = { stacked-xsum (Revision bd7c88e) },
	year         = 2023,
	url          = { https://huggingface.co/datasets/stacked-summaries/stacked-xsum },
	doi          = { 10.57967/hf/0269 },
	publisher    = { Hugging Face }
}
```