---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: answer
    dtype: string
  - name: question
    dtype: string
  splits:
  - name: train
    num_bytes: 5119086
    num_examples: 3296
  download_size: 1939470
  dataset_size: 5119086
task_categories:
- question-answering
language:
- en
pretty_name: Stack Overflow Python - Preprocessed
size_categories:
- 1K<n<10K
---
# Dataset Card for "stackoverflow_python_preprocessed"

This is a preprocessed version of the [stackoverflow_python] dataset.
Questions and answers were filtered to only include questions with more than 100 votes and answers with more than 5 votes.
The dataset has been converted from HTML to plain text and only includes the title, question, and answer columns.

## Additional Information

### License

All Stack Overflow user contributions are licensed under CC-BY-SA 3.0 with attribution required.

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)