---
annotations_creators:
- machine-generated
language:
- fa
- ru
- zh
language_creators:
- machine-generated
multilinguality:
- multilingual
pretty_name: NeuMARCO
size_categories:
- 1M<n<10M
source_datasets:
- extended|irds/msmarco-passage
tags: []
task_categories:
- text-retrieval
---

# Dataset Card for NeuMARCO

## Dataset Description

- **Website:** https://neuclir.github.io/

### Dataset Summary

This is the dataset created for TREC 2022 NeuCLIR Track. The collection consists of documents from [`msmarco-passage`](https://ir-datasets.com/msmarco-passage) translated into
Chinese, Persian, and Russian.

### Languages

 - Chinese
 - Persian
 - Russian

## Dataset Structure

### Data Instances

| Split           | Documents |
|-----------------|----------:|
| `fas` (Persian) |      8.8M |
| `rus` (Russian) |      8.8M |
| `zho` (Chinese) |      8.8M |

### Data Fields
 - `doc_id`: unique identifier for this document
 - `text`: translated passage text

## Dataset Usage

Using 🤗 Datasets:

```python
from datasets import load_dataset

dataset = load_dataset('neuclir/neumarco')
dataset['fas'] # Persian passages
dataset['rus'] # Russian passages
dataset['zho'] # Chinese passages
```
