---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Construction
- Utilities
- Manufacturing
- Logistics
- Ppe
- Assembly Line
- Warehouse
- Factory
- Construction
- Logistics
- Utilities
- Damage Risk
- Ppe
---

<div align="center">
  <img width="640" alt="keremberke/hard-hat-detection" src="https://huggingface.co/datasets/keremberke/hard-hat-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['hardhat', 'no-hardhat']
```


### Number of Images

```json
{'test': 2001, 'train': 13782, 'valid': 3962}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/hard-hat-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/roboflow-universe-projects/hard-hats-fhbh5/dataset/2](https://universe.roboflow.com/roboflow-universe-projects/hard-hats-fhbh5/dataset/2?ref=roboflow2huggingface)

### Citation

```
@misc{ hard-hats-fhbh5_dataset,
    title = { Hard Hats Dataset },
    type = { Open Source Dataset },
    author = { Roboflow Universe Projects },
    howpublished = { \\url{ https://universe.roboflow.com/roboflow-universe-projects/hard-hats-fhbh5 } },
    url = { https://universe.roboflow.com/roboflow-universe-projects/hard-hats-fhbh5 },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { dec },
    note = { visited on 2023-01-16 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 16, 2023 at 9:17 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 19745 images.
Hardhat-ppe are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

No image augmentation techniques were applied.



