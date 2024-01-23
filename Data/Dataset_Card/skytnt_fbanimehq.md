---
annotations_creators: []
language: []
language_creators: []
license:
- cc0-1.0
multilinguality: []
pretty_name: Full Body Anime HQ
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- unconditional-image-generation
task_ids: []
---

## Dataset Description

FBAnimeHQ is a dataset with high-quality full-body anime girl images in a resolution of 1024 × 512.

### Dataset Summary

The dataset contains 112,806 images.

All images are on white background

### Collection Method

#### v1.0
Collect from danbooru website.

Use yolov5 to detect and clip image.

Use anime-segmentation to remove background.

Use deepdanbooru to filter image.

Finally clean the dataset manually.

#### v2.0

Base on v1.0, use Novelai image-to-image to enhance and expand the dataset.

### Contributions

Thanks to [@SkyTNT](https://github.com/SkyTNT) for adding this dataset.