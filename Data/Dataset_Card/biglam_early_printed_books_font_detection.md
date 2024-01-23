---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: labels
    sequence:
      class_label:
        names:
          0: greek
          1: antiqua
          2: other_font
          3: not_a_font
          4: italic
          5: rotunda
          6: textura
          7: fraktur
          8: schwabacher
          9: hebrew
          10: bastarda
          11: gotico_antiqua
  splits:
  - name: test
    num_bytes: 2345451
    num_examples: 10757
  - name: train
    num_bytes: 5430875
    num_examples: 24866
  download_size: 44212934313
  dataset_size: 7776326
annotations_creators:
- expert-generated
language: []
language_creators: []
license:
- cc-by-nc-sa-4.0
multilinguality: []
pretty_name: Early Printed Books Font Detection Dataset
size_categories:
- 10K<n<100K
source_datasets: []
tags: []
task_categories:
- image-classification
task_ids:
- multi-label-image-classification
---

# Dataset Card for Early Printed Books Font Detection Dataset

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
- **Repository:**https://doi.org/10.5281/zenodo.3366686
- **Paper:**: https://doi.org/10.1145/3352631.3352640
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

> This dataset is composed of photos of various resolution of 35'623 pages of printed books dating from the 15th to the 18th century. Each page has been attributed by experts from one to five labels corresponding to the font groups used in the text, with two extra-classes for non-textual content and fonts not present in the following list:  Antiqua, Bastaπrda, Fraktur, Gotico Antiqua, Greek, Hebrew, Italic, Rotunda, Schwabacher, and Textura.

[More Information Needed]

### Supported Tasks and Leaderboards

The primary use case for this datasets is
- `multi-label-image-classification`: This dataset can be used to train a model for multi label image classification where each image can have one, or more labels. 
- `image-classification`: This dataset could also be adapted to only predict a single label for each image

### Languages

The dataset includes books from a range of libraries (see below for further details). The paper doesn't provide a detailed overview of language breakdown. However, the books are from the 15th-18th century and appear to be dominated by European languages from that time period. The dataset also includes Hebrew. 

[More Information Needed]


## Dataset Structure

This dataset has a single configuration.

### Data Instances

An example instance from this dataset:

```python
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x3840 at 0x7F6AC192D850>,
 'labels': [5]}
```

### Data Fields

This dataset contains two fields:

- `image`: the image of the book page
- `labels`: one or more labels for the font used in the book page depicted in the `image`

### Data Splits

The dataset is broken into a train and test split with the following breakdown of number of examples: 

- train: 24,866 
- test: 10,757

## Dataset Creation

### Curation Rationale

The dataset was created to help train and evaluate automatic methods for font detection. The paper describing the paper also states that:

>data was cherry-picked, thus it is not statistically representative of what can be found in libraries. For example, as we had a small amount of Textura at the start, we specifically looked for more pages containing this font group, so we can expect that less than 3.6 % of randomly selected  pages from libraries would contain Textura.

### Source Data

#### Initial Data Collection and Normalization

The images in this dataset are from books held by the British Library (London), Bayerische Staatsbibliothek München, Staatsbibliothek zu Berlin, Universitätsbibliothek Erlangen, Universitätsbibliothek Heidelberg, Staats- und Universitäatsbibliothek Göttingen, Stadt- und Universitätsbibliothek Köln, Württembergische Landesbibliothek Stuttgart and Herzog August Bibliothek Wolfenbüttel. 

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

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.

