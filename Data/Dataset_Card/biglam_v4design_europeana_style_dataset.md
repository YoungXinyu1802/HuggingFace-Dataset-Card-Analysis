---
annotations_creators:
- expert-generated
language: []
language_creators: []
license:
- other
multilinguality: []
pretty_name: V4Design Europeana style dataset
size_categories: []
source_datasets: []
tags: []
task_categories:
- image-classification
task_ids: []
dataset_info:
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: uri
    dtype: string
  - name: style
    dtype:
      class_label:
        names:
          0: Rococo
          1: Baroque
          2: Other
  - name: rights
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 536168550.923
    num_examples: 1613
  download_size: 535393230
  dataset_size: 536168550.923
---

# Dataset Card for V4Design Europeana style dataset

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
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

This dataset contains:
> 1614 paintings belonging to the categories Baroque, Rococo, and Other. The images were obtained using the Europeana Search API, selecting open objects from the art thematic collection. 24k images were obtained, from which the current dataset was derived. The labels were added by the V4Design team, using a custom annotation tool. As described in the project documentation, other categories were used besides Baroque and Rococo. But for the sake of training a machine learning model we have retained only the categories with a significant number of annotations [source](https://zenodo.org/record/4896487)

This version of the dataset is generated using the [CSV file](https://zenodo.org/record/4896487) hosted on Zenodo. This CSV file contains the labels with URLs for the relevant images. Some of these URLs no longer resolve to an image. For consitency with the original dataset and if these URLs become valid again, these rows of the data are preserved here. If you want only successfully loaded images in your dataset, you can filter out the missing images as follows. 

```python
ds = ds.filter(lambda x: x['image'] is not None)
```
 
### Supported Tasks and Leaderboards

This dataset is primarily intended for `image-classification`. 

### Languages

[More Information Needed]

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

[More Information Needed]

### Citation Information

```
@dataset{europeana_2021_4896487,
  author       = {Europeana and
                  V4Design},
  title        = {V4Design/Europeana style dataset},
  month        = jun,
  year         = 2021,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.4896487},
  url          = {https://doi.org/10.5281/zenodo.4896487}
}
```

### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
