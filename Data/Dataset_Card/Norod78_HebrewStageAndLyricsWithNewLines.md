---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 12638465.341690589
    num_examples: 11113
  - name: train
    num_bytes: 240110370.6583094
    num_examples: 211129
  download_size: 133520933
  dataset_size: 252748836.0
language:
- he
multilinguality:
- monolingual
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---
# Dataset Card for "HebrewStageAndLyricsWithNewLines"

* Contains poems and stories from "New Stage" ("במה חדשה")
* Contains text lines from various Hebrew song lyrics
* Data contains new-line characters
* Generated from a text file in which different poems were seperated using a double new-line character
* The script I made for converting the text file into a dataset is [available here](https://huggingface.co/datasets/Norod78/HebrewStageAndLyricsWithNewLines/blob/main/load_ds.py)