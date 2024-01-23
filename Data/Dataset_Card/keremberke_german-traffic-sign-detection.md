---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Self Driving
- Transportation
---

<div align="center">
  <img width="640" alt="keremberke/german-traffic-sign-detection" src="https://huggingface.co/datasets/keremberke/german-traffic-sign-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['animals', 'construction', 'cycles crossing', 'danger', 'no entry', 'pedestrian crossing', 'school crossing', 'snow', 'stop', 'bend', 'bend left', 'bend right', 'give way', 'go left', 'go left or straight', 'go right', 'go right or straight', 'go straight', 'keep left', 'keep right', 'no overtaking', 'no overtaking -trucks-', 'no traffic both ways', 'no trucks', 'priority at next intersection', 'priority road', 'restriction ends', 'restriction ends -overtaking -trucks--', 'restriction ends -overtaking-', 'restriction ends 80', 'road narrows', 'roundabout', 'slippery road', 'speed limit 100', 'speed limit 120', 'speed limit 20', 'speed limit 30', 'speed limit 50', 'speed limit 60', 'speed limit 70', 'speed limit 80', 'traffic signal', 'uneven road']
```


### Number of Images

```json
{'test': 54, 'valid': 108, 'train': 383}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/german-traffic-sign-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/mohamed-traore-2ekkp/gtsdb---german-traffic-sign-detection-benchmark/dataset/1](https://universe.roboflow.com/mohamed-traore-2ekkp/gtsdb---german-traffic-sign-detection-benchmark/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ gtsdb---german-traffic-sign-detection-benchmark_dataset,
    title = { GTSDB - German Traffic Sign Detection Benchmark Dataset },
    type = { Open Source Dataset },
    author = { Mohamed Traore },
    howpublished = { \\url{ https://universe.roboflow.com/mohamed-traore-2ekkp/gtsdb---german-traffic-sign-detection-benchmark } },
    url = { https://universe.roboflow.com/mohamed-traore-2ekkp/gtsdb---german-traffic-sign-detection-benchmark },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { jul },
    note = { visited on 2023-01-16 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 16, 2023 at 9:04 PM GMT

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

The dataset includes 545 images.
Signs are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



