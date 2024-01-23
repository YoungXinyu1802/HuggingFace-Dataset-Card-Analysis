---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
- question-answering
- summarization
- text-generation
task_ids:
- abstractive-qa
- closed-domain-qa
- extractive-qa
- language-modeling
- named-entity-recognition
- text-simplification
pretty_name: worldbank_project_documents
language_bcp47:
- en-US
tags:
- conditional-text-generation
- structure-prediction
---

# Dataset Card for World Bank Project Documents

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

- **Homepage:**
- **Repository:** https://github.com/luke-grassroot/aid-outcomes-ml
- **Paper:** Forthcoming
- **Point of Contact:** Luke Jordan (lukej at mit)

### Dataset Summary

This is a dataset of documents related to World Bank development projects in the period 1947-2020. The dataset includes
the documents used to propose or describe projects when they are launched, and those in the review. The documents are indexed
by the World Bank project ID, which can be used to obtain features from multiple publicly available tabular datasets.

### Supported Tasks and Leaderboards

No leaderboard yet. A wide range of possible supported tasks, including varieties of summarization, QA, and language modelling. To date, the datasets have been used primarily in conjunction with tabular data (via BERT embeddings) to predict project outcomes.

### Languages

English

## Dataset Structure

### Data Instances

### Data Fields

* World Bank project ID
* Document text
* Document type: "APPROVAL" for documents written at the beginning of a project, when it is approved; and "REVIEW" for documents written at the end of a project

### Data Splits

To allow for open exploration, and since different applications will want to do splits based on different sampling weights, we have not done a train test split but left all files in the train branch.

## Dataset Creation

### Source Data

Documents were scraped from the World Bank's public project archive, following links through to specific project pages and then collecting the text files made available by the [World Bank](https://projects.worldbank.org/en/projects-operations/projects-home).

### Annotations

This dataset is not annotated.

### Personal and Sensitive Information

None.

## Considerations for Using the Data

### Social Impact of Dataset

Affects development projects, which can have large-scale consequences for many millions of people.

### Discussion of Biases

The documents reflect the history of development, which has well-documented and well-studied issues with the imposition of developed world ideas on developing world countries. The documents provide a way to study those in the field of development, but should not be used for their description of the recipient countries, since that language will reflect a multitude of biases, especially in the earlier reaches of the historical projects.

## Additional Information

### Dataset Curators

Luke Jordan, Busani Ndlovu.

### Licensing Information

MIT +no-false-attribs license (MITNFA).

### Citation Information

@dataset{world-bank-project-documents,
  author    = {Jordan, Luke and Ndlovu, Busani and Shenk, Justin},
  title     = {World Bank Project Documents Dataset},
  year      = {2021}
}

### Contributions

Thanks to [@luke-grassroot](https://github.com/luke-grassroot), [@FRTNX](https://github.com/FRTNX/) and [@justinshenk](https://github.com/justinshenk) for adding this dataset.