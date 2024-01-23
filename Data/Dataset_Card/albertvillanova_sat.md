---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
- vi
license:
- unknown
multilinguality:
- translation
size_categories:
- 1M<n<10M
source_datasets:
- original
- extended|bible_para
- extended|kde4
- extended|opus_gnome
- extended|open_subtitles
- extended|tatoeba
task_categories:
- text-generation
- translation
task_ids: []
pretty_name: SAT
tags:
- conditional-text-generation
---

# Dataset Card for SAT

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

- **Homepage:** https://blog.vietai.org/sat/
- **Repository:** https://github.com/vietai/sat
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

SAT (Style Augmented Translation) dataset contains roughly 3.3 million English-Vietnamese pairs of texts.

### Supported Tasks and Leaderboards

- Machine Translation

### Languages

The languages in the dataset are:
- Vietnamese (`vi`)
- English (`en`)

## Dataset Structure

### Data Instances

```
{
  'translation': {
    'en': 'Rachel Pike : The science behind a climate headline',
    'vi': 'Khoa học đằng sau một tiêu đề về khí hậu'
  }
}
```

### Data Fields

- `translation`:
  - `en`: Parallel text in English.
  - `vi`: Parallel text in Vietnamese.

### Data Splits

The dataset is split in "train" and "test".

|                    |   train | test |
|--------------------|--------:|-----:|
| Number of examples | 3359574 | 7221 |

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

Unknown.

### Citation Information

Unknown.

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
