---
pretty_name: Fashionpedia_4_categories
task_categories:
- object-detection
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- fashionpedia
tags:
- object-detection
- fashion
- computer-vision
paperswithcode_id: fashionpedia
---

# Dataset Card for Fashionpedia_4_categories

This dataset is a variation of the fashionpedia dataset available [here](https://huggingface.co/datasets/detection-datasets/fashionpedia), with 2 key differences:
- It contains only 4 categories:
  - Clothing
  - Shoes
  - Bags
  - Accessories
- New splits were created:
  - Train: 90% of the images
  - Val: 5%
  - Test 5%

The goal is to make the detection task easier with 4 categories instead of 46 for the full fashionpedia dataset.

This dataset was created using the `detection_datasets` library ([GitHub](https://github.com/blinjrm/detection-datasets), [PyPI](https://pypi.org/project/detection-datasets/)), you can check here the full creation [notebook](https://blinjrm.github.io/detection-datasets/tutorials/2_Transform/).

In a nutshell, the following mapping was applied:
```Python
mapping = {
    'shirt, blouse': 'clothing',
    'top, t-shirt, sweatshirt': 'clothing',
    'sweater': 'clothing',
    'cardigan': 'clothing',
    'jacket': 'clothing',
    'vest': 'clothing',
    'pants': 'clothing',
    'shorts': 'clothing',
    'skirt': 'clothing',
    'coat': 'clothing',
    'dress': 'clothing',
    'jumpsuit': 'clothing',
    'cape': 'clothing',
    'glasses': 'accessories',
    'hat': 'accessories',
    'headband, head covering, hair accessory': 'accessories',
    'tie': 'accessories',
    'glove': 'accessories',
    'belt': 'accessories',
    'tights, stockings': 'accessories',
    'sock': 'accessories',
    'shoe': 'shoes',
    'bag, wallet': 'bags',
    'scarf': 'accessories',
}
```

As a result, annotations with no category equivalent in the mapping have been dropped.