---
dataset_info:
  features:
  - name: color
    dtype: image
  - name: normal
    dtype: image
  splits:
  - name: train
    num_bytes: 110631687.194
    num_examples: 1426
  download_size: 111043422
  dataset_size: 110631687.194
license: cc0-1.0
task_categories:
- image-to-image
size_categories:
- 1K<n<10K
---

# textures-color-normal-1k

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
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

The `textures-color-normal-1k` dataset is an image dataset of 1000+ color and normal map textures in 512x512 resolution.
The dataset was created for use in image to image tasks.
It contains a combination of CC0 procedural and photoscanned PBR materials from [ambientCG](https://ambientcg.com/).

## Dataset Structure

### Data Instances

Each data point contains a 512x512 color texture and the corresponding 512x512 normal map.

### Data Fields

* `color`: the color texture as a PIL image
* `normal`: the normal map as a PIL image

### Data Splits

|    | train |
| -- | ----- |
| ambientCG | 1426 |

## Dataset Creation

### Curation Rationale

`textures-color-normal-1k` was created to provide an accesible source of data for automating 3D-asset creation workflows.
The [Dream Textures](https://github.com/carson-katri/dream-textures) add-on is one such tool providing AI automation in Blender.
By training models designed for image to image tasks, this particular use-case can be more accurately automated.

### Source Data

#### Initial Data Collection and Normalization

The data was obtained from [ambientCG](https://ambientcg.com/)'s CC0 textures. Only the color and normal maps were included in this dataset.

## Additional Information

### Dataset Curators

The dataset was created by Carson Katri, with the images being provided by [ambientCG](https://ambientcg.com/).

### Licensing Information

All of the images used in this dataset are CC0.

### Citation Information

[N/A]

### Contributions

Thanks to [@carson-katri](https://github.com/carson-katri) for adding this dataset.