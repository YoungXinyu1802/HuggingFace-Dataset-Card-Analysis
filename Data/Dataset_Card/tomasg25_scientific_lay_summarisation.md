---
annotations_creators:
- found
language:
- en
language_creators:
- found
license:
- unknown
multilinguality:
- monolingual
pretty_name: ScientificLaySummarisation
size_categories:
- 10K<n<100K
- 1K<n<10K
source_datasets:
- original
tags:
- abstractive-summarization
- scientific-papers
- lay-summarization
- PLOS
- eLife
task_categories:
- summarization
task_ids: []
---

# Dataset Card for "scientific_lay_summarisation"

- **Repository:** https://github.com/TGoldsack1/Corpora_for_Lay_Summarisation
- **Paper:** [Making Science Simple: Corpora for the Lay Summarisation of Scientific Literature](https://arxiv.org/abs/2210.09932)
- **Size of downloaded dataset files:** 850.44 MB
- **Size of the generated dataset:** 1.32 GB
- **Total amount of disk used:** 2.17 GB

### Dataset Summary

This repository contains the PLOS and eLife datasets, introduced in the EMNLP 2022 paper "[Making Science Simple: Corpora for the Lay Summarisation of Scientific Literature
](https://arxiv.org/abs/2210.09932)" . 

Each dataset contains full biomedical research articles paired with expert-written lay summaries (i.e., non-technical summaries). PLOS articles are derived from various journals published by [the Public Library of Science (PLOS)](https://plos.org/), whereas eLife articles are derived from the [eLife](https://elifesciences.org/) journal. More details/analyses on the content of each dataset are provided in the paper.

Both "elife" and "plos" have 6 features:

    - "article": the body of the document (including the abstract), sections separated by "/n".
    - "section_headings": the title of each section, separated by "/n". 
    - "keywords": keywords describing the topic of the article, separated by "/n".
    - "title": the title of the article.
    - "year": the year the article was published.
    - "summary": the lay summary of the document.
  
  
**Note:** The format of both datasets differs from that used in the original repository (given above) in order to make them compatible with the `run_summarization.py` script of Transformers. Specifically, sentence tokenization is removed via " ".join(text), and the abstract and article sections, previously lists of sentences, are combined into a single `string` feature ("article") with each section separated by "\n". For the sentence-tokenized version of the dataset, please use the original git repository.
    
### Supported Tasks and Leaderboards

Papers with code - [PLOS](https://paperswithcode.com/sota/lay-summarization-on-plos) and [eLife](https://paperswithcode.com/sota/lay-summarization-on-elife).

### Languages

English

## Dataset Structure

### Data Instances

#### plos

- **Size of downloaded dataset files:** 425.22 MB
- **Size of the generated dataset:** 1.05 GB
- **Total amount of disk used:** 1.47 GB

An example of 'train' looks as follows.
```
This example was too long and was cropped:
{
    "summary": "In the kidney , structures known as nephrons are responsible for collecting metabolic waste . Nephrons are composed of a ...",
    "article": "Kidney function depends on the nephron , which comprises a 'blood filter , a tubule that is subdivided into functionally ...",
    "section_headings": "Abstract\nIntroduction\nResults\nDiscussion\nMaterials and Methods'",
    "keywords": "developmental biology\ndanio (zebrafish)\nvertebrates\nteleost fishes\nnephrology",
    "title": "The cdx Genes and Retinoic Acid Control the Positioning and Segmentation of the Zebrafish Pronephros",
    "year": "2007"
}
```


#### elife

- **Size of downloaded dataset files:** 425.22 MB
- **Size of the generated dataset:** 275.99 MB
- **Total amount of disk used:** 1.47 MB

An example of 'train' looks as follows.
```
This example was too long and was cropped:
{
    "summary": "In the USA , more deaths happen in the winter than the summer . But when deaths occur varies greatly by sex , age , cause of ...",
    "article": "In temperate climates , winter deaths exceed summer ones . However , there is limited information on the timing and the ...",
    "section_headings": "Abstract\nIntroduction\nResults\nDiscussion\nMaterials and methods",
    "keywords": "epidemiology and global health",
    "title": "National and regional seasonal dynamics of all-cause and cause-specific mortality in the USA from 1980 to 2016",
    "year": "2018"
}
```

### Data Fields

The data fields are the same among all splits.

#### plos

- `article`: a `string` feature.
- `section_headings`: a `string` feature.
- `keywords`: a `string` feature.
- `title` : a `string` feature.
- `year` : a `string` feature.
- `summary`: a `string` feature.


#### elife

- `article`: a `string` feature.
- `section_headings`: a `string` feature.
- `keywords`: a `string` feature.
- `title` : a `string` feature.
- `year` : a `string` feature.
- `summary`: a `string` feature.

### Data Splits

| name |train |validation|test|
|------|-----:|---------:|---:|
|plos  | 24773|      1376|1376|
|elife |  4346|       241| 241|


## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
"Making Science Simple: Corpora for the Lay Summarisation of Scientific Literature"
Tomas Goldsack, Zhihao Zhang, Chenghua Lin, Carolina Scarton
EMNLP 2022
```