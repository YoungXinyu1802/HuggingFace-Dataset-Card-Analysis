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
pretty_name: Div2k
tags:
- other-image-super-resolution
---

# Dataset Card for Div2k

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

- **Homepage**: https://data.vision.ee.ethz.ch/cvl/DIV2K/
- **Repository**: https://huggingface.co/datasets/eugenesiow/Div2k
- **Paper**: http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf
- **Leaderboard**: https://github.com/eugenesiow/super-image#scale-x2

### Dataset Summary

DIV2K is a dataset of RGB images (2K resolution high quality images) with a large diversity of contents.

The DIV2K dataset is divided into:

- train data: starting from 800 high definition high resolution images we obtain corresponding low resolution images and provide both high and low resolution images for 2, 3, and 4 downscaling factors
- validation data: 100 high definition high resolution images are used for genereting low resolution corresponding images, the low res are provided from the beginning of the challenge and are meant for the participants to get online feedback from the validation server; the high resolution images will be released when the final phase of the challenge starts.

Install with `pip`:
```bash
pip install datasets super-image
```

Evaluate a model with the [`super-image`](https://github.com/eugenesiow/super-image) library:
```python
from datasets import load_dataset
from super_image import EdsrModel
from super_image.data import EvalDataset, EvalMetrics

dataset = load_dataset('eugenesiow/Div2k', 'bicubic_x2', split='validation')
eval_dataset = EvalDataset(dataset)
model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=2)
EvalMetrics().evaluate(model, eval_dataset)
```

### Supported Tasks and Leaderboards

The dataset is commonly used for training and evaluation of the `image-super-resolution` task.

Unofficial [`super-image`](https://github.com/eugenesiow/super-image) leaderboard for:
- [Scale 2](https://github.com/eugenesiow/super-image#scale-x2)
- [Scale 3](https://github.com/eugenesiow/super-image#scale-x3)
- [Scale 4](https://github.com/eugenesiow/super-image#scale-x4)
- [Scale 8](https://github.com/eugenesiow/super-image#scale-x8)

### Languages

Not applicable.

## Dataset Structure

### Data Instances

An example of `train` for `bicubic_x2` looks as follows.
```
{
    "hr": "/.cache/huggingface/datasets/downloads/extracted/DIV2K_valid_HR/0801.png",
    "lr": "/.cache/huggingface/datasets/downloads/extracted/DIV2K_valid_LR_bicubic/X2/0801x2.png"
}
```

### Data Fields

The data fields are the same among all splits.

- `hr`: a `string` to the path of the High Resolution (HR) `.png` image.
- `lr`: a `string` to the path of the Low Resolution (LR) `.png` image.

### Data Splits

| name  |train |validation|
|-------|-----:|---:|
|bicubic_x2|800|100|
|bicubic_x3|800|100|
|bicubic_x4|800|100|
|bicubic_x8|800|100|
|unknown_x2|800|100|
|unknown_x3|800|100|
|unknown_x4|800|100|
|realistic_mild_x4|800|100|
|realistic_difficult_x4|800|100|
|realistic_wild_x4|800|100|


## Dataset Creation

### Curation Rationale

Please refer to the [Initial Data Collection and Normalization](#initial-data-collection-and-normalization) section.

### Source Data

#### Initial Data Collection and Normalization

**Resolution and quality**: All the images are 2K resolution, that is they have 2K pixels on at least one of 
the axes (vertical or horizontal). All the images were processed using the same tools. For simplicity, since the most 
common magnification factors in the recent SR literature are of ×2, ×3 and ×4 we cropped the images to multiple of 
12 pixels on both axes. Most of the crawled images were originally above 20M pixels. 
The images are of high quality both aesthetically and in the terms of small amounts of noise and other corruptions 
(like blur and color shifts).

**Diversity**: The authors collected images from dozens of sites. A preference was made for sites with freely 
shared high quality photography (such as https://www.pexels.com/ ). Note that we did not use images from Flickr, 
Instagram, or other legally binding or copyright restricted images. We only seldom used keywords to assure the diversity
for our dataset. DIV2K covers a large diversity of contents, ranging from people, handmade objects and environments 
(cities, villages), to flora and fauna, and natural sceneries including underwater and dim light conditions.

**Partitions**: After collecting the DIV2K 1000 images the authors computed image entropy, bit per pixel (bpp) PNG 
compression rates and CORNIA scores (see Section 7.6) and applied bicubic downscaling ×3 and then upscaling ×3 with 
bicubic interpolation (imresize Matlab function), ANR [47] and A+ [48] methods and default settings. 

The authors randomly generated partitions of 800 train, 100 validation and 100 test images until they achieved a good 
balance firstly in visual contents and then on the average entropy, average bpp, average number of pixels per 
image (ppi), average CORNIA quality scores and also in the relative differences between the average PSNR scores of 
bicubic, ANR and A+ methods. 

Only the 800 train and 100 validation images are included in this dataset.

#### Who are the source language producers?

The authors manually crawled 1000 color RGB images from Internet paying special attention to the image quality,
to the diversity of sources (sites and cameras), to the image contents and to the copyrights. 

### Annotations

#### Annotation process

No annotations.

#### Who are the annotators?

No annotators.

### Personal and Sensitive Information

All the images are collected from the Internet, and the copyright belongs to the original owners. If any of the images 
belongs to you and you would like it removed, please kindly inform the authors, and they will remove it from the dataset 
immediately.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

- **Original Author**: [Radu Timofte](http://people.ee.ethz.ch/~timofter/)

### Licensing Information

Please notice that this dataset is made available for academic research purpose only. All the images are
collected from the Internet, and the copyright belongs to the original owners. If any of the images belongs to 
you and you would like it removed, please kindly inform the authors, and they will remove it from the dataset 
immediately.

### Citation Information

```bibtex
@InProceedings{Agustsson_2017_CVPR_Workshops,
    author = {Agustsson, Eirikur and Timofte, Radu},
    title = {NTIRE 2017 Challenge on Single Image Super-Resolution: Dataset and Study},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    url = "http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf",
    month = {July},
    year = {2017}
} 
```

### Contributions

Thanks to [@eugenesiow](https://github.com/eugenesiow) for adding this dataset.
