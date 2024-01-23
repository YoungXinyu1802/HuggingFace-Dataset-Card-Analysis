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
    num_bytes: 192529551170.037
    num_examples: 441623
  download_size: 190109066617
  dataset_size: 192529551170.037
pretty_name: 'E621 Rising: Curated Image Dataset v1'
size_categories:
- 100K<n<1M
viewer: false
---

> # Deprecation Notice!
> [This dataset has been superseded by v2](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-curated). Use v2 instead of this dataset.


**Warning: THIS dataset is NOT suitable for use by minors. The dataset contains X-rated/NFSW content.**


# E621 Rising: Curated Image Dataset v1

**441,623** images (~200GB) downloaded from `e621.net` with [tags](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-curated/raw/main/meta/tag-counts.json).

This is a curated dataset, picked from the E621 Rising: Raw Image Dataset v1 [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw).

## Image Processing
* Only `jpg` and `png` images were considered
* Image width and height have been clamped to `(0, 4096]px`; larger images have been resized to meet the limit
* Alpha channels have been removed
* All images have been converted to `jpg` format
* All images have been converted to TrueColor `RGB`
* All images have been verified to load with `Pillow`
* Metadata from E621 is [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw/tree/main/meta)

## Tags
For a comprehensive list of tags and counts, [see here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-curated/raw/main/meta/tag-counts.json).

### Changes From E621
* Symbols have been prefixed with `symbol:`, e.g. `symbol:<3`
* Aspect ratio has been prefixed with `aspect_ratio:`, e.g. `aspect_ratio:16_9`
* All categories except `general` have been prefixed with the category name, e.g. `artist:somename`. The categories are:
  * `artist`
  * `copyright`
  * `character`
  * `species`
  * `invalid`
  * `meta`
  * `lore`

### Additional Tags
* Image rating
  * `rating:explicit`
  * `rating:questionable`
  * `rating:safe`