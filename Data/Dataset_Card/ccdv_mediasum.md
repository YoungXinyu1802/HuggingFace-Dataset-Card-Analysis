---
language:
- en
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---

# MediaSum dataset for summarization

Summarization dataset copied from [MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization](https://github.com/zcgzcgzcg1/MediaSum)

This dataset is compatible with the [`run_summarization.py`](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization) script from Transformers if you add this line to the `summarization_name_mapping` variable:
```python
"ccdv/mediasum": ("document", "summary")
```

# Configs
4 possibles configs:
- `roberta` will concatenate documents with "\</s\>"
- `newline` will concatenate documents with "\n"
- `bert` will concatenate documents with "[SEP]"
- `list` will return the list of documents instead of a single string

Add `_prepended` to config name to prepend the speaker name before each dialogue: `speaker: text` \
Default is `roberta_prepended` (compatible with BART).

### Data Fields

- `id`: paper id
- `document`: a string/list containing the body of a set of documents
- `summary`: a string containing the abstract of the set

### Data Splits

This dataset has 3 splits: _train_, _validation_, and _test_. \

| Dataset Split | Number of Instances | 
| ------------- | --------------------|
| Train         | 443596              |
| Validation    | 10000               |
| Test          | 10000               |


# Cite original article
```
@article{zhu2021mediasum,
  title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},
  author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},
  journal={arXiv preprint arXiv:2103.06410},
  year={2021}
}
```