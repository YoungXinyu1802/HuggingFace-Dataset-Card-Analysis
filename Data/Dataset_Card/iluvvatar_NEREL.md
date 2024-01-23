---
language:
- ru
multilinguality:
- monolingual
pretty_name: NEREL
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition
---

# NEREL dataset

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Structure](#dataset-structure)
- [Citation Information](#citation-information)
- [Contacts](#contacts)

## Dataset Description
NEREL dataset (https://doi.org/10.48550/arXiv.2108.13112) is
a Russian dataset for named entity recognition and relation extraction.
NEREL is significantly larger than existing Russian datasets:
to date it contains 56K annotated named entities and 39K annotated relations.
Its important difference from previous datasets is annotation of nested named
entities, as well as relations within nested entities and at the discourse
level. NEREL can facilitate development of novel models that can extract
relations between nested named entities, as well as relations on both sentence
and document levels. NEREL also contains the annotation of events involving
named entities and their roles in the events.

You can see full entity types list in a subset "ent_types"
and full list of relation types in a subset "rel_types".

## Dataset Structure
There are three "configs" or "subsets" of the dataset.

Using 
`load_dataset('MalakhovIlya/NEREL', 'ent_types')['ent_types']` 
you can download list of entity types (
Dataset({features: ['type', 'link']})
) where "link" is a knowledge base name used in entity linking task.
 
Using 
`load_dataset('MalakhovIlya/NEREL', 'rel_types')['rel_types']` 
you can download list of entity types (
Dataset({features: ['type', 'arg1', 'arg2']})
) where "arg1" and "arg2" are lists of entity types that can take part in such
"type" of relation. \<ENTITY> stands for any type.

Using 
`load_dataset('MalakhovIlya/NEREL', 'data')` or `load_dataset('MalakhovIlya/NEREL')`
you can download the data itself, 
DatasetDict with 3 splits: "train", "test" and "dev".
Each of them contains text document with annotated entities, relations and
links.

"entities" are used in named-entity recognition task (see https://en.wikipedia.org/wiki/Named-entity_recognition).  
"relations" are used in relationship extraction task (see https://en.wikipedia.org/wiki/Relationship_extraction).  
"links" are used in entity linking task (see https://en.wikipedia.org/wiki/Entity_linking)

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

Each link is represented by a string of the following format:  
`"<id>\tReference <ent_id> <link>\t<text>"`, where  
`<id>` is a link id,  
`<ent_id>` is an entity id,  
`<link>` is a reference to knowledge base entity (example: "Wikidata:Q1879675" if link exists, else "Wikidata:NULL"),  
`<text>` is a name of entity in knowledge base if link exists, else empty string.

## Citation Information
@article{loukachevitch2021nerel,  
    title={NEREL: A Russian Dataset with Nested Named Entities, Relations and Events},  
    author={Loukachevitch, Natalia and Artemova, Ekaterina and Batura, Tatiana and Braslavski, Pavel and Denisov, Ilia and Ivanov, Vladimir and Manandhar, Suresh and Pugachev, Alexander and Tutubalina, Elena},  
    journal={arXiv preprint arXiv:2108.13112},  
    year={2021}  
}

## Contacts
Malakhov Ilya  
Telegram - https://t.me/noname_4710
