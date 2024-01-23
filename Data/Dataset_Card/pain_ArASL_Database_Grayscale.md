---
splits:
- name: train
  num_bytes: 41355564.009
  num_examples: 54049
download_size: 30479019
dataset_size: 41355564.009
task_categories:
- image-classification
language:
- ar
tags:
- image_classification
- Arabic_Sign_Language
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': ain
          '1': al
          '2': aleff
          '3': bb
          '4': dal
          '5': dha
          '6': dhad
          '7': fa
          '8': gaaf
          '9': ghain
          '10': ha
          '11': haa
          '12': jeem
          '13': kaaf
          '14': khaa
          '15': la
          '16': laam
          '17': meem
          '18': nun
          '19': ra
          '20': saad
          '21': seen
          '22': sheen
          '23': ta
          '24': taa
          '25': thaa
          '26': thal
          '27': toot
          '28': waw
          '29': ya
          '30': yaa
          '31': zay
license: cc-by-4.0
---

# Dataset Card for "ArASL_Database_Grayscale"


## Dataset Description

- **Homepage:** https://data.mendeley.com/datasets/y7pckrw6z2/1
- **Paper:** [ArASL: Arabic Alphabets Sign Language Dataset](https://www.sciencedirect.com/science/article/pii/S2352340919301283)

### Dataset Summary

A new dataset consists of 54,049 images of ArSL alphabets performed by more than 40 people for 32 standard Arabic signs and alphabets.
The number of images per class differs from one class to another. Sample image of all Arabic Language Signs is also attached. The CSV file contains the Label of each corresponding Arabic Sign Language Image based on the image file name. 


### Supported Tasks and Leaderboards

- `image-classification`: The goal of this task is to classify a given image into one of 32 classes.

### Languages

Arabic

### Data Instances

A sample from the training set is provided below:

```
{
  'img': <PIL.PngImagePlugin.PngImageFile image mode=RGB size=32x32 at 0x201FA6EE748>,
  'label': 0
}
```

### Citation Information

```
@article{LATIF2019103777,
title = {ArASL: Arabic Alphabets Sign Language Dataset},
journal = {Data in Brief},
volume = {23},
pages = {103777},
year = {2019},
issn = {2352-3409},
doi = {https://doi.org/10.1016/j.dib.2019.103777},
url = {https://www.sciencedirect.com/science/article/pii/S2352340919301283},
author = {Ghazanfar Latif and Nazeeruddin Mohammad and Jaafar Alghazo and Roaa AlKhalaf and Rawan AlKhalaf},
abstract = {A fully-labelled dataset of Arabic Sign Language (ArSL) images is developed for research related to sign language recognition. The dataset will provide researcher the opportunity to investigate and develop automated systems for the deaf and hard of hearing people using machine learning, computer vision and deep learning algorithms. The contribution is a large fully-labelled dataset for Arabic Sign Language (ArSL) which is made publically available and free for all researchers. The dataset which is named ArSL2018 consists of 54,049 images for the 32 Arabic sign language sign and alphabets collected from 40 participants in different age groups. Different dimensions and different variations were present in images which can be cleared using pre-processing techniques to remove noise, center the image, etc. The dataset is made available publicly at https://data.mendeley.com/datasets/y7pckrw6z2/1.}
}
```

### Contributions

Thanks to [MOHAMMAD ALBARHAM](https://github.com/PAIN-BARHAM) for adding this dataset to huggingface hub.