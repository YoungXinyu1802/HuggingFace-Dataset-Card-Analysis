---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- is
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 100M<n<1B
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: ICC
---

# Dataset Card for ICC

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

- **Point of Contact:** [Jón Friðrik Daðason](mailto:jond19@ru.is)

### Dataset Summary

The Icelandic Crawled Corpus (ICC) contains approximately 930M tokens which have been scraped from a selection of Icelandic websites, including news sites, government websites and forums. The scraped text is presented in its original form, unannotated, untokenized and without deduplication.

### Supported Tasks and Leaderboards

The ICC is primarily intended for use in training language models. It can be combined with other corpora, such as the [Icelandic Gigaword Corpus](http://igc.arnastofnun.is/) and the Icelandic portion of the [mC4](https://huggingface.co/datasets/mc4) corpus.

### Languages

This corpus contains text in Icelandic, scraped from a variety of online sources.

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

Each scraped item consists of two fields:
* **url**: The source URL of the scraped text.
* **text**: The scraped text.

### Data Splits

N/A

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

N/A

#### Who are the annotators?

N/A

### Personal and Sensitive Information

Although this corpus consists entirely of text collected from publicly available websites, it may contain some examples of personal or sensitive information.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This corpus was created by Jón Friðrik Daðason, during work done at the [Language and Voice Lab](https://lvl.ru.is/) at [Reykjavik University](https://www.ru.is/).

This project was funded by the Language Technology Programme for Icelandic 2019-2023. The programme, which is managed and coordinated by [Almannarómur](https://almannaromur.is/), is funded by the Icelandic Ministry of Education, Science and Culture.

### Licensing Information

    This work is licensed under a Creative Commons Attribution 4.0
    International License. Any text, HTML page links, information, metadata or
    other materials in this work may be subject to separate terms and
    conditions between you and the owners of such content.

    If you are a copyright owner or an agent thereof and believe that any
    content in this work infringes upon your copyrights, you may submit a
    notification with the following information:
    * Your full name and information reasonably sufficient to permit us to
      contact you, such as mailing address, phone number and an email address.
    * Identification of the copyrighted work you claim has been infringed.
    * Identification of the material you claim is infringing and should be
      removed, and information reasonably sufficient to permit us to locate
      the material.

### Citation Information

N/A

### Contributions

Thanks to [@jonfd](https://github.com/jonfd) for adding this dataset.
