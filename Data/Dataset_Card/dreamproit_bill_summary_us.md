---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
license: []
multilinguality:
- monolingual
pretty_name: bill_summarization
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- bills
task_categories:
- summarization
task_ids: []
---

# Dataset Card for "bill_summarization"

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

- **Homepage:** https://github.com/dreamproit/BillML
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Leaderboard:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

Dataset for summarization of summarization of US Congressional bills (bill_summarization).


### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

English

## Dataset Structure

### Data Instances

#### default

- **Size of downloaded dataset files:** 186 MB
- **Total amount of disk used:** 177 MB

### Data Fields

- id: id of the bill.
- sections: list of bill sections with section_id and text.
- text: bill text.
- text_len: number of characters in the text.
- summary: summary of the bill.
- summary_len: number of characters in the summary.
- title: official title of the bill.

### Data Splits

No splits.

## Dataset Creation

### Curation Rationale

Bills (proposed laws) are specialized, structured documents with great public significance. Often, the language of a bill may not directly explain the potential impact of the legislation. For bills in the U.S. Congress, the Congressional Research Service of the Library of Congress provides professional, non-partisan summaries of bills. These are valuable for public understanding of the bills and are serve as an essential part of the lawmaking process to understand the meaning and potential legislative impact.

This dataset collects the text of bills, some metadata, as well as the CRS summaries. In order to build more accurate ML models for bill summarization it is important to have a clean dataset, alongside the professionally-written CRS summaries. ML summarization models built on generic data are bound to produce less accurate results (sometimes creating summaries that describe the opposite of a bill's actual effect). In addition, models that attempt to summarize all bills (some of which may reach 4000 pages long) may also be inaccurate due to the current limitations of summarization on long texts.

As a result, this dataset collects bill and summary information for only small bills (10 sections or fewer). It is meant as a starting point for community-driven development of ML models for bill summarization. In the future, we may expand or enhance the dataset in a number of ways-- adding metadata, including larger bills, and providing feedback from expert legislative analysts on any automated summaries that are produced.

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

The data consists of the US congress bills that were collected from the [Govinfo](https://github.com/unitedstates/congress) service provided by the United States Government Publishing Office (GPO) under CC0-1.0 license.

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)


### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

dreamproit.com

### Licensing Information

Bill and summary information are public and are unlicensed, as it is data produced by government entities. The collection and enhancement work that we provide for this dataset, to the degree it may be covered by copyright, is released under CC0 (https://creativecommons.org/share-your-work/public-domain/cc0/)

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@BorodaUA](https://github.com/BorodaUA), [@alexbojko](https://github.com/alexbojko) for adding this dataset.