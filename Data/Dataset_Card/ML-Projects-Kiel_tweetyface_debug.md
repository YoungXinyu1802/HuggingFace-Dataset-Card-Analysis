---
annotations_creators:
  - machine-generated
language:
  - en
  - de
language_creators:
  - crowdsourced
license:
  - apache-2.0
multilinguality:
  - multilingual
pretty_name: tweetyface_debug
size_categories:
  - 10K<n<100K
source_datasets: []
tags: []
task_categories:
  - text-generation
task_ids: []
---

# DEBUG Dataset Card for "tweetyface"

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
- **Repository:** [GitHub](https://github.com/ml-projects-kiel/OpenCampus-ApplicationofTransformers)

### Dataset Summary

DEBUG

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English, German

## Dataset Structure

### Data Instances

#### english

- **Size of downloaded dataset files:** 4.77 MB
- **Size of the generated dataset:** 5.92 MB
- **Total amount of disk used:** 4.77 MB

#### german

- **Size of downloaded dataset files:** 2.58 MB
- **Size of the generated dataset:** 3.10 MB
- **Total amount of disk used:** 2.59 MB

An example of 'validation' looks as follows.

```
{
  "text": "@SpaceX @Space_Station About twice as much useful mass to orbit as rest of Earth combined",
  "label": elonmusk,
  "idx": 1001283
}
```

### Data Fields

The data fields are the same among all splits and languages.

- `text`: a `string` feature.
- `label`: a classification label
- `idx`: an `string` feature.
- `ref_tweet`: a `bool` feature.
- `reply_tweet`: a `bool` feature.

### Data Splits

| name    | train | validation |
| ------- | ----: | ---------: |
| english | 27857 |       6965 |
| german  | 10254 |       2564 |

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
