---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Manufacturing
---

<div align="center">
  <img width="640" alt="keremberke/forklift-object-detection" src="https://huggingface.co/datasets/keremberke/forklift-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['forklift', 'person']
```


### Number of Images

```json
{'test': 42, 'valid': 84, 'train': 295}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/forklift-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/mohamed-traore-2ekkp/forklift-dsitv/dataset/1](https://universe.roboflow.com/mohamed-traore-2ekkp/forklift-dsitv/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ forklift-dsitv_dataset,
    title = { Forklift Dataset },
    type = { Open Source Dataset },
    author = { Mohamed Traore },
    howpublished = { \\url{ https://universe.roboflow.com/mohamed-traore-2ekkp/forklift-dsitv } },
    url = { https://universe.roboflow.com/mohamed-traore-2ekkp/forklift-dsitv },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { mar },
    note = { visited on 2023-01-15 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on April 3, 2022 at 9:01 PM GMT

It includes 421 images.
Forklift are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



