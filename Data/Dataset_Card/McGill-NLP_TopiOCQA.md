---
annotations_creators:
- crowdsourced
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100k
task_categories:
- text-retrieval
- text-generation
- sequence-modeling
task_ids:
- open-domain-cqa
- conversational-question-answering
pretty_name: Open-domain Conversational Question Answering with Topic Switching
---
# Dataset Card for TopiOCQA

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [TopiOCQA homepage](https://mcgill-nlp.github.io/topiocqa/)
- **Repository:** [TopiOCQA Github](https://github.com/McGill-NLP/topiocqa)
- **Paper:** [Open-domain Conversational Question Answering with Topic Switching](https://arxiv.org/abs/2110.00768)
- **Point of Contact:** [Vaibhav Adlakha](mailto:vaibhav.adlakha@mila.quebec)

### Dataset Summary

TopiOCQA is an information-seeking conversational dataset with challenging topic switching phenomena.

### Languages

The language in the dataset is English as spoken by the crowdworkers. The BCP-47 code for English is en.

## Additional Information

### Licensing Information

TopiOCQA is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Citation Information

```
@inproceedings{adlakha2022topiocqa,
  title={Topi{OCQA}: Open-domain Conversational Question Answering with Topic Switching},
  author={Adlakha, Vaibhav and Dhuliawala, Shehzaad and Suleman, Kaheer and de Vries, Harm and Reddy, Siva},
  journal={Transactions of the Association for Computational Linguistics},
  volume = {10},
  pages = {468-483},
  year = {2022},
  month = {04},
  year={2022},
  issn = {2307-387X},
  doi = {10.1162/tacl_a_00471},
  url = {https://doi.org/10.1162/tacl\_a\_00471},
  eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00471/2008126/tacl\_a\_00471.pdf},
}
```