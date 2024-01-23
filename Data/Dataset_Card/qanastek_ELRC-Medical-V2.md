---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- en
- bg
- cs
- da
- de
- el
- es
- et
- fi
- fr
- ga
- hr
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
multilinguality:
- multilingual
pretty_name: ELRC-Medical-V2
size_categories:
- 100K<n<1M
source_datasets:
- extended
task_categories:
- translation
task_ids:
- translation
---

# ELRC-Medical-V2 : European parallel corpus for healthcare machine translation

## Table of Contents
- [Dataset Card for [Needs More Information]](#dataset-card-for-needs-more-information)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://live.european-language-grid.eu/catalogue/project/2209
- **Repository:** https://github.com/qanastek/ELRC-Medical-V2/
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Yanis Labrak](mailto:yanis.labrak@univ-avignon.fr)






### Dataset Summary

`ELRC-Medical-V2` is a parallel corpus for neural machine translation funded by the [European Commission](http://www.lr-coordination.eu/) and coordinated by the [German Research Center for Artificial Intelligence](https://www.dfki.de/web).  

### Supported Tasks and Leaderboards

`translation`: The dataset can be used to train a model for translation.

### Languages

In our case, the corpora consists of a pair of source and target sentences for 23 differents languages from the European Union (EU) with as source language in each cases english (EN).

**List of languages :** `Bulgarian (bg)`,`Czech (cs)`,`Danish (da)`,`German (de)`,`Greek (el)`,`Spanish (es)`,`Estonian (et)`,`Finnish (fi)`,`French (fr)`,`Irish (ga)`,`Croatian (hr)`,`Hungarian (hu)`,`Italian (it)`,`Lithuanian (lt)`,`Latvian (lv)`,`Maltese (mt)`,`Dutch (nl)`,`Polish (pl)`,`Portuguese (pt)`,`Romanian (ro)`,`Slovak (sk)`,`Slovenian (sl)`,`Swedish (sv)`.

## Load the dataset with HuggingFace

```python
from datasets import load_dataset

NAME = "qanastek/ELRC-Medical-V2"

dataset = load_dataset(NAME, use_auth_token=True)
print(dataset)

dataset_train = load_dataset(NAME, "en-es", split='train[:90%]')
dataset_test = load_dataset(NAME, "en-es", split='train[10%:]')
print(dataset_train)
print(dataset_train[0])
print(dataset_test)
```

## Dataset Structure

### Data Instances

```plain
id,lang,source_text,target_text
1,en-bg,"TOC \o ""1-3"" \h \z \u Introduction 3","TOC \o ""1-3"" \h \z \u Въведение 3"
2,en-bg,The international humanitarian law and its principles are often not respected.,Международното хуманитарно право и неговите принципи често не се зачитат.
3,en-bg,"At policy level, progress was made on several important initiatives.",На равнище политики напредък е постигнат по няколко важни инициативи.
```

### Data Fields

**id** : The document identifier of type `Integer`.

**lang** : The pair of source and target language of type `String`.

**source_text** : The source text of type `String`.

**target_text** : The target text of type `String`.

### Data Splits

| Lang   |   # Docs  |   Avg. # Source Tokens |   Avg. # Target Tokens |
|--------|-----------|------------------------|------------------------|
| bg     |    13 149 |                     23 |                     24 |
| cs     |    13 160 |                     23 |                     21 |
| da     |    13 242 |                     23 |                     22 |
| de     |    13 291 |                     23 |                     22 |
| el     |    13 091 |                     23 |                     26 |
| es     |    13 195 |                     23 |                     28 |
| et     |    13 016 |                     23 |                     17 |
| fi     |    12 942 |                     23 |                     16 |
| fr     |    13 149 |                     23 |                     28 |
| ga     |       412 |                     12 |                     12 |
| hr     |    12 836 |                     23 |                     21 |
| hu     |    13 025 |                     23 |                     21 |
| it     |    13 059 |                     23 |                     25 |
| lt     |    12 580 |                     23 |                     18 |
| lv     |    13 044 |                     23 |                     19 |
| mt     |     3 093 |                     16 |                     14 |
| nl     |    13 191 |                     23 |                     25 |
| pl     |    12 761 |                     23 |                     22 |
| pt     |    13 148 |                     23 |                     26 |
| ro     |    13 163 |                     23 |                     25 |
| sk     |    12 926 |                     23 |                     20 |
| sl     |    13 208 |                     23 |                     21 |
| sv     |    13 099 |                     23 |                     21 |
|||||
| Total  |    277 780 |                  22.21 |                  21.47 |

## Dataset Creation

### Curation Rationale

For details, check the corresponding [pages](https://elrc-share.eu/repository/search/?q=mfsp%3A87ef9e5e8ac411ea913100155d026706e19a1a9f908b463c944490c36ba2f454&page=3).

### Source Data

#### Initial Data Collection and Normalization

The acquisition of bilingual data (from multilingual websites), normalization, cleaning, deduplication and identification of parallel documents have been done by [ILSP-FC tool](http://nlp.ilsp.gr/redmine/projects/ilsp-fc/wiki/Introduction). [Maligna aligner](https://github.com/loomchild/maligna) was used for alignment of segments. Merging/filtering of segment pairs has also been applied.

#### Who are the source language producers?

Every data of this corpora as been uploaded by [Vassilis Papavassiliou](mailto:vpapa@ilsp.gr) on [ELRC-Share](https://elrc-share.eu/repository/browse/bilingual-corpus-from-the-publications-office-of-the-eu-on-the-medical-domain-v2-en-fr/6b31b32e8ac411ea913100155d0267061547d9b3ec284584af19a2953baa8937/).

### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Considerations for Using the Data

### Other Known Limitations

The nature of the task introduce a variability in the quality of the target translations.

## Additional Information

### Dataset Curators

__ELRC-Medical-V2__: Labrak Yanis, Dufour Richard

__Bilingual corpus from the Publications Office of the EU on the medical domain v.2 (EN-XX) Corpus__: [Vassilis Papavassiliou](mailto:vpapa@ilsp.gr) and [others](https://live.european-language-grid.eu/catalogue/project/2209).

### Licensing Information

<a rel="license" href="https://elrc-share.eu/static/metashare/licences/CC-BY-4.0.pdf"><img alt="Attribution 4.0 International (CC BY 4.0) License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="https://elrc-share.eu/static/metashare/licences/CC-BY-4.0.pdf">Attribution 4.0 International (CC BY 4.0) License</a>.

### Citation Information

Please cite the following paper when using this model.

```latex
@inproceedings{losch-etal-2018-european,
    title = European Language Resource Coordination: Collecting Language Resources for Public Sector Multilingual Information Management,
    author = {
      L'osch, Andrea  and
      Mapelli, Valérie  and
      Piperidis, Stelios  and
      Vasiljevs, Andrejs  and
      Smal, Lilli  and
      Declerck, Thierry  and
      Schnur, Eileen  and
      Choukri, Khalid  and
      van Genabith, Josef
    },
    booktitle = Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018),
    month = may,
    year = 2018,
    address = Miyazaki, Japan,
    publisher = European Language Resources Association (ELRA),
    url = https://aclanthology.org/L18-1213,
}
```
