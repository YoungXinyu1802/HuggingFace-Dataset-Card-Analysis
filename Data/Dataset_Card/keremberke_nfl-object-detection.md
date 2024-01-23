---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface

---

<div align="center">
  <img width="640" alt="keremberke/nfl-object-detection" src="https://huggingface.co/datasets/keremberke/nfl-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['helmet', 'helmet-blurred', 'helmet-difficult', 'helmet-partial', 'helmet-sideline']
```


### Number of Images

```json
{'valid': 1989, 'train': 6963, 'test': 995}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/nfl-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/home-mxzv1/nfl-competition/dataset/1](https://universe.roboflow.com/home-mxzv1/nfl-competition/dataset/1?ref=roboflow2huggingface?ref=roboflow2huggingface)

### Citation

```
@misc{ nfl-competition_dataset,
    title = { NFL-competition Dataset },
    type = { Open Source Dataset },
    author = { home },
    howpublished = { \\url{ https://universe.roboflow.com/home-mxzv1/nfl-competition } },
    url = { https://universe.roboflow.com/home-mxzv1/nfl-competition },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { sep },
    note = { visited on 2023-01-18 },
}
```

### License
Public Domain

### Dataset Summary
This dataset was exported via roboflow.com on December 29, 2022 at 8:12 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 9947 images.
Helmets are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 1280x720 (Stretch)

No image augmentation techniques were applied.



