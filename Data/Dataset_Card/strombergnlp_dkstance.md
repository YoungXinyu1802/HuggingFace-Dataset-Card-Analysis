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
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- fact-checking
paperswithcode_id: dast
pretty_name: DAST
extra_gated_prompt: 'Warning: the data in this repository contains harmful content
  (misinformative claims).'
tags:
- stance-detection
---

# Dataset Card for "dkstance / DAST"

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

- **Homepage:** [https://stromberg.ai/publication/jointrumourstanceandveracity/](https://stromberg.ai/publication/jointrumourstanceandveracity/)
- **Repository:** [https://figshare.com/articles/dataset/Danish_stance-annotated_Reddit_dataset/8217137](https://figshare.com/articles/dataset/Danish_stance-annotated_Reddit_dataset/8217137)
- **Paper:** [https://aclanthology.org/W19-6122/](https://aclanthology.org/W19-6122/)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:** 

### Dataset Summary

This is an SDQC stance-annotated Reddit dataset for the Danish language generated within a thesis project. The dataset consists of over 5000 comments structured as comment trees and linked to 33 source posts.

The dataset is applicable for supervised stance classification and rumour veracity prediction.

### Supported Tasks and Leaderboards

* Stance prediction

### Languages



## Dataset Structure

### Data Instances

#### DAST / dkstance

- **Size of downloaded dataset files:** 4.72 MiB
- **Size of the generated dataset:** 3.69 MiB
- **Total amount of disk used:**  8.41 MiB

An example of 'train' looks as follows.

```
{
  'id': '1', 
  'native_id': 'ebwjq5z', 
  'text': 'Med de udfordringer som daginstitutionerne har med normeringer, og økonomi i det hele taget, synes jeg det er en vanvittig beslutning at prioritere skattebetalt vegansk kost i daginstitutionerne. Brug dog pengene på noget mere personale, og lad folk selv betale for deres individuelle kostønsker.', 
  'parent_id': 'a6o3us', 
  'parent_text': 'Mai Mercado om mad i daginstitutioner: Sund kost rimer ikke på veganer-mad', 
  'parent_stance': 0, 
  'source_id': 'a6o3us', 
  'source_text': 'Mai Mercado om mad i daginstitutioner: Sund kost rimer ikke på veganer-mad', 
  'source_stance': 0
}
```


### Data Fields

- `id`: a `string` feature.
- `native_id`: a `string` feature representing the native ID of the entry.
- `text`: a `string` of the comment text in which stance is annotated.
- `parent_id`: the `native_id` of this comment's parent.
- `parent_text`: a `string` of the parent comment's text.
- `parent_stance`: the label of the stance in the comment towards its parent comment.

```
                            0: "Supporting",
                            1: "Denying",
                            2: "Querying",
                            3: "Commenting",
```

- `source_id`: the `native_id` of this comment's source / post.
- `source_text`: a `string` of the source / post text.
- `source_stance`: the label of the stance in the comment towards the original source post.

```
                            0: "Supporting",
                            1: "Denying",
                            2: "Querying",
                            3: "Commenting",
```

### Data Splits

|  name   |size|
|---------|----:|
|train|3122|
|validation|1066|
|test|1060|

These splits are specified after the original reserach was reported. The splits add an extra level of rigour, in that no source posts' comment tree is spread over more than one partition.

## Dataset Creation

### Curation Rationale

Comments around rumourous claims to enable rumour and stance analysis in Danish

### Source Data

#### Initial Data Collection and Normalization

The data is from Reddit posts that relate to one of a specific set of news stories; these stories are enumerated in the paper. 

#### Who are the source language producers?

Danish-speaking Twitter users.

### Annotations

#### Annotation process

There was multi-user annotation process mediated through a purpose-built interface for annotating stance in Reddit threads.

#### Who are the annotators?

* Age: 20-30.
* Gender: male.
* Race/ethnicity: white northern European.
* Native language: Danish.
* Socioeconomic status: higher education student.

### Personal and Sensitive Information

The data was public at the time of collection. User names are not preserved.

## Considerations for Using the Data

### Social Impact of Dataset

There's a risk of user-deleted content being in this data. The data has NOT been vetted for any content, so there's a risk of harmful text.

### Discussion of Biases

The source of the text has a strong demographic bias, being mostly young white men who are vocal their opinions. This constrains both the styles of language and discussion contained in the data, as well as the topics discussed and viewpoints held.

### Other Known Limitations

The above limitations apply.

## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. 
An NLP data statement is included in the paper describing the work, [https://aclanthology.org/W19-6122.pdf](https://aclanthology.org/W19-6122.pdf)

### Citation Information

```
@inproceedings{lillie-etal-2019-joint,
    title = "Joint Rumour Stance and Veracity Prediction",
    author = "Lillie, Anders Edelbo  and
      Middelboe, Emil Refsgaard  and
      Derczynski, Leon",
    booktitle = "Proceedings of the 22nd Nordic Conference on Computational Linguistics",
    month = sep # "{--}" # oct,
    year = "2019",
    address = "Turku, Finland",
    publisher = {Link{\"o}ping University Electronic Press},
    url = "https://aclanthology.org/W19-6122",
    pages = "208--221",
}
```


### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
