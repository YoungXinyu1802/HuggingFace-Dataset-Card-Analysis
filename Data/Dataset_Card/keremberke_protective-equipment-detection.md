---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Manufacturing
---

<div align="center">
  <img width="640" alt="keremberke/protective-equipment-detection" src="https://huggingface.co/datasets/keremberke/protective-equipment-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['glove', 'goggles', 'helmet', 'mask', 'no_glove', 'no_goggles', 'no_helmet', 'no_mask', 'no_shoes', 'shoes']
```


### Number of Images

```json
{'valid': 3570, 'test': 1935, 'train': 6473}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/protective-equipment-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/personal-protective-equipment/ppes-kaxsi/dataset/7](https://universe.roboflow.com/personal-protective-equipment/ppes-kaxsi/dataset/7?ref=roboflow2huggingface)

### Citation

```
@misc{ ppes-kaxsi_dataset,
    title = { PPEs Dataset },
    type = { Open Source Dataset },
    author = { Personal Protective Equipment },
    howpublished = { \\url{ https://universe.roboflow.com/personal-protective-equipment/ppes-kaxsi } },
    url = { https://universe.roboflow.com/personal-protective-equipment/ppes-kaxsi },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { jul },
    note = { visited on 2023-01-18 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on July 7, 2022 at 3:49 PM GMT

It includes 11978 images.
Ppe-equipements are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



