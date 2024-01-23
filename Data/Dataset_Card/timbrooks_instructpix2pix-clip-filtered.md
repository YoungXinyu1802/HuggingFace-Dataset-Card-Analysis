---
dataset_info:
  features:
  - name: original_prompt
    dtype: string
  - name: original_image
    dtype: image
  - name: edit_prompt
    dtype: string
  - name: edited_prompt
    dtype: string
  - name: edited_image
    dtype: image
  splits:
  - name: train
    num_bytes: 130930966429.88
    num_examples: 313010
  download_size: 63067247926
  dataset_size: 130930966429.88
language:
- en
size_categories:
- 100K<n<1M
---
# Dataset Card for InstructPix2Pix CLIP-filtered

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

- **Homepage:** https://www.timothybrooks.com/instruct-pix2pix
- **Repository:** https://github.com/timothybrooks/instruct-pix2pix
- **Paper:** https://arxiv.org/abs/2211.09800

## Dataset Summary

The dataset can be used to train models to follow edit instructions. Edit instructions
are available in the `edit_prompt`. `original_image` can be used with the `edit_prompt` and
`edited_image` denotes the image after applying the `edit_prompt` on the `original_image`. 

Refer to the [GitHub repository](https://github.com/timothybrooks/instruct-pix2pix) to know more about
how this dataset can be used to train a model that can follow instructions. 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The text descriptions are in English.

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

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

The license for this dataset is a custom license. Refer to the licensing file to know more. 

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@sayakpaul](https://github.com/sayakpaul) for contributing this dataset.