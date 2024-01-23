---
license: apache-2.0

task_categories:
- text-to-image
pretty_name: text_to_bayc_image
size_categories:
- 1K<n<10K
source_dataset: https://opensea.io/collection/boredapeyachtclub c 2021 Yuga Labs LLC
---

# Disclaimer
All rights belong to their owners. Models and datasets can be removed from the site at the request of the copyright holder.

# How to use

```bash
from datasets import load_dataset
dataset = load_dataset("VESSL/Bored_Ape_NFT_text")
```

# Data Field

image = binary image file and path 
text = auto generated prompt for image

# Citation & Information 
@InProceedings{VESSL,\
    author={Jinpil Choi}\
    year=2023\
}

# Projects
https://github.com/vessl-ai/examples