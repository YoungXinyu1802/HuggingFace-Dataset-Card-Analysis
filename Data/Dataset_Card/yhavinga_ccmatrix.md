---
annotations_creators:
- found
language_creators:
- found
language:
- af
- am
- ar
- ast
- az
- be
- bg
- bn
- br
- ca
- ceb
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- ha
- he
- hi
- hr
- hu
- hy
- id
- ig
- ilo
- is
- it
- ja
- jv
- ka
- kk
- km
- ko
- la
- lb
- lg
- lt
- lv
- mg
- mk
- ml
- mr
- ms
- my
- ne
- nl
- 'no'
- oc
- om
- or
- pl
- pt
- ro
- ru
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- tl
- tr
- tt
- uk
- ur
- uz
- vi
- wo
- xh
- yi
- yo
- zh
- zu
- se
license:
- unknown
multilinguality:
- multilingual
size_categories:
  en-nl:
  - n<110M
  en-af:
  - n<9M
  en-lt:
  - <24M
source_datasets:
- original
task_categories:
- text2text-generation
- translation
task_ids: []
paperswithcode_id: ccmatrix
pretty_name: CCMatrixV1
tags:
- conditional-text-generation
---

# Dataset Card for CCMatrix v1

## Table of Contents
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
- **Homepage:** https://opus.nlpl.eu/CCMatrix.php
- **Repository:** None
- **Paper:** https://arxiv.org/abs/1911.04944
### Dataset Summary

This corpus has been extracted from web crawls using the margin-based bitext mining techniques described at https://github.com/facebookresearch/LASER/tree/master/tasks/CCMatrix.

* 90 languages, 1,197 bitexts
* total number of files: 90
* total number of tokens: 112.14G
* total number of sentence fragments: 7.37G

### Supported Tasks and Leaderboards
[More Information Needed]

### Languages

Configs are generated for all language pairs in both directions.
You can find the valid pairs in Homepage section of Dataset Description: https://opus.nlpl.eu/CCMatrix.php
E.g.

```
from datasets import load_dataset
dataset = load_dataset("yhavinga/ccmatrix", "en-nl", streaming=True)
```

This will open the `en-nl` dataset in streaming mode. Without streaming, download and prepare will take tens of minutes.
You can inspect elements with:

```
print(next(iter(dataset['train'])))
{'id': 0, 'score': 1.2499677, 'translation': {'en': 'They come from all parts of Egypt, just like they will at the day of His coming.', 'nl': 'Zij kwamen uit alle delen van Egypte, evenals zij op de dag van Zijn komst zullen doen.'}}
```

## Dataset Structure
### Data Instances
For example:

```json
{
        "id": 1,
        "score": 1.2498379,
        "translation": {
            "nl": "En we moeten elke waarheid vals noemen die niet minstens door een lach vergezeld ging.”",
            "en": "And we should call every truth false which was not accompanied by at least one laugh.”"
        }
    }
```

### Data Fields
Each example contains an integer id starting with 0, a score, and a translation dictionary with the language 1 and
language 2 texts.

### Data Splits
Only a `train` split is provided.

## Dataset Creation
### Curation Rationale
[More Information Needed]
### Source Data
[More Information Needed]
#### Initial Data Collection and Normalization
[More Information Needed]
#### Who are the source language producers?
[More Information Needed]
### Annotations
[More Information Needed]
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

IMPORTANT: Please cite reference [2][3] if you use this data.

1. **[CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data](https://arxiv.org/abs/1911.00359)**
   by *Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand Jouli
    and Edouard Grave*.
2. **[CCMatrix: Mining Billions of High-Quality Parallel Sentences on the WEB](https://arxiv.org/abs/1911.04944)** by *Holger Schwenk, Guillaume Wenzek, Sergey Edunov, Edouard Grave and Armand Joulin*.
3. **[Beyond English-Centric Multilingual Machine Translation](https://arxiv.org/abs/2010.11125)** by *Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal, Mandeep Baines,
    Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, Naman Goyal, Tom Birch, Vitaliy Liptchinsky,
    Sergey Edunov, Edouard Grave, Michael Auli, and Armand Joulin.*

This HuggingFace CCMatrix dataset is a wrapper around the service and files prepared and hosted by OPUS:

* **[Parallel Data, Tools and Interfaces in OPUS](https://www.aclweb.org/anthology/L12-1246/)** by *Jörg Tiedemann*.

### Contributions
