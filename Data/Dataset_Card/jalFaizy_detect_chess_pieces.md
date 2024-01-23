---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- en
license:
- other
multilinguality:
- monolingual
pretty_name: Object Detection for Chess Pieces
size_categories:
- n<1K
source_datasets: []
task_categories:
- object-detection
task_ids: []
---

# Dataset Card for Object Detection for Chess Pieces

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

- **Homepage:** https://github.com/faizankshaikh/chessDetection
- **Repository:** https://github.com/faizankshaikh/chessDetection
- **Paper:** -
- **Leaderboard:** -
- **Point of Contact:** [Faizan Shaikh](mailto:faizankshaikh@gmail.com)

### Dataset Summary

The "Object Detection for Chess Pieces" dataset is a toy dataset created (as suggested by the name!) to introduce object detection in a beginner friendly way. It is structured in a one object-one image manner, with the objects being of four classes, namely, Black King, White King, Black Queen and White Queen

### Supported Tasks and Leaderboards

- `object-detection`: The dataset can be used to train and evaluate simplistic object detection models

### Languages

The text (labels) in the dataset is in English

## Dataset Structure

### Data Instances

A data point comprises an image and the corresponding objects in bounding boxes.

```
{
  'image': <PIL.PngImagePlugin.PngImageFile image mode=RGB size=224x224 at 0x23557C66160>,
  'objects': { "label": [ 0 ], "bbox": [ [ 151, 151, 26, 26 ] ] }
}
```

### Data Fields

- `image`: A `PIL.Image.Image` object containing the 224x224 image.
- `label`: An integer between 0 and 3 representing the classes with the following mapping:
  | Label | Description |
  | --- | --- |
  | 0 | blackKing |
  | 1 | blackQueen |
  | 2 | whiteKing |
  | 3 | whiteQueen |
- `bbox`: A list of integers having sequence [x_center, y_center, width, height] for a particular bounding box

### Data Splits

The data is split into training and validation set. The training set contains 204 images and the validation set 52 images. 


## Dataset Creation

### Curation Rationale

The dataset was created to be a simple benchmark for object detection

### Source Data

#### Initial Data Collection and Normalization

The data is obtained by machine generating images from "python-chess" library. Please refer [this code](https://github.com/faizankshaikh/chessDetection/blob/main/code/1.1%20create_images_with_labels.ipynb) to understand data generation pipeline

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

The annotations were done manually.

#### Who are the annotators?

The annotations were done manually.

### Personal and Sensitive Information

None

## Considerations for Using the Data

### Social Impact of Dataset

The dataset can be considered as a beginner-friendly toy dataset for object detection. It should not be used for benchmarking state of the art object detection models, or be used for a deployed model.

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

The dataset only contains four classes for simplicity. The complexity can be increased by considering all types of chess pieces, and by making it a multi-object detection problem

## Additional Information

### Dataset Curators

The dataset was created by Faizan Shaikh

### Licensing Information

The dataset is licensed as CC-BY-SA:2.0

### Citation Information

[Needs More Information]