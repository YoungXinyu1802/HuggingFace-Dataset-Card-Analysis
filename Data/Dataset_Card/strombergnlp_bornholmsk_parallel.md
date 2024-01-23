---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- da
- da-bornholm
license:
- cc-by-4.0
multilinguality:
- translation
pretty_name: Bornholmsk/Danish Parallel Texts
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- translation
task_ids: []
paperswithcode_id: bornholmsk-parallel
---


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

- **Homepage:** [https://github.com/StrombergNLP/bornholmsk](https://github.com/StrombergNLP/bornholmsk)
- **Repository:** [https://github.com/StrombergNLP/bornholmsk](https://github.com/StrombergNLP/bornholmsk)
- **Paper:** [https://aclanthology.org/W19-6138/](https://aclanthology.org/W19-6138/)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 490 KB
- **Size of the generated dataset:** 582 KB
- **Total amount of disk used:**  1072 KB

### Dataset Summary

This dataset is parallel text for Bornholmsk and Danish. 

For more details, see the paper [Bornholmsk Natural Language Processing: Resources and Tools](https://aclanthology.org/W19-6138/).

### Supported Tasks and Leaderboards

* 

### Languages

Bornholmsk, a language variant of Danish spoken on the island of Bornholm, and Danish. bcp47: `da-bornholm` and `da-DK`

## Dataset Structure

### Data Instances

### Data Fields

`id`: the sentence ID, `int`
`da-bornholm`: the Bornholmsk text, `string`
`da`: the Danish translation, `string`

### Data Splits

* Train: 5785 sentence pairs
* Validation: 500 sentence pairs
* Test: 500 sentence pairs

## Dataset Creation

### Curation Rationale

To gather as much parallel Bornholmsk together as possible

### Source Data

#### Initial Data Collection and Normalization

From a translation of Kuhre's Sansager, a selection of colloquial resources, and a prototype Bornholmsk/Danish dictionary

#### Who are the source language producers?

Native speakers of Bornholmsk who have produced works in their native language, or translated them to Danish. Much of the data is the result of a community of Bornholmsk speakers volunteering their time across the island in an effort to capture this endangered language.

### Annotations

#### Annotation process

No annotations

#### Who are the annotators?

Native speakers of Bornholmsk, mostly aged 60+.

### Personal and Sensitive Information

Unknown, but low risk of presence, given the source material

## Considerations for Using the Data

### Social Impact of Dataset

The hope behind this data is to enable people to learn and use Bornholmsk

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

This collection of Bornholmsk is curated by Leon Derczynski and Alex Speed Kjeldsen

### Licensing Information

Creative Commons Attribution 4.0

### Citation Information

```
@inproceedings{derczynski-kjeldsen-2019-bornholmsk,
    title = "Bornholmsk Natural Language Processing: Resources and Tools",
    author = "Derczynski, Leon  and
      Kjeldsen, Alex Speed",
    booktitle = "Proceedings of the 22nd Nordic Conference on Computational Linguistics",
    month = sep # "{--}" # oct,
    year = "2019",
    address = "Turku, Finland",
    publisher = {Link{\"o}ping University Electronic Press},
    url = "https://aclanthology.org/W19-6138",
    pages = "338--344",
}
```