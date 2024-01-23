---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: clinical_trial_reason_to_stop
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- bio
- research papers
- clinical trial
- drug development
task_categories:
- text-classification
task_ids:
- multi-class-classification
- multi-label-classification
---

# Dataset Card for Clinical Trials's Reason to Stop

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

- **Homepage:** https://www.opentargets.org
- **Repository:** https://github.com/LesyaR/stopReasons
- **Paper:**
- **Point of Contact:** data@opentargets.org

### Dataset Summary

This dataset contains a curated classification of more than 5000 reasons why a clinical trial has suffered an early stop.
The text has been extracted from clinicaltrials.gov, the largest resource of clinical trial information. The text has been curated by members of the Open Targets organisation, a project aimed at providing data relevant to drug development.

All 17 possible classes have been carefully defined:
- Business_Administrative
- Another_Study
- Negative
- Study_Design
- Invalid_Reason
- Ethical_Reason
- Insufficient_Data
- Insufficient_Enrollment
- Study_Staff_Moved
- Endpoint_Met
- Regulatory
- Logistics_Resources
- Safety_Sideeffects
- No_Context
- Success
- Interim_Analysis
- Covid19

### Supported Tasks and Leaderboards

Multi class classification

### Languages

English

## Dataset Structure

### Data Instances

```json
{'text': 'Due to company decision to focus resources on a larger, controlled study in this patient population."',
 'label': 'Another_Study'}
```


### Data Fields

`text`: contains the reason for the CT early stop
`label`: contains one of the 17 defined classes 

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

This dataset has an Apache 2.0 license.

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@ireneisdoomed](https://github.com/<github-username>) for adding this dataset.