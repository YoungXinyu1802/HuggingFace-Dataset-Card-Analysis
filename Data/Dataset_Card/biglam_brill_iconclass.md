---
annotations_creators:
- expert-generated
language: []
language_creators:
- expert-generated
license:
- cc0-1.0
multilinguality:
- other-iconclass-metadata
pretty_name: 'Brill Iconclass AI Test Set '
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
- image-classification
- image-to-text
task_ids:
- multi-class-image-classification
- multi-label-image-classification
- image-captioning
---

# Dataset Card for Brill Iconclass AI Test Set

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

- **Homepage:** [https://iconclass.org/testset/](https://iconclass.org/testset/)
- **Repository:**[https://iconclass.org/testset/](https://iconclass.org/testset/)
- **Paper:**[https://iconclass.org/testset/ICONCLASS_and_AI.pdf](https://iconclass.org/testset/ICONCLASS_and_AI.pdf)
- **Leaderboard:**
- **Point of Contact:**[info@iconclass.org](mailto:info@iconclass.org)

### Dataset Summary

> A test dataset and challenge to apply machine learning to collections described with the Iconclass classification system.

This dataset contains `87749` images with [Iconclass](https://iconclass.org/) metadata assigned to the images. The [iconclass](https://iconclass.org/) metadata classification system is intended to provide ['the comprehensive classification system for the content of images.'](https://iconclass.org/).

> Iconclass was developed in the Netherlands as a standard classification for recording collections, with the idea of assembling huge databases that will allow the retrieval of images featuring particular details, subjects or other common factors. It was developed in the 1970s and was loosely based on the Dewey Decimal System because it was meant to be used in art library card catalogs. [source](https://en.wikipedia.org/wiki/Iconclass)

The [Iconclass](https://iconclass.org) 

> view of the world is subdivided in 10 main categories...An Iconclass concept consists of an alphanumeric class number (“notation”) and a corresponding content definition (“textual correlate”). An object can be tagged with as many concepts as the user sees fit. [source](https://iconclass.org/)

These ten divisions are as follows:

- 0 Abstract, Non-representational Art
- 1 Religion and Magic
- 2 Nature
- 3 Human being, Man in general
- 4 Society, Civilization, Culture
- 5 Abstract Ideas and Concepts
- 6 History
- 7 Bible
- 8 Literature
- 9 Classical Mythology and Ancient History

Within each of these divisions further subdivision's are possible (9 or 10 subdivisions). For example, under `4 Society, Civilization, Culture`, one can find: 

- 41 · material aspects of daily life
- 42 · family, descendance
- 43 · recreation, amusement
- 44 · state; law; political life
- ... 

See [https://iconclass.org/4](https://iconclass.org/4) for the full list. 


To illustrate we can look at some example Iconclass classifications. 

`41A12` represents `castle`. This classification is generated via building from the 'base' division `4`, with the following attributes: 

- 4 · Society, Civilization, Culture
- 41 · material aspects of daily life
- 41A · housing
- 41A1 · civic architecture; edifices; dwellings 

[source](https://iconclass.org/41A12)

The construction of Iconclass of parts makes it particularly interesting (and challenging) to tackle via Machine Learning. Whilst one could tackle this dataset as a (multi) label image classification problem, this is only one way of tackling it. For example in the above label `castle` giving the model the 'freedom' to predict only a partial label could result in the prediction `41A` i.e. housing. Whilst a very particular form of housing this prediction for 'castle' is not 'wrong' so much as it is not as precise as a human cataloguer may provide. 

### Supported Tasks and Leaderboards

As discussed above this dataset could be tackled in various ways:

- as an image classification task
- as a multi-label classification task 
- as an image to text task
- as a task whereby a model predicts partial sequences of the label. 

This list is not exhaustive. 

### Languages

This dataset doesn't have a natural language. The labels themselves can be treated as a form of language i.e. the label can be thought of as a sequence of tokens that construct a 'sentence'. 


## Dataset Structure

The dataset contains a single configuration. 

### Data Instances

An example instance of the dataset is as follows: 

``` python
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=390x500 at 0x7FC7FFBBD2D0>,
 'label': ['31A235', '31A24(+1)', '61B(+54)', '61B:31A2212(+1)', '61B:31D14']}
```

### Data Fields

The dataset is made up of

- an image 
- a sequence of Iconclass labels 

### Data Splits

The dataset doesn't provide any predefined train, validation or test splits. 

## Dataset Creation

> To facilitate the creation of better models in the cultural heritage domain, and promote the research on tools and techniques using Iconclass, we are making this dataset freely available. All that we ask is that any use is acknowledged and results be shared so that we can all benefit. The content is sampled from the Arkyves database. [source](https://labs.brill.com/ictestset/) 

[More Information Needed]

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The images are samples from the [Arkyves database](https://brill.com/view/db/arko?language=en). This collection includes images from 

> from libraries and museums in many countries among them the Rijksmuseum in Amsterdam, the Netherlands Institute for Art History (RKD), the Herzog August Bibliothek in Wolfenbüttel, and the university libraries of Milan, Utrecht and Glasgow . [source](https://brill.com/view/db/arko?language=en)

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

The annotations are derived from the source dataset see above. It is likely that the majority of the annotations were created by staff with experience with the Iconclass metadata schema. 

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

Iconclass as a metadata standard absorbs biases from the time and place of it's creation (1940's Netherlands). In particular, '32B human races, peoples; nationalities' has been subject to criticism. '32B36 'primitive', 'pre-modern' peoples' is one example of a category which we may not wish to adopt. In general there are components of the subdivsions of `32B` which reflect a belief that race is a scientific category rather than socially constructed. 

These limitations are actively being explored by the Iconclass community, for example, see [Revising Iconclass section 32B human races, peoples; nationalities](https://web.archive.org/web/20210425131753/https://iconclass.org/Updating32B.pdf). 


One should be aware of these limitations to Iconclass, and in particular, before deploying a model trained on this data in any production settings. 

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Etienne Posthumus

### Licensing Information
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)

### Citation Information

```
@MISC{iconclass,
title = {Brill Iconclass AI Test Set},
author={Etienne Posthumus},
year={2020}
}

```


### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
