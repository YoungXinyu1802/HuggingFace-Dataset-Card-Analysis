---
annotations_creators:
- machine-generated
language_creators:
- found
language: []
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: Urban100
tags:
- other-image-super-resolution
---

# Dataset Card for Urban100

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

- **Homepage**: https://github.com/jbhuang0604/SelfExSR
- **Repository**: https://huggingface.co/datasets/eugenesiow/Urban100
- **Paper**: https://openaccess.thecvf.com/content_cvpr_2015/html/Huang_Single_Image_Super-Resolution_2015_CVPR_paper.html
- **Leaderboard**: https://github.com/eugenesiow/super-image#scale-x2

### Dataset Summary

The Urban100 dataset contains 100 images of urban scenes. It commonly used as a test set to evaluate the performance of super-resolution models. It was first published by [Huang et al. (2015)](https://openaccess.thecvf.com/content_cvpr_2015/html/Huang_Single_Image_Super-Resolution_2015_CVPR_paper.html) in the paper "Single Image Super-Resolution From Transformed Self-Exemplars".

Install with `pip`:
```bash
pip install datasets super-image
```

Evaluate a model with the [`super-image`](https://github.com/eugenesiow/super-image) library:
```python
from datasets import load_dataset
from super_image import EdsrModel
from super_image.data import EvalDataset, EvalMetrics

dataset = load_dataset('eugenesiow/Urban100', 'bicubic_x2', split='validation')
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
    "hr": "/.cache/huggingface/datasets/downloads/extracted/Urban100_HR/img_001.png",
    "lr": "/.cache/huggingface/datasets/downloads/extracted/Urban100_LR_x2/img_001.png"
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

The authors have created Urban100 containing 100 HR images with a variety of real-world structures.

### Source Data

#### Initial Data Collection and Normalization

The authors constructed this dataset using images from Flickr (under CC license) using keywords such as urban, city, architecture, and structure.

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

- **Original Authors**: [Huang et al. (2015)](https://github.com/jbhuang0604/SelfExSR) 

### Licensing Information

The dataset provided uses images from Flikr under the CC (CC-BY-4.0) license.

### Citation Information

```bibtex
@InProceedings{Huang_2015_CVPR,
  author = {Huang, Jia-Bin and Singh, Abhishek and Ahuja, Narendra},
  title = {Single Image Super-Resolution From Transformed Self-Exemplars},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  year = {2015}
}
```

### Contributions

Thanks to [@eugenesiow](https://github.com/eugenesiow) for adding this dataset.
