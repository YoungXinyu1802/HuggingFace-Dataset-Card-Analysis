---
license: apache-2.0
task_categories:
- text-generation
language:
- en
---
This is the imdb dataset, https://huggingface.co/datasets/imdb

We've used a reward / sentiment model, https://huggingface.co/lvwerra/distilbert-imdb to compute the rewards of the offline data.
This is so that we can use offline RL on the data.