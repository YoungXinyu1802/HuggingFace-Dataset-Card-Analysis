---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Construction
- Logistics
- Utilities
- Damage Risk
- Ppe
- Construction
- Utilities
- Manufacturing
- Logistics
- Ppe
- Assembly Line
- Warehouse
- Factory
---

<div align="center">
  <img width="640" alt="keremberke/construction-safety-object-detection" src="https://huggingface.co/datasets/keremberke/construction-safety-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['barricade', 'dumpster', 'excavators', 'gloves', 'hardhat', 'mask', 'no-hardhat', 'no-mask', 'no-safety vest', 'person', 'safety net', 'safety shoes', 'safety vest', 'dump truck', 'mini-van', 'truck', 'wheel loader']
```


### Number of Images

```json
{'train': 307, 'valid': 57, 'test': 34}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/construction-safety-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety/dataset/1](https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ construction-site-safety_dataset,
    title = { Construction Site Safety Dataset },
    type = { Open Source Dataset },
    author = { Roboflow Universe Projects },
    howpublished = { \\url{ https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety } },
    url = { https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { jan },
    note = { visited on 2023-01-26 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on December 29, 2022 at 11:22 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 398 images.
Construction are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



