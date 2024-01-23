---
language:
- en
license: cc-by-4.0

tags:
- computer-vision
- object-detection
- ms-coco

datasets:
- stuff-thing
- stuff-only

metrics:
- accuracy
- iou
---

# Dataset Card for COCO-Stuff

[![CI](https://github.com/shunk031/huggingface-datasets_cocostuff/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/huggingface-datasets_cocostuff/actions/workflows/ci.yaml)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Preprocessing](#dataset-preprocessing)
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

- Homepage: https://github.com/nightrome/cocostuff
- Repository: https://github.com/nightrome/cocostuff
- Paper (preprint): https://arxiv.org/abs/1612.03716
- Paper (CVPR2018): https://openaccess.thecvf.com/content_cvpr_2018/html/Caesar_COCO-Stuff_Thing_and_CVPR_2018_paper.html

### Dataset Summary

COCO-Stuff is the largest existing dataset with dense stuff and thing annotations. 

From the paper:

> Semantic classes can be either things (objects with a well-defined shape, e.g. car, person) or stuff (amorphous background regions, e.g. grass, sky). While lots of classification and detection works focus on thing classes, less attention has been given to stuff classes. Nonetheless, stuff classes are important as they allow to explain important aspects of an image, including (1) scene type; (2) which thing classes are likely to be present and their location (through contextual reasoning); (3) physical attributes, material types and geometric properties of the scene. To understand stuff and things in context we introduce COCO-Stuff, which augments all 164K images of the COCO 2017 dataset with pixel-wise annotations for 91 stuff classes. We introduce an efficient stuff annotation protocol based on superpixels, which leverages the original thing annotations. We quantify the speed versus quality trade-off of our protocol and explore the relation between annotation time and boundary complexity. Furthermore, we use COCO-Stuff to analyze: (a) the importance of stuff and thing classes in terms of their surface cover and how frequently they are mentioned in image captions; (b) the spatial relations between stuff and things, highlighting the rich contextual relations that make our dataset unique; (c) the performance of a modern semantic segmentation method on stuff and thing classes, and whether stuff is easier to segment than things.

### Dataset Preprocessing

### Supported Tasks and Leaderboards

### Languages

All of annotations use English as primary language.

## Dataset Structure

### Data Instances

When loading a specific configuration, users has to append a version dependent suffix:

```python
from datasets import load_dataset
load_dataset("shunk031/cocostuff", "stuff-thing")
```

#### stuff-things

An example of looks as follows.

```json
{
    'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x480 at 0x7FCA033C9C40>,
    'image_filename': '000000000009.jpg',
    'image_id': '9',
    'width': 640
    'height': 480,
    'objects': [
        {
            'object_id': '121',
            'x': 0,
            'y': 11,
            'w': 640,
            'h': 469,
            'name': 'food-other'
        },
        {
            'object_id': '143',
            'x': 0,
            'y': 0
            'w': 640,
            'h': 480,
            'name': 'plastic'
        },
        {
            'object_id': '165',
            'x': 0,
            'y': 0,
            'w': 319,
            'h': 118,
            'name': 'table'
        },
        {
            'object_id': '183',
            'x': 0,
            'y': 2,
            'w': 631,
            'h': 472,
            'name': 'unknown-183'
        }
    ],
    'stuff_map': <PIL.PngImagePlugin.PngImageFile image mode=L size=640x480 at 0x7FCA0222D880>,
 }
```

#### stuff-only

An example of looks as follows.

```json
{
    'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x480 at 0x7FCA033C9C40>,
    'image_filename': '000000000009.jpg',
    'image_id': '9',
    'width': 640
    'height': 480,
    'objects': [
        {
            'object_id': '121',
            'x': 0,
            'y': 11,
            'w': 640,
            'h': 469,
            'name': 'food-other'
        },
        {
            'object_id': '143',
            'x': 0,
            'y': 0
            'w': 640,
            'h': 480,
            'name': 'plastic'
        },
        {
            'object_id': '165',
            'x': 0,
            'y': 0,
            'w': 319,
            'h': 118,
            'name': 'table'
        },
        {
            'object_id': '183',
            'x': 0,
            'y': 2,
            'w': 631,
            'h': 472,
            'name': 'unknown-183'
        }
    ]
 }
```

### Data Fields

#### stuff-things

- `image`: A `PIL.Image.Image` object containing the image.
- `image_id`: Unique numeric ID of the image.
- `image_filename`: File name of the image.
- `width`: Image width.
- `height`: Image height.
- `stuff_map`: A `PIL.Image.Image` object containing the Stuff + thing PNG-style annotations
- `objects`: Holds a list of `Object` data classes:
    - `object_id`: Unique numeric ID of the object.
    - `x`: x coordinate of bounding box's top left corner.
    - `y`: y coordinate of bounding box's top left corner.
    - `w`: Bounding box width.
    - `h`: Bounding box height.
    - `name`: object name

#### stuff-only

- `image`: A `PIL.Image.Image` object containing the image.
- `image_id`: Unique numeric ID of the image.
- `image_filename`: File name of the image.
- `width`: Image width.
- `height`: Image height.
- `objects`: Holds a list of `Object` data classes:
    - `object_id`: Unique numeric ID of the object.
    - `x`: x coordinate of bounding box's top left corner.
    - `y`: y coordinate of bounding box's top left corner.
    - `w`: Bounding box width.
    - `h`: Bounding box height.
    - `name`: object name

### Data Splits

| name        | train   | validation |
|-------------|--------:|-----------:|
| stuff-thing | 118,280 | 5,000      |
| stuff-only  | 118,280 | 5,000      |

## Dataset Creation

### Curation Rationale

### Source Data

#### Initial Data Collection and Normalization

#### Who are the source language producers?

### Annotations

#### Annotation process

#### Who are the annotators?

From the paper:

> COCO-Stuff contains 172 classes: 80 thing, 91 stuff, and 1 class unlabeled. The 80 thing classes are the same as in COCO [35]. The 91 stuff classes are curated by an expert annotator. The class unlabeled is used in two situations: if a label does not belong to any of the 171 predefined classes, or if the annotator cannot infer the label of a pixel.

### Personal and Sensitive Information

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

## Additional Information

### Dataset Curators

### Licensing Information

COCO-Stuff is a derivative work of the COCO dataset. The authors of COCO do not in any form endorse this work. Different licenses apply:
- COCO images: [Flickr Terms of use](http://cocodataset.org/#termsofuse) 
- COCO annotations: [Creative Commons Attribution 4.0 License](http://cocodataset.org/#termsofuse)
- COCO-Stuff annotations & code: [Creative Commons Attribution 4.0 License](http://cocodataset.org/#termsofuse)

### Citation Information

```bibtex
@INPROCEEDINGS{caesar2018cvpr,
  title={COCO-Stuff: Thing and stuff classes in context},
  author={Caesar, Holger and Uijlings, Jasper and Ferrari, Vittorio},
  booktitle={Computer vision and pattern recognition (CVPR), 2018 IEEE conference on},
  organization={IEEE},
  year={2018}
}
```

### Contributions

Thanks to [@nightrome](https://github.com/nightrome) for publishing the COCO-Stuff dataset.
