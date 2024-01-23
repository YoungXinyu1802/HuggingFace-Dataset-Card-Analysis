---
annotations_creators:
- machine-generated
- crowdsourced
language_creators:
- machine-generated
- crowdsourced
language:
- ca
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: CAT ManyNames
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-label-image-classification
---

# Dataset Card for CAT ManyNames

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

- **Repository:** https://github.com/MarDominguezOrfila/CAT-ManyNames
- **Point of Contact:** [mar.dominguez01@estudiant.upf.edu](mar.dominguez01@estudiant.upf.edu)

### Dataset Summary

CAT ManyNames is the Catalan version of the [ManyNames dataset](https://github.com/amore-upf/manynames) suitable for training Language & Vision models in the task of object naming. The corpus consists of more than 23K images and their corresponding annotations. 

The human-annotated test set has been built to evaluate the quality of the CAT ManyNames dataset. Its corpus consists of 1,072 images and their corresponding annotations (ca. 10 annotations per image).

### Supported Tasks and Leaderboards

Object Naming, Language & Vision Model.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

[![image](https://object-naming-amore.upf.edu//691_3788097_singleton_obj.png "image")](https://object-naming-amore.upf.edu//691_3788097_singleton_obj.png "image")
`'responses' : {"guepard": 27, "lleopard": 3, "animal": 2, "gat": 2, "tigre": 2}`

### Data Fields

Both CAT ManyNames and its human-annotated test set are provided in a tab-separated text file (.tsv). The first rows contain the column labels. Nested data is stored as Python dictionaries (i.e., "{key: value}").
The columns are labelled as follows (the most important columns are listed first):

- responses: Correct responses and their counts
- topname: The most frequent name of the object in the largest cluster
- domain: The MN domain of the object
- incorrect (not available for the human-annotated test set): Incorrect responses and their counts
- singletons (not available for the human-annotated test set): All responses which were given only once and are not synonyms or - hypernyms of the top name (these are included in responses)
- total_responses: Sum count of correct responses
- split: Use of the image in training vs. test vs. validation
- vg_object_id: The VisualGenome id of the object
- vg_image_id: The VisualGenome id of the image
- topname_agreement (only available for the test split): The number of responses for the top name divided by the number of total responses
- jaccard_similarity (only available for the test split): Jaccard similarity index of the responses column in CAT ManyNames and its human-annotated test set


### Data Splits

-	Test: 1,072 images
-	Val: 1,110 images
-	Train: 21,503 images

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of multimodal models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

The original visual data comes from [VisualGenome](https://visualgenome.org/). The objects were categorized in the categories of people, animals_plants, vehicles, food, home, buildings, and clothing.

#### Who are the source language producers?

The original [ManyNames dataset](https://github.com/amore-upf/manynames).

### Annotations

Annotations for the CAT ManyNames were obtained by performing a machine translation of the ManyNames dataset, originally in English. The test set was humanly annotated.

#### Annotation process

[N/A]

#### Who are the annotators?

The human-annotated test set gathered 220 Catalan native volunteer participants.

### Personal and Sensitive Information

There is no sensitive information in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of multimodal models in Catalan, a low-resource language.

### Discussion of Biases

We have not applied any steps to reduce the impact of biases possibly present in the data.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Mar Domínguez Orfila (mar dot dominguez01 at estudiant dot upf dot edu)

### Licensing Information

CAT ManyNames is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

```
@inproceedings{dominguez-orfila-etal-2022-cat,
    title = "{CAT} {M}any{N}ames: A New Dataset for Object Naming in {C}atalan",
    author = "Dom{\'\i}nguez Orfila, Mar  and
      Melero Nogu{\'e}s, Maite  and
      Boleda Torrent, Gemma",
    booktitle = "Proceedings of the Workshop on Cognitive Aspects of the Lexicon",
    month = nov,
    year = "2022",
    address = "Taipei, Taiwan",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.cogalex-1.4",
    pages = "31--36",
    abstract = "Object Naming is an important task within the field of Language and Vision that consists of generating a correct and appropriate name for an object given an image. The ManyNames dataset uses real-world human annotated images with multiple labels, instead of just one. In this work, we describe the adaptation of this dataset (originally in English) to Catalan, by (i) machine-translating the English labels and (ii) collecting human annotations for a subset of the original corpus and comparing both resources. Analyses reveal divergences in the lexical variation of the two sets showing potential problems of directly translated resources, particularly when there is no resource to a proper context, which in this case is conveyed by the image. The analysis also points to the impact of cultural factors in the naming task, which should be accounted for in future cross-lingual naming tasks.",
}
```