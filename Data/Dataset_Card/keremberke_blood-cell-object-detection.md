---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Biology
---

<div align="center">
  <img width="640" alt="keremberke/blood-cell-object-detection" src="https://huggingface.co/datasets/keremberke/blood-cell-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['platelets', 'rbc', 'wbc']
```


### Number of Images

```json
{'train': 255, 'test': 36, 'valid': 73}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/blood-cell-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/team-roboflow/blood-cell-detection-1ekwu/dataset/3](https://universe.roboflow.com/team-roboflow/blood-cell-detection-1ekwu/dataset/3?ref=roboflow2huggingface)

### Citation

```
@misc{ blood-cell-detection-1ekwu_dataset,
    title = { Blood Cell Detection Dataset },
    type = { Open Source Dataset },
    author = { Team Roboflow },
    howpublished = { \\url{ https://universe.roboflow.com/team-roboflow/blood-cell-detection-1ekwu } },
    url = { https://universe.roboflow.com/team-roboflow/blood-cell-detection-1ekwu },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { nov },
    note = { visited on 2023-01-18 },
}
```

### License
Public Domain

### Dataset Summary
This dataset was exported via roboflow.com on November 4, 2022 at 7:46 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 364 images.
Cells are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

No image augmentation techniques were applied.



