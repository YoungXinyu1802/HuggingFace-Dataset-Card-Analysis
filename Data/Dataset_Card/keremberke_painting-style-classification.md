---
task_categories:
- image-classification
tags:
- roboflow
- roboflow2huggingface

---

<div align="center">
  <img width="640" alt="keremberke/painting-style-classification" src="https://huggingface.co/datasets/keremberke/painting-style-classification/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['Realism', 'Art_Nouveau_Modern', 'Analytical_Cubism', 'Cubism', 'Expressionism', 'Action_painting', 'Synthetic_Cubism', 'Symbolism', 'Ukiyo_e', 'Naive_Art_Primitivism', 'Post_Impressionism', 'Impressionism', 'Fauvism', 'Rococo', 'Minimalism', 'Mannerism_Late_Renaissance', 'Color_Field_Painting', 'High_Renaissance', 'Romanticism', 'Pop_Art', 'Contemporary_Realism', 'Baroque', 'New_Realism', 'Pointillism', 'Northern_Renaissance', 'Early_Renaissance', 'Abstract_Expressionism']
```


### Number of Images

```json
{'valid': 1295, 'train': 4493, 'test': 629}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/painting-style-classification", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/art-dataset/wiki-art/dataset/1](https://universe.roboflow.com/art-dataset/wiki-art/dataset/1?ref=roboflow2huggingface)

### Citation

```
@misc{ wiki-art_dataset,
    title = { wiki art Dataset },
    type = { Open Source Dataset },
    author = { Art Dataset },
    howpublished = { \\url{ https://universe.roboflow.com/art-dataset/wiki-art } },
    url = { https://universe.roboflow.com/art-dataset/wiki-art },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { mar },
    note = { visited on 2023-01-18 },
}
```

### License
CC BY 4.0

### Dataset Summary
This dataset was exported via roboflow.ai on March 9, 2022 at 1:47 AM GMT

It includes 6417 images.
27 are annotated in folder format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

No image augmentation techniques were applied.



