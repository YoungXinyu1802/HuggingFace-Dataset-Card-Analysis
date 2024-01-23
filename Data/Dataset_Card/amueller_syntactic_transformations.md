---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
- de
license:
- mit
multilinguality:
- 2 languages
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- syntactic-evaluation
task_ids:
- syntactic-transformations
---

# Dataset Card for syntactic_transformations

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
- **Repository:** https://github.com/sebschu/multilingual-transformations
- **Paper:** [Coloring the Blank Slate: Pre-training Imparts a Hierarchical Inductive Bias to Sequence-to-sequence Models](https://aclanthology.org/2022.findings-acl.106/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Aaron Mueller](mailto:amueller@jhu.edu)

### Dataset Summary

This contains the the syntactic transformations datasets used in [Coloring the Blank Slate: Pre-training Imparts a Hierarchical Inductive Bias to Sequence-to-sequence Models](https://aclanthology.org/2022.findings-acl.106/). It consists of English and German question formation and passivization transformations. This dataset also contains zero-shot cross-lingual transfer training and evaluation data.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

English and German.

## Dataset Structure

### Data Instances

A typical data point consists of a source sequence ("src"), a target sequence ("tgt"), and a task prefix ("prefix"). The prefix indicates whether a given sequence should be kept the same in the target (indicated by the "decl:" prefix) or transformed into a question/passive ("quest:"/"passiv:", respectively). An example follows:

{"src": "the yak has entertained the walruses that have amused the newt.",
"tgt": "has the yak entertained the walruses that have amused the newt?",
"prefix": "quest: "
}

### Data Fields

- src: the original source sequence.
- tgt: the transformed target sequence.
- prefix: indicates which transformation to perform to map from the source to target sequences.

### Data Splits

The datasets are split into training, dev, test, and gen ("generalization") sets. The training sets are for fine-tuning the model. The dev and test sets are for evaluating model abilities on in-domain transformations. The generalization sets are for evaluating the inductive biases of the model.

NOTE: for the zero-shot cross-lingual transfer datasets, the generalization sets are split into in-domain and out-of-domain syntactic structures. For in-domain transformations, use "gen_rc_o" for question formation or "gen_pp_o" for passivization. For out-of-domain transformations, use "gen_rc_s" for question formation or "gen_pp_s" for passivization.

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]