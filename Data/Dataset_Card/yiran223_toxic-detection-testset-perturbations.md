---
language:
- en
size_categories:
- 10K<n<100K
---

# Dataset Card for toxic-detection-testset-perturnations

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

This dataset a test set for toxic detection that contains both clean data and it's perturbed version with human-written perturbations online. 
In addition, our dataset can be used to benchmark misspelling correctors as well.


### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

### Data Instances
```
{
  "clean_version": "this is pretty much exactly how i feel damn",
  "perturbed_version": "this is pretty much exactly how i feel daaammnn",
  "toxicity": 0.7,
  "obscene": 0.7,
  "sexual_explicit": 0,
  "identity_attack": 0,
    ...
  "insult": 0.2,
  "quality_mean": 4
}
	
```

### Data Fields

This dataset is derived from the [Jigsaw data](https://www.kaggle.com/competitions/jigsaw-unintended-bias-in-toxicity-classification/data). Hence, it keeps all the useful metrics and attributes.

**Main**
* clean_version
* perturbed_version


**Metrics**
* toxicity
* severe_toxicity
* obscene
* threat
* insult
* identity_attack
* sexual_explicit


**Identity attributes**
* male
* female
* transgender
* other_gender
* heterosexual
* homosexual_gay_or_lesbian
* bisexual
* other_sexual_orientation
* christian
* jewish
* muslim
* hindu
* buddhist
* atheist
* other_religion
* black
* white
* asian
* latino
* other_race_or_ethnicity
* physical_disability
* intellectual_or_learning_disability
* psychiatric_or_mental_illness
* other_disability


### Data Splits

test: 1339

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

US Amazon MTurk workers with HIT Approval Rate greater than 98%, and Number of HITs approved greater than 1000.

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

[More Information Needed]