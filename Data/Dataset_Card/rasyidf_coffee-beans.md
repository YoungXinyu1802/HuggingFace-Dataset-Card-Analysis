---
license: mit
annotations_creators:
- expert-generated
language_creators:
- expert-generated
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
language:
- id
pretty_name: Cofee Beans Grading
size_categories:
- n<1K
dataset_info:
  features:
  - name: image_file_path
    dtype: string
  - name: image
    dtype: image
  - name: labels
    dtype:
      class_label:
        names:
          '1': 0
          '2': 1
          '3': 2
          '0': 3
  splits:
  - name: train
    num_bytes: 202.173.747 
    num_examples: 200
  - name: validation
    num_bytes: 57.633.053
    num_examples: 400
  - name: test
    num_bytes: 28.985.470
    num_examples: 1400
  download_size: 288792270
  dataset_size: 2000
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

- **Homepage:** 
- **Repository:**
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** N/A

### Dataset Summary

Coffee Beans Grading 

### Supported Tasks and Leaderboards

- `image-classification`: Based on a coffee bean grading, the goal of this task is to grade single beans for clusterization.

### Languages

Indonesia

## Dataset Structure

### Data Instances

A sample from the training set is provided below:

```
{
    'image_file_path': '/root/.cache/huggingface/datasets/downloads/extracted/0aaa78294d4bf5114f58547e48d91b7826649919505379a167decb629aa92b0a/train/bean_rust/bean_rust_train.109.jpg',
    'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=500x500 at 0x16BAA72A4A8>,
    'labels': 1
}
```

### Data Fields

The data instances have the following fields:

- `image_file_path`: a `string` filepath to an image.
- `image`: A `PIL.Image.Image` object containing the image. Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the `"image"` column, *i.e.* `dataset[0]["image"]` should **always** be preferred over `dataset["image"][0]`.
- `labels`: an `int` classification label.

Class Label Mappings:

```json
{
  "1": 0,
  "2": 1,
  "3": 2,
}
```

### Data Splits

 
|             |train|validation|test|
|-------------|----:|---------:|---:|
|# of examples|1400 |400       |200 |

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


### Contributions
