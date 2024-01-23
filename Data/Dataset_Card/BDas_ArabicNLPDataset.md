---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- ar
license:
- other
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
- multi-label-classification
pretty_name: 'ArabicNLPDataset'
---


# Dataset Card for "ArabicNLPDataset"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Preprocessing](#dataset-preprocessing)
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
- **Homepage:** [https://github.com/BihterDass/ArabicTextClassificationDataset]
- **Repository:** [https://github.com/BihterDass/ArabicTextClassificationDataset]
- **Size of downloaded dataset files:** 23.5 MB
- **Size of the generated dataset:** 23.5 MB

### Dataset Summary
The dataset was compiled from user comments from e-commerce sites. It consists of 10,000 validations, 10,000 tests and 80000 train data. Data were classified into 3 classes (positive(pos), negative(neg) and natural(nor). The data is available to you on github.

### Supported Tasks and Leaderboards
[More Information Needed]

### Languages
[More Information Needed]

## Dataset Structure

### Data Instances
[More Information Needed]

#### arabic-dataset-v1
- **Size of downloaded dataset files:** 23.5 MB
- **Size of the generated dataset:** 23.5 MB

### Data Fields
The data fields are the same among all splits.

#### arabic-dataset-v-v1
- `text`: a `string` feature.
- `label`: a classification label, with possible values including `positive` (2),  `natural` (1), `negative` (0).

### Data Splits
|    |train    |validation|test      |
|----|--------:|---------:|---------:|
|Data|  80000  |   10000 |     10000 |

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
Thanks to [@PnrSvc](https://github.com/PnrSvc) for adding this dataset.