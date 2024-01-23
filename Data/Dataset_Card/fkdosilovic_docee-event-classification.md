---
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: DocEE
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- wiki
- news
- event-detection
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# Dataset Card for DocEE Dataset

## Dataset Description

- **Homepage:**
- **Repository:** [DocEE Dataset repository](https://github.com/tongmeihan1995/docee)
- **Paper:** [DocEE: A Large-Scale and Fine-grained Benchmark for Document-level Event Extraction](https://aclanthology.org/2022.naacl-main.291/)

### Dataset Summary

DocEE dataset is an English-language dataset containing more than 27k news and Wikipedia articles. Dataset is primarily annotated and collected for large-scale document-level event extraction.

### Data Fields

- `title`: TODO
- `text`: TODO
- `event_type`: TODO
- `date`: TODO
- `metadata`: TODO

**Note: this repo contains only event detection portion of the dataset.**

### Data Splits

The dataset has 2 splits: _train_ and _test_. Train split contains 21949 documents while test split contains 5536 documents. In total, dataset contains 27485 documents classified into 59 event types.

#### Differences from the original split(s)

Originally, the dataset is split into three splits: train, validation and test. For the purposes of this repository, original splits were joined back together and divided into train and test splits while making sure that splits were stratified across document sources (news and wiki) and event types.

Originally, the `title` column additionally contained information from `date` and `metadata` columns. They are now separated into three columns: `date`, `metadata` and `title`.