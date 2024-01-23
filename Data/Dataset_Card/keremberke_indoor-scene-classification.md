---
task_categories:
- image-classification
tags:
- roboflow
- roboflow2huggingface
- Retail
- Pest Control
- Benchmark
---

<div align="center">
  <img width="640" alt="keremberke/indoor-scene-classification" src="https://huggingface.co/datasets/keremberke/indoor-scene-classification/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['meeting_room', 'cloister', 'stairscase', 'restaurant', 'hairsalon', 'children_room', 'dining_room', 'lobby', 'museum', 'laundromat', 'computerroom', 'grocerystore', 'hospitalroom', 'buffet', 'office', 'warehouse', 'garage', 'bookstore', 'florist', 'locker_room', 'inside_bus', 'subway', 'fastfood_restaurant', 'auditorium', 'studiomusic', 'airport_inside', 'pantry', 'restaurant_kitchen', 'casino', 'movietheater', 'kitchen', 'waitingroom', 'artstudio', 'toystore', 'kindergarden', 'trainstation', 'bedroom', 'mall', 'corridor', 'bar', 'classroom', 'shoeshop', 'dentaloffice', 'videostore', 'laboratorywet', 'tv_studio', 'church_inside', 'operating_room', 'jewelleryshop', 'bathroom', 'clothingstore', 'closet', 'winecellar', 'livingroom', 'nursery', 'gameroom', 'inside_subway', 'deli', 'bakery', 'library', 'prisoncell', 'gym', 'concert_hall', 'greenhouse', 'elevator', 'poolinside', 'bowling']
```


### Number of Images

```json
{'train': 10885, 'test': 1558, 'valid': 3128}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("keremberke/indoor-scene-classification", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/popular-benchmarks/mit-indoor-scene-recognition/dataset/5](https://universe.roboflow.com/popular-benchmarks/mit-indoor-scene-recognition/dataset/5?ref=roboflow2huggingface)

### Citation

```

```

### License
MIT

### Dataset Summary
This dataset was exported via roboflow.com on October 24, 2022 at 4:09 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 15571 images.
Indoor-scenes are annotated in folder format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

No image augmentation techniques were applied.



