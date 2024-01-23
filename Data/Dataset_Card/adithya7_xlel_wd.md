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
pretty_name: XLEL-WD is a multilingual event linking dataset. This dataset contains
  mention references in multilingual Wikipedia/Wikinews articles to event items from
  Wikidata. The descriptions for Wikidata event items are taken from the corresponding
  Wikipedia articles.
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories: []
task_ids: []
---

# Dataset Card for XLEL-WD

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

XLEL-WD is a multilingual event linking dataset. This dataset repo contains mention references in multilingual Wikipedia/Wikinews articles to event items from Wikidata.

The descriptions for Wikidata event items were collected from the corresponding Wikipedia articles. Download the event dictionary from [adithya7/xlel_wd_dictionary](https://huggingface.co/datasets/adithya7/xlel_wd_dictionary).

### Supported Tasks and Leaderboards

This dataset can be used for the task of event linking. There are two variants of the task, multilingual and crosslingual.

- Multilingual linking: mention and the event descriptions are in the same language.
- Crosslingual linking: the event descriptions are only available in English.

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

Each instance in the `train.jsonl`, `dev.jsonl` and `test.jsonl` files follow the below template.

```json
{
    "context_left": "Minibaev's first major international medal came in the men's synchronized 10 metre platform event at the ",
    "mention": "2010 European Championships",
    "context_right": ".",
    "context_lang": "en",
    "label_id": "830917",
}
```

### Data Fields

| Field | Meaning |
| ----- | ------- |
| `mention` | text span of the mention |
| `context_left` | left paragraph context from the document |
| `context_right` | right paragraph context from the document |
| `context_lang` | language of the context (and mention) |
| `context_title` | document title of the mention (only Wikinews subset) |
| `context_date` | document publication date of the mention (only Wikinews subset) |
| `label_id` | Wikidata label ID for the event. E.g. 830917 refers to Q830917 from Wikidata. |

### Data Splits

The Wikipedia-based corpus has three splits. This is a zero-shot evaluation setup.

|      | Train | Dev | Test | Total |
| ---- | :-----: | :---: | :----: | :-----: |
| Events | 8653 | 1090 | 1204 | 10947 |
| Event Sequences | 6758 | 844 | 846 | 8448 |
| Mentions | 1.44M | 165K | 190K | 1.8M |
| Languages | 44 | 44 | 44 | 44 |

The Wikinews-based evaluation set has two variants, one for cross-domain evaluation and another for zero-shot evaluation.

|     | (Cross-domain) Test | (Zero-shot) Test |
| --- | :------------------: | :-----: |
| Events | 802 | 149 |
| Mentions | 2562 | 437 |
| Languages | 27 | 21 |

## Dataset Creation

### Curation Rationale

This dataset helps address the task of event linking. KB linking is extensively studied for entities, but its unclear if the same methodologies can be extended for linking mentions to events from KB. We use Wikidata as our KB, as it allows for linking mentions from multilingual Wikipedia and Wikinews articles.

### Source Data

#### Initial Data Collection and Normalization

First, we utilize spatial & temporal properties from Wikidata to identify event items. Second, we identify corresponding multilingual Wikipedia pages for each Wikidata event item. Third, we pool hyperlinks from multilingual Wikipedia & Wikinews articles to these event items.

#### Who are the source language producers?

The documents in XLEL-WD are written by Wikipedia and Wikinews contributors in respective languages.

### Annotations

#### Annotation process

This dataset was originally collected automatically from Wikipedia, Wikinews and Wikidata. It was post-processed to improve data quality.

#### Who are the annotators?

The annotations in XLEL-WD (hyperlinks from Wikipedia/Wikinews to Wikidata) are added the original Wiki contributors.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

XLEL-WD v1.0.0 mostly caters to eventive nouns from Wikidata. It does not include any links to other event items from Wikidata such as disease outbreak (Q3241045), military offensive (Q2001676) and war (Q198).

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
