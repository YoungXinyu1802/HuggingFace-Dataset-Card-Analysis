---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7440671071.55
    num_examples: 198771
  download_size: 7196594621
  dataset_size: 7440671071.55
---
# Dataset Card for "OSD-Dataset"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

This is a reformat of Huggingface Project's [SD Multiplayer Dataset](https://huggingface.co/datasets/huggingface-projects/sd-multiplayer-data) 
It converts the image bucket into a parquet format. The text column is the prompt + the timestamp for it to the minutes precision.
The model finetuned on it is [here](https://huggingface.co/BirdL/OSD-Model)