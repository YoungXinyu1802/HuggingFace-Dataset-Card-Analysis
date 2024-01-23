---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface

---

<div align="center">
  <img width="640" alt="keremberke/valorant-object-detection" src="https://huggingface.co/datasets/keremberke/valorant-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['dropped spike', 'enemy', 'planted spike', 'teammate']
```


### Number of Images

```json
{'valid': 1983, 'train': 6927, 'test': 988}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/valorant-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/daniels-magonis-0pjzx/valorant-9ufcp/dataset/3](https://universe.roboflow.com/daniels-magonis-0pjzx/valorant-9ufcp/dataset/3?ref=roboflow2huggingface)

### Citation

```
@misc{ valorant-9ufcp_dataset,
    title = { valorant Dataset },
    type = { Open Source Dataset },
    author = { Daniels Magonis },
    howpublished = { \\url{ https://universe.roboflow.com/daniels-magonis-0pjzx/valorant-9ufcp } },
    url = { https://universe.roboflow.com/daniels-magonis-0pjzx/valorant-9ufcp },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { nov },
    note = { visited on 2023-01-27 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on December 22, 2022 at 5:10 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 9898 images.
Planted are annotated in COCO format.

The following pre-processing was applied to each image:
* Resize to 416x416 (Stretch)

No image augmentation techniques were applied.



