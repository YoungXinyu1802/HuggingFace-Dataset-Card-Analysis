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

# CANTEMIST

## Dataset Description

Manually classified collection of Spanish oncological clinical case reports.

- **Homepage:** [zenodo](https://zenodo.org/record/3978041)
- **Paper:** [Named Entity Recognition, Concept Normalization and Clinical Coding: Overview of the Cantemist Track for Cancer Text Mining in Spanish, Corpus, Guidelines, Methods and Results](https://www.researchgate.net/profile/Antonio-Miranda-Escalada-2/publication/352786464_Named_Entity_Recognition_Concept_Normalization_and_Clinical_Coding_Overview_of_the_Cantemist_Track_for_Cancer_Text_Mining_in_Spanish_Corpus_Guidelines_Methods_and_Results/links/60d98a3b458515d6fbe382d8/Named-Entity-Recognition-Concept-Normalization-and-Clinical-Coding-Overview-of-the-Cantemist-Track-for-Cancer-Text-Mining-in-Spanish-Corpus-Guidelines-Methods-and-Results.pdf)
- **Point of Contact:** encargo-pln-life@bsc.es

### Dataset Summary

Collection of 1301 oncological clinical case reports written in Spanish, with tumor morphology mentions manually annotated and mapped by clinical experts to a controlled terminology. Every tumor morphology mention is linked to an eCIE-O code (the Spanish equivalent of ICD-O).

The training subset contains 501 documents, the development subsets 500, and the test subset 300. The original dataset is distributed in [Brat](https://brat.nlplab.org/standoff.html) format.

This dataset was designed for the CANcer TExt Mining Shared Task, sponsored by [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

For further information, please visit [the official website](https://temu.bsc.es/cantemist/).

### Supported Tasks

Named Entity Recognition (NER)

### Languages

- Spanish (es)

### Directory Structure

* README.md
* cantemist.py
* train.conll
* dev.conll
* test.conll

## Dataset Structure

### Data Instances

Three four-column files, one for each split.

### Data Fields

Every file has 4 columns:
* 1st column: Word form or punctuation symbol
* 2nd column: Original BRAT file name
* 3rd column: Spans
* 4th column: IOB tag

#### Example

<pre>
El                  cc_onco101    662_664    O
informe             cc_onco101    665_672    O
HP                  cc_onco101    673_675    O
es                  cc_onco101    676_678    O
compatible          cc_onco101    679_689    O
con                 cc_onco101    690_693    O
adenocarcinoma      cc_onco101    694_708    B-MORFOLOGIA_NEOPLASIA
moderadamente       cc_onco101    709_722    I-MORFOLOGIA_NEOPLASIA
diferenciado        cc_onco101    723_735    I-MORFOLOGIA_NEOPLASIA
que                 cc_onco101    736_739    O
afecta              cc_onco101    740_746    O
a                   cc_onco101    747_748    O
grasa               cc_onco101    749_754    O
peripancreática     cc_onco101    755_770    O
sobrepasando        cc_onco101    771_783    O
la                  cc_onco101    784_786    O
serosa              cc_onco101    787_793    O
,                   cc_onco101    793_794    O
infiltración        cc_onco101    795_807    O
perineural          cc_onco101    808_818    O
.                   cc_onco101    818_819    O
</pre>

### Data Splits

| Split | Size |
| ------------- | ------------- |
| `train`  | 19,397  |
| `dev`  | 18,165  |
| `test`  | 11,168  |

## Dataset Creation

### Curation Rationale

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines.

### Source Data

#### Initial Data Collection and Normalization

The selected clinical case reports are fairly similar to hospital health records. To increase the usefulness and practical relevance of the CANTEMIST corpus, we selected clinical cases affecting all genders and that comprised most ages (from children to the elderly) and of various complexity levels (solid tumors, hemato-oncological malignancies, neuroendocrine cancer...).

The CANTEMIST cases include clinical signs and symptoms, personal and family history, current illness, physical examination, complementary tests (blood tests, imaging, pathology), diagnosis, treatment (including adverse effects of chemotherapy), evolution and outcome.

#### Who are the source language producers?

Humans, there is no machine generated data.

### Annotations

#### Annotation process

The manual annotation of the Cantemist corpus was performed by clinical experts following the Cantemist guidelines (for more detail refer to this [paper](http://ceur-ws.org/Vol-2664/cantemist_overview.pdf)). These guidelines contain rules for annotating morphology neoplasms in Spanish oncology clinical cases, as well as for mapping these annotations to eCIE-O.

A medical doctor was regularly consulted by annotators (scientists with PhDs on cancer-related subjects) for the most difficult pathology expressions. This same doctor periodically checked a random selection of annotated clinical records and these annotations were compared and discussed with the annotators. To normalize a selection of very complex cases, MD specialists in pathology from one of the largest university hospitals in Spain were consulted.

#### Who are the annotators?

Clinical experts.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This corpus contributes to the development of medical language models in Spanish.

### Discussion of Biases

Not applicable.

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
@article{cantemist,
  title={Named Entity Recognition, Concept Normalization and Clinical Coding: Overview of the Cantemist Track for Cancer Text Mining in Spanish, Corpus, Guidelines, Methods and Results.},
  author={Miranda-Escalada, Antonio and Farr{\'e}, Eul{\`a}lia and Krallinger, Martin},
  journal={IberLEF@ SEPLN},
  pages={303--323},
  year={2020}
}
```

### Contributions

[N/A]
