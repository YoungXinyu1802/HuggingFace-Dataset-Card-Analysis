---
annotations_creators:
- no-annotation
language_creators:
- other
language: []
license:
- lgpl-3.0
multilinguality: []
pretty_name: Sketch Data Model Dataset
size_categories:
- 1M<n<10M
task_categories: []
task_ids: []
---
# Dataset Card for Sketch Data Model Dataset

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
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

- **Homepage:** https://github.com/sketchai
- **Repository:** https://github.com/sketchai/preprocessing
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset contains over 6M CAD 2D sketches extracted from Onshape. Sketches are stored as python objects in the custom SAM format.
SAM leverages the [Sketchgraphs](https://github.com/PrincetonLIPS/SketchGraphs) dataset for industrial needs and allows for easier transfer learning on other CAD softwares.

### Supported Tasks and Leaderboards

Tasks: Automatic Sketch Generation, Auto Constraint

## Dataset Structure

### Data Instances

The presented npy files contain python pickled objects and require the [flat_array](https://github.com/PrincetonLIPS/SketchGraphs/blob/master/sketchgraphs/data/flat_array.py) module of Sketchgraphs to be loaded. The normalization_output_merged.npy file contains sketch sequences represented as a list of SAM Primitives and Constraints. The sg_merged_final_*.npy files contain encoded constraint graphs of the sketches represented as a dictionnary of arrays.

### Data Fields

[Needs More Information]

### Data Splits
|Train |Val   |Test  |
|------|------|------|
|6M    |50k   | 50k  |

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