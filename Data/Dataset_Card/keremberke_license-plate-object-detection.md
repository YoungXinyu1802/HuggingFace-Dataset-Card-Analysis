---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Self Driving
- Anpr
---

<div align="center">
  <img width="640" alt="keremberke/license-plate-object-detection" src="https://huggingface.co/datasets/keremberke/license-plate-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['license_plate']
```


### Number of Images

```json
{'train': 6176, 'valid': 1765, 'test': 882}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/license-plate-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/augmented-startups/vehicle-registration-plates-trudk/dataset/1](https://universe.roboflow.com/augmented-startups/vehicle-registration-plates-trudk/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ vehicle-registration-plates-trudk_dataset,
    title = { Vehicle Registration Plates Dataset },
    type = { Open Source Dataset },
    author = { Augmented Startups },
    howpublished = { \\url{ https://universe.roboflow.com/augmented-startups/vehicle-registration-plates-trudk } },
    url = { https://universe.roboflow.com/augmented-startups/vehicle-registration-plates-trudk },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { jun },
    note = { visited on 2023-01-18 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on January 13, 2022 at 5:20 PM GMT

It includes 8823 images.
VRP are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



