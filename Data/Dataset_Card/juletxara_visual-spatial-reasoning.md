---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- machine-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: Visual Spatial Reasoning
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- image-classification
task_ids: []
---

# Dataset Card for Visual Spatial Reasoning

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

- **Homepage:** https://ltl.mmll.cam.ac.uk/
- **Repository:** https://github.com/cambridgeltl/visual-spatial-reasoning
- **Paper:** https://arxiv.org/abs/2205.00363
- **Leaderboard:** https://paperswithcode.com/sota/visual-reasoning-on-vsr
- **Point of Contact:** https://ltl.mmll.cam.ac.uk/

### Dataset Summary

The Visual Spatial Reasoning (VSR) corpus is a collection of caption-image pairs with true/false labels. Each caption describes the spatial relation of two individual objects in the image, and a vision-language model (VLM) needs to judge whether the caption is correctly describing the image (True) or not (False).

### Supported Tasks and Leaderboards

We test three baselines, all supported in huggingface. They are VisualBERT [(Li et al. 2019)](https://arxiv.org/abs/1908.03557), LXMERT [(Tan and Bansal, 2019)](https://arxiv.org/abs/1908.07490) and ViLT [(Kim et al. 2021)](https://arxiv.org/abs/2102.03334). The leaderboard can be checked at [Papers With Code](https://paperswithcode.com/sota/visual-reasoning-on-vsr).

model   |  random split | zero-shot
:-------------|:-------------:|:-------------:
*human* | *95.4* | *95.4* 
VisualBERT | 57.4 | 54.0
LXMERT | **72.5** | **63.2**
ViLT | 71.0 | 62.4

### Languages

The language in the dataset is English as spoken by the annotators. The BCP-47 code for English is en. [`meta_data.csv`](https://github.com/cambridgeltl/visual-spatial-reasoning/tree/master/data/data_files/meta_data.jsonl) contains meta data of annotators.

## Dataset Structure

### Data Instances

Each line is an individual data point. Each `jsonl` file is of the following format:
```json
{"image": "000000050403.jpg", "image_link": "http://images.cocodataset.org/train2017/000000050403.jpg", "caption": "The teddy bear is in front of the person.", "label": 1, "relation": "in front of", "annotator_id": 31, "vote_true_validator_id": [2, 6], "vote_false_validator_id": []}
{"image": "000000401552.jpg", "image_link": "http://images.cocodataset.org/train2017/000000401552.jpg", "caption": "The umbrella is far away from the motorcycle.", "label": 0, "relation": "far away from", "annotator_id": 2, "vote_true_validator_id": [], "vote_false_validator_id": [2, 9, 1]}
```

### Data Fields

`image` denotes name of the image in COCO and `image_link` points to the image on the COCO server (so you can also access directly). `caption` is self-explanatory. `label` being `0` and `1` corresponds to False and True respectively. `relation` records the spatial relation used. `annotator_id` points to the annotator who originally wrote the caption. `vote_true_validator_id` and `vote_false_validator_id` are annotators who voted True or False in the second phase validation.

### Data Splits

The VSR corpus, after validation, contains 10,119 data points with high agreement. On top of these, we create two splits (1) random split and (2) zero-shot split. For random split, we randomly split all data points into train, development, and test sets. Zero-shot split makes sure that train, development and test sets have no overlap of concepts (i.e., if *dog* is in test set, it is not used for training and development). Below are some basic statistics of the two splits.

split   |  train | dev | test | total
:------|:--------:|:--------:|:--------:|:--------:
random | 7,083 | 1,012 | 2,024 | 10,119 
zero-shot | 5,440 | 259 | 731 | 6,430

Check out [`data/`](https://github.com/cambridgeltl/visual-spatial-reasoning/tree/master/data) for more details.

## Dataset Creation

### Curation Rationale

Understanding spatial relations is fundamental to achieve intelligence. Existing vision-language reasoning datasets are great but they compose multiple types of challenges and can thus conflate different sources of error.
The VSR corpus focuses specifically on spatial relations so we can have accurate diagnosis and maximum interpretability.

### Source Data

#### Initial Data Collection and Normalization

**Image pair sampling.** MS COCO 2017 contains
123,287 images and has labelled the segmentation and classes of 886,284 instances (individual
objects). Leveraging the segmentation, we first
randomly select two concepts, then retrieve all images containing the two concepts in COCO 2017 (train and
validation sets). Then images that contain multiple instances of any of the concept are filtered
out to avoid referencing ambiguity. For the single-instance images, we also filter out any of the images with instance area size < 30, 000, to prevent extremely small instances. After these filtering steps,
we randomly sample a pair in the remaining images.
We repeat such process to obtain a large number of
individual image pairs for caption generation.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

**Fill in the blank: template-based caption generation.** Given a pair of images, the annotator needs to come up with a valid caption that makes it correctly describing one image but incorrect for the other. In this way, the annotator could focus on the key difference of the two images (which should be spatial relation of the two objects of interest) and come up with challenging relation that differentiates the two. Similar paradigms are also used in the annotation of previous vision-language reasoning datasets such as NLVR2 (Suhr et al., 2017,
2019) and MaRVL (Liu et al., 2021). To regularise annotators from writing modifiers and differentiating the image pair with things beyond accurate spatial relations, we opt for a template-based classification task instead of free-form caption writing. Besides, the template-generated dataset can be easily categorised based on relations and their meta-categories.

The caption template has the format of “The
`OBJ1` (is) __ the `OBJ2`.”, and the annotators
are instructed to select a relation from a fixed set
to fill in the slot. The copula “is” can be omitted
for grammaticality. For example, for “contains”,
“consists of”, and “has as a part”, “is” should be
discarded in the template when extracting the final
caption.

The fixed set of spatial relations enable us to obtain the full control of the generation process. The
full list of used relations are listed in the table below. It
contains 71 spatial relations and is adapted from
the summarised relation table of Fagundes et al.
(2021). We made minor changes to filter out clearly
unusable relations, made relation names grammatical under our template, and reduced repeated relations.
In our final dataset, 65 out of the 71 available relations are actually included (the other 6 are
either not selected by annotators or are selected but
the captions did not pass the validation phase).

| Category    | Spatial Relations                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Adjacency   | Adjacent to, alongside, at the side of, at the right side of, at the left side of, attached to, at the back of, ahead of, against, at the edge of                    |
| Directional | Off, past, toward, down, deep down*, up*, away from, along, around, from*, into, to*, across, across from, through*, down from |
| Orientation | Facing, facing away from, parallel to, perpendicular to |
| Projective  | On top of, beneath, beside, behind, left of, right of, under, in front of, below, above, over, in the middle of                                 |
| Proximity   | By, close to, near, far from, far away from |
| Topological | Connected to, detached from, has as a part, part of, contains, within, at, on, in, with, surrounding, among, consists of, out of, between, inside, outside, touching                      |
| Unallocated | Beyond, next to, opposite to, after*, among, enclosed by |

**Second-round Human Validation.** Every annotated data point is reviewed by at least
two additional human annotators (validators). In
validation, given a data point (consists of an image
and a caption), the validator gives either a True or
False label. We exclude data points that have <
2/3 validators agreeing with the original label.

In the guideline, we communicated to the validators that, for relations such as “left”/“right”, “in
front of”/“behind”, they should tolerate different
reference frame: i.e., if the caption is true from either the object’s or the viewer’s reference, it should
be given a True label. Only
when the caption is incorrect under all reference
frames, a False label is assigned. This adds
difficulty to the models since they could not naively
rely on relative locations of the objects in the images but also need to correctly identify orientations of objects to make the best judgement.

#### Who are the annotators?

Annotators are hired from [prolific.co](https://prolific.co). We
require them (1) have at least a bachelor’s degree,
(2) are fluent in English or native speaker, and (3)
have a >99% historical approval rate on the platform. All annotators are paid with an hourly salary
of 12 GBP. Prolific takes an extra 33% of service
charge and 20% VAT on the service charge.

For caption generation, we release the task with
batches of 200 instances and the annotator is required to finish a batch in 80 minutes. An annotator
cannot take more than one batch per day. In this
way we have a diverse set of annotators and can
also prevent annotators from being fatigued. For
second round validation, we group 500 data points
in one batch and an annotator is asked to label each
batch in 90 minutes.

In total, 24 annotators participated in caption
generation and 26 participated in validation. The
annotators have diverse demographic background:
they were born in 13 different countries; live in 13
different couturiers; and have 14 different nationalities. 57.4% of the annotators identify themselves
as females and 42.6% as males.

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

[More Information Needed]

### Licensing Information

This project is licensed under the [Apache-2.0 License](https://github.com/cambridgeltl/visual-spatial-reasoning/blob/master/LICENSE).

### Citation Information

```bibtex
@article{Liu2022VisualSR,
  title={Visual Spatial Reasoning},
  author={Fangyu Liu and Guy Edward Toh Emerson and Nigel Collier},
  journal={ArXiv},
  year={2022},
  volume={abs/2205.00363}
}
```

### Contributions

Thanks to [@juletx](https://github.com/juletx) for adding this dataset.