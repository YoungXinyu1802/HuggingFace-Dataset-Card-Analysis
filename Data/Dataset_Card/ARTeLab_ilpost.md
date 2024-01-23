---
language:
- it
multilinguality:
- monolingual
size_categories:
- 10K<n<100k
task_categories:
- summarization
---

# Dataset Card for ilpost

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

IlPost dataset, containing news articles taken from IlPost.

There are two features:

- source: Input news article.
- target: Summary of the article.

### Supported Tasks and Leaderboards

- `abstractive-summarization`, `summarization`

### Languages

The text in the dataset is in Italian

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

More details and results in [published work](https://www.mdpi.com/2078-2489/13/5/228)

```
@Article{info13050228,
    AUTHOR = {Landro, Nicola and Gallo, Ignazio and La Grassa, Riccardo and Federici, Edoardo},
    TITLE = {Two New Datasets for Italian-Language Abstractive Text Summarization},
    JOURNAL = {Information},
    VOLUME = {13},
    YEAR = {2022},
    NUMBER = {5},
    ARTICLE-NUMBER = {228},
    URL = {https://www.mdpi.com/2078-2489/13/5/228},
    ISSN = {2078-2489},
    ABSTRACT = {Text summarization aims to produce a short summary containing relevant parts from a given text. Due to the lack of data for abstractive summarization on low-resource languages such as Italian, we propose two new original datasets collected from two Italian news websites with multi-sentence summaries and corresponding articles, and from a dataset obtained by machine translation of a Spanish summarization dataset. These two datasets are currently the only two available in Italian for this task. To evaluate the quality of these two datasets, we used them to train a T5-base model and an mBART model, obtaining good results with both. To better evaluate the results obtained, we also compared the same models trained on automatically translated datasets, and the resulting summaries in the same training language, with the automatically translated summaries, which demonstrated the superiority of the models obtained from the proposed datasets.},
    DOI = {10.3390/info13050228}
}
```