---
task_categories:
- object-detection
tags:
- roboflow
- roboflow2huggingface
- Gaming
---

<div align="center">
  <img width="640" alt="keremberke/clash-of-clans-object-detection" src="https://huggingface.co/datasets/keremberke/clash-of-clans-object-detection/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['ad', 'airsweeper', 'bombtower', 'canon', 'clancastle', 'eagle', 'inferno', 'kingpad', 'mortar', 'queenpad', 'rcpad', 'scattershot', 'th13', 'wardenpad', 'wizztower', 'xbow']
```


### Number of Images

```json
{'train': 88, 'test': 13, 'valid': 24}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/clash-of-clans-object-detection", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/find-this-base/clash-of-clans-vop4y/dataset/5](https://universe.roboflow.com/find-this-base/clash-of-clans-vop4y/dataset/5?ref=roboflow2huggingface?ref=roboflow2huggingface)

### Citation

```
@misc{ clash-of-clans-vop4y_dataset,
    title = { Clash of Clans Dataset },
    type = { Open Source Dataset },
    author = { Find This Base },
    howpublished = { \\url{ https://universe.roboflow.com/find-this-base/clash-of-clans-vop4y } },
    url = { https://universe.roboflow.com/find-this-base/clash-of-clans-vop4y },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { feb },
    note = { visited on 2023-01-18 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on March 30, 2022 at 4:31 PM GMT

It includes 125 images.
CoC are annotated in COCO format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 1920x1920 (Fit (black edges))

No image augmentation techniques were applied.



