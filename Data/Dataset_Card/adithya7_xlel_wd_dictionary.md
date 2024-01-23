---
annotations_creators:
- found
language_creators:
- found
language:
- af
- ar
- be
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- fa
- fi
- fr
- he
- hi
- hu
- id
- it
- ja
- ko
- ml
- mr
- ms
- nl
- 'no'
- pl
- pt
- ro
- ru
- si
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- vi
- zh
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: XLEL-WD is a multilingual event linking dataset. This supplementary dataset
  contains a dictionary of event items from Wikidata. The descriptions for Wikidata
  event items are taken from the corresponding multilingual Wikipedia articles.
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories: []
task_ids: []
---

# Dataset Card for XLEL-WD-Dictionary

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

- **Homepage:** <https://github.com/adithya7/xlel-wd>
- **Repository:** <https://github.com/adithya7/xlel-wd>
- **Paper:** <https://arxiv.org/abs/2204.06535>
- **Leaderboard:** N/A
- **Point of Contact:** Adithya Pratapa

### Dataset Summary

XLEL-WD is a multilingual event linking dataset. This supplementary dataset contains a dictionary of event items from Wikidata. The descriptions for Wikidata event items are taken from the corresponding multilingual Wikipedia articles.

### Supported Tasks and Leaderboards

This dictionary can be used as a part of the event linking task.

### Languages

This dataset contains text from 44 languages. The language names and their ISO 639-1 codes are listed below. For details on the dataset distribution for each language, refer to the original paper.

| Language     | Code | Language     | Code | Language     | Code | Language     | Code |
| --------     | ---- | --------     | ---- | --------     | ---- | --------     | ---- |
| Afrikaans  | af  | Arabic  | ar  | Belarusian  | be  | Bulgarian  | bg  |
| Bengali  | bn  | Catalan  | ca  | Czech  | cs  | Danish  | da  |
| German  | de  | Greek  | el  | English  | en  | Spanish  | es  |
| Persian  | fa  | Finnish  | fi  | French  | fr  | Hebrew  | he  |
| Hindi  | hi  | Hungarian  | hu  | Indonesian  | id  | Italian  | it  |
| Japanese  | ja  | Korean  | ko  | Malayalam  | ml  | Marathi  | mr  |
| Malay  | ms  | Dutch  | nl  | Norwegian  | no  | Polish  | pl  |
| Portuguese  | pt  | Romanian  | ro  | Russian  | ru  | Sinhala  | si  |
| Slovak  | sk  | Slovene  | sl  | Serbian  | sr  | Swedish  | sv  |
| Swahili  | sw  | Tamil  | ta  | Telugu  | te  | Thai  | th  |
| Turkish  | tr  | Ukrainian  | uk  | Vietnamese  | vi  | Chinese  | zh  |

## Dataset Structure

### Data Instances

Each instance in the `label_dict.jsonl` file follows the below template,

```json
{
    "label_id": "830917",
    "label_title": "2010 European Aquatics Championships",
    "label_desc": "The 2010 European Aquatics Championships were held from 4–15 August 2010 in Budapest and Balatonfüred, Hungary. It was the fourth time that the city of Budapest hosts this event after 1926, 1958 and 2006. Events in swimming, diving, synchronised swimming (synchro) and open water swimming were scheduled.",
    "label_lang": "en"
}
```

### Data Fields

| Field | Meaning |
| ----- | ------- |
| `label_id` | Wikidata ID |
| `label_title` | Title for the event, as collected from the corresponding Wikipedia article |
| `label_desc` | Description for the event, as collected from the corresponding Wikipedia article  |
| `label_lang` | language used for the title and description |

### Data Splits

This dictionary has a single split, `dictionary`. It contains 10947 event items from Wikidata and a total of 114834 text descriptions collected from multilingual Wikipedia articles.

## Dataset Creation

### Curation Rationale

This datasets helps address the task of event linking. KB linking is extensively studied for entities, but its unclear if the same methodologies can be extended for linking mentions to events from KB. Event items are collected from Wikidata.

### Source Data

#### Initial Data Collection and Normalization

A Wikidata item is considered a potential event if it has spatial and temporal properties. The final event set is collected after post-processing for quality control.

#### Who are the source language producers?

The titles and descriptions for the events are written by Wikipedia contributors.

### Annotations

#### Annotation process

This dataset was automatically compiled from Wikidata. It was post-processed to improve data quality.

#### Who are the annotators?

Wikidata and Wikipedia contributors.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

This dictionary primarily contains eventive nouns from Wikidata. It does not include other event items from Wikidata such as disease outbreak (Q3241045), military offensive (Q2001676), war (Q198), etc.,

## Additional Information

### Dataset Curators

The dataset was curated by Adithya Pratapa, Rishubh Gupta and Teruko Mitamura. The code for collecting the dataset is available at [Github:xlel-wd](https://github.com/adithya7/xlel-wd).

### Licensing Information

XLEL-WD dataset is released under [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

```bib
@article{pratapa-etal-2022-multilingual,
  title = {Multilingual Event Linking to Wikidata},
  author = {Pratapa, Adithya and Gupta, Rishubh and Mitamura, Teruko},
  publisher = {arXiv},
  year = {2022},
  url = {https://arxiv.org/abs/2204.06535},
}
```

### Contributions

Thanks to [@adithya7](https://github.com/adithya7) for adding this dataset.
