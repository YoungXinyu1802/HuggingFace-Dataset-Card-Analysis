---
pretty_name: GLENDA - The ITEC Gynecologic Laparoscopy Endometriosis Dataset
language:
- en
annotations_creators:
- expert-generated
language_creators:
- machine-generated
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- image-classification
task_ids: []
dataset_info:
- config_name: binary_classification
  features:
  - name: image
    dtype: image
  - name: metadata
    struct:
    - name: id
      dtype: int32
    - name: width
      dtype: int32
    - name: height
      dtype: int32
    - name: file_name
      dtype: string
    - name: path
      dtype: string
    - name: fickr_url
      dtype: string
    - name: coco_url
      dtype: string
    - name: date_captured
      dtype: string
    - name: case_id
      dtype: int32
    - name: video_id
      dtype: int32
    - name: frame_id
      dtype: int32
    - name: from_seconds
      dtype: int32
    - name: to_seconds
      dtype: int32
  - name: labels
    dtype:
      class_label:
        names:
          '0': no_pathology
          '1': endometriosis
  splits:
  - name: train
    num_bytes: 4524957
    num_examples: 13811
  download_size: 895554144
  dataset_size: 4524957
- config_name: multiclass_classification
  features:
  - name: image
    dtype: image
  - name: metadata
    struct:
    - name: id
      dtype: int32
    - name: width
      dtype: int32
    - name: height
      dtype: int32
    - name: file_name
      dtype: string
    - name: path
      dtype: string
    - name: fickr_url
      dtype: string
    - name: coco_url
      dtype: string
    - name: date_captured
      dtype: string
    - name: case_id
      dtype: int32
    - name: video_id
      dtype: int32
    - name: frame_id
      dtype: int32
    - name: from_seconds
      dtype: int32
    - name: to_seconds
      dtype: int32
  - name: labels
    dtype:
      class_label:
        names:
          '0': No-Pathology
          '1': 6.1.1.1_Endo-Peritoneum
          '2': 6.1.1.2_Endo-Ovar
          '3': 6.1.1.3_Endo-TIE
          '4': 6.1.1.4_Endo-Uterus
  splits:
  - name: train
    num_bytes: 4524957
    num_examples: 13811
  download_size: 895554144
  dataset_size: 4524957
---

# Dataset Card for GLENDA - The ITEC Gynecologic Laparoscopy Endometriosis Dataset

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

- **Homepage:** http://ftp.itec.aau.at/datasets/GLENDA/index.html
- **Repository:**
- **Paper:** [GLENDA: Gynecologic Laparoscopy Endometriosis Dataset](https://link.springer.com/chapter/10.1007/978-3-030-37734-2_36)
- **Leaderboard:** 
- **Point of Contact:** freidankm@gmail.com

### Dataset Summary

GLENDA (Gynecologic Laparoscopy ENdometriosis DAtaset) comprises over 350 annotated endometriosis lesion images taken from 100+ gynecologic laparoscopy surgeries as well as over 13K unannotated non pathological images of 20+ surgeries. The dataset is purposefully created to be utilized for a variety of automatic content analysis problems in the context of Endometriosis recognition.

**Usage Information (Disclaimer)**

The dataset is exclusively provided for scientific research purposes and as such cannot be used commercially or for any other purpose. If any other purpose is intended, you may directly contact the originator of the videos. 
For additional information (including contact details), please visit [the official website](http://ftp.itec.aau.at/datasets/GLENDA/index.html).

**Description**

Endometriosis is a benign but potentially painful condition among women in child bearing age involving the growth of uterine-like tissue in locations outside of the uterus. Corresponding lesions can be found in various positions and severities, often in multiple instances per patient requiring a physician to determine its extent. This most frequently is accomplished by calculating its magnitude via utilizing the combination of two popular classification systems, the revised American Society for Reproductive Medicine (rASRM) and the European Enzian scores. Endometriosis can not reliably identified by laymen, therefore, the dataset has been created with the help of medical experts in the field of endometriosis treatment.

**Purposes**

* binary (endometriosis) classification
* detection/localization

**Overview**

The dataset includes region-based annotations of 4 pathological endometriosis categories as well as non pathological counter example images. Annotations are created for single video frames that may be part of larger sequences comprising several consecutive frames (all showing the annotated condition). Frames can contain multiple annotations, potentially of different categories. Each single annotation is exported as a binary image (similar to below examples, albeit one image per annotation).

# TODO: FIXME: A bit more useful info on dataset case distribution class distribution and link  to original + preview link
TODO: FIXME: A bit more useful info on dataset case distribution class distribution and link  to original + preview link

### Supported Tasks and Leaderboards
- `image_classification`: The dataset can be used for binary (no pathology / endometriosis) or multiclass image classification (No-Pathology, 6.1.1.1\_Endo-Peritoneum,  6.1.1.2\_Endo-Ovar,  6.1.1.3\_Endo-DIE, 6.1.1.4\_Endo-Uterus. These classes respectively correspond to: no visible pathology in relation to endometriosis, peritoneal endometriosis, endometriosis on ovaries, deep infiltrating endometriosis (DIE) and uterine endometriosis.).

## Dataset Structure

### Data Instances

#### binary\_classification
TODO DESCRIBE

#### multiclass\_classification
TODO DESCRIBE

## Dataset Creation

### Curation Rationale

From the [official website](http://ftp.itec.aau.at/datasets/GLENDA/index.html)
> The dataset is purposefully created to be utilized for a variety of automatic content analysis problems in the context of Endometriosis recognition

### Source Data

#### Initial Data Collection and Normalization

From the [official website](http://ftp.itec.aau.at/datasets/GLENDA/index.html)
> The dataset includes region-based annotations of 4 pathological endometriosis categories as well as non pathological counter example images. Annotations are created for single video frames that may be part of larger sequences comprising several consecutive frames (all showing the annotated condition). Frames can contain multiple annotations, potentially of different categories. Each single annotation is exported as a binary image (similar to below examples, albeit one image per annotation).

### Annotations

#### Annotation process

From the [official website](http://ftp.itec.aau.at/datasets/GLENDA/index.html)
> Corresponding lesions can be found in various positions and severities, often in multiple instances per patient requiring a physician to determine its extent. This most frequently is accomplished by calculating its magnitude via utilizing the combination of two popular classification systems, the revised American Society for Reproductive Medicine (rASRM) and the European Enzian scores. Endometriosis can not reliably identified by laymen, therefore, the dataset has been created with the help of medical experts in the field of endometriosis treatment.

#### Who are the annotators?

Medical experts in the field of endometriosis treatment.

### Personal and Sensitive Information

[More Information Needed]

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators
[More Information Needed]

### Licensing Information

The dataset is exclusively provided for scientific research purposes and as such cannot be used commercially or for any other purpose. If any other purpose is intended, you may directly contact the originator of the videos, Prof. Dr. Jörg Keckstein.

GLENDA is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0, Creative Commons License) and is created as well as maintained by Distributed Multimedia Systems Group of the Institute of Information Technology (ITEC) at Alpen-Adria Universität in Klagenfurt, Austria. 

This license allows users of this dataset to copy, distribute and transmit the work under the following conditions:
* Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* Non-Commercial: You may not use the material for commercial purposes.

For further legal details, please read the [complete license terms](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

For additional information, please visit the [official website](http://ftp.itec.aau.at/datasets/GLENDA/index.html).


### Citation Information

```
@inproceedings{10.1007/978-3-030-37734-2_36,
	abstract = {Gynecologic laparoscopy as a type of minimally invasive surgery (MIS) is performed via a live feed of a patient's abdomen surveying the insertion and handling of various instruments for conducting treatment. Adopting this kind of surgical intervention not only facilitates a great variety of treatments, the possibility of recording said video streams is as well essential for numerous post-surgical activities, such as treatment planning, case documentation and education. Nonetheless, the process of manually analyzing surgical recordings, as it is carried out in current practice, usually proves tediously time-consuming. In order to improve upon this situation, more sophisticated computer vision as well as machine learning approaches are actively developed. Since most of such approaches heavily rely on sample data, which especially in the medical field is only sparsely available, with this work we publish the Gynecologic Laparoscopy ENdometriosis DAtaset (GLENDA) -- an image dataset containing region-based annotations of a common medical condition named endometriosis, i.e. the dislocation of uterine-like tissue. The dataset is the first of its kind and it has been created in collaboration with leading medical experts in the field.},
	address = {Cham},
	author = {Leibetseder, Andreas and Kletz, Sabrina and Schoeffmann, Klaus and Keckstein, Simon and Keckstein, J{\"o}rg},
	booktitle = {MultiMedia Modeling},
	editor = {Ro, Yong Man and Cheng, Wen-Huang and Kim, Junmo and Chu, Wei-Ta and Cui, Peng and Choi, Jung-Woo and Hu, Min-Chun and De Neve, Wesley},
	isbn = {978-3-030-37734-2},
	pages = {439--450},
	publisher = {Springer International Publishing},
	title = {GLENDA: Gynecologic Laparoscopy Endometriosis Dataset},
	year = {2020}
}
```
