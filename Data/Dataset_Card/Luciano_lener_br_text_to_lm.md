---
annotations_creators: []
language:
- pt
language_creators: []
license: []
multilinguality:
- monolingual
pretty_name: 'The LeNER-Br language modeling dataset is a collection of legal texts
  in Portuguese from the LeNER-Br dataset (https://cic.unb.br/~teodecampos/LeNER-Br/).


  The legal texts were obtained from the original token classification Hugging Face
  LeNER-Br dataset (https://huggingface.co/datasets/lener_br) and processed to create
  a DatasetDict with train and validation dataset (20%).


  The LeNER-Br language modeling dataset allows the finetuning of language models
  as BERTimbau base and large.'
size_categories:
- 10K<n<100K
source_datasets: []
tags: []
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
- language-modeling
---

# Dataset Card for lener_br_text_to_lm

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

The LeNER-Br language modeling dataset is a collection of legal texts
  in Portuguese from the LeNER-Br dataset (https://cic.unb.br/~teodecampos/LeNER-Br/).


  The legal texts were obtained from the original token classification Hugging Face
  LeNER-Br dataset (https://huggingface.co/datasets/lener_br) and processed to create
  a DatasetDict with train and validation dataset (20%).


  The LeNER-Br language modeling dataset allows the finetuning of language models
  as BERTimbau base and large.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

```
DatasetDict({
    train: Dataset({
        features: ['text'],
        num_rows: 8316
    })
    test: Dataset({
        features: ['text'],
        num_rows: 2079
    })
})
```

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

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.