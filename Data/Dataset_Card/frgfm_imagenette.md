---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- apache-2.0
multilinguality: []
size_categories:
- 1K<n<10K
source_datasets:
- extended
task_categories:
- image-classification
task_ids: []
paperswithcode_id: imagenette
pretty_name: Imagenette
---

# Dataset Card for Imagenette

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

- **Homepage:** https://github.com/fastai/imagenette
- **Repository:** https://github.com/fastai/imagenette
- **Leaderboard:** https://paperswithcode.com/sota/image-classification-on-imagenette

### Dataset Summary

A smaller subset of 10 easily classified classes from [Imagenet](https://huggingface.co/datasets/imagenet-1k#dataset-summary), and a little more French.
This dataset was created by [Jeremy Howard](https://twitter.com/jeremyphoward), and this repository is only there to share his work on this platform. The repository owner takes no credit of any kind in the creation, curation or packaging of the dataset.

### Supported Tasks and Leaderboards

- `image-classification`: The dataset can be used to train a model for Image Classification.

### Languages

The class labels in the dataset are in English.

## Dataset Structure

### Data Instances

A data point comprises an image URL and its classification label.

```
{
  'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=320x320 at 0x19FA12186D8>,
  'label': 'tench',
}
```

### Data Fields

- `image`: A `PIL.Image.Image` object containing the image.
- `label`: the expected class label of the image.

### Data Splits

|          |train|validation|
|----------|----:|---------:|
|imagenette| 9469|      3925|


## Dataset Creation

### Curation Rationale

cf. https://huggingface.co/datasets/imagenet-1k#curation-rationale

### Source Data

#### Initial Data Collection and Normalization

Imagenette is a subset of [ImageNet](https://huggingface.co/datasets/imagenet-1k). Information about data collection of the source data can be found [here](https://huggingface.co/datasets/imagenet-1k#initial-data-collection-and-normalization).

### Annotations

#### Annotation process

cf. https://huggingface.co/datasets/imagenet-1k#annotation-process

#### Who are the annotators?

cf. https://huggingface.co/datasets/imagenet-1k#who-are-the-annotators

### Personal and Sensitive Information

cf. https://huggingface.co/datasets/imagenet-1k#personal-and-sensitive-information

## Considerations for Using the Data

### Social Impact of Dataset

cf. https://huggingface.co/datasets/imagenet-1k#social-impact-of-dataset

### Discussion of Biases

cf. https://huggingface.co/datasets/imagenet-1k#discussion-of-biases

### Other Known Limitations

cf. https://huggingface.co/datasets/imagenet-1k#other-known-limitations

## Additional Information

### Dataset Curators

cf. https://huggingface.co/datasets/imagenet-1k#dataset-curators
and Jeremy Howard

### Licensing Information

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### Citation Information

```
@software{Howard_Imagenette_2019,
    title={Imagenette: A smaller subset of 10 easily classified classes from Imagenet},
    author={Jeremy Howard},
    year={2019},
    month={March},
    publisher = {GitHub},
    url = {https://github.com/fastai/imagenette}
}
```

### Contributions

This dataset was created by [Jeremy Howard](https://twitter.com/jeremyphoward) and published on [Github](https://github.com/fastai/imagenette). It was then only integrated into HuggingFace Datasets by [@frgfm](https://huggingface.co/frgfm).
