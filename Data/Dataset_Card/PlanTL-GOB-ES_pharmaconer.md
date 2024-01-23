---
annotations_creators:
- expert-generated
language:
- es
tags:
- biomedical
- clinical
- spanish
multilinguality:
- monolingual
task_categories:
- token-classification
task_ids:
- named-entity-recognition
license:
- cc-by-4.0
---

# PharmaCoNER

## Dataset Description

Manually classified collection of Spanish clinical case studies.

- **Homepage:** [zenodo](https://zenodo.org/record/4270158)
- **Paper:** [PharmaCoNER: Pharmacological Substances, Compounds and proteins Named Entity Recognition track](https://aclanthology.org/D19-5701/)
- **Point of Contact:** encargo-pln-life@bsc.es

### Dataset Summary

Manually classified collection of clinical case studies derived from the Spanish Clinical Case Corpus (SPACCC), an open access electronic library that gathers Spanish medical publications from [SciELO](https://scielo.org/).

The PharmaCoNER corpus contains a total of 396,988 words and 1,000 clinical cases that have been randomly sampled into 3 subsets.
The training set contains 500 clinical cases, while the development and test sets contain 250 clinical cases each.
In terms of training examples, this translates to a total of 8129, 3787 and 3952 annotated sentences in each set.
The original dataset is distributed in [Brat](https://brat.nlplab.org/standoff.html) format.

The annotation of the entire set of entity mentions was carried out by domain experts.
It includes the following 4 entity types: NORMALIZABLES, NO_NORMALIZABLES, PROTEINAS and UNCLEAR.

This dataset was designed for the PharmaCoNER task, sponsored by [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

For further information, please visit [the official website](https://temu.bsc.es/pharmaconer/).

### Supported Tasks

Named Entity Recognition (NER)

### Languages

- Spanish (es)

### Directory Structure

* README.md
* pharmaconer.py
* dev-set_1.1.conll
* test-set_1.1.conll
* train-set_1.1.conll

## Dataset Structure

### Data Instances

Three four-column files, one for each split.

### Data Fields

Every file has four columns:
* 1st column: Word form or punctuation symbol 
* 2nd column: Original BRAT file name
* 3rd column: Spans
* 4th column: IOB tag

#### Example
<pre>
La                S0004-06142006000900008-1  123_125  O
paciente          S0004-06142006000900008-1  126_134  O
tenía             S0004-06142006000900008-1  135_140  O
antecedentes      S0004-06142006000900008-1  141_153  O
de                S0004-06142006000900008-1  154_156  O
hipotiroidismo    S0004-06142006000900008-1  157_171  O
,                 S0004-06142006000900008-1  171_172  O
hipertensión      S0004-06142006000900008-1  173_185  O
arterial          S0004-06142006000900008-1  186_194  O
en                S0004-06142006000900008-1  195_197  O
tratamiento       S0004-06142006000900008-1  198_209  O
habitual          S0004-06142006000900008-1  210_218  O
con               S0004-06142006000900008-1  219-222  O
atenolol          S0004-06142006000900008-1  223_231  B-NORMALIZABLES
y                 S0004-06142006000900008-1  232_233  O
enalapril         S0004-06142006000900008-1  234_243  B-NORMALIZABLES
</pre>

### Data Splits

| Split | Size |
| ------------- | ------------- |
| `train`  | 8,129  |
| `dev`  | 3,787  |
| `test`  | 3,952  |

## Dataset Creation

### Curation Rationale

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines.

### Source Data

#### Initial Data Collection and Normalization

Manually classified collection of clinical case report sections. The clinical cases were not restricted to a single medical discipline, covering a variety of medical disciplines, including oncology, urology, cardiology, pneumology or infectious diseases. This is key to cover a diverse set of chemicals and drugs.

#### Who are the source language producers?

Humans, there is no machine generated data.

### Annotations

#### Annotation process

The annotation process of the PharmaCoNER corpus was inspired by previous annotation schemes and corpora used for the BioCreative CHEMDNER and GPRO tracks, translating the guidelines used for these tracks into Spanish and adapting them to the characteristics and needs of clinically oriented documents by modifying the annotation criteria and rules to cover medical information needs. This adaptation was carried out in collaboration with practicing physicians and medicinal chemistry experts. The adaptation, translation and refinement of the guidelines was done on a sample set of the SPACCC corpus and linked to an iterative process of annotation consistency analysis through interannotator agreement (IAA) studies until a high annotation quality in terms of IAA was reached.

#### Who are the annotators?

Practicing physicians and medicinal chemistry experts.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This corpus contributes to the development of medical language models in Spanish.

### Discussion of Biases

[N/A]

## Additional Information

### Dataset Curators 
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es). 

For further information, send an email to (plantl-gob-es@bsc.es).

This work was funded by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://avancedigital.mineco.gob.es/en-us/Paginas/index.aspx) within the framework of the [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

### Licensing information
This work is licensed under [CC Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) License.

Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Citation Information

```bibtex
@inproceedings{,
    title = "PharmaCoNER: Pharmacological Substances, Compounds and proteins Named Entity Recognition track",
    author = "Gonzalez-Agirre, Aitor  and
      Marimon, Montserrat  and
      Intxaurrondo, Ander  and
      Rabal, Obdulia  and
      Villegas, Marta  and
      Krallinger, Martin",
    booktitle = "Proceedings of The 5th Workshop on BioNLP Open Shared Tasks",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5701",
    doi = "10.18653/v1/D19-5701",
    pages = "1--10",
}
```
### Contributions

[N/A]

