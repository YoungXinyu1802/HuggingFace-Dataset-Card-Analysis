---
YAML tags:

annotations_creators:
- expert-generated
language:
- ca
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: UD_Catalan-AnCora
size_categories: []
source_datasets: []
tags: []
task_categories:
- token-classification
task_ids:
- part-of-speech

---


# UD_Catalan-AnCora

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
- **Website:** https://github.com/UniversalDependencies/UD_Catalan-AnCora
- **Point of Contact:** [Daniel Zeman](zeman@ufal.mff.cuni.cz) 


### Dataset Summary

This dataset is composed of the annotations from the [AnCora corpus](http://clic.ub.edu/corpus/), projected on the [Universal Dependencies treebank](https://universaldependencies.org/). We use the POS annotations of this corpus as part of the [Catalan Language Understanding Benchmark (CLUB)](https://club.aina.bsc.es/).


### Supported Tasks and Leaderboards

POS tagging

### Languages

The dataset is in Catalan (`ca-CA`)

## Dataset Structure

### Data Instances

Three conllu files.

Annotations are encoded in plain text files (UTF-8, normalized to NFC, using only the LF character as line break, including an LF character at the end of file) with three types of lines:

1) Word lines containing the annotation of a word/token in 10 fields separated by single tab characters (see below).
2) Blank lines marking sentence boundaries.
3) Comment lines starting with hash (#).

### Data Fields
Word lines contain the following fields:

1) ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
2) FORM: Word form or punctuation symbol.
3) LEMMA: Lemma or stem of word form.
4) UPOS: Universal part-of-speech tag.
5) XPOS: Language-specific part-of-speech tag; underscore if not available.
6) FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available.
7) HEAD: Head of the current word, which is either a value of ID or zero (0).
8) DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.
9) DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
10) MISC: Any other annotation.
  
From: [https://universaldependencies.org](https://universaldependencies.org/guidelines.html)

### Data Splits

- ca_ancora-ud-train.conllu
- ca_ancora-ud-dev.conllu
- ca_ancora-ud-test.conllu

## Dataset Creation

### Curation Rationale
[N/A] 

### Source Data

- [UD_Catalan-AnCora](https://github.com/UniversalDependencies/UD_Catalan-AnCora)

#### Initial Data Collection and Normalization

The original annotation was done in a constituency framework as a part of the [AnCora project](http://clic.ub.edu/corpus/) at the University of Barcelona. It was converted to dependencies by the [Universal Dependencies team](https://universaldependencies.org/) and used in the CoNLL 2009 shared task. The CoNLL 2009 version was later converted to HamleDT and to Universal Dependencies.

For more information on the AnCora project, visit the [AnCora site](http://clic.ub.edu/corpus/).

To learn about the Universal Dependences, visit the webpage [https://universaldependencies.org](https://universaldependencies.org)

#### Who are the source language producers?

For more information on the AnCora corpus and its sources, visit the [AnCora site](http://clic.ub.edu/corpus/).

### Annotations

#### Annotation process

For more information on the first AnCora annotation, visit the [AnCora site](http://clic.ub.edu/corpus/).

#### Who are the annotators?

For more information on the AnCora annotation team, visit the [AnCora site](http://clic.ub.edu/corpus/).

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators



### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC Attribution 4.0 International License</a>.

### Citation Information

The following paper must be cited when using this corpus:

Taulé, M., M.A. Martí, M. Recasens (2008) 'Ancora: Multilevel Annotated Corpora for Catalan and Spanish', Proceedings of 6th International Conference on Language Resources and Evaluation. Marrakesh (Morocco).

To cite the Universal Dependencies project:

Rueter, J. (Creator), Erina, O. (Contributor), Klementeva, J. (Contributor), Ryabov, I. (Contributor), Tyers, F. M. (Contributor), Zeman, D. (Contributor), Nivre, J. (Creator) (15 Nov 2020). Universal Dependencies version 2.7 Erzya JR. Universal Dependencies Consortium. 



