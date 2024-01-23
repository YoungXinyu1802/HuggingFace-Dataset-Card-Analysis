---
source_datasets: kmfoda/booksum
license:
- bsd-3-clause
train-eval-index:
- config: pszemraj--booksum_short
  task: summarization
  task_id: summarization
  splits:
    eval_split: test
  col_mapping:
    chapter: text
    summary_text: target
task_categories:
- summarization
- text2text-generation
language:
- en
tags:
- booksum
- long-document
size_categories:
- 10K<n<100K
---
---


# booksum short


`BookSum` but all summaries with length greater than 512 `long-t5` tokens are filtered out.

The columns `chapter_length` and `summary_length` **in this dataset** have been updated to reflect the total of Long-T5 tokens in the respective source text.

## Token Length Distribution for inputs

![distribution](https://i.imgur.com/Cv37odF.png)