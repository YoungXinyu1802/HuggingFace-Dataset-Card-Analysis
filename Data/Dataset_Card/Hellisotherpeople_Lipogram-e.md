---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- expert-generated
license:
- mit
multilinguality:
- monolingual
pretty_name: 'Lipogram-e from Most Language Models can be Poets too: An AI Writing Assistant and Constrained Text Generation Studio'
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- ctgs
- CTGS
- constrained-text-generation
- lipogram
- i-hate-the-letter-e
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---


# Dataset Card for Lipogram-e

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage**: https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio
- **Repository**: https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio
- **Paper** Most Language Models can be Poets too: An AI Writing Assistant
and Constrained Text Generation Studio
- **Leaderboard**: https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio
- **Point of Contact**: https://www.linkedin.com/in/allen-roush-27721011b/

### Dataset Summary

![Gadsby](https://upload.wikimedia.org/wikipedia/commons/1/1d/Gadsby_%28book_cover%29.jpg)
![Eunoia](https://upload.wikimedia.org/wikipedia/en/1/12/Eunoia_%28book%29.png)
![A Void](https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388699493i/28294.jpg)

This is a dataset of 3 English books which do not contain the letter "e" in them. This dataset includes all of "Gadsby" by Ernest Vincent Wright, all of "A Void" by Georges Perec, and almost all of "Eunoia" by Christian Bok (except for the single chapter that uses the letter "e" in it) 

This dataset is contributed as part of a paper titled "Most Language Models can be Poets too: An AI Writing Assistant and Constrained Text Generation Studio" to appear at COLING 2022. 

This dataset and the works within them are examples of Lipograms, which are works where a letter or string is systematically omitted. Lipograms are an example of hard-constrained writing.

### Supported Tasks and Leaderboards

The main task for this dataset is Constrained Text Generation - but all types of language modeling are suitable. 

### Languages

English

## Dataset Structure

### Data Instances

Each is extracted directly from the available pdf or epub documents converted to txt using pandoc.

### Data Fields

Text. The name of each work appears before the work starts and again at the end, so the books can be trivially split again if necessary. 

### Data Splits

None given. The way I do so in the paper is to extract the final 20% of each book, and concatenate these together. This may not be the most ideal way to do a train/test split, but I couldn't think of a better way. I did not believe randomly sampling was appropriate, but I could be wrong. 

## Dataset Creation

### Curation Rationale

One way that we could extract text from datasets that doesn't use the letter "e" in it would be to simply computationally parse through large existing datasets for blocks or sentences which don't have the letter "e" in them. Unfortunately, this is extremely unlikely to lead to coherent or meaningful text. Doing so over increasingly large blocks or spans is likely to result in fewer and fewer examples. While the preparation of such a dataset would be fascinating in its own right - it is more interesting from the perspective of fine-tuning language models to have large scale prose narratives which fulfill the given constraint. This constraint of omitting the letter "e" is attractive because several book length works exist which do this.

### Source Data

#### Initial Data Collection and Normalization

Project Gutenberg

#### Who are the source language producers?
Ernest Vincent Wright
Georges Perec
Christian Bok


### Annotations

#### Annotation process

None

#### Who are the annotators?

n/a

### Personal and Sensitive Information

None

## Considerations for Using the Data

There may be conversion artifacts. I noticed 3 cases of the letter "e" being hallucinated from the pdf conversion of "a void" that I had to fix manually. They were reading special characters as the letter "e", and were not due to the authors making mistakes themselves. This implies that at least a few OCR errors exist. 

### Social Impact of Dataset

These books have existed for a awhile now, so it's unlikely that this will have dramatic Social Impact. 

### Discussion of Biases

This dataset is 100% biased against the letter "e". There may be biases present in contents of these works. It's recommended to read the books before using this in any non research application to verify that they are not problematic. 

### Other Known Limitations

It's possible that more works exist but were not well known enough for the authors to find them and include them. Finding such inclusions would be grounds for iteration of this dataset (e.g. a version 1.1 would be released). The goal of this project is to eventually encompass all book length english language "e" lipograms. 

## Additional Information
n/a

### Dataset Curators

Allen Roush

### Licensing Information

MIT

### Citation Information
TBA

### Contributions

Thanks to [@Hellisotherpeople](https://github.com/Hellisotherpeople) for adding this dataset.
