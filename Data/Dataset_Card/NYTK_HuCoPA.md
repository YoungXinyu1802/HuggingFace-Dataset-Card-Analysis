---
YAML tags:
annotations_creators:
- found
language_creators:
- found
- expert-generated
language:
- hu
license:
- bsd-2-clause
multilinguality:
- monolingual
pretty_name: HuCoPA
size_categories:
- unknown
source_datasets:
- extended|other
task_categories:
- other
task_ids:
- commonsense-reasoning
---

# Dataset Card for HuCoPA

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
- **Repository:**
[HuCoPA dataset](https://github.com/nytud/HuCoPA)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**
[lnnoemi](mailto:ligeti-nagy.noemi@nytud.hu)

### Dataset Summary

This is the dataset card for the Hungarian Choice of Plausible Alternatives Corpus (HuCoPA), which is also part of the Hungarian Language Understanding Evaluation Benchmark Kit [HuLU](hulu.nlp.nytud.hu). The corpus was created by translating and re-annotating the original English CoPA corpus (Roemmele et al., 2011).

### Supported Tasks and Leaderboards

'commonsense reasoning'
'question answering'

### Languages

The BCP-47 code for Hungarian, the only represented language in this dataset, is hu-HU. 

## Dataset Structure

### Data Instances

For each instance, there is an id, a premise, a question ('cause' or 'effect'), two alternatives and a label (1 or 2). 

An example:

```
{"idx": "1",
 "question": "cause",
 "label": "1",
 "premise": "A testem árnyékot vetett a fűre.",
 "choice1": "Felkelt a nap.",
 "choice2": "A füvet lenyírták."}
```

### Data Fields
- id: unique id of the instances, an integer between 1 and 1000;
- question: "cause" or "effect". It suggests what kind of causal relation are we looking for: in the case of "cause" we search for the more plausible alternative that may be a cause of the premise. In the case of "effect" we are looking for a plausible result of the premise;
- premise: the premise, a sentence;
- choice1: the first alternative, a sentence;
- choice2: the second alternative, a sentence;
- label: the number of the more plausible alternative (1 or 2).

### Data Splits

HuCoPA has 3 splits: *train*, *validation* and *test*. 

| Dataset split | Number of instances in the split |
|---------------|----------------------------------|
| train         | 400                              |
| validation    | 100                              |
| test          | 500                              |

The test data is distributed without the labels. To evaluate your model, please [contact us](mailto:ligeti-nagy.noemi@nytud.hu), or check [HuLU's website](hulu.nlp.nytud.hu) for an automatic evaluation (this feature is under construction at the moment). 

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The data is a translation of the content of the CoPA corpus. Each sentence was translated by a human translator. Each translation was manually checked and further refined by another annotator. 

### Annotations

#### Annotation process

The instances initially inherited their original labels from the CoPA dataset. Each instance was annotated by a human annotator. If the original label and the human annotator's label did not match, we manually curated the instance and assigned a final label to that. This step was necessary to ensure that the causal realationship had not been changed or lost during the translation process. 

#### Who are the annotators?
The translators were native Hungarian speakers with English proficiency. The annotators were university students with some linguistic background.

## Additional Information

The human performance on the test set is 96% (accuracy).

### Licensing Information

HuCoPA is released under the BSD 2-Clause License.

Copyright (c) 2010, University of Southern California
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


### Citation Information


If you use this resource or any part of its documentation, please refer to:

Ligeti-Nagy, N., Ferenczi, G., Héja, E., Jelencsik-Mátyus, K., Laki, L. J., Vadász, N., Yang, Z. Gy. and Váradi, T. (2022) HuLU: magyar nyelvű benchmark adatbázis
kiépítése a neurális nyelvmodellek kiértékelése céljából [HuLU: Hungarian benchmark dataset to evaluate neural language models]. In: Berend, Gábor and Gosztolya, Gábor and Vincze, Veronika (eds), XVIII. Magyar Számítógépes Nyelvészeti Konferencia. JATEPress, Szeged. 431–446.
```
@inproceedings{ligetinagy2022hulu,
  title={HuLU: magyar nyelvű benchmark adatbázis kiépítése a neurális nyelvmodellek kiértékelése céljából},
  author={Ligeti-Nagy, N. and Ferenczi, G. and Héja, E. and Jelencsik-Mátyus, K. and Laki, L. J. and Vadász, N. and Yang, Z. Gy. and Váradi, T.},
  booktitle={XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
  year={2022},
  editors = {Berend, Gábor and Gosztolya, Gábor and Vincze, Veronika},
  address = {Szeged},
  publisher = {JATEPress},
  pages = {431–446}
}
```
and to:

Roemmele, M., Bejan, C., and Gordon, A. (2011) Choice of Plausible Alternatives: An Evaluation of Commonsense Causal Reasoning. AAAI Spring Symposium on Logical Formalizations of Commonsense Reasoning, Stanford University, March 21-23, 2011.
```
@inproceedings{roemmele2011choice,
  title={Choice of plausible alternatives: An evaluation of commonsense causal reasoning},
  author={Roemmele, Melissa and Bejan, Cosmin Adrian and Gordon, Andrew S},
  booktitle={2011 AAAI Spring Symposium Series},
  year={2011},
  url={https://people.ict.usc.edu/~gordon/publications/AAAI-SPRING11A.PDF},
}
```

### Contributions

Thanks to [lnnoemi](https://github.com/lnnoemi) for adding this dataset.
