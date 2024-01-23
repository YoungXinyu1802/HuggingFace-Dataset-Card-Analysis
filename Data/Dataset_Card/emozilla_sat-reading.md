---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: answer
    dtype: string
  - name: requires_line
    dtype: bool
  - name: id
    dtype: string
  splits:
  - name: train
    num_bytes: 1399648
    num_examples: 298
  - name: test
    num_bytes: 196027
    num_examples: 38
  - name: validation
    num_bytes: 183162
    num_examples: 39
  download_size: 365469
  dataset_size: 1778837
language:
- en
---
# Dataset Card for "sat-reading"

This dataset contains the passages and questions from the Reading part of ten publicly available SAT Practice Tests.
For more information see the blog post [Language Models vs. The SAT Reading Test](https://jeffq.com/blog/language-models-vs-the-sat-reading-test).

For each question, the reading passage from the section it is contained in is prefixed.
Then, the question is prompted with `Question #:`, followed by the four possible answers.
Each entry ends with `Answer:`.
Questions which reference a diagram, chart, table, etc. have been removed (typically three per test).
In addition, there is a boolean `requires_line` feature, which indiciates if the question references specific lines within the passage.
To maintain generalizability in finetuning scenarios, `SAT READING COMPREHENSION TEST` appears at the beginning of each entry -- it may be desireable to remove this depending on your intentions.

Eight tests appear in the training split; one each in the validation and test splits.
