---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 596319589.625
    num_examples: 119027
  download_size: 575443290
  dataset_size: 596319589.625
size_categories:
- 100K<n<1M
---

# Dataset Card for Text Dataset

_Dataset used to train [Font text to image model](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning)_

For each row the dataset contains an `image` and a `text` key. The `image` is a varying size PIL png, and `text` is the accompanying text caption.