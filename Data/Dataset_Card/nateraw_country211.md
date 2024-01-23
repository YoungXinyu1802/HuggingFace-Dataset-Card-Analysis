---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- unknown
multilinguality:
- monolingual
pretty_name: Country 211
size_categories:
- 10K<n<100K
source_datasets:
- extended|yfcc100m
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
---

# Dataset Card for Country211

The [Country 211 Dataset](https://github.com/openai/CLIP/blob/main/data/country211.md) from OpenAI.

This dataset was built by filtering the images from the YFCC100m dataset that have GPS coordinate corresponding to a ISO-3166 country code. The dataset is balanced by sampling 150 train images, 50 validation images, and 100 test images images for each country.