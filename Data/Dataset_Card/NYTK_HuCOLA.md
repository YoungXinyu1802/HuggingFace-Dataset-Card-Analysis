---
YAML tags:
annotations_creators:
- expert-generated
language_creators:
- found
language:
- hu
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: HuCOLA
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
- summarization
- text-simplification
---
# Dataset Card for HuCOLA

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
[HuCOLA dataset](https://github.com/nytud/HuCOLA)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**
[lnnoemi](mailto:ligeti-nagy.noemi@nytud.hu)

### Dataset Summary

This is the dataset card for the Hungarian Corpus of Linguistic Acceptability (HuCOLA), which is also part of the Hungarian Language Understanding Evaluation Benchmark Kit [HuLU](hulu.nlp.nytud.hu).

### Supported Tasks and Leaderboards




### Languages

The BCP-47 code for Hungarian, the only represented language in this dataset, is hu-HU. 

## Dataset Structure

### Data Instances

For each instance, there is aN id, a sentence and a label.

An example:

```
{"Sent_id": "dev_0",
 "Sent": "A földek eláradtak.",
 "Label": "0"}
```

### Data Fields
- Sent_id: unique id of the instances, an integer between 1 and 1000;
- Sent: a Hungarian sentence;
- label: '0' for wrong, '1' for good sentences.

### Data Splits

HuCOLA has 3 splits: *train*, *validation* and *test*. 

| Dataset split | Number of sentences in the split | Proportion of the split
|---------------|----------------------------------| ---------|
| train         | 7276                              | 80%|
| validation    | 900                             |10%|
| test          | 900                              |10%|

The test data is distributed without the labels. To evaluate your model, please [contact us](mailto:ligeti-nagy.noemi@nytud.hu), or check [HuLU's website](hulu.nlp.nytud.hu) for an automatic evaluation (this feature is under construction at the moment). The evaluation metric is Matthew's correlation coefficient. 

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The data was collected by two human annotators from 3 main linguistic books on Hungarian language: 
 
 - Kiefer Ferenc (ed.) (1992), Strukturális magyar nyelvtan 1. Mondattan. Budapest, Akadémiai Kiadó.
 - Alberti, Gábor and Laczkó, Tibor (eds) (2018), Syntax of Hungarian Nouns and Noun Phrases. I., II. Comprehensive grammar resources. Amsterdam University Press, Amsterdam.
 - Katalin É. Kiss and Veronika Hegedűs (eds) (2021), Postpositions and Postpositional Phrases. Amsterdam: Amsterdam University Press.

The process of collecting sentences partly followed the one described in Warstadt et. al (2018). The guideline of our process is available in the repository of [HuCOLA](https://github.com/nytud/HuCOLA). 


### Annotations

#### Annotation process

Each instance was annotated by 4 human annotators for its acceptability (see the annotation guidelines in the repository of [HuCOLA](https://github.com/nytud/HuCOLA)).

#### Who are the annotators?

The annotators were native Hungarian speakers (of various ages, from 20 to 67) without any linguistic backround.

## Additional Information

### Licensing Information

HuCOLA is released under the CC-BY-SA 4.0 licence.

### Citation Information

If you use this resource or any part of its documentation, please refer to:

Ligeti-Nagy, N., Ferenczi, G., Héja, E., Jelencsik-Mátyus, K., Laki, L. J., Vadász, N., Yang, Z. Gy. and Váradi, T. (2022) HuLU: magyar nyelvű benchmark adatbázis
kiépítése a neurális nyelvmodellek kiértékelése céljából [HuLU: Hungarian benchmark dataset to evaluate neural language models]. XVIII. Magyar Számítógépes Nyelvészeti Konferencia. (in press)
```
@inproceedings{ligetinagy2022hulu,
  title={HuLU: magyar nyelvű benchmark adatbázis kiépítése a neurális nyelvmodellek kiértékelése céljából},
  author={Ligeti-Nagy, N. and Ferenczi, G. and Héja, E. and Jelencsik-Mátyus, K. and Laki, L. J. and Vadász, N. and Yang, Z. Gy. and Váradi, T.},
  booktitle={XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
  year={2022}
}
```


### Contributions

Thanks to [lnnoemi](https://github.com/lnnoemi) for adding this dataset.