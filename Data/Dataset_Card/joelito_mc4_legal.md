---
annotations_creators:
- other
language_creators:
- found
language:
- bg 
- cs 
- da 
- de 
- el 
- en
- es 
- et 
- fi 
- fr 
- ga
- hu 
- it 
- lt 
- lv 
- mt
- nl 
- pl 
- pt 
- ro 
- sk 
- sl 
- sv
license:
- cc-by-4.0
multilinguality:
- multilingual
paperswithcode_id: null
pretty_name: "MC4_Legal: A Corpus Covering the Legal Part of MC4 for European Languages"
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# Dataset Card for MC4_Legal: A Corpus Covering the Legal Part of MC4 for European Languages

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
- **Repository:** [GitHub](https://github.com/JoelNiklaus/LegalDatasets/tree/main/pretrain/mc4_legal)
- **Paper:** 
- **Leaderboard:**
- **Point of Contact:** [Joel Niklaus](mailto:joel.niklaus.2@bfh.ch)

### Dataset Summary

This dataset contains large text resources (~133GB in total) from mc4 filtered for legal data that can be used for pretraining language models.

Use the dataset like this:
```python
from datasets import load_dataset
dataset = load_dataset("joelito/mc4_legal", "de", split='train', streaming=True)
```

### Supported Tasks and Leaderboards

The dataset supports the task of masked language modeling.

### Languages

The following languages are supported: bg, cs, da, de, el, en, es, et, fi, fr, ga, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv

## Dataset Structure

### Data Instances

The file format is jsonl.xz and there is one split available ("train"). 


| Source | Size (MB) | Tokens | Documents | Words/Document |
|-------:|----------:|-------:|----------:|---------------:|
|     bg |      13.9 |    xxx |       xxx |            xxx |
|     cs |    7252.4 |    xxx |       xxx |            xxx |
|     da |      37.7 |    xxx |       xxx |            xxx |
|     de |   27651.3 |    xxx |       xxx |            xxx |
|     el |      69.2 |    xxx |       xxx |            xxx |
|     en |   22043.9 |    xxx |       xxx |            xxx |
|     es |   21410.2 |    xxx |       xxx |            xxx |
|     et |     552.7 |    xxx |       xxx |            xxx |
|     fi |    8074.0 |    xxx |       xxx |            xxx |
|     fr |   10974.1 |    xxx |       xxx |            xxx |
|     ga |       3.5 |    xxx |       xxx |            xxx |
|     hu |    1450.0 |    xxx |       xxx |            xxx |
|     it |   12368.6 |    xxx |       xxx |            xxx |
|     lt |     175.9 |    xxx |       xxx |            xxx |
|     lv |       0.3 |    xxx |       xxx |            xxx |
|     mt |     227.7 |    xxx |       xxx |            xxx |
|     nl |      82.9 |    xxx |       xxx |            xxx |
|     pl |   10008.0 |    xxx |       xxx |            xxx |
|     pt |    4799.3 |    xxx |       xxx |            xxx |
|     ro |    2124.3 |    xxx |       xxx |            xxx |
|     sk |    1388.5 |    xxx |       xxx |            xxx |
|     sl |     404.6 |    xxx |       xxx |            xxx |
|     sv |    1888.1 |    xxx |       xxx |            xxx |
|  total |  133001.1 |    xxx |       xxx |            xxx |


### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

The dataset was created by filtering mc4 for legal data. 
We used terms indicating legal citations to get the texts. 
Note that this dataset can be quite noisy, and the quality is not known.

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

[More Information Needed]

### Contributions

Thanks to [@JoelNiklaus](https://github.com/joelniklaus) for adding this dataset.
