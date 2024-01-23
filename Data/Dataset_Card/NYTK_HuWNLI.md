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
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: HuWNLI
size_categories:
- unknown
source_datasets:
- extended|other
task_categories:
- structure-prediction
task_ids:
- coreference-resolution
---

# Dataset Card for HuWNLI
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
[HuWNLI dataset](https://github.com/nytud/HuWNLI)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**
[lnnoemi](mailto:ligeti-nagy.noemi@nytud.hu)

### Dataset Summary

This is the dataset card for the Hungarian translation of the Winograd schemata formatted as an inference task. A Winograd schema is a pair of sentences that differ in only one or two words and that contain an ambiguity that is resolved in opposite ways in the two sentences and requires the use of world knowledge and reasoning for its resolution (Levesque et al. 2012). This dataset is also part of the Hungarian Language Understanding Evaluation Benchmark Kit [HuLU](hulu.nlp.nytud.hu). The corpus was created by translating and manually curating the original English Winograd schemata. The NLI format was created by replacing the ambiguous pronoun with each possible referent (the method is described in GLUE's paper, Wang et al. 2019). We extended the set of sentence pairs derived from the schemata by the translation of the sentence pairs that - together with the Winograd schema sentences - build up the WNLI dataset of GLUE. 

### Languages

The BCP-47 code for Hungarian, the only represented language in this dataset, is hu-HU. 

## Dataset Structure

### Data Instances

For each instance, there is an orig_id, an id, two sentences and a label. 

An example:

```

{"orig_id": "4",
 "id": "4",
 "sentence1": "A férfi nem tudta felemelni a fiát, mert olyan nehéz volt.",
 "sentence2": "A fia nehéz volt.",
 "Label": "1"
}

```

### Data Fields
- orig_id: the original id of this sentence pair (more precisely, its English counterpart's) in GLUE's WNLI dataset;

- id: unique id of the instances;

- sentence1: the premise;

- sentence2: the hypothesis;  

- label: "1" if sentence2 is entailed by sentence1, and "0" otherwise.

### Data Splits

The data is distributed in three splits: training set (562), development set (59) and test set (134). The splits follow GLUE's WNLI's splits, but contain less instances as many sentence pairs had to be thrown away for being untranslatable to Hungarian. The train and the development set have been extended from nli sentence pairs formatted from the Hungarian translation of 6 Winograd schemata left out from the original WNLI dataset.
The test set's sentence pairs are translated from GLUE's WNLI's test set. This set was distributed without labels. 3 annotators annotated the Hungarian sentence pairs.
The test set of HuWNLI is also distributed without labels. To evaluate your model, please [contact us](mailto:ligeti-nagy.noemi@nytud.hu), or check [HuLU's website](hulu.nlp.nytud.hu) for an automatic evaluation (this feature is under construction at the moment). 

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The data is a translation of the English Winograd schemata and the additional sentence pairs of GLUE's WNLI. Each schema and sentence pair was translated by a human translator. Each schema was manually curated by a linguistic expert. The schemata were transformed into nli format by a linguistic expert.

During the adaption method, we found two erroneous labels in GLUE's WNLI's train set (id 347 and id 464). We corrected them in our dataset.


## Additional Information

Average human performance on the test set is 92,78% (accuracy).

### Licensing Information

HuWNLI is released under the Creative Commons Attribution-ShareAlike 4.0 International License.


### Citation Information

If you use this resource or any part of its documentation, please refer to:

Ligeti-Nagy, N., Ferenczi, G., Héja, E., Jelencsik-Mátyus, K., Laki, L. J., Vadász, N., Yang, Z. Gy. and Váradi, T. (2022) HuLU: magyar nyelvű benchmark adatbázis kiépítése a neurális nyelvmodellek kiértékelése céljából [HuLU: Hungarian benchmark dataset to evaluate neural language models]. In: Berend, Gábor and Gosztolya, Gábor and Vincze, Veronika (eds), XVIII. Magyar Számítógépes Nyelvészeti Konferencia. JATEPress, Szeged. 431–446.

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

Levesque, Hector, Davis, Ernest, Morgenstern, Leora (2012) he winograd schema challenge. In: Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning.

```
@inproceedings{levesque2012winograd,
  title={The Winograd Schema Challenge},
  author={Levesque, Hector and Davis, Ernest and Morgenstern, Leora},
  booktitle={Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning},
  year={2012},
  organization={Citeseer}
}
```

### Contributions

Thanks to [lnnoemi](https://github.com/lnnoemi) for adding this dataset.