---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: MIT Restaurant
---

# Dataset Card for "tner/mit_restaurant"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Dataset:** MIT restaurant
- **Domain:** Restaurant
- **Number of Entity:** 8

### Dataset Summary
MIT Restaurant NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.

- Entity Types: `Rating`, `Amenity`, `Location`, `Restaurant_Name`, `Price`, `Hours`, `Dish`, `Cuisine`.

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tags': [0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 4, 0],
    'tokens': ['can', 'you', 'find', 'the', 'phone', 'number', 'for', 'the', 'closest', 'family', 'style', 'restaurant']
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/mit_restaurant/raw/main/dataset/label.json).
```python
{
    "O": 0,
    "B-Rating": 1,
    "I-Rating": 2,
    "B-Amenity": 3,
    "I-Amenity": 4,
    "B-Location": 5,
    "I-Location": 6,
    "B-Restaurant_Name": 7,
    "I-Restaurant_Name": 8,
    "B-Price": 9,
    "B-Hours": 10,
    "I-Hours": 11,
    "B-Dish": 12,
    "I-Dish": 13,
    "B-Cuisine": 14,
    "I-Price": 15,
    "I-Cuisine": 16
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|mit_restaurant      |6900  |       760| 1521|
