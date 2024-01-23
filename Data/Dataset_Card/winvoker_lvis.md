---
viewer: false
annotations_creators: []
language: []
language_creators: []
license:
- cc-by-4.0
pretty_name: lvis
size_categories:
- 1M<n<10M
source_datasets: []
tags:
- segmentation
- coco
task_categories:
- image-segmentation
task_ids:
- instance-segmentation
---

# LVIS
### Dataset Summary

This dataset is the implementation of LVIS dataset into Hugging Face datasets. Please visit the original website for more information. 

- https://www.lvisdataset.org/

### Loading
This code returns train, validation and test generators.

```python
from datasets import load_dataset

dataset = load_dataset("winvoker/lvis")
```

Objects is a dictionary which contains annotation information like bbox, class.
```
DatasetDict({
    train: Dataset({
        features: ['id', 'image', 'height', 'width', 'objects'],
        num_rows: 100170
    })
    validation: Dataset({
        features: ['id', 'image', 'height', 'width', 'objects'],
        num_rows: 4809
    })
    test: Dataset({
        features: ['id', 'image', 'height', 'width', 'objects'],
        num_rows: 19822
    })
})
```
### Access Generators
```python
train = dataset["train"]
validation = dataset["validation"]
test = dataset["test"] 
```

An example row is as follows.

```json
{  'id': 0, 
   'image': '000000437561.jpg', 
   'height': 480, 
   'width': 640, 
   'objects': {
               'bboxes': [[[392, 271, 14, 3]], 
               'classes': [117], 
               'segmentation': [[376, 272, 375, 270, 372, 269, 371, 269, 373, 269, 373]]
               }
 }
```