---
license:
- cc-by-sa-4.0
kaggle_id: kapitanov/hagrid
---

# Dataset Card for HaGRID - HAnd Gesture Recognition Image Dataset

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

- **Homepage:** https://kaggle.com/datasets/kapitanov/hagrid
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

![](https://github.com/hukenovs/hagrid/blob/master/images/hagrid.jpg?raw=true)

We introduce a large image dataset **HaGRID** (**HA**nd **G**esture **R**ecognition **I**mage **D**ataset) for hand gesture recognition (HGR) systems. You can use it for image classification or image detection tasks. Proposed dataset allows to build HGR systems, which can be used in video conferencing services (Zoom, Skype, Discord, Jazz etc.), home automation systems, the automotive sector, etc.

**HaGRID** size is **716GB** and dataset contains **552,992 FullHD** (1920 × 1080) RGB images divided into **18** classes of gestures. Also, some images have `no_gesture` class if there is a second free hand in the frame. This extra class contains **123,589** samples. The data were split into training **92%**, and testing **8%** sets by subject **user-id**, with **509,323** images for train and 43,669 images for test.

![](https://github.com/hukenovs/hagrid/raw/master/images/gestures.jpg)

The dataset contains **34,730** unique persons and at least this number of unique scenes. The subjects are people from 18 to 65 years old. The dataset was collected mainly indoors with considerable variation in lighting, including artificial and natural light. Besides, the dataset includes images taken in extreme conditions such as facing and backing to a window. Also, the subjects had to show gestures at a distance of 0.5 to 4 meters from the camera.

## Annotations
The annotations consist of bounding boxes of hands with gesture labels in COCO format `[top left X position, top left Y position, width, height]`. Also annotations have markups of `leading hands` (`left` of `right` for gesture hand) and `leading_conf` as confidence for `leading_hand` annotation. We provide `user_id` field that will allow you to split the train / val dataset yourself.
```json
"03487280-224f-490d-8e36-6c5f48e3d7a0": {
  "bboxes": [
    [0.0283366, 0.8686061, 0.0757000, 0.1149820],
    [0.6824319, 0.2661254, 0.1086447, 0.1481245]
  ],
  "labels": [
    "no_gesture",
    "one"
  ],
  "leading_hand": "left",
  "leading_conf": 1.0,
  "user_id": "bb138d5db200f29385f..."
}
```

## Downloads
We split the train dataset into 18 archives by gestures because of the large size of data. Download and unzip them from the following links:

### Trainval

| Gesture                           | Size     | Gesture                                   | Size    |
|-----------------------------------|----------|-------------------------------------------|---------|
| [`call`](https://sc.link/ykEn)    | 39.1 GB  | [`peace`](https://sc.link/l6nM)           | 38.6 GB |
| [`dislike`](https://sc.link/xjDB) | 38.7 GB  | [`peace_inverted`](https://sc.link/mXoG)  | 38.6 GB |
| [`fist`](https://sc.link/wgB8)    | 38.0 GB  | [`rock`](https://sc.link/kMm6)            | 38.9 GB |
| [`four`](https://sc.link/vJA5)    | 40.5 GB  | [`stop`](https://sc.link/gXgk)            | 38.3 GB |
| [`like`](https://sc.link/r7wp)    | 38.3 GB  | [`stop_inverted`](https://sc.link/jJlv)   | 40.2 GB |
| [`mute`](https://sc.link/q8vp)    | 39.5 GB  | [`three`](https://sc.link/wgBr)           | 39.4 GB |
| [`ok`](https://sc.link/pV0V)      | 39.0 GB  | [`three2`](https://sc.link/vJA8)          | 38.5 GB |
| [`one`](https://sc.link/oJqX)     | 39.9 GB  | [`two_up`](https://sc.link/q8v7)          | 41.2 GB |
| [`palm`](https://sc.link/nJp7)    | 39.3 GB  | [`two_up_inverted`](https://sc.link/r7w2) | 39.2 GB |

`train_val` **annotations**: [`ann_train_val`](https://sc.link/BE5Y)

### Test

| Test        | Archives                            | Size      |
|-------------|-------------------------------------|-----------|
| images      | [`test`](https://sc.link/zlGy)      | 60.4 GB   |
| annotations | [`ann_test`](https://sc.link/DE5K)  | 3.4 MB    |

### Subsample
Subsample has 100 items per gesture.

| Subsample   | Archives                                | Size      |
|-------------|-----------------------------------------|-----------|
| images      | [`subsample`](https://sc.link/AO5l)     | 2.5 GB    |
| annotations | [`ann_subsample`](https://sc.link/EQ5g) | 153.8 KB  |

## Models
We provide some pre-trained classifiers and one detector as baselines.

| Classifiers                               | F1 Gesture | F1 Leading hand |
|-------------------------------------------|------------|-----------------|
| [ResNet18](https://sc.link/KEnx)          | 98.72      | 99.27           |
| [ResNet152](https://sc.link/O9rr)         | 99.11      | **99.45**       |
| [ResNeXt50](https://sc.link/GKjJ)         | 98.99      | 99.39           |
| [ResNeXt101](https://sc.link/JXmg)        | **99.28**  | 99.28           |
| [MobileNetV3-small](https://sc.link/XVEg) | 96.78      | 98.28           |
| [MobileNetV3-large](https://sc.link/YXG2) | 97.88      | 98.58           |
| [VitB-32](https://sc.link/XV4g)            | 98.49      | 99.13           |


| Detector                        | mAP   |
|---------------------------------|-------|
| [SSDLite](https://sc.link/YXg2) | 71.49 |


## Links
- [Github](https://github.com/hukenovs/hagrid), [Mirror](https://gitlab.aicloud.sbercloud.ru/rndcv/hagrid)
- [arXiv](https://arxiv.org/abs/2206.08219)
- [Paperswithcode](https://paperswithcode.com/paper/hagrid-hand-gesture-recognition-image-dataset)

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

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

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

This dataset was shared by [@kapitanov](https://kaggle.com/kapitanov)

### Licensing Information

The license for this dataset is cc-by-sa-4.0

### Citation Information

```bibtex
[More Information Needed]
```

### Contributions

[More Information Needed]