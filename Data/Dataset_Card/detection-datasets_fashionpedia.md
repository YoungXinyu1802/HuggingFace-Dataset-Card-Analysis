---
pretty_name: Fashionpedia
task_categories:
- object-detection
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- object-detection
- fashion
- computer-vision
paperswithcode_id: fashionpedia
---

# Dataset Card for Fashionpedia

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://fashionpedia.github.io/home/index.html
- **Repository:** https://github.com/cvdfoundation/fashionpedia
- **Paper:** https://arxiv.org/abs/2004.12276

### Dataset Summary

Fashionpedia is a dataset mapping out the visual aspects of the fashion world.
From the paper:
> Fashionpedia is a new dataset which consists of two parts: (1) an ontology built by fashion experts containing 27 main apparel categories, 19 apparel parts, 294 fine-grained attributes and their relationships; (2) a dataset with everyday and celebrity event fashion images annotated with segmentation masks and their associated per-mask fine-grained attributes, built upon the Fashionpedia ontology.
Fashionpedia has:
- 46781 images
- 342182 bounding-boxes

### Supported Tasks

- Object detection
- Image classification

### Languages

All of annotations use English as primary language.

## Dataset Structure

The dataset is structured as follows:
```py
DatasetDict({
    train: Dataset({
        features: ['image_id', 'image', 'width', 'height', 'objects'],
        num_rows: 45623
    })
    val: Dataset({
        features: ['image_id', 'image', 'width', 'height', 'objects'],
        num_rows: 1158
    })
})
```

### Data Instances

An example of the data for one image is:
```py
{'image_id': 23,
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=682x1024>,
 'width': 682,
 'height': 1024,
 'objects': {'bbox_id': [150311, 150312, 150313, 150314],
  'category': [23, 23, 33, 10],
  'bbox': [[445.0, 910.0, 505.0, 983.0],
   [239.0, 940.0, 284.0, 994.0],
   [298.0, 282.0, 386.0, 352.0],
   [210.0, 282.0, 448.0, 665.0]],
  'area': [1422, 843, 373, 56375]}}
 ```
 
 With the type of each field being defined as:
 ```py
 {'image_id': Value(dtype='int64'),
 'image': Image(decode=True),
 'width': Value(dtype='int64'),
 'height': Value(dtype='int64'),
 'objects': Sequence(feature={
   'bbox_id': Value(dtype='int64'), 
   'category': ClassLabel(num_classes=46, names=['shirt, blouse', 'top, t-shirt, sweatshirt', 'sweater', 'cardigan', 'jacket', 'vest', 'pants', 'shorts', 'skirt', 'coat', 'dress', 'jumpsuit', 'cape', 'glasses', 'hat', 'headband, head covering, hair accessory', 'tie', 'glove', 'watch', 'belt', 'leg warmer', 'tights, stockings', 'sock', 'shoe', 'bag, wallet', 'scarf', 'umbrella', 'hood', 'collar', 'lapel', 'epaulette', 'sleeve', 'pocket', 'neckline', 'buckle', 'zipper', 'applique', 'bead', 'bow', 'flower', 'fringe', 'ribbon', 'rivet', 'ruffle', 'sequin', 'tassel']), 
   'bbox': Sequence(feature=Value(dtype='float64'), length=4), 
   'area': Value(dtype='int64')}, 
length=-1)}
```

### Data Fields

The dataset has the following fields:

- `image_id`: Unique numeric ID of the image.
- `image`: A `PIL.Image.Image` object containing the image. Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the `"image"` column, *i.e.* `dataset[0]["image"]` should **always** be preferred over `dataset["image"][0]`
- `width`: Image width.
- `height`: Image height.
- `objects`: A dictionary containing bounding box metadata for the objects in the image:
  - `bbox_id`: Unique numeric ID of the bounding box annotation.
  - `category`: The object’s category.
  - `area`: The area of the bounding box.
  - `bbox`: The object’s bounding box (in the Pascal VOC format)  

### Data Splits

|                | Train  | Validation | Test |
|----------------|--------|------------|------|
| Images         | 45623  | 1158       | 0    |
| Bounding boxes | 333401 | 8781       | 0    |

## Additional Information

### Licensing Information

Fashionpedia is licensed under a Creative Commons Attribution 4.0 International License.

### Citation Information

```
@inproceedings{jia2020fashionpedia,
  title={Fashionpedia: Ontology, Segmentation, and an Attribute Localization Dataset},
  author={Jia, Menglin and Shi, Mengyun and Sirotenko, Mikhail and Cui, Yin and Cardie, Claire and Hariharan, Bharath and Adam, Hartwig and Belongie, Serge}
  booktitle={European Conference on Computer Vision (ECCV)},
  year={2020}
}
```

### Contributions

Thanks to [@blinjrm](https://github.com/blinjrm) for adding this dataset.
