---
annotations_creators:
- expert-generated
language: []
language_creators: []
license:
- cc0-1.0
multilinguality: []
pretty_name: 19th Century United States Newspaper Advert images with 'illustrated'
  or 'non illustrated' labels
size_categories:
- n<1K
source_datasets: []
tags:
- lam
- historic newspapers
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
---


The Dataset contains images derived from the [Newspaper Navigator](https://news-navigator.labs.loc.gov/), a dataset of images drawn from the Library of Congress Chronicling America collection (chroniclingamerica.loc.gov/). 

> [The Newspaper Navigator dataset](https://news-navigator.labs.loc.gov/) consists of extracted visual content for 16,358,041 historic newspaper pages in Chronicling America. The visual content was identified using an object detection model trained on annotations of World War 1-era Chronicling America pages, including annotations made by volunteers as part of the Beyond Words crowdsourcing project. source: https://news-navigator.labs.loc.gov/

One of these categories is 'advertisements'. This dataset contains a sample of these images with additional labels indicating if the advert is 'illustrated' or 'not illustrated'.

This dataset was created for use in a [Programming Historian tutorial](http://programminghistorian.github.io/ph-submissions/lessons/computer-vision-deep-learning-pt1). The primary aim of the data was to provide a realistic example dataset for teaching computer vision for working with digitised heritage material.


# Dataset Card for 19th Century United States Newspaper Advert images with 'illustrated' or 'non illustrated' labels

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

- **Homepage:**
- **Repository:**[https://doi.org/10.5281/zenodo.5838410](https://doi.org/10.5281/zenodo.5838410)
- **Paper:**[https://doi.org/10.46430/phen0101](https://doi.org/10.46430/phen0101)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The Dataset contains images derived from the [Newspaper Navigator](news-navigator.labs.loc.gov/), a dataset of images drawn from the Library of Congress Chronicling America collection (chroniclingamerica.loc.gov/). 

> [The Newspaper Navigator dataset](https://news-navigator.labs.loc.gov/) consists of extracted visual content for 16,358,041 historic newspaper pages in Chronicling America. The visual content was identified using an object detection model trained on annotations of World War 1-era Chronicling America pages, including annotations made by volunteers as part of the Beyond Words crowdsourcing project. source: https://news-navigator.labs.loc.gov/

One of these categories is 'advertisements. This dataset contains a sample of these images with additional labels indicating if the advert is 'illustrated' or 'not illustrated'.

This dataset was created for use in a [Programming Historian tutorial](http://programminghistorian.github.io/ph-submissions/lessons/computer-vision-deep-learning-pt1). The primary aim of the data was to provide a realistic example dataset for teaching computer vision for working with digitised heritage material.


### Supported Tasks and Leaderboards

- `image-classification`: the primary purpose of this dataset is for classifying historic newspaper images identified as being 'advertisements' into 'illustrated' and 'not-illustrated' categories. 

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

An example instance from this dataset

``` python
{'file': 'pst_fenske_ver02_data_sn84026497_00280776129_1880042101_0834_002_6_96.jpg',
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=L size=388x395 at 0x7F9A72038950>,
 'label': 0,
 'pub_date': Timestamp('1880-04-21 00:00:00'),
 'page_seq_num': 834,
 'edition_seq_num': 1,
 'batch': 'pst_fenske_ver02',
 'lccn': 'sn84026497',
 'box': [0.649412214756012,
  0.6045778393745422,
  0.8002520799636841,
  0.7152365446090698],
 'score': 0.9609346985816956,
 'ocr': "H. II. IIASLKT & SOXN, Dealers in General Merchandise In New Store Room nt HASLET'S COS ITERS, 'JTionoMtii, ln. .Tau'y 1st, 1?0.",
 'place_of_publication': 'Tionesta, Pa.',
 'geographic_coverage': "['Pennsylvania--Forest--Tionesta']",
 'name': 'The Forest Republican. [volume]',
 'publisher': 'Ed. W. Smiley',
 'url': 'https://news-navigator.labs.loc.gov/data/pst_fenske_ver02/data/sn84026497/00280776129/1880042101/0834/002_6_96.jpg',
 'page_url': 'https://chroniclingamerica.loc.gov/data/batches/pst_fenske_ver02/data/sn84026497/00280776129/1880042101/0834.jp2'}
```
### Data Fields

[More Information Needed]

### Data Splits

The dataset contains a single split. 

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

A description of the annotation process is outlined in this [GitHub repository](https://github.com/Living-with-machines/nnanno)
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

``` bibtex
@dataset{van_strien_daniel_2021_5838410,
  author       = {van Strien, Daniel},
  title        = {{19th Century United States Newspaper Advert images 
                   with 'illustrated' or 'non illustrated' labels}},
  month        = oct,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {0.0.1},
  doi          = {10.5281/zenodo.5838410},
  url          = {https://doi.org/10.5281/zenodo.5838410}}

```


[More Information Needed]

### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
