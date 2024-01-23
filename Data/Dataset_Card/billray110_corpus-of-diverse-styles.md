---
annotations_creators: []
language_creators:
- found
language: []
license: []
multilinguality:
- monolingual
pretty_name: Corpus of Diverse Styles
size_categories:
- 10M<n<100M
source_datasets: []
task_categories:
- text-classification
task_ids: []
---

# Dataset Card for Corpus of Diverse Styles



## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)

## Disclaimer
I am not the original author of the paper that presents the Corpus of Diverse Styles. I uploaded the dataset to HuggingFace as a convenience. 

## Dataset Description

- **Homepage:** http://style.cs.umass.edu/
- **Repository:** https://github.com/martiansideofthemoon/style-transfer-paraphrase
- **Paper:** https://arxiv.org/abs/2010.05700

### Dataset Summary

A new benchmark dataset that contains 15M
sentences from 11 diverse styles.

To create CDS, we obtain data from existing academic
research datasets and public APIs or online collections
like Project Gutenberg. We choose
styles that are easy for human readers to identify at
a sentence level (e.g., Tweets or Biblical text). While
prior benchmarks involve a transfer between two
styles, CDS has 110 potential transfer directions.

### Citation Information
```
@inproceedings{style20,
author={Kalpesh Krishna and John Wieting and Mohit Iyyer},
Booktitle = {Empirical Methods in Natural Language Processing},
Year = "2020",
Title={Reformulating Unsupervised Style Transfer as Paraphrase Generation},
}
```