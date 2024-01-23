---
task_categories:
- image-classification
tags:
- roboflow
- roboflow2huggingface
- Sports
- Retail
- Benchmark
---

<div align="center">
  <img width="640" alt="keremberke/shoe-classification" src="https://huggingface.co/datasets/keremberke/shoe-classification/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['converse', 'adidas', 'nike']
```


### Number of Images

```json
{'train': 576, 'test': 83, 'valid': 166}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/shoe-classification", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/popular-benchmarks/nike-adidas-and-converse-shoes-classification/dataset/4](https://universe.roboflow.com/popular-benchmarks/nike-adidas-and-converse-shoes-classification/dataset/4?ref=roboflow2huggingface)

### Citation

```

```

### License
Public Domain

### Dataset Summary
This dataset was exported via roboflow.com on October 28, 2022 at 2:38 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 825 images.
Shoes are annotated in folder format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

No image augmentation techniques were applied.



