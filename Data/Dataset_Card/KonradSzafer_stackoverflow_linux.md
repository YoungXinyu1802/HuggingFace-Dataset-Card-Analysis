---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 303464
    num_examples: 270
  - name: test
    num_bytes: 37456
    num_examples: 30
  download_size: 172425
  dataset_size: 340920
task_categories:
- question-answering
language:
- en
pretty_name: Stack Overflow Linux
size_categories:
- n<1K
---
# Dataset Card for "stackoverflow_linux"

Dataset information:
- Source: Stack Overflow
- Category: Linux
- Number of samples: 300
- Train/Test split: 270/30
- Quality: Data come from the top 1k most upvoted questions

## Additional Information

### License

All Stack Overflow user contributions are licensed under CC-BY-SA 3.0 with attribution required.

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)