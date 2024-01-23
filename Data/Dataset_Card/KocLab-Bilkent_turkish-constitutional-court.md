---
license: cc-by-4.0
task_categories:
- text-classification
annotations_creators:
- found
language_creators:
- found
multilinguality:
- monolingual
language:
- tr
size_categories:
- 10M<n<100M
pretty_name: predicting-turkish-constitutional-court-decisions
source_datasets:
- original
---

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

- **Homepage:**
- **Repository:** https://github.com/koc-lab/law-turk
- **Paper:** https://doi.org/10.1016/j.ipm.2021.102684
- **Point of Contact:** [Ceyhun Emre Öztürk](mailto:ceyhun.ozturk@bilkent.edu.tr)

### Dataset Summary
This dataset is extracted from the following Github repo, which was created for the journal paper with URL https://www.sciencedirect.com/science/article/abs/pii/S0306457321001692.

https://github.com/koc-lab/law-turk

The dataset includes 1290 court case decision texts from the Turkish Court of Cassation. Each sample has one label, which is the ruling of the court. The possible rulings are "Violation" and "No violation". There are 1290 samples. 1141 of these samples are labeled as "Violation". 

### Supported Tasks and Leaderboards

Legal Judgment Prediction

### Languages

Turkish

## Dataset Structure

### Data Instances

The file format is jsonl and three data splits are present (train, validation and test) for each configuration.

### Data Fields

The dataset contains the following fields:

 - `Text`: Legal case decision texts
 - `Label`: The ruling of the court.
   - 'Violation': The court decides for the legal case that there is a violation of the constitution.
   - 'No violation': The court decides for the legal case that there is no violation of the constitution.

### Data Splits

The data has been split randomly into 70% train (903), 15% validation (195), 15% test (195).

## Dataset Creation

### Curation Rationale

This dataset was created to further the research on developing models for predicting Brazilian court decisions that are
also able to predict whether the decision will be unanimous.

### Source Data

The data were collected from *Türkiye Cumhuriyeti Anayasa Mahkemesi* (T.C. AYM, Turkish Constitutional Court).

#### Initial Data Collection and Normalization

The data were collected from the official website of the Turkish Contitutional Court: https://www.anayasa.gov.tr/tr/kararlar-bilgi-bankasi/.

#### Who are the source language producers?

The source language producers are judges.

### Annotations

#### Annotation process

The dataset was not annotated.

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

The court decisions might contain sensitive information about individuals.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

### Dataset Curators

The data collection was done by Emre Mumcuoğlu ([Email](mailto:mumcuoglu@ee.bilkent.edu.tr)).

### Licensing Information

No licensing information was provided for this dataset. However, please make sure that you use the dataset according to
Turkish law.

### Citation Information

```
@article{mumcuoglu21natural,
    title = {{Natural language processing in law: Prediction of outcomes in the higher courts of Turkey}},
    journal = {Information Processing \& Management},
    volume = {58},
    number = {5},
    year = {2021},
    author = {Mumcuoğlu, Emre and Öztürk, Ceyhun E. and Ozaktas, Haldun M. and Koç, Aykut}
}
```