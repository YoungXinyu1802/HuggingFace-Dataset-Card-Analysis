---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
- vi
license:
- cc-by-nc-sa-4.0
multilinguality:
- translation
pretty_name: MTet
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
- conditional-text-generation
task_ids:
- machine-translation
---

# Dataset Card for MTet

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

- **Homepage:** https://translate.vietai.org/
- **Repository:** https://github.com/vietai/mTet
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

MTet (Multi-domain Translation for English-Vietnamese) dataset contains roughly 4.2 million English-Vietnamese pairs of
texts, ranging across multiple different domains such as medical publications, religious texts, engineering articles,
literature, news, and poems.

This dataset extends our previous SAT (Style Augmented Translation) dataset (v1.0) by adding more high-quality
English-Vietnamese sentence pairs on various domains.

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
    'en': 'He said that existing restrictions would henceforth be legally enforceable, and violators would be fined.',
    'vi': 'Ông nói những biện pháp hạn chế hiện tại sẽ được nâng lên thành quy định pháp luật, và những ai vi phạm sẽ chịu phạt.'
  }
}
```

### Data Fields

- `translation`:
  - `en`: Parallel text in English.
  - `vi`: Parallel text in Vietnamese.

### Data Splits

The dataset is in a single "train" split.

|                    |   train | 
|--------------------|--------:|
| Number of examples | 4163853 |

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

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Citation Information

```bibtex
@article{mTet2022,
    author  = {Chinh Ngo, Hieu Tran, Long Phan, Trieu H. Trinh, Hieu Nguyen, Minh Nguyen, Minh-Thang Luong},
    title   = {MTet: Multi-domain Translation for English and Vietnamese},
    journal = {https://github.com/vietai/mTet},
    year    = {2022},
}
```

### Contributions

Thanks to [@albertvillanova](https://huggingface.co/albertvillanova) for adding this dataset.
