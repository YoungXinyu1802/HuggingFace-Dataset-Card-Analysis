---
task_categories:
- object-detection
tags:
- roboflow
---

### Roboflow Dataset Page
[https://universe.roboflow.com/material-identification/garbage-classification-3/dataset/2](https://universe.roboflow.com/material-identification/garbage-classification-3/dataset/2?ref=roboflow2huggingface)

### Dataset Labels

```
['biodegradable', 'cardboard', 'glass', 'metal', 'paper', 'plastic']
```

### Citation

```
@misc{ garbage-classification-3_dataset,
    title = { GARBAGE CLASSIFICATION 3 Dataset },
    type = { Open Source Dataset },
    author = { Material Identification },
    howpublished = { \\url{ https://universe.roboflow.com/material-identification/garbage-classification-3 } },
    url = { https://universe.roboflow.com/material-identification/garbage-classification-3 },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { mar },
    note = { visited on 2023-01-02 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on July 27, 2022 at 5:44 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 10464 images.
GARBAGE-GARBAGE-CLASSIFICATION are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 1 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down



