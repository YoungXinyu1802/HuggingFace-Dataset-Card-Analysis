---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- crowdsourced
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: wiki-paragraphs
size_categories:
- 10M<n<100M
source_datasets:
- original
tags:
- wikipedia
- self-similarity
task_categories:
- text-classification
- sentence-similarity
task_ids:
- semantic-similarity-scoring
---

# Dataset Card for `wiki-paragraphs`

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

- **Homepage:** [Needs More Information]
- **Repository:** https://github.com/dennlinger/TopicalChange
- **Paper:** https://arxiv.org/abs/2012.03619
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Dennis Aumiller](aumiller@informatik.uni-heidelberg.de)

### Dataset Summary

The wiki-paragraphs dataset is constructed by automatically sampling two paragraphs from a Wikipedia article. If they are from the same section, they will be considered a "semantic match", otherwise as "dissimilar". Dissimilar paragraphs can in theory also be sampled from other documents, but have not shown any improvement in the particular evaluation of the linked work.  
The alignment is in no way meant as an accurate depiction of similarity, but allows to quickly mine large amounts of samples.

### Supported Tasks and Leaderboards

The dataset can be used for "same-section classification", which is a binary classification task (either two sentences/paragraphs belong to the same section or not).
This can be combined with document-level coherency measures, where we can check how many misclassifications appear within a single document.
Please refer to [our paper](https://arxiv.org/abs/2012.03619) for more details.

### Languages

The data was extracted from English Wikipedia, therefore predominantly in English.

## Dataset Structure

### Data Instances

A single instance contains three attributes:

```
{
  "sentence1": "<Sentence from the first paragraph>",
  "sentence2": "<Sentence from the second paragraph>",
  "label": 0/1 # 1 indicates two belong to the same section
}
```

### Data Fields

- sentence1: String containing the first paragraph
- sentence2: String containing the second paragraph
- label: Integer, either 0 or 1. Indicates whether two paragraphs belong to the same section (1) or come from different sections (0)

### Data Splits

We provide train, validation and test splits, which were split as 80/10/10 from a randomly shuffled original data source.
In total, we provide 25375583 training pairs, as well as 3163685 validation and test instances, respectively.

## Dataset Creation

### Curation Rationale

The original idea was applied to self-segmentation of Terms of Service documents. Given that these are of domain-specific nature, we wanted to provide a more generally applicable model trained on Wikipedia data.  
It is meant as a cheap-to-acquire pre-training strategy for large-scale experimentation with semantic similarity for long texts (paragraph-level).
Based on our experiments, it is not necessarily sufficient by itself to replace traditional hand-labeled semantic similarity datasets.

### Source Data

#### Initial Data Collection and Normalization

The data was collected based on the articles considered in the Wiki-727k dataset by Koshorek et al. The dump of their dataset can be found through the [respective Github repository](https://github.com/koomri/text-segmentation). Note that we did *not* use the pre-processed data, but rather only information on the considered articles, which were re-acquired from Wikipedia at a more recent state.
This is due to the fact that paragraph information was not retained by the original Wiki-727k authors.
We did not verify the particular focus of considered pages.

#### Who are the source language producers?

We do not have any further information on the contributors; these are volunteers contributing to en.wikipedia.org.

### Annotations

#### Annotation process

No manual annotation was added to the dataset.
We automatically sampled two sections from within the same article; if these belong to the same section, they were assigned a label indicating the "similarity" (1), otherwise the label indicates that they are not belonging to the same section (0).
We sample three positive and three negative samples per section, per article.

#### Who are the annotators?

No annotators were involved in the process.

### Personal and Sensitive Information

We did not modify the original Wikipedia text in any way. Given that personal information, such as dates of birth (e.g., for a person of interest) may be on Wikipedia, this information is also considered in our dataset.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of the dataset is to serve as a *pre-training addition* for semantic similarity learning.

Systems building on this dataset should consider additional, manually annotated data, before using a system in production.

### Discussion of Biases

To our knowledge, there are some works indicating that male people have a several times larger chance of having a Wikipedia page created (especially in historical contexts). Therefore, a slight bias towards over-representation might be left in this dataset.

### Other Known Limitations

As previously stated, the automatically extracted semantic similarity is not perfect; it should be treated as such.

## Additional Information

### Dataset Curators

The dataset was originally developed as a practical project by Lucienne-Sophie Marm� under the supervision of Dennis Aumiller.
Contributions to the original sampling strategy were made by Satya Almasian and Michael Gertz

### Licensing Information

Wikipedia data is available under the CC-BY-SA 3.0 license.

### Citation Information
```
@inproceedings{DBLP:conf/icail/AumillerAL021,
  author    = {Dennis Aumiller and
               Satya Almasian and
               Sebastian Lackner and
               Michael Gertz},
  editor    = {Juliano Maranh{\~{a}}o and
               Adam Zachary Wyner},
  title     = {Structural text segmentation of legal documents},
  booktitle = {{ICAIL} '21: Eighteenth International Conference for Artificial Intelligence
               and Law, S{\~{a}}o Paulo Brazil, June 21 - 25, 2021},
  pages     = {2--11},
  publisher = {{ACM}},
  year      = {2021},
  url       = {https://doi.org/10.1145/3462757.3466085},
  doi       = {10.1145/3462757.3466085}
}
```