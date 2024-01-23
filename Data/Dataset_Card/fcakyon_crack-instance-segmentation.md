---
task_categories:
- image-segmentation
tags:
- roboflow
- roboflow2huggingface

---

<div align="center">
  <img width="640" alt="fcakyon/crack-instance-segmentation" src="https://huggingface.co/datasets/fcakyon/crack-instance-segmentation/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['cracks-and-spalling', 'object']
```


### Number of Images

```json
{'valid': 73, 'test': 37, 'train': 323}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("fcakyon/crack-instance-segmentation", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/palmdetection-1cjxw/crack_detection_experiment/dataset/5](https://universe.roboflow.com/palmdetection-1cjxw/crack_detection_experiment/dataset/5?ref=roboflow2huggingface)

### Citation

```
@misc{ 400-img_dataset,
    title = { 400 img Dataset },
    type = { Open Source Dataset },
    author = { Master dissertation },
    howpublished = { \\url{ https://universe.roboflow.com/master-dissertation/400-img } },
    url = { https://universe.roboflow.com/master-dissertation/400-img },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { dec },
    note = { visited on 2023-01-14 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 14, 2023 at 10:08 AM GMT

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

The dataset includes 433 images.
Crack-spall are annotated in COCO format.

The following pre-processing was applied to each image:

No image augmentation techniques were applied.



