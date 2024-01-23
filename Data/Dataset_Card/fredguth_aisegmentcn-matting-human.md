---
annotations_creators:
  - Beijing Wanxing Convergence Technology Co
license:
  - mit
pretty_name: aisegmentcn-matting-human
size_categories:
  - 10K<n<100K
tags:
  - binary
  - aisegment.cn
task_categories:
  - image-segmentation
task_ids:
  - semantic-segmentation
---

# Dataset Card for AISegment.cn - Matting Human datasets

## Table of Contents

- [Dataset Card for AISegment.cn - Matting Human datasets](#dataset-card-for-aisegmentcn---matting-human-datasets)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
  - [Dataset Structure](#dataset-structure)
    - [Licensing Information](#licensing-information)

## Dataset Description

Quoting the [dataset's github](https://github.com/aisegmentcn/matting_human_datasets) (translated by Apple Translator):

> This dataset is currently the largest portrait matting dataset, containing 34,427 images and corresponding matting results.
> The data set was marked by the high quality of Beijing Play Star Convergence Technology Co. Ltd., and the portrait soft segmentation model trained using this data set has been commercialized.

> The original images in the dataset are from `Flickr`, `Baidu`, and `Taobao`. After face detection and area cropping, a half-length portrait of 600\*800 was generated.
> The clip_img directory is a half-length portrait image in the format jpg; the matting directory is the corresponding matting file (convenient to confirm the matting quality), the format is png, you should first extract the alpha map from the png image before training.

- **Repository:** [aisegmentcn/matting_human_datasets](https://github.com/aisegmentcn/matting_human_datasets)

## Dataset Structure

```text
└── data/
    ├── clip_img/
    │   └── {group-id}/
    │       └── clip_{subgroup-id}/
    │           └── {group-id}-{img-id}.jpg
    └── matting/
        └── {group-id}/
            └── matting_{subgroup-id}/
                └── {group-id}-{img-id}.png
```

The input `data/clip_img/1803151818/clip_00000000/1803151818-00000003.jpg` matches the label `data/matting/1803151818/matting_00000000/1803151818-00000003.png`

### Licensing Information

See authors [Github](https://github.com/aisegmentcn/matting_human_datasets)
