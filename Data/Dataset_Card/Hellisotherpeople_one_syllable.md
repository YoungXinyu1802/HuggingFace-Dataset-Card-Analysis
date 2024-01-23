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
pretty_name: 'one_syllable from Most Language Models can be Poets too: An AI Writing Assistant and Constrained Text Generation Studio'
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- syllable
- one_syllable
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

![Gadsby](https://www.gutenberg.org/cache/epub/6936/pg6936.cover.medium.jpg)


This is a dataset of English books which only write using one syllable at a time. At this time, the dataset only contains Robinson Crusoe — in Words of One Syllable by Lucy Aikin and Daniel Defoe

This dataset is contributed as part of a paper titled "Most Language Models can be Poets too: An AI Writing Assistant and Constrained Text Generation Studio" to appear at COLING 2022. This dataset does not appear in the paper itself, but was gathered as a candidate constrained text generation dataset.  

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

There are several books which claim to only be written using one syllable words. A list of them can be found here: https://diyhomeschooler.com/2017/01/25/classics-in-words-of-one-syllable-free-ebooks/

Unfortunately, after careful human inspection, it appears that only one of these works actually does reliably maintain the one syllable constraint through the whole text. Outside of proper names, I cannot spot or computationally find a single example of a more-than-one-syllable word in this whole work. 


### Source Data

Robinson Crusoe — in Words of One Syllable by Lucy Aikin and Daniel Defoe

#### Initial Data Collection and Normalization

Project Gutenberg

#### Who are the source language producers?
Lucy Aikin and Daniel Defoe


### Annotations

#### Annotation process

None

#### Who are the annotators?

n/a

### Personal and Sensitive Information

None

## Considerations for Using the Data

There may be OCR conversion artifacts.

### Social Impact of Dataset

These books have existed for a awhile now, so it's unlikely that this will have dramatic Social Impact. 

### Discussion of Biases

The only biases possible are related to the contents of Robinson Crusoe or the possibility of the authors changing Robinson Crusoe in some problematic way by using one-syllable words. This is unlikely, as this work was aimed at children. 

### Other Known Limitations

It's possible that more works exist but were not well known enough for the authors to find them and include them. Finding such inclusions would be grounds for iteration of this dataset (e.g. a version 1.1 would be released). The goal of this project is to eventually encompass all book length english language works that do not use more than one syllable in each of their words (except for names) 

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
