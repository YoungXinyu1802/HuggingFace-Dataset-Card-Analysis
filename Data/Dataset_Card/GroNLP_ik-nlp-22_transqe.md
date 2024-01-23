---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
- machine-generated
language:
- en
- nl
license:
- apache-2.0
multilinguality:
- translation
size_categories:
- unknown
source_datasets:
- extended|esnli
task_categories:
- text-classification
task_ids:
- natural-language-inference
pretty_name: iknlp22-transqe
tags:
- quality-estimation
---
# Dataset Card for IK-NLP-22 Project 3: Translation Quality-driven Data Selection for Natural Language Inference
## Table of Contents
- [Dataset Card for IK-NLP-22 Project 3: Translation Quality-driven Data Selection for Natural Language Inference](#dataset-card-for-ik-nlp-22-project-3-translation-quality-driven-data-selection-for-natural-language-inference)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Splits](#data-splits)
    - [Data Example](#data-example)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
## Dataset Description
- **Source:** [Github](https://github.com/OanaMariaCamburu/e-SNLI)
- **Point of Contact:** [Gabriele Sarti](mailto:ik-nlp-course@rug.nl)
### Dataset Summary
This dataset contains the full [e-SNLI](https://huggingface.co/datasets/esnli) dataset, automatically translated to Dutch using the [Helsinki-NLP/opus-mt-en-nl](https://huggingface.co/Helsinki-NLP/opus-mt-en-nl) neural machine translation model. The translation of each field has been anotated with two quality estimation scores using the referenceless version of the [COMET](https://github.com/Unbabel/COMET/) metric by Unbabel.

The intended usage of this corpus is restricted to the scope of final project for the 2022 edition of the Natural Language Processing course at the Information Science Master's Degree (IK) at the University of Groningen, taught by [Arianna Bisazza](https://research.rug.nl/en/persons/arianna-bisazza) and [Gabriele Sarti](https://research.rug.nl/en/persons/gabriele-sarti), with the assistance of [Anjali Nair](https://nl.linkedin.com/in/anjalinair012).

*The e-SNLI corpus was made freely available by the authors on Github. The present dataset was created for educational purposes, and is based on the original e-SNLI dataset by Camburu et al..All rights of the present contents are attributed to the original authors.*

### Languages
The language data of this corpus is in English (BCP-47 `en`) and Dutch (BCP-47 `nl`).
## Dataset Structure
### Data Instances

The dataset contains a single condiguration by default, named `plain_text`, with the three original splits `train`, `validation` and `test`. Every split contains the following fields:

| **Field** | **Description** |
|------------|-----------------------------|
|`premise_en`| The original English premise.|
|`premise_nl`| The premise automatically translated to Dutch.|
|`hypothesis_en`| The original English hypothesis.|
|`hypothesis_nl`| The hypothesis automatically translated to Dutch.|
|`label`| The label of the data instance (0 for entailment, 1 for neutral, 2 for contradiction).|
|`explanation_1_en`| The first explanation for the assigned label in English.|
|`explanation_1_nl`| The first explanation automatically translated to Dutch.|
|`explanation_2_en`| The second explanation for the assigned label in English.|
|`explanation_2_nl`| The second explanation automatically translated to Dutch.|
|`explanation_3_en`| The third explanation for the assigned label in English.|
|`explanation_3_nl`| The third explanation automatically translated to Dutch.|
|`da_premise`| The quality estimation produced by the `wmt20-comet-qe-da` model for the premise translation.|
|`da_hypothesis`| The quality estimation produced by the `wmt20-comet-qe-da` model for the hypothesis translation.|
|`da_explanation_1`| The quality estimation produced by the `wmt20-comet-qe-da` model for the first explanation translation.|
|`da_explanation_2`| The quality estimation produced by the `wmt20-comet-qe-da` model for the second explanation translation.|
|`da_explanation_3`| The quality estimation produced by the `wmt20-comet-qe-da` model for the third explanation translation.|
|`mqm_premise`| The quality estimation produced by the `wmt21-comet-qe-mqm` model for the premise translation.|
|`mqm_hypothesis`| The quality estimation produced by the `wmt21-comet-qe-mqm` model for the hypothesis translation.|
|`mqm_explanation_1`| The quality estimation produced by the `wmt21-comet-qe-mqm` model for the first explanation translation.|
|`mqm_explanation_2`| The quality estimation produced by the `wmt21-comet-qe-mqm` model for the second explanation translation.|
|`mqm_explanation_3`| The quality estimation produced by the `wmt21-comet-qe-mqm` model for the third explanation translation.|

Explanation 2 and 3 and related quality estimation scores are only present in the `validation` and `test` splits.

### Data Splits

|       config| train   | validation | test |
|------------:|---------|------------|------|
|`plain_text` | 549'367 | 9842       | 9824 |

For your analyses, use the amount of data that is the most reasonable for your computational setup. The more, the better.

### Data Example

The following is an example of entry 2000 taken from the `test` split:

```json
{
  "premise_en": "A young woman wearing a yellow sweater and black pants is ice skating outdoors.",
  "premise_nl": "Een jonge vrouw met een gele trui en zwarte broek schaatst buiten.",
  "hypothesis_en": "a woman is practicing for the olympics",
  "hypothesis_nl": "een vrouw oefent voor de Olympische Spelen",
  "label": 1,
  "explanation_1_en": "You can not infer it's for the Olympics.",
  "explanation_1_nl": "Het is niet voor de Olympische Spelen.",
  "explanation_2_en": "Just because a girl is skating outdoors does not  mean she is practicing for the Olympics.",
  "explanation_2_nl": "Alleen omdat een meisje buiten schaatst betekent niet dat ze oefent voor de Olympische Spelen.",
  "explanation_3_en": "Ice skating doesn't imply practicing for the olympics.",
  "explanation_3_nl": "Schaatsen betekent niet oefenen voor de Olympische Spelen.",
  "da_premise": "0.6099",
  "mqm_premise": "0.1298",
  "da_hypothesis": "0.8504",
  "mqm_hypothesis": "0.1521",
  "da_explanation_1": "0.0001",
  "mqm_explanation_1": "0.1237",
  "da_explanation_2": "0.4017",
  "mqm_explanation_2": "0.1467",
  "da_explanation_3": "0.6069",
  "mqm_explanation_3": "0.1389"
}
```

### Dataset Creation

The dataset was created through the following steps:

- Translating every field of the original e-SNLI corpus to Dutch using the [Helsinki-NLP/opus-mt-en-nl](https://huggingface.co/Helsinki-NLP/opus-mt-en-nl) neural machine translation model.

- Annotating the quality estimation of the translations with two referenceless versions of the [COMET](https://github.com/Unbabel/COMET/) metric by Unbabel.

## Additional Information

### Dataset Curators

For problems on this 🤗 Datasets version, please contact us at [ik-nlp-course@rug.nl](mailto:ik-nlp-course@rug.nl).

### Licensing Information

The dataset is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.html).

### Citation Information

Please cite the authors if you use these corpora in your work:

```bibtex
@incollection{NIPS2018_8163,
    title = {e-SNLI: Natural Language Inference with Natural Language Explanations},
    author = {Camburu, Oana-Maria and Rockt\"{a}schel, Tim and Lukasiewicz, Thomas and Blunsom, Phil},
    booktitle = {Advances in Neural Information Processing Systems 31},
    editor = {S. Bengio and H. Wallach and H. Larochelle and K. Grauman and N. Cesa-Bianchi and R. Garnett},
    pages = {9539--9549},
    year = {2018},
    publisher = {Curran Associates, Inc.},
    url = {http://papers.nips.cc/paper/8163-e-snli-natural-language-inference-with-natural-language-explanations.pdf}
}
```