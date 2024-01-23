---
annotations_creators:
- no-annotation
language:
- fa
- ru
- zh
language_creators:
- found
license:
- odc-by
multilinguality:
- multilingual
pretty_name: NeuCLIR1
size_categories:
- 1M<n<10M
source_datasets:
- extended|c4
tags: []
task_categories:
- text-retrieval
task_ids:
- document-retrieval
---

# Dataset Card for NeuCLIR1

## Dataset Description

- **Website:** https://neuclir.github.io/
- **Repository:** https://github.com/NeuCLIR/download-collection

### Dataset Summary

This is the dataset created for TREC 2022 NeuCLIR Track. The collection designed to be similar to HC4 and a large portion of documents from HC4 are ported to this collection.
The documents are Web pages from Common Crawl in Chinese, Persian, and Russian.

### Languages

 - Chinese
 - Persian
 - Russian

## Dataset Structure

### Data Instances

| Split           | Documents |
|-----------------|----------:|
| `fas` (Persian) |      2.2M |
| `rus` (Russian) |      4.6M |
| `zho` (Chinese) |      3.2M |

### Data Fields
 - `id`: unique identifier for this document
 - `cc_file`: source file from connon crawl
 - `time`: extracted date/time from article
 - `title`: title extracted from article
 - `text`: extracted article body
 - `url`: source URL

## Dataset Usage

Using 🤗 Datasets:

```python
from datasets import load_dataset

dataset = load_dataset('neuclir/neuclir1')
dataset['fas'] # Persian documents
dataset['rus'] # Russian documents
dataset['zho'] # Chinese documents
```
