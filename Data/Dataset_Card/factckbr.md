---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- pt
license:
- mit
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- fact-checking
pretty_name: FACTCK BR
dataset_info:
  features:
  - name: url
    dtype: string
  - name: author
    dtype: string
  - name: date
    dtype: string
  - name: claim
    dtype: string
  - name: review
    dtype: string
  - name: title
    dtype: string
  - name: rating
    dtype: float32
  - name: best_rating
    dtype: float32
  - name: label
    dtype:
      class_label:
        names:
          '0': falso
          '1': distorcido
          '2': impreciso
          '3': exagerado
          '4': insustentável
          '5': verdadeiro
          '6': outros
          '7': subestimado
          '8': impossível provar
          '9': discutível
          '10': sem contexto
          '11': de olho
          '12': verdadeiro, mas
          '13': ainda é cedo para dizer
  splits:
  - name: train
    num_bytes: 750646
    num_examples: 1313
  download_size: 721314
  dataset_size: 750646
---

# Dataset Card for FACTCK BR

## Table of Contents
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

- **Homepage:** https://github.com/jghm-f/FACTCK.BR
- **Repository:** https://github.com/jghm-f/FACTCK.BR
- **Paper:** https://dl.acm.org/doi/10.1145/3323503.3361698
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

A dataset to study Fake News in Portuguese, presenting a supposedly false News along with their respective fact check and classification.
The data is collected from the ClaimReview, a structured data schema used by fact check agencies to share their results in search engines, enabling data collect in real time.
The FACTCK.BR dataset contains 1309 claims with its corresponding label.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

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

[More Information Needed]

### Contributions

Thanks to [@hugoabonizio](https://github.com/hugoabonizio) for adding this dataset.