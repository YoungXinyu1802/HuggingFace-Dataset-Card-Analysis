---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- es
multilinguality:
- monolingual
pretty_name: MSMARCO_ES
size_categories:
- 100K<n<1M
source_datasets:
- ms_marco
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---
# MSMARCO_ES
This is an automatically translated version of the [msmarco v1 dataset](https://huggingface.co/datasets/ms_marco) , a dataset used for text similarity tasks.
The translation was performed for the queries and passages using the [marianMT english-spanish](https://huggingface.co/Helsinki-NLP/opus-mt-en-es) . A posterior processing was required to sample the querys because there was some of them with more or less positive and negative labels than the recommended (4 neg and 1 pos).

License, distribution and usage conditions of the original dataset apply.

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this dataset.