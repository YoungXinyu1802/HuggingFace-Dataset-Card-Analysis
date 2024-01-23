---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 59834059.794
    num_examples: 1447
  download_size: 52173880
  dataset_size: 59834059.794
license: cc0-1.0
task_categories:
- text-to-image
language:
- en
size_categories:
- 1K<n<10K
---

# textures-normal-1k

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
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

The `textures-normal-1k` dataset is an image dataset of 1000+ normal map textures in 512x512 resolution with associated text descriptions.
The dataset was created for training/fine-tuning models for text to image tasks.
It contains a combination of CC0 procedural and photoscanned PBR materials from [ambientCG](https://ambientcg.com/).

### Languages

The text descriptions are in English, and created by joining the tags of each material with a space character.

## Dataset Structure

### Data Instances

Each data point contains a 512x512 image and and additional `text` feature containing the description of the texture.

### Data Fields

* `image`: the normal map as a PIL image
* `text`: the associated text description created by merging the material's tags

### Data Splits

|    | train |
| -- | ----- |
| ambientCG | 1447 |

## Dataset Creation

### Curation Rationale

`textures-normal-1k` was created to provide an accesible source of data for automating 3D-asset creation workflows.
The [Dream Textures](https://github.com/carson-katri/dream-textures) add-on is one such tool providing AI automation in Blender.
By fine-tuning models such as Stable Diffusion on textures, this particular use-case can be more accurately automated.

### Source Data

#### Initial Data Collection and Normalization

The data was obtained from [ambientCG](https://ambientcg.com/)'s CC0 textures. Only the normal maps were included in this dataset.

Text descriptions were synthesized by joining the tags associated with each material with a space.

## Additional Information

### Dataset Curators

The dataset was created by Carson Katri, with the images being provided by [ambientCG](https://ambientcg.com/).

### Licensing Information

All of the images used in this dataset are CC0.

### Citation Information

[N/A]

### Contributions

Thanks to [@carson-katri](https://github.com/carson-katri) for adding this dataset.