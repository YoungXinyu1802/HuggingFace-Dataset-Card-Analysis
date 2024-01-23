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
    num_bytes: 135370373465.422
    num_examples: 285466
  download_size: 133991087241
  dataset_size: 135370373465.422
pretty_name: 'E621 Rising: Curated Image Dataset v2'
size_categories:
- 100K<n<1M
viewer: false
---
**Warning: THIS dataset is NOT suitable for use by minors. The dataset contains X-rated/NFSW content.**


# E621 Rising: Curated Image Dataset v2

**285,466** images (~125GB) downloaded from `e621.net` with [tags](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-curated/raw/main/meta/tag-counts.by-name.json).

This is a curated dataset, picked from the E621 Rising: Raw Image Dataset v2 [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-raw).

## Image Processing
* Only `jpg` and `png` images were considered
* Image width and height have been clamped to `(0, 4096]px`; larger images have been resized to meet the limit
* Alpha channels have been removed
* All images have been converted to `jpg` format
* All images have been converted to TrueColor `RGB`
* All images have been verified to load with `Pillow`
* Metadata from E621 is [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-raw/tree/main/meta)

## Tags
Comprehensive list of tags and counts:

* [By name](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-curated/raw/main/meta/tag-counts.by-name.json)
* [By count](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-curated/raw/main/meta/tag-counts.by-count.json)


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
