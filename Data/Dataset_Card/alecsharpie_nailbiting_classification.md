---
annotations_creators:
- expert-generated
- machine-generated
language:
- en
language_creators: []
license:
- mit
multilinguality: []
paperswithcode_id: acronym-identification
pretty_name: Nailbiting Classification
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- nailbiting
- image
- preprocesses
task_categories:
- image-classification
task_ids: []
train-eval-index:
- col_mapping:
    labels: tags
    tokens: tokens
  config: default
  splits:
    eval_split: test
  task: token-classification
  task_id: entity_extraction
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': biting
          '1': no_biting
  splits:
  - name: train
    num_bytes: 11965731.715
    num_examples: 6629
  - name: test
    num_bytes: 1485426.0
    num_examples: 736
  download_size: 11546517
  dataset_size: 13451157.715
---

# Dataset Card for Nail Biting Classification

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


- **Homepage:** [https://huggingface.co/datasets/alecsharpie/nailbiting_classification](https://huggingface.co/datasets/alecsharpie/nailbiting_classification)
- **Repository:** [https://github.com/alecsharpie/nomo_nailbiting](https://github.com/alecsharpie/nomo_nailbiting)
- **Point of Contact:** [alecsharpie@gmail.com](alecsharpie@gmail.com)

### Dataset Summary

A binary image dataset for classifying nailbiting. Images are cropped to only show the mouth area.
Should contain edge cases such as drinking water, talking on the phone, scratching chin etc.. all in "no biting" category

## Dataset Structure

### Data Instances

 - 7147 Images
 - 14879790 bytes total
 - 12332617 bytes download

### Data Fields

128 x 64 (w x h, pixels)
Black and white

Labels
 - '0': biting
 - '1': no_biting

### Data Splits

- train: 6629 (11965737 bytes)
- test: 1471 (2914053 bytes)

## Dataset Creation

### Curation Rationale

I wanted to create a notification system to help me stop biting my nails. It needed to contain lots of possible no-biting scenarios. eg talking on the phone

### Source Data

#### Initial Data Collection and Normalization

The data was scraped from stock images sites and photos of myself were taken with my webcam. 
MTCNN (https://github.com/ipazc/mtcnn) was then used to crop the images down to only the show the mouth area
The images were then converted to a black & white colour scheme.

### Annotations

#### Annotation process

During the scraping process images were labelled with a description, which I then manually sanity checked. I labelled the ones of me manually. 

#### Who are the annotators?

Alec Sharp

## Considerations for Using the Data

### Discussion of Biases & Limitations

Tried to make the dataset diverse in terms of age and skin tone. Although, this dataset contains a large number of images of one subject (me) so is biased towards lower quality webcam pictures of a white male with a short beard.

### Dataset Curators

Alec Sharp

### Licensing Information

MIT

### Contributions

Thanks to [@alecsharpie](https://github.com/alecsharpie) for adding this dataset.