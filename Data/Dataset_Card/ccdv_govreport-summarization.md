---
language:
- en
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- summarization
- text-generation
task_ids: []
tags:
- conditional-text-generation
---

# GovReport dataset for summarization

Dataset for summarization of long documents.\
Adapted from this [repo](https://github.com/luyang-huang96/LongDocSum) and this [paper](https://arxiv.org/pdf/2104.02112.pdf)\
This dataset is compatible with the [`run_summarization.py`](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization) script from Transformers if you add this line to the `summarization_name_mapping` variable:
```python
"ccdv/govreport-summarization": ("report", "summary")
```

### Data Fields

- `id`: paper id
- `report`: a string containing the body of the report
- `summary`: a string containing the summary of the report

### Data Splits

This dataset has 3 splits: _train_, _validation_, and _test_. \
Token counts with a RoBERTa tokenizer.

| Dataset Split | Number of Instances |     Avg. tokens       |
| ------------- | --------------------|:----------------------|
| Train         | 17,517              |    < 9,000 / < 500    |
| Validation    | 973                 |    < 9,000 / < 500    |
| Test          | 973                 |    < 9,000 / < 500    |


# Cite original article
```
@misc{huang2021efficient,
      title={Efficient Attentions for Long Document Summarization}, 
      author={Luyang Huang and Shuyang Cao and Nikolaus Parulian and Heng Ji and Lu Wang},
      year={2021},
      eprint={2104.02112},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
    }
```

