---
language:
- ru
multilinguality:
- monolingual
pretty_name: RuNNE
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition
---

# RuNNE dataset

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Structure](#dataset-structure)
- [Citation Information](#citation-information)
- [Contacts](#contacts)

## Dataset Description
Part of NEREL dataset (https://arxiv.org/abs/2108.13112), a Russian dataset
for named entity recognition and relation extraction, used in RuNNE (2022)
competition (https://github.com/dialogue-evaluation/RuNNE).

Entities may be nested (see https://arxiv.org/abs/2108.13112).

Entity types list:
* AGE
* AWARD
* CITY
* COUNTRY
* CRIME
* DATE
* DISEASE
* DISTRICT
* EVENT
* FACILITY
* FAMILY
* IDEOLOGY
* LANGUAGE
* LAW
* LOCATION
* MONEY
* NATIONALITY
* NUMBER
* ORDINAL
* ORGANIZATION
* PENALTY
* PERCENT
* PERSON
* PRODUCT
* PROFESSION
* RELIGION
* STATE_OR_PROVINCE
* TIME
* WORK_OF_ART

## Dataset Structure
There are two "configs" or "subsets" of the dataset.  
Using 
`load_dataset('MalakhovIlya/RuNNE', 'ent_types')['ent_types']` 
you can download list of entity types (
Dataset({
    features: ['type'],
    num_rows: 29
})
)  
Using 
`load_dataset('MalakhovIlya/RuNNE', 'data')` or `load_dataset('MalakhovIlya/RuNNE')`
you can download the data itself (DatasetDict)

Dataset consists of 3 splits: "train", "test" and "dev". Each of them contains text document. "Train" and "test" splits also contain annotated entities, "dev" doesn't.
Each entity is represented by a string of the following format: "\<start> \<stop> \<type>", where \<start> is a position of the first symbol of entity in text, \<stop> is the last symbol position in text and \<type> is a one of the aforementioned list of types.

P.S.
Original NEREL dataset also contains relations, events and linked entities, but they were not added here yet ¯\\\_(ツ)_/¯

## Citation Information
@article{Artemova2022runne, 
  title={{RuNNE-2022 Shared Task: Recognizing Nested Named Entities}},
  author={Artemova, Ekaterina and Zmeev, Maksim and Loukachevitch, Natalia and Rozhkov, Igor and Batura, Tatiana and Braslavski, Pavel and Ivanov, Vladimir and Tutubalina, Elena},
  journal={Computational Linguistics and Intellectual Technologies: Proceedings of the International Conference "Dialog"},
  year={2022}
}

## Contacts
Malakhov Ilya  
Telegram - https://t.me/noname_4710
