---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4051563749.765
    num_examples: 9999
  download_size: 3979423376
  dataset_size: 4051563749.765
size_categories:
- 1K<n<10K
viewer: false
pretty_name: 'E621 Rising: Mini Image Dataset v1'
---
**Warning: THIS dataset is NOT suitable for use by minors. The dataset contains X-rated/NFSW content.**

# E621 Rising: Mini Image Dataset v1

**9,999** images (~4GB) downloaded from `e621.net` with [tags](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-curated/raw/main/meta/tag-counts.json).

This is a small sample of the E621 Rising: Raw Dataset [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw).

## Image Processing
* Only `jpg` and `png` images were considered
* Image width and height have been clamped to `(0, 4096]px`; larger images have been resized to meet the limit
* Alpha channels have been removed
* All images have been converted to `jpg` format
* All images have been converted to TrueColor `RGB`
* All images have been verified to load with `Pillow`
* Metadata from E621 is [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw/tree/main/meta)