---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Documents
---

<div align="center">
  <img width="640" alt="keremberke/table-extraction" src="https://huggingface.co/datasets/keremberke/table-extraction/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['bordered', 'borderless']
```


### Number of Images

```json
{'test': 34, 'train': 238, 'valid': 70}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/table-extraction", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/mohamed-traore-2ekkp/table-extraction-pdf/dataset/2](https://universe.roboflow.com/mohamed-traore-2ekkp/table-extraction-pdf/dataset/2?ref=roboflow2huggingface)

### Citation

```

```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 18, 2023 at 9:41 AM GMT

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

The dataset includes 342 images.
Data-table are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



