---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- da
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-analysis
paperswithcode_id: polstance
pretty_name: Political Stance for Danish
tags:
- stance-detection
---

# Dataset Card for "polstance"

## Table of Contents
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

- **Homepage:** [https://stromberg.ai/publication/politicalstanceindanish/](https://stromberg.ai/publication/politicalstanceindanish/)
- **Repository:** [https://github.com/StrombergNLP/Political-Stance-in-Danish/](https://github.com/StrombergNLP/Political-Stance-in-Danish/)
- **Paper:** [https://aclanthology.org/W19-6121/](https://aclanthology.org/W19-6121/)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 548 KB
- **Size of the generated dataset:** 222 KB
- **Total amount of disk used:**  770 KB

### Dataset Summary

Political stance in Danish. Examples represent statements by 
politicians and are annotated for, against, or neutral to a given topic/article.

### Supported Tasks and Leaderboards

* 

### Languages

Danish, bcp47: `da-DK`

## Dataset Structure

### Data Instances

#### polstance

An example of 'train' looks as follows.

```
{
  'id': '0', 
  'topic': 'integration', 
  'quote': 'Der kunne jeg godt tænke mig, at der stod mere eksplicit, at de (landene, red.) skal bekæmpe menneskesmuglere og tage imod deres egne borgere', 
  'label': 2, 
  'quoteID': '516', 
  'party': 'Det Konservative Folkeparti', 
  'politician': 'Naser Khader', 
}
```


### Data Fields

- `id`: a `string` feature.
- `topic`: a `string` expressing a topic.
- `quote`: a `string` to be classified for its stance to the topic.
- `label`: a class label representing the stance the text expresses towards the target. Full tagset with indices:

```
                            0: "against",
                            1: "neutral",
                            2: "for",
```
- `quoteID`: a `string` of the internal quote ID.
- `party`: a `string` describing the party affiliation of the quote utterer at the time of utterance.
- `politician`: a `string` naming the politician who uttered the quote.

### Data Splits

|  name   |train|
|---------|----:|
|polstance|900 sentences|

## Dataset Creation

### Curation Rationale

Collection of quotes from politicians to allow detecting how political quotes orient to issues.

### Source Data

#### Initial Data Collection and Normalization

The data is taken from proceedings of the Danish parliament, the Folketing - [ft.dk](https://ft.dk).

#### Who are the source language producers?

Danish polticians

### Annotations

#### Annotation process

Annotators labelled comments for being against, neutral, or for a specified topic

#### Who are the annotators?

Danish native speakers, 20s, male, studying Software Design.

### Personal and Sensitive Information

The data was public at the time of collection and will remain open public record by law in Denmark.

## Considerations for Using the Data

### Social Impact of Dataset


### Discussion of Biases


### Other Known Limitations

The above limitations apply.

## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. 

### Citation Information

```
@inproceedings{lehmann2019political,
  title={Political Stance in Danish},
  author={Lehmann, Rasmus and Derczynski, Leon},
  booktitle={Proceedings of the 22nd Nordic Conference on Computational Linguistics},
  pages={197--207},
  year={2019}
}
```


### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
