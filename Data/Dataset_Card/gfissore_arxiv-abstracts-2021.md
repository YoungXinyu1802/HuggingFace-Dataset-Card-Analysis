---
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- en
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: arxiv-abstracts-2021
size_categories:
- 1M<n<10M
source_datasets: []
task_categories:
- summarization
- text-retrieval
- text2text-generation
task_ids:
- explanation-generation
- text-simplification
- document-retrieval
- entity-linking-retrieval
- fact-checking-retrieval
---

# Dataset Card for arxiv-abstracts-2021

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
- **Repository:** [Needs More Information]
- **Paper:** [Clement et al., 2019, On the Use of ArXiv as a Dataset, https://arxiv.org/abs/1905.00075](https://arxiv.org/abs/1905.00075)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Giancarlo Fissore](mailto:giancarlo.fissore@gmail.com)

### Dataset Summary

A dataset of metadata including title and abstract for all arXiv articles up to the end of 2021 (~2 million papers).
Possible applications include trend analysis, paper recommender engines, category prediction,  knowledge graph construction and semantic search interfaces.

In contrast to [arxiv_dataset](https://huggingface.co/datasets/arxiv_dataset), this dataset doesn't include papers submitted to arXiv after 2021 and it doesn't require any external download.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

English

## Dataset Structure

### Data Instances

Here's an example instance:
```
{  
  "id": "1706.03762",
  "submitter": "Ashish Vaswani",
  "authors": "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion\n  Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin",
  "title": "Attention Is All You Need",
  "comments": "15 pages, 5 figures",
  "journal-ref": null,
  "doi": null,
  "abstract": "  The dominant sequence transduction models are based on complex recurrent or\nconvolutional neural     
networks in an encoder-decoder configuration. The best\nperforming models also connect the encoder and decoder through 
an attention\nmechanism. We propose a new simple network architecture, the Transformer, based\nsolely on attention     
mechanisms, dispensing with recurrence and convolutions\nentirely. Experiments on two machine translation tasks show   
these models to be\nsuperior in quality while being more parallelizable and requiring significantly\nless time to      
train. Our model achieves 28.4 BLEU on the WMT 2014\nEnglish-to-German translation task, improving over the existing   
best results,\nincluding ensembles by over 2 BLEU. On the WMT 2014 English-to-French\ntranslation task, our model      
establishes a new single-model state-of-the-art\nBLEU score of 41.8 after training for 3.5 days on eight GPUs, a small 
fraction\nof the training costs of the best models from the literature. We show that the\nTransformer generalizes well 
to other tasks by applying it successfully to\nEnglish constituency parsing both with large and limited training       
data.\n",
  "report-no": null,
  "categories": [   
    "cs.CL cs.LG"
  ],     
  "versions": [  
    "v1",
    "v2",
    "v3",
    "v4",
    "v5"
  ]
}
```

### Data Fields

These fields are detailed on the [arXiv](https://arxiv.org/help/prep):

- `id`: ArXiv ID (can be used to access the paper)
- `submitter`: Who submitted the paper
- `authors`: Authors of the paper
- `title`: Title of the paper
- `comments`: Additional info, such as number of pages and figures
- `journal-ref`: Information about the journal the paper was published in
- `doi`: [Digital Object Identifier](https://www.doi.org)
- `report-no`: Report Number
- `abstract`: The abstract of the paper
- `categories`: Categories / tags in the ArXiv system

### Data Splits

No splits

## Dataset Creation

### Curation Rationale

For about 30 years, ArXiv has served the public and research communities by providing open access to scholarly articles, from the vast branches of physics to the many subdisciplines of computer science to everything in between, including math, statistics, electrical engineering, quantitative biology, and economics. This rich corpus of information offers significant, but sometimes overwhelming, depth. In these times of unique global challenges, efficient extraction of insights from data is essential. The `arxiv-abstracts-2021` dataset aims at making the arXiv more easily accessible for machine learning applications, by providing important metadata (including title and abstract) for ~2 million papers.

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

The language producers are members of the scientific community at large, but not necessarily affiliated to any institution.

### Annotations

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

The full names of the papers' authors are included in the dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The original data is maintained by [ArXiv](https://arxiv.org/)

### Licensing Information

The data is under the [Creative Commons CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)

### Citation Information
```
@misc{clement2019arxiv,
    title={On the Use of ArXiv as a Dataset},
    author={Colin B. Clement and Matthew Bierbaum and Kevin P. O'Keeffe and Alexander A. Alemi},
    year={2019},
    eprint={1905.00075},
    archivePrefix={arXiv},
    primaryClass={cs.IR}
}
```