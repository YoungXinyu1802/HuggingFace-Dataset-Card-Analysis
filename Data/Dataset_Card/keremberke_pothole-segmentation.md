---
task_categories:
- image-segmentation
tags:
- roboflow
- roboflow2huggingface
- Construction
- Self Driving
- Transportation
- Damage Risk
---

<div align="center">
  <img width="640" alt="keremberke/pothole-segmentation" src="https://huggingface.co/datasets/keremberke/pothole-segmentation/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['pothole']
```


### Number of Images

```json
{'test': 5, 'train': 80, 'valid': 5}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/pothole-segmentation", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/imacs-pothole-detection-wo8mu/pothole-detection-irkz9/dataset/4](https://universe.roboflow.com/imacs-pothole-detection-wo8mu/pothole-detection-irkz9/dataset/4?ref=roboflow2huggingface)

### Citation

```
@misc{ pothole-detection-irkz9_dataset,
    title = { Pothole Detection Dataset },
    type = { Open Source Dataset },
    author = { IMACS Pothole Detection },
    howpublished = { \\url{ https://universe.roboflow.com/imacs-pothole-detection-wo8mu/pothole-detection-irkz9 } },
    url = { https://universe.roboflow.com/imacs-pothole-detection-wo8mu/pothole-detection-irkz9 },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { jan },
    note = { visited on 2023-01-15 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 15, 2023 at 6:38 PM GMT

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

The dataset includes 90 images.
Pothole are annotated in COCO format.

The following pre-processing was applied to each image:

No image augmentation techniques were applied.



