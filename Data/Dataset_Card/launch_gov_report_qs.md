---
annotations_creators:
- expert-generated
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
- launch/gov_report
task_categories:
- summarization
task_ids: []
pretty_name: GovReport-QS
---


# Dataset Card for GovReport-QS

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

- **Homepage:** [https://gov-report-data.github.io](https://gov-report-data.github.io)
- **Repository:** [https://github.com/ShuyangCao/hibrids_summ](https://github.com/ShuyangCao/hibrids_summ)
- **Paper:** [https://aclanthology.org/2022.acl-long.58/](https://aclanthology.org/2022.acl-long.58/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Based on the GovReport dataset, GovReport-QS additionally includes annotated question-summary hierarchies for government reports. This hierarchy proactively highlights the document structure, to further promote content engagement and comprehension.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

Two configs are available:
- **paragraph** (default): paragraph-level annotated data
- **document**: aggregated paragraph-level annotated data for the same document

To use different configs, set the `name` argument of the `load_dataset` function.

### Data Instances

#### paragraph

An example looks as follows.
```
{
    "doc_id": "GAO_123456",
    "summary_paragraph_index": 2,
    "document_sections": {
      "title": ["test docment section 1 title", "test docment section 1.1 title"],
      "paragraphs": ["test document\nsection 1 paragraphs", "test document\nsection 1.1 paragraphs"],
      "depth": [1, 2]
    },
    "question_summary_pairs": {
      "question": ["What is the test question 1?", "What is the test question 1.1?"],
      "summary": ["This is the test answer 1.", "This is the test answer 1.1"],
      "parent_pair_index": [-1, 0]
    }
}
```

#### document

An example looks as follows.
```
{
    "doc_id": "GAO_123456",
    "document_sections": {
      "title": ["test docment section 1 title", "test docment section 1.1 title"],
      "paragraphs": ["test document\nsection 1 paragraphs", "test document\nsection 1.1 paragraphs"],
      "depth": [1, 2],
      "alignment": ["h0_title", "h0_full"]
    },
    "question_summary_pairs": {
      "question": ["What is the test question 1?", "What is the test question 1.1?"],
      "summary": ["This is the test answer 1.", "This is the test answer 1.1"],
      "parent_pair_index": [-1, 0],
      "summary_paragraph_index": [2, 2]
    }
}
```

### Data Fields

#### paragraph

**Note that document_sections in this config are the sections aligned with the annotated summary paragraph.**

- `doc_id`: a `string` feature.
- `summary_paragraph_index`: a `int32` feature.
- `document_sections`: a dictionary feature containing lists of (each element corresponds to a section):
  - `title`: a `string` feature.
  - `paragraphs`: a of `string` feature, with `\n` separating different paragraphs.
  - `depth`: a `int32` feature.
- `question_summary_pairs`: a dictionary feature containing lists of (each element corresponds to a question-summary pair):
  - `question`: a `string` feature.
  - `summary`: a `string` feature.
  - `parent_pair_index`: a `int32` feature indicating which question-summary pair is the parent of the current pair. `-1` indicates that the current pair does not have parent.

#### document

**Note that document_sections in this config are the all sections in the document.**

- `id`: a `string` feature.
- `document_sections`: a dictionary feature containing lists of (each element corresponds to a section):
  - `title`: a `string` feature.
  - `paragraphs`: a of `string` feature, with `\n` separating different paragraphs.
  - `depth`: a `int32` feature.
  - `alignment`: a `string` feature. Whether the `full` section or the `title` of the section should be included when aligned with each annotated hierarchy. For example, `h0_full` indicates that the full section should be included for the hierarchy indexed `0`.
- `question_summary_pairs`: a dictionary feature containing lists of:
  - `question`: a `string` feature.
  - `summary`: a `string` feature.
  - `parent_pair_index`: a `int32` feature indicating which question-summary pair is the parent of the current pair. `-1` indicates that the current pair does not have parent. Note that the indices start from `0` for pairs with the same `summary_paragraph_index`.
  - `summary_paragraph_index`: a `int32` feature indicating which summary paragraph the question-summary pair is annotated for.

### Data Splits

#### paragraph

- train: 17519
- valid: 974
- test: 973

#### document

- train: 1371
- valid: 171
- test: 172

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
@inproceedings{cao-wang-2022-hibrids,
    title = "{HIBRIDS}: Attention with Hierarchical Biases for Structure-aware Long Document Summarization",
    author = "Cao, Shuyang  and
      Wang, Lu",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.58",
    pages = "786--807",
    abstract = "Document structure is critical for efficient information consumption. However, it is challenging to encode it efficiently into the modern Transformer architecture. In this work, we present HIBRIDS, which injects Hierarchical Biases foR Incorporating Document Structure into attention score calculation. We further present a new task, hierarchical question-summary generation, for summarizing salient content in the source document into a hierarchy of questions and summaries, where each follow-up question inquires about the content of its parent question-summary pair. We also annotate a new dataset with 6,153 question-summary hierarchies labeled on government reports. Experiment results show that our model produces better question-summary hierarchies than comparisons on both hierarchy quality and content coverage, a finding also echoed by human judges. Additionally, our model improves the generation of long-form summaries from long government reports and Wikipedia articles, as measured by ROUGE scores.",
}
```
