---
task_categories:
- image-classification
tags:
- roboflow
- roboflow2huggingface
- Biology
---

<div align="center">
  <img width="640" alt="trpakov/chest-xray-classification" src="https://huggingface.co/datasets/trpakov/chest-xray-classification/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['PNEUMONIA', 'NORMAL']
```


### Number of Images

```json
{'test': 582, 'valid': 1165, 'train': 12230}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("trpakov/chest-xray-classification", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/mohamed-traore-2ekkp/chest-x-rays-qjmia/dataset/3](https://universe.roboflow.com/mohamed-traore-2ekkp/chest-x-rays-qjmia/dataset/3?ref=roboflow2huggingface)

### Citation

```

```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on December 8, 2021 at 12:45 AM GMT

It includes 13977 images.
Pneumonia are annotated in folder format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random shear of between -3° to +3° horizontally and -2° to +2° vertically
* Random brigthness adjustment of between -5 and +5 percent
* Random exposure adjustment of between -5 and +5 percent



