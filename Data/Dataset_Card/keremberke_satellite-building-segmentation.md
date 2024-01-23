---
task_categories:
- image-segmentation
tags:
- roboflow
- roboflow2huggingface
- Aerial
- Logistics
- Construction
- Damage Risk
- Other
---

<div align="center">
  <img width="640" alt="keremberke/satellite-building-segmentation" src="https://huggingface.co/datasets/keremberke/satellite-building-segmentation/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['building']
```


### Number of Images

```json
{'train': 6764, 'valid': 1934, 'test': 967}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/satellite-building-segmentation", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/roboflow-universe-projects/buildings-instance-segmentation/dataset/1](https://universe.roboflow.com/roboflow-universe-projects/buildings-instance-segmentation/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ buildings-instance-segmentation_dataset,
    title = { Buildings Instance Segmentation Dataset },
    type = { Open Source Dataset },
    author = { Roboflow Universe Projects },
    howpublished = { \\url{ https://universe.roboflow.com/roboflow-universe-projects/buildings-instance-segmentation } },
    url = { https://universe.roboflow.com/roboflow-universe-projects/buildings-instance-segmentation },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { jan },
    note = { visited on 2023-01-18 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 16, 2023 at 9:09 PM GMT

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

The dataset includes 9665 images.
Buildings are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



