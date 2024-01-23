---
language:
- ru
multilinguality:
- monolingual
pretty_name: RuREBus
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition
---

# RuREBus dataset

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Structure](#dataset-structure)
- [Citation Information](#citation-information)
- [Contacts](#contacts)

## Dataset Description
RuREBus dataset (https://github.com/dialogue-evaluation/RuREBus) is
a Russian dataset for named entity recognition and relation extraction.

## Dataset Structure
There are two subsets of the dataset.

Using 
`load_dataset('MalakhovIlya/RuREBus')` 
you can download annotated data (DatasetDict) for named entity recognition task and
relation extraction tasks. 
This subset consists of two splits: "train" and "test".
 
Using 
`load_dataset('MalakhovIlya/NEREL', 'raw_txt')['raw_txt']` 
you can download (Dataset) large corpus (~3gb) raw texts of the same subject
area, but without any annotations.

"entities" are used in named-entity recognition task (see https://en.wikipedia.org/wiki/Named-entity_recognition).  
"relations" are used in relationship extraction task (see https://en.wikipedia.org/wiki/Relationship_extraction).

Each entity is represented by a string of the following format:  
`"<id>\t<type> <start> <stop>\t<text>"`, where  
`<id>` is an entity id,  
`<type>` is one of entity types,  
`<start>` is a position of the first symbol of entity in text,  
`<stop>` is the last symbol position in text +1.

Each relation is represented by a string of the following format:  
`"<id>\t<type> Arg1:<arg1_id> Arg2:<arg2_id>"`, where  
`<id>` is a relation id,  
`<arg1_id>` and `<arg2_id>` are entity ids.

## Citation Information
@inproceedings{rurebus,
  Address = {Moscow, Russia},
  Author = {Ivanin, Vitaly and Artemova, Ekaterina and Batura, Tatiana and Ivanov, Vladimir and Sarkisyan, Veronika and Tutubalina, Elena and Smurov, Ivan},
  Title = {RuREBus-2020 Shared Task: Russian Relation Extraction for Business},
  Booktitle = {Computational  Linguistics  and  Intellectual  Technologies:  Proceedings of the International Conference “Dialog” [Komp’iuternaia Lingvistika  i  Intellektual’nye  Tehnologii:  Trudy  Mezhdunarodnoj  Konferentsii  “Dialog”]},
  Year = {2020}
}

## Contacts
Malakhov Ilya  
Telegram - https://t.me/noname_4710
