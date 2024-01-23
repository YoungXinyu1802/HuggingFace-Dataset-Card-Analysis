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
    num_bytes: 1192534908282.634
    num_examples: 2905671
  download_size: 210413447679
  dataset_size: 1192534908282.634
pretty_name: 'E621 Rising: Raw Image Dataset v1'
size_categories:
- 1M<n<10M
viewer: false
---

> # Deprecation Notice!
> [This dataset has been superseded by v2](https://huggingface.co/datasets/hearmeneigh/e621-rising-v2-raw). Use v2 instead of this dataset.


**Warning: THIS dataset is NOT suitable for use by minors. The dataset contains X-rated/NFSW content.**

# E621 Rising: Raw Image Dataset v1

**2,905,671** images (~1.1TB) downloaded from `e621.net` with [tags](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw/raw/main/meta/tag-counts.json).

This is a raw, uncurated, and largely unprocessed dataset. You likely want to use the curated version, [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-curated). This dataset contains all kinds of NFSW material. You have been warned.

## Image Processing
* Only `jpg` and `png` images were considered
* Image width and height have been clamped to `(0, 4096]px`; larger images have been resized to meet the limit
* Alpha channels have been removed
* All images have been converted to `jpg` format
* All images have been converted to TrueColor `RGB`
* All images have been verified to load with `Pillow`
* Metadata from E621 is [available here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw/tree/main/meta).

## Tags
For a comprehensive list of tags and counts, [see here](https://huggingface.co/datasets/hearmeneigh/e621-rising-v1-raw/raw/main/meta/tag-counts.json).

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
* Image score
  * `score:above_250`
  * `score:above_500`
  * `score:above_1000`
  * `score:above_1500`
  * `score:above_2000`
  * `score:below_250`
  * `score:below_100`
  * `score:below_50`
  * `score:below_25`
  * `score:below_0`
* Image favorites
  * `favorites:above_4000`
  * `favorites:above_3000`
  * `favorites:above_2000`
  * `favorites:above_1000`
  * `favorites:below_1000`
  * `favorites:below_500`
  * `favorites:below_250`
  * `favorites:below_100`
  * `favorites:below_50`
  * `favorites:below_25`