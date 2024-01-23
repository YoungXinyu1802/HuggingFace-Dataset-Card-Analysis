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
- natural-language-inference
paperswithcode_id: danfever
pretty_name: DanFEVER
tags:
- knowledge-verification
---


# Dataset Card for DanFEVER

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

- **Homepage:** [https://github.com/StrombergNLP/danfever](https://github.com/StrombergNLP/danfever)
- **Repository:** [https://stromberg.ai/publication/danfever/](https://stromberg.ai/publication/danfever/)
- **Paper:** [https://aclanthology.org/2021.nodalida-main.47/](https://aclanthology.org/2021.nodalida-main.47/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Leon Derczynski](mailto:leod@itu.dk)
- **Size of downloaded dataset files:** 2.82 MiB
- **Size of the generated dataset:** 2.80 MiB
- **Total amount of disk used:** 5.62 MiB

### Dataset Summary

We present a dataset, DanFEVER, intended for multilingual misinformation research. The dataset is in Danish and has the same format as the well-known English FEVER dataset. It can be used for testing methods in multilingual settings, as well as for creating models in production for the Danish language.

### Supported Tasks and Leaderboards

This dataset supports the FEVER task, but in Danish.

* PwC leaderboard: [Fact Verification on DanFEVER](https://paperswithcode.com/sota/fact-verification-on-danfever)

### Languages

This dataset is in Danish; the bcp47 is `da_DK`.

## Dataset Structure

### Data Instances

```
{
  'id': '0', 
  'claim': 'Den 31. oktober 1920 opdagede Walter Baade kometen (944) Hidalgo i det ydre solsystem.', 
  'label': 0, 
  'evidence_extract': '(944) Hidalgo (oprindeligt midlertidigt navn: 1920 HZ) er en mørk småplanet med en diameter på ca. 50 km, der befinder sig i det ydre solsystem. Objektet blev opdaget den 31. oktober 1920 af Walter Baade. En asteroide (småplanet, planetoide) er et fast himmellegeme, hvis bane går rundt om Solen (eller en anden stjerne). Pr. 5. maj 2017 kendes mere end 729.626 asteroider og de fleste befinder sig i asteroidebæltet mellem Mars og Jupiter.', 
  'verifiable': 1, 
  'evidence': 'wiki_26366, wiki_12289', 
  'original_id': '1'
}
```

### Data Fields

[Needs More Information]

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

A dump of the Danish Wikipedia of 13 February 2020 was stored as well as the relevant articles from Den Store Danske (excerpts only, to comply with copyright laws). Two teams of two people independently sampled evidence, and created and annotated claims from these two sites.

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

The source language is from Wikipedia contributors editors and from dictionary contributors and editors.

### Annotations

#### Annotation process

Detailed in [this paper](http://www.derczynski.com/papers/danfever.pdf).

#### Who are the annotators?

The annotators are native Danish speakers and masters students of IT; two female, two male, ages 25-35.

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to enable construction of fact-checking systems in Danish. A system that succeeds at this may be able to identify questionable conclusions or inferences.

### Discussion of Biases

The data is drawn from relatively formal topics, and so may perform poorly outside these areas.

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

The data here is licensed CC-BY 4.0. If you use this data, you MUST state its origin.

### Citation Information

Refer to this work as:

> Nørregaard and Derczynski (2021). "DanFEVER: claim verification dataset for Danish", Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa).

Bibliographic reference:

````
@inproceedings{norregaard-derczynski-2021-danfever,
    title = "{D}an{FEVER}: claim verification dataset for {D}anish",
    author = "N{\o}rregaard, Jeppe  and  Derczynski, Leon",
    booktitle = "Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)",
    year = "2021",
    publisher = {Link{\"o}ping University Electronic Press, Sweden},
    url = "https://aclanthology.org/2021.nodalida-main.47",
    pages = "422--428"
}
```
