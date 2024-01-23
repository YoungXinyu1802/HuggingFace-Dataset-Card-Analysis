---
language:
- en
tags:
- reddit
- law
pretty_name: Legal Advice Reddit
---

# Dataset Card for Legal Advice Reddit Dataset

## Dataset Description

- **Paper: [Parameter-Efficient Legal Domain Adaptation](https://aclanthology.org/2022.nllp-1.10/)** 
- **Point of Contact: jxl@queensu.ca** 

### Dataset Summary

New dataset introduced in [Parameter-Efficient Legal Domain Adaptation](https://aclanthology.org/2022.nllp-1.10) (Li et al., NLLP 2022) from the Legal Advice Reddit community (known as "/r/legaldvice"), sourcing the Reddit posts from the Pushshift
Reddit dataset. The dataset maps the text and title of each legal question posted into one of eleven classes, based on the original Reddit
post's "flair" (i.e., tag). Questions are typically informal and use non-legal-specific language. Per the Legal Advice Reddit rules, posts 
must be about actual personal circumstances or situations. We limit the number of labels to the top eleven classes and remove the other 
samples from the dataset.

### Citation Information
```
@inproceedings{li-etal-2022-parameter,
    title = "Parameter-Efficient Legal Domain Adaptation",
    author = "Li, Jonathan  and
      Bhambhoria, Rohan  and
      Zhu, Xiaodan",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.nllp-1.10",
    pages = "119--129",
}
```