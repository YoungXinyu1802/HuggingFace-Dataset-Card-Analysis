---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- extended|wikipedia
task_categories:
- text-classification
task_ids: []
paperswithcode_id: feverous
pretty_name: FEVEROUS
tags:
- knowledge-verification
---
# Dataset Card for FEVEROUS

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

- **Homepage:** https://fever.ai/dataset/feverous.html
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [FEVEROUS: Fact Extraction and VERification Over Unstructured and Structured information](https://arxiv.org/abs/2106.05707)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

With billions of individual pages on the web providing information on almost every conceivable topic, we should have
the ability to collect facts that answer almost every conceivable question. However, only a small fraction of this
information is contained in structured sources (Wikidata, Freebase, etc.) – we are therefore limited by our ability to
transform free-form text to structured knowledge. There is, however, another problem that has become the focus of a lot
of recent research and media coverage: false information coming from unreliable sources.

The FEVER workshops are a venue for work in verifiable knowledge extraction and to stimulate progress in this direction.

FEVEROUS (Fact Extraction and VERification Over Unstructured and Structured information) is a fact
verification dataset which consists of 87,026 verified claims. Each claim is annotated with evidence in the form of
sentences and/or cells from tables in Wikipedia, as well as a label indicating whether this evidence supports, refutes,
or does not provide enough information to reach a verdict. The dataset also contains annotation metadata such as
annotator actions (query keywords, clicks on page, time signatures), and the type of challenge each claim poses.

### Supported Tasks and Leaderboards

The task is verification of textual claims against textual sources.

When compared to textual entailment (TE)/natural language inference, the key difference is that in these tasks the
passage to verify each claim is given, and in recent years it typically consists a single sentence, while in
verification systems it is retrieved from a large set of documents in order to form the evidence.

### Languages

The dataset is in English (`en`).

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 187.82 MB
- **Size of the generated dataset:** 123.25 MB
- **Total amount of disk used:** 311.07 MB

An example of 'wikipedia_pages' looks as follows:
```
{'id': 24435,
 'label': 1,
 'claim': 'Michael Folivi competed with ten teams from 2016 to 2021, appearing in 54 games and making seven goals in total.',
 'evidence': [{'content': ['Michael Folivi_cell_1_2_0',
    'Michael Folivi_cell_1_7_0',
    'Michael Folivi_cell_1_8_0',
    'Michael Folivi_cell_1_9_0',
    'Michael Folivi_cell_1_12_0'],
   'context': [['Michael Folivi_title',
     'Michael Folivi_section_4',
     'Michael Folivi_header_cell_1_0_0'],
    ['Michael Folivi_title',
     'Michael Folivi_section_4',
     'Michael Folivi_header_cell_1_0_0'],
    ['Michael Folivi_title',
     'Michael Folivi_section_4',
     'Michael Folivi_header_cell_1_0_0'],
    ['Michael Folivi_title',
     'Michael Folivi_section_4',
     'Michael Folivi_header_cell_1_0_0'],
    ['Michael Folivi_title',
     'Michael Folivi_section_4',
     'Michael Folivi_header_cell_1_0_0']]},
  {'content': ['Michael Folivi_cell_0_13_1',
    'Michael Folivi_cell_0_14_1',
    'Michael Folivi_cell_0_15_1',
    'Michael Folivi_cell_0_16_1',
    'Michael Folivi_cell_0_18_1'],
   'context': [['Michael Folivi_title',
     'Michael Folivi_header_cell_0_13_0',
     'Michael Folivi_header_cell_0_11_0'],
    ['Michael Folivi_title',
     'Michael Folivi_header_cell_0_14_0',
     'Michael Folivi_header_cell_0_11_0'],
    ['Michael Folivi_title',
     'Michael Folivi_header_cell_0_15_0',
     'Michael Folivi_header_cell_0_11_0'],
    ['Michael Folivi_title',
     'Michael Folivi_header_cell_0_16_0',
     'Michael Folivi_header_cell_0_11_0'],
    ['Michael Folivi_title',
     'Michael Folivi_header_cell_0_18_0',
     'Michael Folivi_header_cell_0_11_0']]}],
 'annotator_operations': [{'operation': 'start',
   'value': 'start',
   'time': 0.0},
  {'operation': 'Now on', 'value': '?search=', 'time': 0.78},
  {'operation': 'search', 'value': 'Michael Folivi', 'time': 78.101},
  {'operation': 'Now on', 'value': 'Michael Folivi', 'time': 78.822},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_1_2_0',
   'time': 96.202},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_1_7_0',
   'time': 96.9},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_1_8_0',
   'time': 97.429},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_1_9_0',
   'time': 97.994},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_1_12_0',
   'time': 99.02},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_0_13_1',
   'time': 106.108},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_0_14_1',
   'time': 106.702},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_0_15_1',
   'time': 107.423},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_0_16_1',
   'time': 108.186},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_0_17_1',
   'time': 108.788},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_header_cell_0_17_0',
   'time': 108.8},
  {'operation': 'Highlighting',
   'value': 'Michael Folivi_cell_0_18_1',
   'time': 109.469},
  {'operation': 'Highlighting deleted',
   'value': 'Michael Folivi_cell_0_17_1',
   'time': 124.28},
  {'operation': 'Highlighting deleted',
   'value': 'Michael Folivi_header_cell_0_17_0',
   'time': 124.293},
  {'operation': 'finish', 'value': 'finish', 'time': 141.351}],
 'expected_challenge': '',
 'challenge': 'Numerical Reasoning'}
```

### Data Fields

The data fields are the same among all splits.

- `id` (int): ID of the sample.
- `label` (ClassLabel): Annotated label for the claim. Can be one of {"SUPPORTS", "REFUTES", "NOT ENOUGH INFO"}.
- `claim` (str): Text of the claim.
- `evidence` (list of dict): Evidence sets (at maximum three). Each set consists of dictionaries with two fields:
  - `content` (list of str): List of element IDs serving as the evidence for the claim. Each element ID is in the format
      `"[PAGE ID]_[EVIDENCE TYPE]_[NUMBER ID]"`, where `[EVIDENCE TYPE]` can be: `sentence`, `cell`, `header_cell`,
      `table_caption`, `item`.
  - `context` (list of list of str): List (for each element ID in `content`) of a list of Wikipedia elements that are
      automatically associated with that element ID and serve as context. This includes an article's title, relevant
      sections (the section and sub-section(s) the element is located in), and for cells the closest row and column
      header (multiple row/column headers if they follow each other).
- `annotator_operations` (list of dict): List of operations an annotator used to find the evidence and reach a verdict,
    given the claim. Each element in the list is a dictionary with the fields:
  - `operation` (str): Operation name. Any of the following:
    - `start`, `finish`: Annotation started/finished. The value is the name of the operation.
    - `search`: Annotator used the Wikipedia search function. The value is the entered search term or the term selected
        from the automatic suggestions. If the annotator did not select any of the suggestions but instead went into
        advanced search, the term is prefixed with "contains...".
    - `hyperlink`: Annotator clicked on a hyperlink in the page. The value is the anchor text of the hyperlink.
    - `Now on`: The page the annotator has landed after a search or a hyperlink click. The value is the PAGE ID.
    - `Page search`: Annotator search on a page. The value is the search term.
    - `page-search-reset`: Annotator cleared the search box. The value is the name of the operation.
    - `Highlighting`, `Highlighting deleted`: Annotator selected/unselected an element on the page. The value is
        `ELEMENT ID`.
    - `back-button-clicked`: Annotator pressed the back button. The value is the name of the operation.
  - `value` (str): Value associated with the operation.
  - `time` (float): Time in seconds from the start of the annotation.
- `expected_challenge` (str): The challenge the claim generator selected will be faced when verifying the claim, one
    out of the following: `Numerical Reasoning`, `Multi-hop Reasoning`, `Entity Disambiguation`,
    `Combining Tables and Text`, `Search terms not in claim`, `Other`.
- `challenge` (str): Main challenge to verify the claim, one out of the following: `Numerical Reasoning`,
    `Multi-hop Reasoning`, `Entity Disambiguation`, `Combining Tables and Text`, `Search terms not in claim`, `Other`.

### Data Splits

|                    | train | validation | test |
|--------------------|------:|-----------:|-----:|
| Number of examples | 71291 |       7890 | 7845 |

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

```
These data annotations incorporate material from Wikipedia, which is licensed pursuant to the Wikipedia Copyright Policy. These annotations are made available under the license terms described on the applicable Wikipedia article pages, or, where Wikipedia license terms are unavailable, under the Creative Commons Attribution-ShareAlike License (version 3.0), available at http://creativecommons.org/licenses/by-sa/3.0/ (collectively, the â€œLicense Termsâ€). You may not use these files except in compliance with the applicable License Terms.
```

### Citation Information

If you use this dataset, please cite:
```bibtex
@inproceedings{Aly21Feverous,
    author = {Aly, Rami and Guo, Zhijiang and Schlichtkrull, Michael Sejr and Thorne, James and Vlachos, Andreas and Christodoulopoulos, Christos and Cocarascu, Oana and Mittal, Arpit},
    title = {{FEVEROUS}: Fact Extraction and {VERification} Over Unstructured and Structured information},
    eprint={2106.05707},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    year = {2021}
}
```

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
