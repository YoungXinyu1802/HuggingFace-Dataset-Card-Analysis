---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Manufacturing
- Construction
- Machinery
---

<div align="center">
  <img width="640" alt="keremberke/excavator-detector" src="https://huggingface.co/datasets/keremberke/excavator-detector/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['excavators', 'dump truck', 'wheel loader']
```


### Number of Images

```json
{'test': 144, 'train': 2245, 'valid': 267}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/excavator-detector", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/mohamed-sabek-6zmr6/excavators-cwlh0/dataset/3](https://universe.roboflow.com/mohamed-sabek-6zmr6/excavators-cwlh0/dataset/3?ref=roboflow2huggingface)

### Citation

```
@misc{ excavators-cwlh0_dataset,
    title = { Excavators Dataset },
    type = { Open Source Dataset },
    author = { Mohamed Sabek },
    howpublished = { \\url{ https://universe.roboflow.com/mohamed-sabek-6zmr6/excavators-cwlh0 } },
    url = { https://universe.roboflow.com/mohamed-sabek-6zmr6/excavators-cwlh0 },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { nov },
    note = { visited on 2023-01-16 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on April 4, 2022 at 8:56 AM GMT

It includes 2656 images.
Excavator are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

No image augmentation techniques were applied.



