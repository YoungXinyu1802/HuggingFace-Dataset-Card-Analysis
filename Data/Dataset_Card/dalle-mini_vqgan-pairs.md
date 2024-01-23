---
license:
- cc-by-4.0
- cc-by-2.0
- unknown
source_datasets:
- Open Images
task_categories:
- other
task_ids: []
pretty_name: VQGAN Pairs
tags:
- super-resolution
- image-enhancement
---

# VQGAN Pairs

This dataset contains ~2.4 million image pairs intended for improvement of image quality in VQGAN predictions. Each pair consists of:
- A 512x512 crop of an image taken from Open Images.
- A 256x256 image encoded and decoded using VQGAN, corresponding to the same image crop as the original.

This is the VQGAN implementation that was used for encoding and decoding: https://github.com/patil-suraj/vqgan-jax

# License
This dataset is created using Open Images, which has the following license:
The annotations are licensed by Google LLC under CC BY 4.0 license. The images are listed as having a CC BY 2.0 license. Note: while we tried to identify images that are licensed under a Creative Commons Attribution license, we make no representations or warranties regarding the license status of each image and you should verify the license for each image yourself.