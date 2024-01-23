---
license: apache-2.0
task_categories:
- image-to-text
- question-answering
- zero-shot-classification
language:
- en
multilinguality:
  - monolingual
task_ids:
  - text-scoring
pretty_name: HL (High-Level Dataset)
size_categories:
- 10K<n<100K
annotations_creators:
- crowdsourced
annotations_origin:
- crowdsourced
dataset_info:
  splits:
    - name: train
      num_examples: 13498
    - name: test
      num_examples: 1499
---
# Dataset Card for the High-Level Dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Supported Tasks](#supported-tasks)
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

## Dataset Description

The High-Level (HL) dataset aligns **object-centric descriptions** from [COCO](https://arxiv.org/pdf/1405.0312.pdf) 
with **high-level descriptions** crowdsourced along 3 axes: **_scene_, _action_, _rationale_**

The HL dataset contains 149997 images from COCO and a total of 134973 crowdsourced captions (3 captions for each axis) aligned with ~749984 object-centric captions from COCO.

Each axis is collected by asking the following 3 questions:

1) Where is the picture taken?
2) What is the subject doing?
3) Why is the subject doing it?

**The high-level descriptions capture the human interpretations of the images**. These interpretations contain abstract concepts not directly linked to physical objects.
Each high-level description is provided with a _confidence score_, crowdsourced by an independent worker measuring the extent to which
the high-level description is likely given the corresponding image, question, and caption. The higher the score, the more the high-level caption is close to the commonsense (in a Likert scale from 1-5).

- **🗃️ Repository:** [github.com/michelecafagna26/HL-dataset](https://github.com/michelecafagna26/HL-dataset)
- **📜 Paper:** [HL Dataset: Grounding High-Level Linguistic Concepts in Vision](https://arxiv.org/pdf/2302.12189.pdf)
- **🧭 Spaces:** [Dataset explorer](https://huggingface.co/spaces/michelecafagna26/High-Level-Dataset-explorer)
- **🖊️ Point of Contact:** michele.cafagna@um.edu.mt

### Supported Tasks

- image captioning
- visual question answering
- multimodal text-scoring
- zero-shot evaluation

### Languages

English

## Dataset Structure

The dataset is provided with images from COCO and two metadata jsonl files containing the annotations

### Data Instances

An instance looks like this:
```json
{
  "file_name": "COCO_train2014_000000138878.jpg",
  "captions": {
    "scene": [
      "in a car",
      "the picture is taken in a car",
      "in an office."
    ],
    "action": [
      "posing for a photo",
      "the person is posing for a photo",
      "he's sitting in an armchair."
    ],
    "rationale": [
      "to have a picture of himself",
      "he wants to share it with his friends",
      "he's working and took a professional photo."
    ],
    "object": [
      "A man sitting in a car while wearing a shirt and tie.",
      "A man in a car wearing a dress shirt and tie.",
      "a man in glasses is wearing a tie",
      "Man sitting in the car seat with button up and tie",
      "A man in glasses and a tie is near a window."
    ]
  },
  "confidence": {
    "scene": [
      5,
      5,
      4
    ],
    "action": [
      5,
      5,
      4
    ],
    "rationale": [
      5,
      5,
      4
    ]
  },
  "purity": {
    "scene": [
      -1.1760284900665283,
      -1.0889461040496826,
      -1.442818284034729
    ],
    "action": [
      -1.0115827322006226,
      -0.5917857885360718,
      -1.6931917667388916
    ],
    "rationale": [
      -1.0546956062316895,
      -0.9740906357765198,
      -1.2204363346099854
    ]
  },
  "diversity": {
    "scene": 25.965358893403383,
    "action": 32.713305568898775,
    "rationale": 2.658757840479801
  }
}
```

### Data Fields

- ```file_name```: original COCO filename
- ```captions```: Dict containing all the captions for the image. Each axis can be accessed with the axis name and it contains a list of captions.
- ```confidence```: Dict containing the captions confidence scores. Each axis can be accessed with the axis name and it contains a list of captions. Confidence scores are not provided for the _object_ axis (COCO captions).t
- ```purity score```: Dict containing the captions purity scores. The purity  score measures the semantic similarity of the captions within the same axis (Bleurt-based).
- ```diversity score```: Dict containing the captions diversity scores. The diversity  score measures the lexical diversity of the captions within the same axis (Self-BLEU-based).

### Data Splits

There are 14997 images and 134973 high-level captions split into:
- Train-val: 13498 images and 121482 high-level captions
- Test: 1499 images and 13491 high-level captions

## Dataset Creation

The dataset has been crowdsourced on Amazon Mechanical Turk.
From the paper:

>We randomly select 14997 images from the COCO 2014 train-val split. In order to answer questions related to _actions_ and _rationales_ we need to
> ensure the presence of a subject in the image.  Therefore, we leverage the entity annotation provided in COCO to select images containing
> at least one person. The whole annotation is conducted on Amazon Mechanical Turk (AMT). We split the workload into batches in order to ease
>the monitoring of the quality of the data collected. Each image is annotated by three different annotators, therefore we collect three annotations per axis.

### Curation Rationale

From the paper:

>In this work, we tackle the issue of **grounding high-level linguistic concepts in the visual modality**, proposing the High-Level (HL) Dataset: a   
V\&L resource aligning existing object-centric captions with  human-collected high-level descriptions of images along three different axes: _scenes_, _actions_ and _rationales_. 
The high-level captions capture the human interpretation of the scene, providing abstract linguistic concepts complementary to object-centric captions
>used in current V\&L datasets, e.g. in COCO. We take a step further, and we collect _confidence scores_ to distinguish  commonsense assumptions
>from subjective interpretations and we characterize our data under a variety of semantic and lexical aspects.


### Source Data

- Images:  COCO
- object axis annotations: COCO
- scene, action, rationale annotations: crowdsourced
- confidence scores: crowdsourced
- purity score and diversity score: automatically computed

#### Annotation process

From the paper:

>**Pilot:** We run a pilot study with the double goal of collecting feedback and defining the task instructions.
>With the results from the pilot we design a beta version of the task and we run a small batch of cases on the crowd-sourcing platform.
>We manually inspect the results and we further refine the instructions and the formulation of the task before finally proceeding with the
>annotation in bulk. The final annotation form is shown in Appendix D.

>***Procedure:*** The participants are shown an image and three questions regarding three aspects or axes: _scene_, _actions_ and _rationales_
> i,e. _Where is the picture taken?_, _What is the subject doing?_, _Why is the subject doing it?_. We explicitly ask the participants to use
>their personal interpretation of the scene and add examples and suggestions in the instructions to further guide the annotators. Moreover,
>differently from other VQA datasets like (Antol et al., 2015) and (Zhu et al., 2016), where each question can refer to different entities
>in the image, we systematically ask the same three questions about the same subject for each image. The full instructions are reported
>in Figure 1. For details regarding the annotation costs see Appendix A.


#### Who are the annotators?

Turkers from Amazon Mechanical Turk

### Personal and Sensitive Information

There is no personal or sensitive information

## Considerations for Using the Data

[More Information Needed]

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

From the paper:

>**Quantitying grammatical errors:** We ask two expert annotators to correct grammatical errors in a sample of 9900 captions, 900 of which are shared between the two annotators.
> The annotators are shown the image caption pairs and they are asked to edit the caption whenever they identify a grammatical error.
>The most common errors reported by the annotators are:
>- Misuse of prepositions
>- Wrong verb conjugation
>- Pronoun omissions

>In order to quantify the extent to which the corrected captions differ from the original ones, we compute the Levenshtein distance (Levenshtein, 1966) between them.
>We observe that 22.5\%  of the sample has been edited and only 5\% with a Levenshtein distance greater than 10. This suggests a reasonable 
>level of grammatical quality overall, with no  substantial grammatical problems. This can also be observed from the Levenshtein distance 
>distribution reported in Figure 2. Moreover, the human evaluation is quite reliable as we observe a moderate inter-annotator agreement 
>(alpha = 0.507, (Krippendorff, 2018) computed over the shared sample.

### Dataset Curators

Michele Cafagna

### Licensing Information

The Images and the object-centric captions follow the [COCO terms of Use](https://cocodataset.org/#termsofuse)
The remaining annotations are licensed under Apache-2.0 license.

### Citation Information

```BibTeX
@inproceedings{Cafagna2023HLDG,
  title={HL Dataset: Grounding High-Level Linguistic Concepts in Vision},
  author={Michele Cafagna and Kees van Deemter and Albert Gatt},
  year={2023}
}
```
