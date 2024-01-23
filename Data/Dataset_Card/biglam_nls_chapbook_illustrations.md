---
annotations_creators:
- expert-generated
language_creators: []
license:
- other
multilinguality: []
pretty_name: National Library of Scotland Chapbook Illustrations
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- lam
- historic
task_categories:
- object-detection
- image-classification
task_ids:
- multi-class-image-classification
---

# Dataset Card for National Library of Scotland Chapbook Illustrations

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

- **Homepage:** https://www.robots.ox.ac.uk/~vgg/research/chapbooks/
- **Repository:** https://data.nls.uk/data/digitised-collections/chapbooks-printed-in-scotland/
- **Paper:** https://www.robots.ox.ac.uk/~vgg/research/chapbooks/data/dutta2021visual.pdf
- **Leaderboard:**
- **Point of Contact:** giles.bergel@eng.ox.ac.uk

### Dataset Summary

This dataset comprises of images from chapbooks held by the [National Library of Scotland](https://www.nls.uk/) and digitised and published as its [Chapbooks Printed in Scotland](https://data.nls.uk/data/digitised-collections/chapbooks-printed-in-scotland/) dataset.

> "Chapbooks were staple everyday reading material from the end of the 17th to the later 19th century. They were usually printed on a single sheet and then folded into books of 8, 12, 16 and 24 pages, and they were often illustrated with crude woodcuts. Their subjects range from news courtship, humour, occupations, fairy tales, apparitions, war, politics, crime, executions, historical figures, transvestites [*sic*] and freemasonry to religion and, of course, poetry. It has been estimated that around two thirds of chapbooks contain songs and poems, often under the title garlands." -[Source](https://data.nls.uk/data/digitised-collections/chapbooks-printed-in-scotland/)

Chapbooks were frequently illustrated, particularly on their title pages to attract customers, usually with a woodblock-printed illustration, or occasionally with a stereotyped woodcut or cast metal ornament. Apart from their artistic interest, these illustrations can also provide historical evidence such as the date, place or persons behind the publication of an item.

This dataset contains annotations for a subset of these chapbooks, created by Giles Bergel and Abhishek Dutta, based in the [Visual Geometry Group](https://www.robots.ox.ac.uk/~vgg/) in the University of Oxford. They were created under a National Librarian of Scotland's Fellowship in Digital Scholarship [awarded](https://data.nls.uk/projects/the-national-librarians-research-fellowship-in-digital-scholarship/) to Giles Bergel in 2020. These annotations provide bounding boxes around illustrations printed on a subset of the chapbook pages, created using a combination of manual annotation and machine classification, described in [this paper](https://www.robots.ox.ac.uk/~vgg/research/chapbooks/data/dutta2021visual.pdf). 

The dataset also includes computationally inferred 'visual groupings' to which illustrated chapbook pages may belong. These groupings are based on the recurrence of illustrations on chapbook pages, as determined through the use of the [VGG Image Search Engine (VISE) software](https://www.robots.ox.ac.uk/~vgg/software/vise/)


### Supported Tasks and Leaderboards

- `object-detection`: the dataset contains bounding boxes for images contained in the Chapbooks
- `image-classification`: a configuration for this dataset provides a classification label indicating if a page contains an illustration or not. 
- `image-matching`: a configuration for this dataset contains the annotations sorted into clusters or 'visual groupings' of illustrations that contain visually-matching content as determined by using the [VGG Image Search Engine (VISE) software](https://www.robots.ox.ac.uk/~vgg/software/vise/). 

The performance on the `object-detection` task reported in the paper [Visual Analysis of Chapbooks Printed in Scotland](https://dl.acm.org/doi/10.1145/3476887.3476893) is as follows:

| IOU threshold | Precision | Recall |
|---------------|-----------|--------|
| 0.50          | 0.993     | 0.911  |
| 0.75          | 0.987     | 0.905  |
| 0.95          | 0.973     | 0.892  |


The performance on the `image classification` task reported in the paper [Visual Analysis of Chapbooks Printed in Scotland](https://dl.acm.org/doi/10.1145/3476887.3476893) is as follows: 

Images in original dataset: 47329
Numbers of images on which at least one illustration was detected: 3629

Note that these figures do not represent images that contained multiple detections. 

See the [paper](https://dl.acm.org/doi/10.1145/3476887.3476893) for examples of false-positive detections.

The performance on the 'image-matching' task is undergoing evaluation.  

### Languages

Text accompanying the illustrations is in English, Scots or Scottish Gaelic.

## Dataset Structure

### Data Instances

An example instance from the `illustration-detection` split:

```python
{'image_id': 4,
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=600x1080>,
 'width': 600,
 'height': 1080,
 'objects': [{'category_id': 0,
   'image_id': '4',
   'id': 1,
   'area': 110901,
   'bbox': [34.529998779296875,
    556.8300170898438,
    401.44000244140625,
    276.260009765625],
   'segmentation': [[34.529998779296875,
     556.8300170898438,
     435.9700012207031,
     556.8300170898438,
     435.9700012207031,
     833.0900268554688,
     34.529998779296875,
     833.0900268554688]],
   'iscrowd': False}]}
```

An example instance from the `image-classification` split:

```python
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=600x1080>,
 'label': 1}
```

An example from the `image-matching` split:

```python
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=600x1080>,
 'group-label': 231}
```


### Data Fields

The fields for the `illustration-detection` config:

- image_id: id for the image
- height: height of the image
- width: width of the image
- image: image of the chapbook page
- objects: annotations in COCO format, consisting of a list containing dictionaries with the following keys:
  - bbox: bounding boxes for the images
  - category_id: a label for the image
  - image_id: id for the image
  - iscrowd: COCO is a crowd flag
  - segmentation: COCO segmentation annotations (empty in this case but kept for compatibility with other processing scripts)

The fields for the `image-classification` config:

- image: image
- label: a label indicating if the page contains an illustration or not 

The fields for the `image-matching` config:

- image: image of the chapbook page
- label: an id for a particular instance of an image i.e. the same images will share the same id. 

### Data Splits

There is a single split `train` for all configs. K-fold validation was used in the [paper](https://dl.acm.org/doi/10.1145/3476887.3476893) describing this dataset, so no existing splits were defined. 


## Dataset Creation

### Curation Rationale

The dataset was created to facilitate research into Scottish chapbook illustration and publishing. Detected illustrations can be browsed under publication metadata: together with the use of [VGG Image Search Engine (VISE) software](https://www.robots.ox.ac.uk/~vgg/software/vise/), this allows researchers to identify matching imagery and to infer the source of a chapbook from partial evidence. This browse and search functionality is available in this [public demo](http://meru.robots.ox.ac.uk/nls_chapbooks/filelist) documented [here](https://www.robots.ox.ac.uk/~vgg/research/chapbooks/)  

### Source Data

#### Initial Data Collection and Normalization

The initial data was taken from the [National Library of Scotland's Chapbooks Printed in Scotland dataset](https://data.nls.uk/data/digitised-collections/chapbooks-printed-in-scotland/) No normalisation was performed, but only the images and a subset of the metadata was used. OCR text was not used.

#### Who are the source language producers?

The initial dataset was created by the National Library of Scotland from scans and in-house curated catalogue descriptions for the NLS [Data Foundry](https://data.nls.uk) under the direction of Dr. Sarah Ames.

 This subset of the data was created by Dr. Giles Bergel and Dr. Abhishek Dutta using a combination of manual annotation and machine classification, described below. 

### Annotations

#### Annotation process

Annotation was initially performed on a subset of 337 of the 47329 images, using the [VGG List Annotator (LISA](https://gitlab.com/vgg/lisa) software. Detected illustrations, displayed as annotations in LISA, were reviewed and refined in a number of passes (see [this paper](https://dl.acm.org/doi/10.1145/3476887.3476893) for more details). Initial detections were performed with an [EfficientDet](https://ai.googleblog.com/2020/04/efficientdet-towards-scalable-and.html) object detector trained on [COCO](https://cocodataset.org/#home), the annotation of which is described in [this paper](https://arxiv.org/abs/1405.0312) 

#### Who are the annotators?

Abhishek Dutta created the initial 337 annotations for retraining the EfficentDet model. Detections were reviewed and in some cases revised by Giles Bergel.

### Personal and Sensitive Information

None

## Considerations for Using the Data

### Social Impact of Dataset

We believe this dataset will assist in the training and benchmarking of illustration detectors. It is hoped that by automating a task that would otherwise require manual annotation it will save researchers time and labour in preparing data for both machine and human analysis. The dataset in question is based on a category of popular literature that reflected the learning, tastes and cultural faculties of both its large audiences and its largely-unknown creators - we hope that its use, reuse and adaptation will highlight the importance of cheap chapbooks in the spread of literature, knowledge and entertainment in both urban and rural regions of Scotland and the United Kingdom during this period. 

### Discussion of Biases

While the original Chapbooks Printed in Scotland is the largest single collection of digitised chapbooks, it is as yet unknown if it is fully representative of all chapbooks printed in Scotland, or of cheap printed literature in general. It is known that a small number of chapbooks (less than 0.1%) within the original collection were not printed in Scotland but this is not expected to have a significant impact on the profile of the collection as a representation of the population of chapbooks as a whole.

 The definition of an illustration as opposed to an ornament or other non-textual printed feature is somewhat arbitrary: edge-cases were evaluated by conformance with features that are most characteristic of the chapbook genre as a whole in terms of content, style or placement on the page.

As there is no consensus definition of the chapbook even among domain specialists, the composition of the original dataset is based on the judgement of those who assembled and curated the original collection.

### Other Known Limitations

Within this dataset, illustrations are repeatedly reused to an unusually high degree compared to other printed forms. The positioning of illustrations on the page and the size and format of chapbooks as a whole is also characteristic of the chapbook format in particular. The extent to which these annotations may be generalised to other printed works is under evaluation: initial results have been promising for other letterpress illustrations surrounded by texts. 

## Additional Information

### Dataset Curators

- Giles Bergel
- Abhishek Dutta

### Licensing Information

In accordance with the [original data](https://data.nls.uk/data/digitised-collections/chapbooks-printed-in-scotland/), this dataset is in the public domain.   

### Citation Information

``` bibtex
@inproceedings{10.1145/3476887.3476893,
author = {Dutta, Abhishek and Bergel, Giles and Zisserman, Andrew},
title = {Visual Analysis of Chapbooks Printed in Scotland},
year = {2021},
isbn = {9781450386906},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3476887.3476893},
doi = {10.1145/3476887.3476893},
abstract = {Chapbooks were short, cheap printed booklets produced in large quantities in Scotland, England, Ireland, North America and much of Europe between roughly the seventeenth and nineteenth centuries. A form of popular literature containing songs, stories, poems, games, riddles, religious writings and other content designed to appeal to a wide readership, they were frequently illustrated, particularly on their title-pages. This paper describes the visual analysis of such chapbook illustrations. We automatically extract all the illustrations contained in the National Library of Scotland Chapbooks Printed in Scotland dataset, and create a visual search engine to search this dataset using full or part-illustrations as queries. We also cluster these illustrations based on their visual content, and provide keyword-based search of the metadata associated with each publication. The visual search; clustering of illustrations based on visual content; and metadata search features enable researchers to forensically analyse the chapbooks dataset and to discover unnoticed relationships between its elements. We release all annotations and software tools described in this paper to enable reproduction of the results presented and to allow extension of the methodology described to datasets of a similar nature.},
booktitle = {The 6th International Workshop on Historical Document Imaging and Processing},
pages = {67–72},
numpages = {6},
keywords = {illustration detection, chapbooks, image search, visual grouping, printing, digital scholarship, illustration dataset},
location = {Lausanne, Switzerland},
series = {HIP '21}
}
```


### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) and Giles Bergel for adding this dataset.