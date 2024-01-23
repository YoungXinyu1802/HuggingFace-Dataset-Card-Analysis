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
pretty_name: Set5
tags:
- other-image-super-resolution
---

# Dataset Card for Set5

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

- **Homepage**: http://people.rennes.inria.fr/Aline.Roumy/results/SR_BMVC12.html
- **Repository**: https://huggingface.co/datasets/eugenesiow/Set5
- **Paper**: http://people.rennes.inria.fr/Aline.Roumy/publi/12bmvc_Bevilacqua_lowComplexitySR.pdf
- **Leaderboard**: https://github.com/eugenesiow/super-image#scale-x2

### Dataset Summary

Set5 is a evaluation dataset with 5 RGB images for the image super resolution task. The 5 images of the dataset are (“baby”, “bird”, “butterfly”, “head”, “woman”).

Install with `pip`:
```bash
pip install datasets super-image
```

Evaluate a model with the [`super-image`](https://github.com/eugenesiow/super-image) library:
```python
from datasets import load_dataset
from super_image import EdsrModel
from super_image.data import EvalDataset, EvalMetrics

dataset = load_dataset('eugenesiow/Set5', 'bicubic_x2', split='validation')
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
    "hr": "/.cache/huggingface/datasets/downloads/extracted/Set5_HR/baby.png",
    "lr": "/.cache/huggingface/datasets/downloads/extracted/Set5_LR_x2/baby.png"
}
```

### Data Fields

The data fields are the same among all splits.

- `hr`: a `string` to the path of the High Resolution (HR) `.png` image.
- `lr`: a `string` to the path of the Low Resolution (LR) `.png` image.

### Data Splits

| name  |validation|
|-------|---:|
|bicubic_x2|5|
|bicubic_x3|5|
|bicubic_x4|5|


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

- **Original Authors**: [Bevilacqua et al.](http://people.rennes.inria.fr/Aline.Roumy/results/SR_BMVC12.html)

### Licensing Information

Academic use only.

### Citation Information

```bibtex
@article{bevilacqua2012low,
  title={Low-complexity single-image super-resolution based on nonnegative neighbor embedding},
  author={Bevilacqua, Marco and Roumy, Aline and Guillemot, Christine and Alberi-Morel, Marie Line},
  year={2012},
  publisher={BMVA press}
}
```

### Contributions

Thanks to [@eugenesiow](https://github.com/eugenesiow) for adding this dataset.
