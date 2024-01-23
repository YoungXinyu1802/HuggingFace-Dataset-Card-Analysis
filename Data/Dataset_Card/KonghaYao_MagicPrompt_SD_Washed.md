---
license: cc0-1.0
task_categories:
- text-generation
- text-classification
language:
- en
tags:
- code
- art
pretty_name: mg_sd_washed
size_categories:
- 10K<n<100K
---

# MagicPrompt_SD_Washed

It's a version of datasets of [Gustavosta/MagicPrompt-Stable-Diffusion](https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion).

When I want to train a model using origin data, some bad prompts broke model and waste many time. 

So I washed the origin datasets: 

1. 😄 delete some meanless words like some artists name with misspelling
2. 😂 delete many spaces that make `100mm` to `10 0m`
3. 😭 some url in datasets
4. 😭 and many unknown words


And this version is doing well in my train test!😍
