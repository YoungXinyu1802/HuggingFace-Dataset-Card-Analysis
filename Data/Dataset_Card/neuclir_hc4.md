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
pretty_name: HC4
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

# Dataset Card for HC4

## Dataset Description

- **Repository:** https://github.com/hltcoe/HC4
- **Paper:** https://arxiv.org/abs/2201.09992

### Dataset Summary

HC4 is a suite of test collections for ad hoc Cross-Language Information Retrieval (CLIR), with Common Crawl News documents in Chinese, Persian, and Russian. The documents
are Web pages from Common Crawl in Chinese, Persian, and Russian.

### Languages

 - Chinese
 - Persian
 - Russian

## Dataset Structure

### Data Instances

| Split           | Documents |
|-----------------|----------:|
| `fas` (Persian) |      486K |
| `rus` (Russian) |      4.7M |
| `zho` (Chinese) |      646K |

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

dataset = load_dataset('neuclir/hc4')
dataset['fas'] # Persian documents
dataset['rus'] # Russian documents
dataset['zho'] # Chinese documents
```

## Citation Information

```
@article{Lawrie2022HC4,
  author = {Dawn Lawrie and James Mayfield and Douglas W. Oard and Eugene Yang},
  title = {HC4: A New Suite of Test Collections for Ad Hoc CLIR},
  booktitle = {{Advances in Information Retrieval. 44th European Conference on IR Research (ECIR 2022)},
  year = {2022},
  month = apr,
  publisher = {Springer},
  series = {Lecture Notes in Computer Science},
  site = {Stavanger, Norway},
  url = {https://arxiv.org/abs/2201.09992}
}
```
