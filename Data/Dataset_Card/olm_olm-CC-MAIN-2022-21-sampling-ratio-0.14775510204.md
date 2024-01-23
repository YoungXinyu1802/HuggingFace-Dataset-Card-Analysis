---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- found
license: []
multilinguality:
- monolingual
pretty_name: OLM May 2022 Common Crawl
size_categories:
- 10M<n<100M
source_datasets: []
tags:
- pretraining
- language modelling
- common crawl
- web
task_categories: []
task_ids: []
---

# Dataset Card for OLM May 2022 Common Crawl

Cleaned and deduplicated pretraining dataset, created with the OLM repo [here](https://github.com/huggingface/olm-datasets) from 15% of the May 2022 Common Crawl snapshot.

Note: `last_modified_timestamp` was parsed from whatever a website returned in it's `Last-Modified` header; there are likely a small number of outliers that are incorrect, so we recommend removing the outliers before doing statistics with `last_modified_timestamp`.