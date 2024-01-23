---
annotations_creators:
- machine-generated
language_creators:
- found
language: []
license:
- other
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: BSD100
tags:
- image-super-resolution
---

# Dataset Card for BSD100

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage**: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/
- **Repository**: https://huggingface.co/datasets/eugenesiow/BSD100
- **Paper**: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=937655
- **Leaderboard**: https://github.com/eugenesiow/super-image#scale-x2

### Dataset Summary

BSD is a dataset used frequently for image denoising and super-resolution. Of the subdatasets, BSD100 is aclassical image dataset having 100 test images proposed by [Martin et al. (2001)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=937655). The dataset is composed of a large variety of images ranging from natural images to object-specific such as plants, people, food etc. BSD100 is the testing set of the Berkeley segmentation dataset BSD300.

Install with `pip`:
```bash
pip install datasets super-image
```

Evaluate a model with the [`super-image`](https://github.com/eugenesiow/super-image) library:
```python
from datasets import load_dataset
from super_image import EdsrModel
from super_image.data import EvalDataset, EvalMetrics

dataset = load_dataset('eugenesiow/BSD100', 'bicubic_x2', split='validation')
eval_dataset = EvalDataset(dataset)
model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=2)
EvalMetrics().evaluate(model, eval_dataset)
```

### Supported Tasks and Leaderboards

The dataset is commonly used for evaluation of the `image-super-resolution` task.

Unofficial [`super-image`](https://github.com/eugenesiow/super-image) leaderboard for:
- [Scale 2](https://github.com/eugenesiow/super-image#scale-x2)
- [Scale 3](https://github.com/eugenesiow/super-image#scale-x3)
- [Scale 4](https://github.com/eugenesiow/super-image#scale-x4)
- [Scale 8](https://github.com/eugenesiow/super-image#scale-x8)

### Languages

Not applicable.

## Dataset Structure

### Data Instances

An example of `validation` for `bicubic_x2` looks as follows.
```
{
    "hr": "/.cache/huggingface/datasets/downloads/extracted/BSD100_HR/3096.png",
    "lr": "/.cache/huggingface/datasets/downloads/extracted/BSD100_LR_x2/3096.png"
}
```

### Data Fields

The data fields are the same among all splits.

- `hr`: a `string` to the path of the High Resolution (HR) `.png` image.
- `lr`: a `string` to the path of the Low Resolution (LR) `.png` image.

### Data Splits

| name  |validation|
|-------|---:|
|bicubic_x2|100|
|bicubic_x3|100|
|bicubic_x4|100|


## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

No annotations.

#### Who are the annotators?

No annotators.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

- **Original Authors**: [Martin et al. (2001)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=937655)

### Licensing Information

You are free to download a portion of the dataset for non-commercial research and educational purposes.
In exchange, we request only that you make available to us the results of running your segmentation or 
boundary detection algorithm on the test set as described below. Work based on the dataset should cite 
the [Martin et al. (2001)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=937655) paper.

### Citation Information

```bibtex
@inproceedings{martin2001database,
  title={A database of human segmented natural images and its application to evaluating segmentation algorithms and measuring ecological statistics},
  author={Martin, David and Fowlkes, Charless and Tal, Doron and Malik, Jitendra},
  booktitle={Proceedings Eighth IEEE International Conference on Computer Vision. ICCV 2001},
  volume={2},
  pages={416--423},
  year={2001},
  organization={IEEE}
}
```

### Contributions

Thanks to [@eugenesiow](https://github.com/eugenesiow) for adding this dataset.
