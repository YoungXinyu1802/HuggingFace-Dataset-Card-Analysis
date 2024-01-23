---
annotations_creators:
- expert-generated
language: []
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality: []
pretty_name: YALTAi Tabular Dataset
size_categories:
- n<1K
source_datasets: []
tags:
- manuscripts
- LAM
task_categories:
- object-detection
task_ids: []
---

# YALTAi Tabular Dataset

## Table of Contents
- [YALTAi Tabular Dataset](#YALTAi-Tabular-Dataset)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** [https://doi.org/10.5281/zenodo.6827706](https://doi.org/10.5281/zenodo.6827706) 
- **Paper:** [https://arxiv.org/abs/2207.11230](https://arxiv.org/abs/2207.11230)

### Dataset Summary

This dataset contains a subset of data used in the paper [You Actually Look Twice At it (YALTAi): using an object detectionapproach instead of region segmentation within the Kraken engine](https://arxiv.org/abs/2207.11230). This paper proposes treating page layout recognition on historical documents as an object detection task (compared to the usual pixel segmentation approach). This dataset covers pages with tabular information with the following objects "Header", "Col", "Marginal", "text". 

### Supported Tasks and Leaderboards

- `object-detection`: This dataset can be used to train a model for object-detection on historic document images. 


## Dataset Structure

This dataset has two configurations. These configurations both cover the same data and annotations but provide these annotations in different forms to make it easier to integrate the data with existing processing pipelines. 

- The first configuration, `YOLO`, uses the data's original format. 
- The second configuration converts the YOLO format into a format which is closer to the `COCO` annotation format. This is done to make it easier to work with the `feature_extractor`s from the `Transformers` models for object detection, which expect data to be in a COCO style format. 

### Data Instances

An example instance from the COCO config:

```
{'height': 2944,
 'image': <PIL.PngImagePlugin.PngImageFile image mode=L size=2064x2944 at 0x7FA413CDA210>,
 'image_id': 0,
 'objects': [{'area': 435956,
   'bbox': [0.0, 244.0, 1493.0, 292.0],
   'category_id': 0,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 88234,
   'bbox': [305.0, 127.0, 562.0, 157.0],
   'category_id': 2,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 5244,
   'bbox': [1416.0, 196.0, 92.0, 57.0],
   'category_id': 2,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 5720,
   'bbox': [1681.0, 182.0, 88.0, 65.0],
   'category_id': 2,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 374085,
   'bbox': [0.0, 540.0, 163.0, 2295.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 577599,
   'bbox': [104.0, 537.0, 253.0, 2283.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 598670,
   'bbox': [304.0, 533.0, 262.0, 2285.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 56,
   'bbox': [284.0, 539.0, 8.0, 7.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 1868412,
   'bbox': [498.0, 513.0, 812.0, 2301.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 307800,
   'bbox': [1250.0, 512.0, 135.0, 2280.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 494109,
   'bbox': [1330.0, 503.0, 217.0, 2277.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 52,
   'bbox': [1734.0, 1013.0, 4.0, 13.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []},
  {'area': 90666,
   'bbox': [0.0, 1151.0, 54.0, 1679.0],
   'category_id': 1,
   'id': 0,
   'image_id': '0',
   'iscrowd': False,
   'segmentation': []}],
 'width': 2064}
```

An example instance from the YOLO config: 

``` python
{'image': <PIL.PngImagePlugin.PngImageFile image mode=L size=2064x2944 at 0x7FAA140F2450>,
 'objects': {'bbox': [[747, 390, 1493, 292],
   [586, 206, 562, 157],
   [1463, 225, 92, 57],
   [1725, 215, 88, 65],
   [80, 1688, 163, 2295],
   [231, 1678, 253, 2283],
   [435, 1675, 262, 2285],
   [288, 543, 8, 7],
   [905, 1663, 812, 2301],
   [1318, 1653, 135, 2280],
   [1439, 1642, 217, 2277],
   [1737, 1019, 4, 13],
   [26, 1991, 54, 1679]],
  'label': [0, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]}}
```



### Data Fields

The fields for the YOLO config:

- `image`: the image
- `objects`: the annotations which consist of:
    - `bbox`: a list of bounding boxes for the image
    - `label`: a list of labels for this image

The fields for the COCO config:

- `height`: height of the image
- `width`: width of the image
- `image`: image 
- `image_id`: id for the image
- `objects`: annotations in COCO format, consisting of a list containing dictionaries with the following keys:
  - `bbox`: bounding boxes for the images
  - `category_id`: a label for the image
  - `image_id`: id for the image
  - `iscrowd`: COCO `iscrowd` flag
  - `segmentation`: COCO segmentation annotations (empty in this case but kept for compatibility with other processing scripts)


 
### Data Splits

The dataset contains a train, validation and test split with the following numbers per split:


|          | train | validation | test |
|----------|-------|------------|------|
| examples | 196   | 22         | 135  |


## Dataset Creation

> [this] dataset was produced using a single source, the Lectaurep Repertoires dataset [Rostaing et al., 2021], which served as a basis for only the training and development split. The testset is composed of original data, from various documents, from the 17th century up to the early 20th with a single soldier war report. The test set is voluntarily very different and out of domain with column borders that are not drawn nor printed in certain cases, layout in some kind of masonry layout. p.8
.
### Curation Rationale

This dataset was created to produce a simplified version of the [Lectaurep Repertoires dataset](https://github.com/HTR-United/lectaurep-repertoires), which was found to contain:

> around 16 different ways to describe columns, from Col1 to Col7, the case-different col1-col7 and finally ColPair and ColOdd, which we all reduced to Col p.8



### Source Data

#### Initial Data Collection and Normalization

The LECTAUREP (LECTure Automatique de REPertoires) project, which began in 2018, is a joint initiative of the Minutier central des notaires de Paris, the National Archives and the 
 Minutier central des notaires de Paris of the National Archives, the [ALMAnaCH (Automatic Language Modeling and Analysis & Computational Humanities)](https://www.inria.fr/en/almanach) team at Inria and the EPHE (Ecole Pratique des Hautes Etudes), in partnership with the Ministry of Culture.

> The lectaurep-bronod corpus brings together 100 pages from the repertoire of Maître Louis Bronod (1719-1765), notary in Paris from December 13, 1719 to July 23, 1765. The pages concerned were written during the years 1742 to 1745.

#### Who are the source language producers?

[More information needed]

### Annotations

|          | Train | Dev | Test | Total | Average area | Median area |
|----------|-------|-----|------|-------|--------------|-------------|
| Col      | 724   | 105 | 829  | 1658  | 9.32         | 6.33        |
| Header   | 103   | 15  | 42   | 160   | 6.78         | 7.10        |
| Marginal | 60    | 8   | 0    | 68    | 0.70         | 0.71        |
| Text     | 13    | 5   | 0    | 18    | 0.01         | 0.00        |
|          |       |     | -    |       |              |             |


#### Annotation process

[More information needed]

#### Who are the annotators?

[More information needed]

### Personal and Sensitive Information

This data does not contain information relating to living individuals.

## Considerations for Using the Data

### Social Impact of Dataset

A growing number of datasets are related to page layout for historical documents. This dataset offers a different approach to annotating these datasets (focusing on object detection rather than pixel-level annotations). Improving document layout recognition can have a positive impact on downstream tasks, in particular Optical Character Recognition.

### Discussion of Biases

Historical documents contain a wide variety of page layouts. This means that the ability of models trained on this dataset to transfer to documents with very different layouts is not guaranteed. 

### Other Known Limitations

[More information needed]


## Additional Information

### Dataset Curators


### Licensing Information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

### Citation Information

```
@dataset{clerice_thibault_2022_6827706,
  author       = {Clérice, Thibault},
  title        = {YALTAi: Tabular Dataset},
  month        = jul,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.6827706},
  url          = {https://doi.org/10.5281/zenodo.6827706}
}
```



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6827706.svg)](https://doi.org/10.5281/zenodo.6827706)


    
### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
