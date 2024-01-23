---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
license: []
multilinguality:
- monolingual
pretty_name: SciArg
size_categories:
- 1K<n<10K
source_datasets:
- dr inventor corpus
tags:
- argument mining
- scientific text
- relation extraction
- argumentative discourse unit recognition
task_categories:
- token-classification
task_ids: []
---

# Dataset Card for "sciarg"

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

- **Homepage:** [https://github.com/anlausch/ArguminSci](https://github.com/anlausch/ArguminSci)
- **Repository:** [https://github.com/anlausch/ArguminSci](https://github.com/anlausch/ArguminSci)
- **Paper:** [An argument-annotated corpus of scientific publications](https://aclanthology.org/W18-5206.pdf)
- **Leaderboard:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

The SciArg dataset is an extension of the Dr. Inventor corpus (Fisas et al., 2015, 2016) with an annotation layer containing 
fine-grained argumentative components and relations. It is the first argument-annotated corpus of scientific 
publications (in English), which allows for joint analyses of argumentation and other rhetorical dimensions of 
scientific writing.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The language in the dataset is English.

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- `document_id`: the base file name, e.g. "A28"
- `text`: the parsed text of the scientific publication in the XML format
- `text_bound_annotations`: span annotations that mark argumentative discourse units (ADUs). Each entry has the following fields: `offsets`, `text`, `type`, and `id`.
- `relations`: binary relation annotations that mark the argumentative relations that hold between a head and a tail ADU. Each entry has the following fields: `id`, `head`, `tail`, and `type` where `head` and `tail` each have the fields: `ref_id` and `role`. 

### Data Splits

The dataset consists of a single `train` split that has 40 documents.

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

```
@inproceedings{lauscher2018b,
  title = {An argument-annotated corpus of scientific publications},
  booktitle = {Proceedings of the 5th Workshop on Mining Argumentation},
  publisher = {Association for Computational Linguistics},
  author = {Lauscher, Anne and Glava\v{s}, Goran and Ponzetto, Simone Paolo},
  address = {Brussels, Belgium},
  year = {2018},
  pages = {40–46}
}

```

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
