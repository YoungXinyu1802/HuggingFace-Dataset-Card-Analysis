---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: Incivility in Arizona Daily Star Comments
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- social media
- incivility
- aspersion
- hyperbole
- lying
- namecalling
- noncooperation
- pejorative
- sarcasm
- vulgarity
task_categories:
- text-classification
task_ids:
- multi-label-classification
dataset_info:
  features:
  - name: text
    dtype: string
  - name: aspersion
    dtype: int64
  - name: hyperbole
    dtype: int64
  - name: lying
    dtype: int64
  - name: namecalling
    dtype: int64
  - name: noncooperation
    dtype: int64
  - name: offtopic
    dtype: int64
  - name: other_incivility
    dtype: int64
  - name: pejorative
    dtype: int64
  - name: sarcasm
    dtype: int64
  - name: vulgarity
    dtype: int64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 1568771
    num_examples: 3910
  - name: validation
    num_bytes: 398667
    num_examples: 976
  - name: test
    num_bytes: 486262
    num_examples: 1228
  download_size: 1400753
  dataset_size: 2453700
---

# Dataset Card for incivility-arizona-daily-star-comments

This is a collection of more than 6000 comments on Arizona Daily Star news articles from 2011 that have been manually annotated for various forms of incivility including aspersion, namecalling, sarcasm, and vulgarity.

## Dataset Structure

Each instance in the dataset corresponds to a single comment from a single commenter.

An instance's `text` field contains the text of the comment with any quotes of other commenters removed.
The remaining fields in each instance provide binary labels for each type of incivility annotated:
`aspersion`, `hyperbole`, `lying`, `namecalling`, `noncooperation`, `offtopic`, `pejorative`, `sarcasm`, `vulgarity`, and `other_incivility`.

The dataset provides three standard splits: `train`, `validation`, and `test`.

## Dataset Creation

The original annotation effort is described in:

- Kevin Coe, Kate Kenski, Stephen A. Rains.
  [Online and Uncivil? Patterns and Determinants of Incivility in Newspaper Website Comments](https://doi.org/10.1111/jcom.12104).
  Journal of Communication, Volume 64, Issue 4, August 2014, Pages 658–679.

That dataset was converted to a computer-friendly form as described in section 4.2.1 of:

- Farig Sadeque.
  [User behavior in social media: engagement, incivility, and depression](https://repository.arizona.edu/handle/10150/633192).
  PhD thesis. The University of Arizona. 2019.

The current upload is a 2023 conversion of that form to a huggingface Dataset.

## Considerations for Using the Data

The data is intended for the study of incivility.
It should not be used to train models to generate incivility.

The human coders and their trainers were mostly [Western, educated, industrialized, rich and democratic (WEIRD)](https://www.nature.com/articles/466029a), which may have shaped how they evaluated incivility.

## Citation

```bibtex
@article{10.1111/jcom.12104,
    author = {Coe, Kevin and Kenski, Kate and Rains, Stephen A.},
    title = {Online and Uncivil? Patterns and Determinants of Incivility in Newspaper Website Comments},
    journal = {Journal of Communication},
    volume = {64},
    number = {4},
    pages = {658-679},
    year = {2014},
    month = {06},
    issn = {0021-9916},
    doi = {10.1111/jcom.12104},
    url = {https://doi.org/10.1111/jcom.12104},
}
```