---
task_categories:
- object-detection
tags:
- roboflow
---

### Roboflow Dataset Page
[https://universe.roboflow.com/riis/aerial-sheep/dataset/1](https://universe.roboflow.com/riis/aerial-sheep/dataset/1?ref=roboflow2huggingface)

### Dataset Labels

```
['sheep']
```

### Citation

```
@misc{ aerial-sheep_dataset,
    title = { Aerial Sheep Dataset },
    type = { Open Source Dataset },
    author = { Riis },
    howpublished = { \\url{ https://universe.roboflow.com/riis/aerial-sheep } },
    url = { https://universe.roboflow.com/riis/aerial-sheep },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { jun },
    note = { visited on 2023-01-02 },
}
```

### License
Public Domain

### Dataset Summary
This dataset was exported via roboflow.com on December 2, 2022 at 4:47 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 4133 images.
Sheep are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 600x600 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Randomly crop between 0 and 20 percent of the image
* Random brigthness adjustment of between -15 and +15 percent
* Random exposure adjustment of between -10 and +10 percent



