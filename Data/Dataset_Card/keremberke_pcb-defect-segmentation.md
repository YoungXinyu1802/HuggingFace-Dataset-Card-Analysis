---
task_categories:
- image-segmentation
tags:
- roboflow
- roboflow2huggingface

---

<div align="center">
  <img width="640" alt="keremberke/pcb-defect-segmentation" src="https://huggingface.co/datasets/keremberke/pcb-defect-segmentation/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['dry_joint', 'incorrect_installation', 'pcb_damage', 'short_circuit']
```


### Number of Images

```json
{'valid': 25, 'train': 128, 'test': 36}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/pcb-defect-segmentation", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/diplom-qz7q6/defects-2q87r/dataset/8](https://universe.roboflow.com/diplom-qz7q6/defects-2q87r/dataset/8?ref=roboflow2huggingface)

### Citation

```
@misc{ defects-2q87r_dataset,
    title = { Defects Dataset },
    type = { Open Source Dataset },
    author = { Diplom },
    howpublished = { \\url{ https://universe.roboflow.com/diplom-qz7q6/defects-2q87r } },
    url = { https://universe.roboflow.com/diplom-qz7q6/defects-2q87r },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { jan },
    note = { visited on 2023-01-27 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.com on January 27, 2023 at 1:45 PM GMT

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

The dataset includes 189 images.
Defect are annotated in COCO format.

The following pre-processing was applied to each image:

No image augmentation techniques were applied.



