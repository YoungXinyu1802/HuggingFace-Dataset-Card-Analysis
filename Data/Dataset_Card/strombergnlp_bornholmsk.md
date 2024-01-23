---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- da
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
language_bcp47:
- da
- da-bornholm
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

- **Homepage:** https://github.com/StrombergNLP/bornholmsk
- **Repository:** https://github.com/StrombergNLP/bornholmsk
- **Paper:** https://aclanthology.org/W19-6138/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)

### Dataset Summary

This corpus introduces language processing resources and tools for Bornholmsk, a language spoken on the island of Bornholm, with roots in Danish and closely related to Scanian. 

Sammenfattnijng på borrijnholmst: Dæjnna artikkelijn introduserer natursprågsresurser å varktoi for borrijnholmst, ed språg a dær snakkes på ön Borrijnholm me rødder i danst å i nær familia me skånst.

For more details, see the paper [Bornholmsk Natural Language Processing: Resources and Tools](https://aclanthology.org/W19-6138/).

### Supported Tasks and Leaderboards

* 

### Languages

Bornholmsk, a language variant of Danish spoken on the island of Bornholm. bcp47: `da-bornholm`

## Dataset Structure

### Data Instances

13169 lines, 175 167 words, 801 KB

### Data Fields

`id`: the sentence ID, `int`
`text`: the Bornholmsk text, `string`

### Data Splits

Monolithic

## Dataset Creation

### Curation Rationale

To gather as much digital Bornholmsk together as possible

### Source Data

#### Initial Data Collection and Normalization

From many places - see paper for details. Sources include poems, songs, translations from Danish, folk stories, dictionary entries.

#### Who are the source language producers?

Native speakers of Bornholmsk who have produced works in their native language, or translated them to Danish. Much of the data is the result of a community of Bornholmsk speakers volunteering their time across the island in an effort to capture this endangered language.

### Annotations

#### Annotation process

No annotations

#### Who are the annotators?

No annotations

### Personal and Sensitive Information

Unknown, but low risk of presence, given the source material

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to capture Bornholmsk digitally and provide a way for NLP systems to interact with it, and perhaps even spark interest in dealing with the language.

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