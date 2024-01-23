---
annotations_creators:
- crowdsourced
- expert-generated
- machine-generated
language_creators:
- found
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
- 1K<n<10K
source_datasets:
- original
task_categories:
- token-classification
task_ids: []
paperswithcode_id: numeric-fused-head
pretty_name: Numeric Fused Heads
configs:
- identification
- resolution
tags:
- fused-head-identification
dataset_info:
- config_name: identification
  features:
  - name: tokens
    sequence: string
  - name: start_index
    dtype: int32
  - name: end_index
    dtype: int32
  - name: label
    dtype:
      class_label:
        names:
          '0': neg
          '1': pos
  splits:
  - name: train
    num_bytes: 22290345
    num_examples: 165606
  - name: test
    num_bytes: 68282
    num_examples: 500
  - name: validation
    num_bytes: 2474528
    num_examples: 18401
  download_size: 24407520
  dataset_size: 24833155
- config_name: resolution
  features:
  - name: tokens
    sequence: string
  - name: line_indices
    sequence: int32
  - name: head
    sequence: string
  - name: speakers
    sequence: string
  - name: anchors_indices
    sequence: int32
  splits:
  - name: train
    num_bytes: 19766437
    num_examples: 7412
  - name: test
    num_bytes: 2743071
    num_examples: 1000
  - name: validation
    num_bytes: 2633549
    num_examples: 1000
  download_size: 24923403
  dataset_size: 25143057
---

# Dataset Card for Numeric Fused Heads

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

- **Homepage:** [The Numeric Fused-Head demo](https://nlp.biu.ac.il/~lazary/fh/)
- **Repository:** [Github Repo](https://github.com/yanaiela/num_fh)
- **Paper:** [Where’s My Head? Definition, Dataset and Models for Numeric Fused-Heads Identification and Resolution](https://www.mitpressjournals.org/doi/full/10.1162/tacl_a_00280)
- **Leaderboard:** [NLP Progress](http://nlpprogress.com/english/missing_elements.html)
- **Point of Contact:** [Yanai Elazar](https://yanaiela.github.io), [Yoav Goldberg](https://www.cs.bgu.ac.il/~yoavg/uni/)

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

- Numeric Fused Head Identification
- Numeric Fused Head Resolution

### Languages

English

## Dataset Structure

### Data Instances

## Identification

```
{
    "tokens": ["It", "’s", "a", "curious", "thing", ",", "the", "death", "of", "a", "loved", "one", "."]
    "start_index": 11
    "end_index": 12
    "label": 1
}
```

## Resolution

```
{
    "tokens": ["I", "'m", "eighty", "tomorrow", ".", "Are", "you", "sure", "?"],
    "line_indices": [0, 0, 0, 0, 0, 1, 1, 1, 1],
    "head": ["AGE"],
    "speakers": ["John Doe", "John Doe", "John Doe", "John Doe", "John Doe", "Joe Bloggs", "Joe Bloggs", "Joe Bloggs", "Joe Bloggs"],
    "anchors_indices": [2]
}
```

### Data Fields

## Identification

- `tokens` - List of token strings as tokenized with [Spacy](spacy.io).
- `start_index` - Start index of the anchor.
- `end_index` - End index of the anchor.
- `label` - "pos" or "neg" depending on whether this example contains a numeric fused head.

## Resolution

- `tokens` - List of token strings as tokenized with [Spacy](spacy.io)
- `line_indices` - List of indices indicating line number (one for each token)
- `head` -  Reference to the missing head. If the head exists elsewhere in the sentence this is given as a token index.
- `speakers` - List of speaker names (one for each token)
- `anchors_indices` - Index to indicate which token is the anchor (the visible number)

### Data Splits

Train, Test, Dev

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

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

[More Information Needed]

### Licensing Information

MIT License

### Citation Information
```
@article{doi:10.1162/tacl\_a\_00280,
    author = {Elazar, Yanai and Goldberg, Yoav},
    title = {Where’s My Head? Definition, Data Set, and Models for Numeric Fused-Head Identification and Resolution},
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {7},
    number = {},
    pages = {519-535},
    year = {2019},
    doi = {10.1162/tacl\_a\_00280},
}
```

### Contributions

Thanks to [@ghomasHudson](https://github.com/ghomasHudson) for adding this dataset.