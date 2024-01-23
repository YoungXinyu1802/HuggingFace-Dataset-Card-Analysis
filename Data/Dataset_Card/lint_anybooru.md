---
license: openrail
---

# Anybooru 

## Synthetic Anime Image Dataset

Synthetic anime image dataset generated using Andite's Anything-v4.5 checkpoint with Danbooru2021 tags collected in https://gwern.net/danbooru2021. 
See https://github.com/1lint/anybooru for details and code to generate your own variant of the dataset. I have also uploaded the extracted Danbooru2021 tags to https://huggingface.co/datasets/lint/danbooru_tags, this dataset was generated with a small subset of the tags in `2021_0_pruned.parquet`.

Each string of tags was used to generate 4 different images with different seeds. This serves a similar purpose as random resize crop and image flip transformations to train the model to focus on general concepts encoded in the tags, rather than memorizing specific images.


## Quick Start

```
from datasets import load_dataset

dataset = load_dataset('lint/anybooru')

sample = dataset['train'][0]

image = sample['image']
tags = image.info['tags']

print(tags)
```

## Samples

Each row of samples share the same generation prompt (string of tags). 

![](./anybooru_grid.png)


## Citations

```
@misc{danbooru2021, author = {Anonymous and Danbooru community and Gwern Branwen}, title = {Danbooru2021: A Large-Scale Crowdsourced and Tagged Anime Illustration Dataset}, howpublished = {\url{https://gwern.net/danbooru2021}}, url = {https://gwern.net/danbooru2021}, type = {dataset}, year = {2022}, month = {January}, timestamp = {2022-01-21}, note = {Accessed: 03/01/2023} }
```


