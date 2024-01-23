---
annotations_creators:
- crowdsourced
- expert-generated
language_creators:
- expert-generated
language: []
license: []
multilinguality: []
pretty_name: sidewalk-semantic
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- image-segmentation
task_ids:
- semantic-segmentation
---

# Dataset Card for sidewalk-semantic

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
- [Dataset Structure](#dataset-structure)
  - [Data Categories](#data-categories)
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

- **Homepage:** [Dataset homepage on Segments.ai](https://segments.ai/segments/sidewalk-imagery/)
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Bert De Brabandere](mailto:bert@segments.ai)

### Dataset Summary

A dataset of sidewalk images gathered in Belgium in the summer of 2021. Label your own semantic segmentation datasets on [segments.ai](https://segments.ai/?utm_source=hf&utm_medium=hf-ds&utm_campaign=sidewalk)

### Supported Tasks and Leaderboards

- `semantic-segmentation`: The dataset can be used to train a semantic segmentation model, where each pixel is classified. The model performance is measured by how high its [mean IoU (intersection over union)](https://huggingface.co/metrics/mean_iou) to the reference is.

## Dataset Structure

### Data categories

| Id  | Name | Description |
| --- | ---- | ----------- |
| 0 | unlabeled | - |
| 1 | flat-road | - |
| 2 | flat-sidewalk | - |
| 3 | flat-crosswalk | - |
| 4 | flat-cyclinglane | - |
| 5 | flat-parkingdriveway | - |
| 6 | flat-railtrack | - |
| 7 | flat-curb | - |
| 8 | human-person | - |
| 9 | human-rider | - |
| 10 | vehicle-car | - |
| 11 | vehicle-truck | - |
| 12 | vehicle-bus | - |
| 13 | vehicle-tramtrain | - |
| 14 | vehicle-motorcycle | - |
| 15 | vehicle-bicycle | - |
| 16 | vehicle-caravan | - |
| 17 | vehicle-cartrailer | - |
| 18 | construction-building | - |
| 19 | construction-door | - |
| 20 | construction-wall | - |
| 21 | construction-fenceguardrail | - |
| 22 | construction-bridge | - |
| 23 | construction-tunnel | - |
| 24 | construction-stairs | - |
| 25 | object-pole | - |
| 26 | object-trafficsign | - |
| 27 | object-trafficlight | - |
| 28 | nature-vegetation | - |
| 29 | nature-terrain | - |
| 30 | sky | - |
| 31 | void-ground | - |
| 32 | void-dynamic | - |
| 33 | void-static | - |
| 34 | void-unclear | - |

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

This dataset only contains one split.

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

[Needs More Information]