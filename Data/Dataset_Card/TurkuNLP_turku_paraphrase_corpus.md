---
YAML tags:
annotations_creators:
- expert-generated
language_creators: []
language:
- fi
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Turku Paraphrase Corpus
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
- sentence-similarity
- text2text-generation
- other
task_ids:
- semantic-similarity-classification
---

# Dataset Card for [Dataset Name]

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

- **Homepage:** https://turkunlp.org/paraphrase.html
- **Repository:** https://github.com/TurkuNLP/Turku-paraphrase-corpus
- **Paper:** https://aclanthology.org/2021.nodalida-main.29
- **Leaderboard:** Not available
- **Point of Contact:** [Jenna Kanerva, Filip Ginter](mailto:jmnybl@utu.fi,filip.ginter@gmail.com)

### Dataset Summary

The project gathered a large dataset of Finnish paraphrase pairs (over 100,000). The paraphrases are selected and classified manually, so as to minimize lexical overlap, and provide examples that are maximally structurally and lexically different. The objective is to create a dataset which is challenging and better tests the capabilities of natural language understanding. An important feature of the data is that most paraphrase pairs are distributed in their document context. The primary application for the dataset is the development and evaluation of deep language models, and representation learning in general.

Usage:
```
  from datasets import load_dataset
  dataset = load_dataset('TurkuNLP/turku_paraphrase_corpus', name="plain")
```
where `name` is one of the supported loading options: `plain`, `plain-context`, `classification`, `classification-context`, or `generation`. See Data Fields for more information. 

### Supported Tasks and Leaderboards

* Paraphrase classification
* Paraphrase generation

### Languages

Finnish

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

The dataset consist of pairs of text passages, where a typical passage is about a sentence long, however, a passage may also be longer or shorter than a sentence. Thus, each example includes two text passages (string), a manually annotated label to indicate the paraphrase type (string), and additional metadata. The dataset includes three different configurations: `plain`, `classification`, and `generation`. The `plain` configuration loads the original data without any additional preprocessing or transformations, while the `classification` configuration directly builds the data in a form suitable for training a paraphrase classifier, where each example is doubled in the data with different directions (text1, text2, label) --> (text2, text1, label) taking care of the label flipping as well if needed (paraphrases with directionality flag < or >). In the `generation` configuration, the examples are preprocessed to be directly suitable for the paraphrase generation task. In here, paraphrases not suitable for generation are discarded (negative, and highly context-dependent paraphrases), and directional paraphrases are provided so that the generation goes from more detailed passage to the more general one in order to prevent model hallucination (i.e. model learning to introduce new information). The rest of the paraphrases are provided in both directions (text1, text2, label) --> (text2, text1, label).

Each pair in the `plain` and `classification` configurations will include fields:

`id`: 
Identifier of the paraphrase pair (string)

`gem_id`:
Identifier of the paraphrase pair in the GEM dataset (string)

`goeswith`: 
Identifier of the document from which the paraphrase was extracted, can be `not available` in case the source of the paraphrase is not from document-structured data. All examples with the same `goeswith` value (other than `not available`) should be kept together in any train/dev/test split; most users won't need this  (string)

`fold`: 
0-99, data split into 100 parts respecting document boundaries, you can use this e.g. to implement crossvalidation safely as all paraphrases from one document are in one fold, most users won't need this (int)

`text1`: 
First paraphrase passage (string)

`text2`: 
Second paraphrase passage (string)

`label`: 
Manually annotated labels (string)

`binary_label`: 
Label turned into binary with values `positive` (paraphrase) and `negative` (not-paraphrase) (string)

`is_rewrite`: 
Indicator whether the example is human produced rewrite or naturally occurring paraphrase (bool)

Each pair in the `generation` config will include the same fields except `text1` and `text2` are renamed to `input` and `output` in order to indicate the generation direction. Thus the fields are: `id`, `gem_id`, `goeswith`, `fold`, `input`, `output`, `label`, `binary_label`, and `is_rewrite`

**Context**: Most (but not all) of the paraphrase pairs are identified in their document context. By default, these contexts are not included to conserve memory, but can be accessed using the configurations `plain-context` and `classification-context`. These are exactly like `plain` and `classification` with these additional fields:

`context1`: 
a dictionary with the fields `doctext` (string), `begin` (int), `end` (int). These mean that the paraphrase in `text1` was extracted from `doctext[begin:end]`. In most cases, `doctext[begin:end]` and `text1` are the exact same string, but occassionally that is not the case when e.g. intervening punctuations or other unrelated texts were "cleaned" from `text1` during annotation. In case the context is not available, `doctext` is an empty string and `beg==end==0`

`context2`: 
same as `context1` but for `text2`

### Data Splits

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

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@jmnybl](https://github.com/jmnybl) and [@fginter](https://github.com/fginter) for adding this dataset.