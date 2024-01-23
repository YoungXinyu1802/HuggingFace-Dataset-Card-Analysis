#---
#license: mit
#---

---
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- en
license:
- cc0-1.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: arxiv-co-ga
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text2text-generation
task_ids:
- explanation-generation
- text-simplification
---

# Dataset Card for `arxiv-co-ga`

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

This is a dataset of metadata that includes titles and abstracts for all Cosmology and Galaxy Astrophysics arXiv articles to date (99,659 papers).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- `id`: ArXiv ID (can be used to access the paper, see below)
- `submitter`: Who submitted the paper
- `authors`: Authors of the paper
- `title`: Title of the paper
- `comments`: Additional info, such as number of pages and figures
- `journal-ref`: Information about the journal the paper was published in
- `doi`: [https://www.doi.org](Digital Object Identifier)
- `abstract`: The abstract of the paper
- `categories`: Categories / tags in the ArXiv system
- `versions`: A version history

### Data Splits

This dataset has 3 splits: _train_, _validation_, and _test_. Below are the statistics for these splits.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 63,781                                      |
| Validation    | 15,946                                      |
| Test          | 19,932                                      |

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

The original data is maintained by ArXiv, huge thanks to the team for building and maintaining this dataset.

### Licensing Information

Creative Commons CC0 1.0 Universal Public Domain Dedication applies to the metadata in this dataset. See https://arxiv.org/help/license for further details and licensing on individual papers.

### Citation Information

```
@misc{clement2019arxiv,
    title={On the Use of ArXiv as a Dataset},
    author={Colin B. Clement and Matthew Bierbaum and Kevin P. O'Keeffe and Alexander A. Alemi},
    year={2019},
    eprint={1905.00075},
    archivePrefix={arXiv},
    primaryClass={cs.IR}
}
```

### Contributions

#Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.