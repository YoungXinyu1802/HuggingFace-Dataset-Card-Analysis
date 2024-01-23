---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: WSDMCup2023
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- toloka
task_categories:
- visual-question-answering
task_ids:
- visual-question-answering
dataset_info:
  features:
  - name: image
    dtype: string
  - name: width
    dtype: int64
  - name: height
    dtype: int64
  - name: left
    dtype: int64
  - name: top
    dtype: int64
  - name: right
    dtype: int64
  - name: bottom
    dtype: int64
  - name: question
    dtype: string
  splits:
  - name: train
    num_examples: 38990
  - name: train_sample
    num_examples: 1000
  - name: test_public
    num_examples: 1705
  - name: test_private
    num_examples: 4504
  config_name: wsdmcup2023
---

# Dataset Card for WSDMCup2023

## Dataset Description

- **Homepage:** [Toloka Visual Question Answering Challenge](https://toloka.ai/challenges/wsdm2023)
- **Repository:** [WSDM Cup 2023 Starter Pack](https://github.com/Toloka/WSDMCup2023)
- **Paper:** 
- **Leaderboard:** [CodaLab Competition Leaderboard](https://codalab.lisn.upsaclay.fr/competitions/7434#results)
- **Point of Contact:** research@toloka.ai

| Question | Image and Answer |
| --- | --- |
| What do you use to hit the ball? | <img src="https://tlk-infra-front.azureedge.net/portal-static/images/wsdm2023/tennis/x2/image.webp" width="228" alt="What do you use to hit the ball?"> |
| What do people use for cutting? | <img src="https://tlk-infra-front.azureedge.net/portal-static/images/wsdm2023/scissors/x2/image.webp" width="228" alt="What do people use for cutting?"> |
| What do we use to support the immune system and get vitamin C? | <img src="https://tlk-infra-front.azureedge.net/portal-static/images/wsdm2023/juice/x2/image.webp" width="228" alt="What do we use to support the immune system and get vitamin C?"> |

### Dataset Summary

The WSDMCup2023 Dataset consists of images associated with textual questions.
One entry (instance) in our dataset is a question-image pair labeled with the ground truth coordinates of a bounding box containing
the visual answer to the given question. The images were obtained from a CC BY-licensed subset of the Microsoft Common Objects in
Context dataset, [MS COCO](https://cocodataset.org/). All data labeling was performed on the [Toloka crowdsourcing platform](https://toloka.ai/).

Our dataset has 45,199 instances split among three subsets: train (38,990 instances), public test (1,705 instances),
and private test (4,504 instances). The entire train dataset was available for everyone since the start of the challenge.
The public test dataset was available since the evaluation phase of the competition, but without any ground truth labels.
After the end of the competition, public and private sets were released.

## Dataset Citation

Please cite the challenge results or dataset description as follows.

- Ustalov D., Pavlichenko N., Likhobaba D., and Smirnova A. [WSDM Cup 2023 Challenge on Visual Question Answering](http://ceur-ws.org/Vol-3357/invited1.pdf). *Proceedings of the 4th Crowd Science Workshop on Collaboration of Humans and Learning Algorithms for Data Labeling.* Singapore, 2023, pp.&nbsp;1&ndash;7.

```bibtex
@inproceedings{TolokaWSDMCup2023,
  author    = {Ustalov, Dmitry and Pavlichenko, Nikita and Likhobaba, Daniil and Smirnova, Alisa},
  title     = {{WSDM~Cup 2023 Challenge on Visual Question Answering}},
  year      = {2023},
  booktitle = {Proceedings of the 4th Crowd Science Workshop on Collaboration of Humans and Learning Algorithms for Data Labeling},
  pages     = {1--7},
  address   = {Singapore},
  issn      = {1613-0073},
  url       = {http://ceur-ws.org/Vol-3357/invited1.pdf},
  language  = {english},
}
```

### Supported Tasks and Leaderboards

The Visual Question Answering.

### Language

English

## Dataset Structure

### Data Instances
A data instance contains a url to the picture, information about the image size - width and height,
information about ground truth bounding box - left top and right bottom dots, 
contains the question related to the picture.
image,width,height,left,top,right,bottom,question
```
{'image': https://toloka-cdn.azureedge.net/wsdmcup2023/000000000013.jpg,
'width': 640,
'height': 427,
'left': 129,
'top': 192,
'right': 155,
'bottom': 212,
'question': What does it use to breath?}
```
### Data Fields

* image: contains url to the image
* width: value in pixels of image width
* heigth: value in pixels of image height
* left: the x coordinate in pixels to determin left-top dot of bounding box
* top: the y coordinate in pixels to determin left-top dot of bounding box
* right: the x coordinate in pixels to determin right-bottom dot of bounding box
* bottom: the y coordinate in pixels to determin right-bottom dot of bounding box
* question: a question related to the picture

### Data Splits
There are four splits in the data: train, train_sample, test_public, test_private. 'train' split contains the full pull for model training.
'train-sample' split contains the part of 'train' split. 'test_public' split contains public data to test the model. 
'test_private' split contains private data for final model test.

### Source Data

The images were obtained from a CC BY-licensed subset of the Microsoft Common Objects in
Context dataset, [MS COCO](https://cocodataset.org/).

### Annotations

All data labeling was performed on the [Toloka crowdsourcing platform](https://toloka.ai/).

Only annotators who self-reported the knowledge of English had access to the annotation task.

### Citation Information

* Competition: https://toloka.ai/challenges/wsdm2023
* CodaLab: https://codalab.lisn.upsaclay.fr/competitions/7434
* Dataset: https://doi.org/10.5281/zenodo.7057740