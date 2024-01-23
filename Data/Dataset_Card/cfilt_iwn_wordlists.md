---
annotations_creators:
- Shivam Mhaskar, Diptesh Kanojia
language_creators:
- found
language:
- as
- bn
- mni
- gu
- hi
- kn
- ks
- kok
- ml
- mr
- or
- ne
- pa
- sa
- ta
- te
- ur
license: cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids: []
paperswithcode_id: plod-filtered
pretty_name: 'PLOD: An Abbreviation Detection Dataset'
tags:
- abbreviation-detection
---

<p align="center"><img src="https://huggingface.co/datasets/cfilt/HiNER-collapsed/raw/main/cfilt-dark-vec.png" alt="Computation for Indian Language Technology Logo" width="150" height="150"/></p>

# IWN Wordlists

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%20--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![Twitter Follow](https://img.shields.io/twitter/follow/cfiltnlp?color=1DA1F2&logo=twitter&style=flat-square)](https://twitter.com/cfiltnlp) [![Twitter Follow](https://img.shields.io/twitter/follow/PeopleCentredAI?color=1DA1F2&logo=twitter&style=flat-square)](https://twitter.com/PeopleCentredAI)


We provide the unique word list form the [IndoWordnet (IWN)](https://www.cfilt.iitb.ac.in/indowordnet/) knowledge base.

## Usage
```python
from datasets import load_dataset
language = "hindi" // supported languages: assamese, bengali, bodo, gujarati, hindi, kannada, kashmiri, konkani, malayalam, manipuri, marathi, meitei, nepali, oriya, punjabi, sanskrit, tamil, telugu, urdu.
words = load_dataset("cfilt/iwn_wordlists", language)
word_list = words["train"]["word"]
```

## Citation
```latex
@inproceedings{bhattacharyya2010indowordnet,
  title={IndoWordNet},
  author={Bhattacharyya, Pushpak},
  booktitle={Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC'10)},
  year={2010}
}
```