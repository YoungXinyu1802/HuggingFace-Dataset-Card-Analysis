---
annotations_creators: []
language:
- en
language_creators: []
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: CompanyWeb
size_categories:
- 1M<n<10M
source_datasets: []
tags:
- business
- company websites
task_categories:
- fill-mask
- other
task_ids:
- masked-language-modeling
---

# Dataset Card for "CompanyWeb"

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

- **Homepage:** [PLACEHOLDER]()
- **Repository:** [PLACEHOLDER]()
- **Paper:** [PLACEHOLDER]()
- **Leaderboard:** [PLACEHOLDER]()
- **Point of Contact:** [PLACEHOLDER]()

### Dataset Summary

The dataset contains textual content extracted from 1,788,413 company web pages of 393,542 companies. The companies included in the dataset are small, medium and large international enterprises including publicly listed companies. Additional company information is provided in form of the corresponding Standard Industry Classification (SIC) label `sic4`. 
The text includes all textual information contained on the website with a timeline ranging from 2014 to 2021. The search includes all subsequent pages with links from the homepage containing the company domain name. 
We filter the resulting textual data to only include English text utilizing the FastText language detection API [(Joulin et al., 2016)](https://aclanthology.org/E17-2068/). 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

- en

## Dataset Structure

### Data Instances

- **#Instances:** 1789413
- **#Companies:** 393542
- **#Timeline:** 2014-2021

### Data Fields

- `id`: instance identifier `(string)`
- `cid`: company identifier `(string)`
- `text`: website text `(string)`
- `sic4`: 4-digit SIC `(string)`

### Data Splits

[More Information Needed]

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

```bibtex
@misc{title_year,
      title={TITLE},
      author={AUTHORS},
      year={2022},
}
```

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.