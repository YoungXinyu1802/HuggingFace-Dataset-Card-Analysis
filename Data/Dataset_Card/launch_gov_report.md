---
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: GovReport
---


# Dataset Card for GovReport

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Versions](#versions)
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

- **Homepage:** [https://gov-report-data.github.io](https://gov-report-data.github.io)
- **Repository:** [https://github.com/luyang-huang96/LongDocSum](https://github.com/luyang-huang96/LongDocSum)
- **Paper:** [https://aclanthology.org/2021.naacl-main.112/](https://aclanthology.org/2021.naacl-main.112/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Government report dataset consists of reports and associated summaries written by government research agencies including Congressional Research Service and U.S. Government Accountability Office.

Compared with other long document summarization datasets, government report dataset has longer summaries and documents and requires reading in more context to cover salient words to be summarized.

### Versions

- `1.0.1` (default): remove extra whitespace.
- `1.0.0`: the dataset used in the original paper.

To use different versions, set the `revision` argument of the `load_dataset` function.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

Three configs are available:
- **plain_text** (default): the text-to-text summarization setting used as in the original paper.
- **plain_text_with_recommendations**: the text-to-text summarization setting, with "What GAO recommends" included in the summary.
- **structure**: data with the section structure.

To use different configs, set the `name` argument of the `load_dataset` function.

### Data Instances

#### plain_text & plain_text_with_recommendations

An example looks as follows.
```
{
    "id": "GAO_123456",
    "document": "This is a test document.",
    "summary": "This is a test summary"
}
```

#### structure

An example looks as follows.
```
{
    "id": "GAO_123456",
    "document_sections": {
      "title": ["test docment section 1 title", "test docment section 1.1 title"],
      "paragraphs": ["test document\nsection 1 paragraphs", "test document\nsection 1.1 paragraphs"],
      "depth": [1, 2]
    },
    "summary_sections": {
      "title": ["test summary section 1 title", "test summary section 2 title"],
      "paragraphs": ["test summary\nsection 1 paragraphs", "test summary\nsection 2 paragraphs"]
    }
}
```

### Data Fields

#### plain_text & plain_text_with_recommendations

- `id`: a `string` feature.
- `document`: a `string` feature.
- `summary`: a `string` feature.

#### structure

- `id`: a `string` feature.
- `document_sections`: a dictionary feature containing lists of (each element corresponds to a section):
  - `title`: a `string` feature.
  - `paragraphs`: a of `string` feature, with `\n` separating different paragraphs.
  - `depth`: a `int32` feature.
- `summary_sections`: a dictionary feature containing lists of (each element corresponds to a section):
  - `title`: a `string` feature.
  - `paragraphs`: a `string` feature, with `\n` separating different paragraphs.

### Data Splits

- train: 17519
- valid: 974
- test: 973

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

Editors of the Congressional Research Service and U.S. Government Accountability Office.

### Personal and Sensitive Information

None.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

CC BY 4.0

### Citation Information

```
@inproceedings{huang-etal-2021-efficient,
    title = "Efficient Attentions for Long Document Summarization",
    author = "Huang, Luyang  and
      Cao, Shuyang  and
      Parulian, Nikolaus  and
      Ji, Heng  and
      Wang, Lu",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.112",
    doi = "10.18653/v1/2021.naacl-main.112",
    pages = "1419--1436",
    abstract = "The quadratic computational and memory complexities of large Transformers have limited their scalability for long document summarization. In this paper, we propose Hepos, a novel efficient encoder-decoder attention with head-wise positional strides to effectively pinpoint salient information from the source. We further conduct a systematic study of existing efficient self-attentions. Combined with Hepos, we are able to process ten times more tokens than existing models that use full attentions. For evaluation, we present a new dataset, GovReport, with significantly longer documents and summaries. Results show that our models produce significantly higher ROUGE scores than competitive comparisons, including new state-of-the-art results on PubMed. Human evaluation also shows that our models generate more informative summaries with fewer unfaithful errors.",
}
```
