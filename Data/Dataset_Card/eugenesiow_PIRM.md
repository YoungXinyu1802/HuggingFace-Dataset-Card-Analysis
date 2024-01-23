---
annotations_creators:
- machine-generated
language_creators:
- found
language: []
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: PIRM
tags:
- other-image-super-resolution
---

# Dataset Card for PIRM

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

- **Homepage**: https://github.com/roimehrez/PIRM2018
- **Repository**: https://huggingface.co/datasets/eugenesiow/PIRM
- **Paper**: https://arxiv.org/abs/1809.07517
- **Leaderboard**: https://github.com/eugenesiow/super-image#scale-x2

### Dataset Summary

The PIRM dataset consists of 200 images, which are divided into two equal sets for validation and testing. 
These images cover diverse contents, including people, objects, environments, flora, natural scenery, etc. 
Images vary in size, and are typically ~300K pixels in resolution.

This dataset was first used for evaluating the perceptual quality of super-resolution algorithms in The 2018 PIRM 
challenge on Perceptual Super-resolution, in conjunction with ECCV 2018.

Install with `pip`:
```bash
pip install datasets super-image
```

Evaluate a model with the [`super-image`](https://github.com/eugenesiow/super-image) library:
```python
from datasets import load_dataset
from super_image import EdsrModel
from super_image.data import EvalDataset, EvalMetrics

dataset = load_dataset('eugenesiow/PIRM', 'bicubic_x2', split='validation')
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
    "hr": "/.cache/huggingface/datasets/downloads/extracted/PIRM_valid_HR/1.png",
    "lr": "/.cache/huggingface/datasets/downloads/extracted/PIRM_valid_LR_x2/1.png"
}
```

### Data Fields

The data fields are the same among all splits.

- `hr`: a `string` to the path of the High Resolution (HR) `.png` image.
- `lr`: a `string` to the path of the Low Resolution (LR) `.png` image.

### Data Splits

| name  |validation|test|
|-------|---:|---:|
|bicubic_x2|100|100|
|bicubic_x3|100|100|
|bicubic_x4|100|100|
|unknown_x4|100|100|

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

- **Original Authors**: [Blau et al. (2018)](https://arxiv.org/abs/1809.07517)

### Licensing Information

This dataset is published under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Citation Information

```bibtex
@misc{blau20192018,
    title={The 2018 PIRM Challenge on Perceptual Image Super-resolution}, 
    author={Yochai Blau and Roey Mechrez and Radu Timofte and Tomer Michaeli and Lihi Zelnik-Manor},
    year={2019},
    eprint={1809.07517},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

### Contributions

Thanks to [@eugenesiow](https://github.com/eugenesiow) for adding this dataset.
