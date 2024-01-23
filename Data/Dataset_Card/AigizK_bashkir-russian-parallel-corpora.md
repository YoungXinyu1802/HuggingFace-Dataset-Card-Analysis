---
dataset_info:
  features:
  - name: ba
    dtype: string
  - name: ru
    dtype: string
  - name: corpus
    dtype: string
  splits:
  - name: train
    num_bytes: 282054412
    num_examples: 702100
  download_size: 129601180
  dataset_size: 282054412
task_categories:
- translation
language:
- ba
- ru
license: cc-by-4.0
---
# Dataset Card for "bashkir-russian-parallel-corpora"

### How the dataset was assembled.

1. find the text in two languages. it can be a translated book or an internet page (wikipedia, news site)
2. our algorithm tries to match Bashkir sentences with their translation in Russian
3. We give these pairs to people to check
```
@inproceedings{
title={Bashkir-Russian parallel corpora},
author={Iskander Shakirov, Aigiz Kunafin},
year={2023}
}
```