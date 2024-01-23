---
annotations_creators: []
language:
- ch
language_creators:
- found
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
pretty_name: ArchiMob Corpus
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- dialect
task_categories:
- text-generation
- text-classification
task_ids:
- language-modeling
---

# Dataset Card for ArchiMod Corpus

## Dataset Description

- **Homepage:** https://wortschatz.uni-leipzig.de/en/download/Swiss%20German
- **Repository:** https://huggingface.co/datasets/statworx/leipzip-swiss

### Dataset Summary

The ArchiMob corpus represents German linguistic varieties spoken within the territory of Switzerland. This corpus is the first electronic resource containing long samples of transcribed text in Swiss German, intended for studying the spatial distribution of morphosyntactic features and for natural language processing.

### Languages

Swiss-German

## Dataset Structure

### Data Instances

``
{
  'sentence': Sentence in Swiss-German,
  'label': Dialect as category
}
``

### Data Fields

`sentence`: Text as string.
`label`: Label as string.

### Data Splits

[More Information Needed]

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

https://www.spur.uzh.ch/en/departments/research/textgroup/ArchiMob.html

## Additional Information

### Licensing Information

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

### Citation Information

Scherrer, Y., T. Samardžić, E. Glaser (2019). "Digitising Swiss German -- How to process and study a polycentric spoken language". Language Resources and Evaluation. (First online) 

Scherrer, Y., T. Samardžić, E. Glaser (2019). "ArchiMob: Ein multidialektales Korpus schweizerdeutscher Spontansprache". Linguistik Online, 98(5), 425-454. https://doi.org/10.13092/lo.98.5947
