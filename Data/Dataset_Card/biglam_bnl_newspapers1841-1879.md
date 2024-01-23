---
annotations_creators:
- no-annotation
language:
- de
- fr
- lb
- nl
- la
- en
language_creators:
- expert-generated
license:
- cc0-1.0
multilinguality:
- multilingual
pretty_name: BnL Newspapers 1841-1879
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- newspapers
- 1800-1900
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---

# Dataset Card for bnl_newspapers1841-1879

## Table of Contents
- [Dataset Card for bnl_newspapers1841-1879](#dataset-card-for-bnl_newspapers1841-1879)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [size of dataset](#size-of-dataset)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://data.bnl.lu](https://data.bnl.lu)
- **Repository:** 
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** opendata at bnl.etat.lu

### Dataset Summary

630.709 articles from historical newspapers (1841-1879) along with metadata and the full text.

21 newspaper titles
24.415 newspaper issues
99.957 scanned pages
Transcribed using a variety of OCR engines and corrected using [https://github.com/natliblux/nautilusocr](https://github.com/natliblux/nautilusocr) (95% threshold)
Public Domain, CC0 (See copyright notice)

The newspapers used are:
- Der Arbeiter (1878)
- L'Arlequin (1848-1848)
- L'Avenir (1868-1871)
- Courrier du Grand-Duché de Luxembourg (1844-1868)
- Cäcilia (1863-1871)
- Diekircher Wochenblatt (1841-1848)
- Le Gratis luxembourgeois (1857-1858)
- L'Indépendance luxembourgeoise (1871-1879)
- Kirchlicher Anzeiger für die Diözese Luxemburg (1871-1879)
- La Gazette du Grand-Duché de Luxembourg (1878)
- Luxemburger Anzeiger (1856)
- Luxemburger Bauernzeitung (1857)
- Luxemburger Volks-Freund (1869-1876)
- Luxemburger Wort (1848-1879)
- Luxemburger Zeitung (1844-1845)
- Luxemburger Zeitung = Journal de Luxembourg (1858-1859)
- L'Union (1860-1871)
- Das Vaterland (1869-1870)
- Der Volksfreund (1848-1849)
- Der Wächter an der Sauer (1849-1869)
- D'Wäschfra (1868-1879)

### Supported Tasks and Leaderboards

### Languages

German, French, Luxembourgish

## Dataset Structure

JSONL file zipped.

### Data Instances

### Data Fields

- `identifier` : unique and persistent identifier using ARK for the Article.
- `date` : publishing date of the document e.g "1848-12-15".
- `metsType` : set to "newspaper".
- `newpaperTitle` : title of the newspaper. It is transcribed as in the masthead of the individual issue and can thus change.
- `paperID` : local identifier for the newspaper title. It remains the same, even for short-term title changes.
- `publisher` : publisher of the document e.g. "Verl. der St-Paulus-Druckerei".
- `title` : main title of the article, section, advertisement, etc.
- `text` : full text of the entire article, section, advertisement etc. It includes any titles and subtitles as well. The content does not contain layout information, such as headings, paragraphs or lines.
- `creator` : author of the article, section, advertisement etc. Most articles do not have an associated author.
- `type` : type of the exported data e.g. ARTICLE, SECTION, ADVERTISEMENT, ...

## Dataset Creation

The dataset was created by the National library of Luxembourg with the output of its newspaper digitisation program. 

### Curation Rationale

The selection of newspapers represent the current state of digitisation of the Luxembourg legal deposit collection of newspapers that are in the public domain. That means all newspapers printed in Luxembourg before and including 1879.

### Source Data

Printed historical newspapers.

#### Initial Data Collection and Normalization

The data was created through digitisation. The full digitisation specifications are available at [https://data.bnl.lu/data/historical-newspapers/](https://data.bnl.lu/data/historical-newspapers/)

### Annotations

#### Annotation process

During the digitisation process, newspaper pages were semi-automatically zoned into articles. This was done by external suppliers to the library according to the digitisation specifications.

#### Who are the annotators?

Staff at the external suppliers.

### Personal and Sensitive Information

The dataset contains only data that was published in a newspaper. Since it contains only articles before 1879, no living person is expected to be included.

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

The biases in the text represent the biases from newspaper editors and journalists at the time of the publication. In particular during the period from 1940/05/10 to 1944/09/10 the Nazi occupier controlled all information published. 

### Other Known Limitations

The OCR transcription is not perfect. It is estimated that the quality is 95% or better.

## Additional Information

### size of dataset

500MB-2GB

### Dataset Curators

This dataset is curated by the national library of Luxembourg (opendata at bnl.etat.lu).

### Licensing Information

Creative Commons Public Domain Dedication and Certification

### Citation Information

```
@misc{bnl_newspapers,
title={Historical Newspapers},
url={https://data.bnl.lu/data/historical-newspapers/},
author={ Bibliothèque nationale du Luxembourg},
```

### Contributions

Thanks to [@ymaurer](https://github.com/ymaurer) for adding this dataset.
