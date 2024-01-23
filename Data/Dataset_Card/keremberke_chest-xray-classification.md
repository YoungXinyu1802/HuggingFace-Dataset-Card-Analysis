---
task_categories:
- image-classification
tags:
- roboflow
- roboflow2huggingface
- Biology
---

<div align="center">
  <img width="640" alt="keremberke/chest-xray-classification" src="https://huggingface.co/datasets/keremberke/chest-xray-classification/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['NORMAL', 'PNEUMONIA']
```


### Number of Images

```json
{'train': 4077, 'test': 582, 'valid': 1165}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/chest-xray-classification", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/mohamed-traore-2ekkp/chest-x-rays-qjmia/dataset/2](https://universe.roboflow.com/mohamed-traore-2ekkp/chest-x-rays-qjmia/dataset/2?ref=roboflow2huggingface)

### Citation

```

```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on March 31, 2022 at 3:11 PM GMT

It includes 5824 images.
Pneumonia are annotated in folder format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

No image augmentation techniques were applied.



