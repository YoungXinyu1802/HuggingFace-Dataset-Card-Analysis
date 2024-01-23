---
license: openrail
dataset_info:
  features:
  - name: image
    dtype: image
  - name: name
    dtype: string
  - name: type
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 22392351.0
    num_examples: 219
  download_size: 22365600
  dataset_size: 22392351.0
annotations_creators:
- found
language:
- en
language_creators:
- found
multilinguality:
- monolingual
pretty_name: Dead by daylight video game perks
size_categories:
- n<1K
source_datasets:
- original
tags:
- dead by daylight
task_categories:
- image-classification
- text-to-image
task_ids:
- multi-class-image-classification
---

# Dataset Card for Dead by Daylight perks

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Contributions](#contributions)

### Dataset Summary

This dataset contains all images (on black background and upscaled to 512x512) of perks from the video game [Dead by Daylight](https://deadbydaylight.com/) with type, name and description (the first sentence) in english.

## Dataset Creation
### Source Data

All images and text have been found online, mainly on the [Dead by Daylight wiki](https://deadbydaylight.fandom.com/wiki/Dead_by_Daylight_Wiki).

## Additional Information

### Licensing Information

All images belong to [Dead by Daylight](https://deadbydaylight.com/).

### Contributions

Thanks to [@GabrielVidal1](https://github.com/GabrielVidal1) for adding this dataset.