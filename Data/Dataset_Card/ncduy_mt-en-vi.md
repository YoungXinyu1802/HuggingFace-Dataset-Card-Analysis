---
annotations_creators:
- found
language_creators:
- found
language:
- en
- vi
license:
- mit
multilinguality:
- translation
pretty_name: "Machine Translation Paired English-Vietnamese Sentences"
size_categories:
- 1M<n<10M
source_datasets:
- own
- open_subtitles
- tatoeba
- opus_tedtalks
- qed_amara
- opus_wikipedia
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
---

# Dataset Card for Machine Translation Paired English-Vietnamese Sentences

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
- **Repository:**
- **Paper:** 
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The language of the dataset text sentence is English ('en') and Vietnamese (`vi`).

## Dataset Structure

### Data Instances

An instance example:
```
{
  'en': 'And what I think the world needs now is more connections.', 
  'vi': 'Và tôi nghĩ điều thế giới đang cần bây giờ là nhiều sự kết nối hơn.', 
  'source': 'TED2020 v1'
}
```

### Data Fields

- `en` (str): English sentence
- `vi` (str): Vietnamese sentence
- `source` (str): Source.

### Data Splits

The dataset is split in train, validation and test.

|                    |  Tain | Validation | Test |
|--------------------|------:|-----------:|-----:|
| Number of examples |2884451|       11316| 11225|


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

[More Information Needed]

### Contributions

Thanks to [@ncduy0303](https://github.com/ncduy0303) for adding this dataset.