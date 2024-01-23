---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: FaceMask
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
dataset_info:
  features:

  - name: image
    dtype: image
  - name: labels
    dtype:
      class_label:
        names:
          0: mask_weared_incorrect
          1: with_mask
          2: without_mask
  splits:
  - name: train
    num_bytes: 38806014
    num_examples: 1500
  - name: validation
    num_bytes: 4758962
    num_examples: 180
  - name: test
    num_bytes: 4693735
    num_examples: 180
  download_size: 48258711
  dataset_size: 49140913
---

# Dataset Card for Beans

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

- **Homepage:** (https://huggingface.co/datasets/poolrf2001/FaceMask)
- **Repository:** (https://huggingface.co/datasets/poolrf2001/FaceMask)
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** N/A

### Dataset Summary

Beans leaf dataset with images of diseased and health leaves.

### Supported Tasks and Leaderboards

- `image-classification`: Based on a leaf image, the goal of this task is to predict the disease type (Angular Leaf Spot and Bean Rust), if any.

### Languages

English

## Dataset Structure

### Data Instances

A sample from the training set is provided below:

```
{
    'image': <PIL.PngImagePlugin.PngImageFile image mode=RGB size=128x128 at 0x16BAA72A4A8>,
    'labels': 1
}
```

### Data Fields

The data instances have the following fields:


- `image`: A `PIL.Image.Image` object containing the image. Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the `"image"` column, *i.e.* `dataset[0]["image"]` should **always** be preferred over `dataset["image"][0]`.
- `labels`: an `int` classification label.

Class Label Mappings:

```json
{
  "mask_weared_incorrect": 0,
  "with_mask": 1,
  "without_mask": 2,
}
```

### Data Splits

 
|             |train|validation|test|
|-------------|----:|---------:|---:|
|# of examples|1500 |180       |180 |

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

```
@ONLINE {beansdata,
    author="Pool",
    title="FaceMask dataset",
    month="January",
    year="2023",
    url="https://github.com/poolrf2001/maskFace"
}
```

### Contributions
