---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- nl
language_bcp47:
- nl-BE
license:
- unknown
multilinguality:
- monolingual
pretty_name: XSum NL
size_categories:
- unknown
source_datasets:
- extended|xsum
task_categories:
- conditional-text-generation
task_ids:
- summarization
---
# Dataset Card for XSum NL

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

This dataset is a machine translated dataset. It's the [XSum dataset](https://huggingface.co/datasets/xsum) translated with [this model](https://huggingface.co/Helsinki-NLP/opus-mt-en-nl) from English to Dutch.

See the [Hugginface page of the original dataset](https://huggingface.co/datasets/xsum) for more information on the format of this dataset.

Use with: 

```python
from datasets import load_dataset
load_dataset("csv", "ml6team/xsum_nl")
```
### Languages

Dutch

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- `id`: BBC ID of the article.
- `document`: a string containing the body of the news article 
- `summary`: a string containing a one sentence summary of the article.

### Data Splits

- `train`
- `test`
- `validation`

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

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.