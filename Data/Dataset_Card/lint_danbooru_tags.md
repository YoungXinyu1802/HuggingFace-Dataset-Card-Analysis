---
license: mit
---
License is for code inside this repository

This dataset consists of tag strings for Danbooru image posts. I originally extracted the tag strings to generate a synthetic dataset of anime styled images at https://github.com/1lint/anybooru for tuning stable diffusion. The tag strings could also be used to train a language model for generating prompts for anime styled stable diffusion checkpoints. I hope this dataset can be of use to you!

Quick start
```
from datasets import load_dataset

data_files = {"train": "2021_0_pruned.parquet"}
dataset = load_dataset("lint/danbooru_tags", data_files=data_files)

print(dataset['train'][0])
```

The data is stored as pandas dataframes in parquet format, with the filename specifying the year, section number and whether the data was pruned.
The full dataframe contains all metadata fields collected by Gwern, while the pruned data contains only the tag string and post ID fields: ['tags', 'id'], where the submission score is > 2 and rated as (relatively) SFW. 
If it's helpful, I can also upload similar extracted tags for other years of metadata, just leave a request in the `community tab`. You can also extract the tags and/or filter the dataset using the included notebook. 
See the `generate_tags_dataset.ipynb` for how the tags dataset was extracted from Danbooru metadata collected by Gwern in https://gwern.net/danbooru2021. 

@misc{danbooru2021,    author = {Anonymous and Danbooru community and Gwern Branwen},    title = {Danbooru2021: A Large-Scale Crowdsourced and Tagged Anime Illustration Dataset},    howpublished = {\url{https://gwern.net/danbooru2021}},    url = {https://gwern.net/danbooru2021},    type = {dataset},    year = {2022},    month = {January},    timestamp = {2022-01-21},    note = {Accessed: 03/01/2023} }