---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface

---

<div align="center">
  <img width="640" alt="keremberke/csgo-object-detection" src="https://huggingface.co/datasets/keremberke/csgo-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['ct', 'cthead', 't', 'thead']
```


### Number of Images

```json
{'train': 3879, 'valid': 383, 'test': 192}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/csgo-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/asd-culfr/wlots/dataset/1](https://universe.roboflow.com/asd-culfr/wlots/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ wlots_dataset,
    title = { wlots Dataset },
    type = { Open Source Dataset },
    author = { asd },
    howpublished = { \\url{ https://universe.roboflow.com/asd-culfr/wlots } },
    url = { https://universe.roboflow.com/asd-culfr/wlots },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { may },
    note = { visited on 2023-01-27 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on December 28, 2022 at 8:08 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 4454 images.
Ct-cthead-t-thead are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Fill (with center crop))

The following augmentation was applied to create 3 versions of each source image:
* Random brigthness adjustment of between -15 and +15 percent



