---
annotations_creators:
- expert-generated
language:
- cs
language_creators:
- other
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: Czech Court Decisions NER
size_categories:
- n<1K
source_datasets:
- original
tags:
- czech NER
- court decisions
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Dataset Card for Czech Court Decisions NER


## Dataset Description
Czech Court Decisions NER is a dataset of 300 court decisions published by The Supreme Court of the Czech Republic and the Constitutional Court of the Czech Republic.
In the documents, 4 types of named entities are selected.


## Dataset Features

Each sample contains:
- `filename`: file name in the original dataset
- `text`: court decision document in plain text
- `entities`: list of selected entities. Each entity contains:
  - `category_id`: integer identifier of the entity category
  - `category_str`: human-friendly category name in Czech (verbalizer)
  - `start`: index on which the entity starts in the source text
  - `end`: index on which the entity ends in the source text
  - `content`: entity content, it was created as `text[start:end]`
  - `entity_id`: unique entity string identifier
  - `refers_to`: some entities (mostly of category 'Reference na rozhodnutí soudu') refer to a specific other entity. `refers_to` attribute contains the `entity_id` of the referred entity

The `entity_id` field was checked to be globally unique (across data samples and dataset splits.)


## Entity categories

The list of the recognized entities (`category_id`, `category_str` pairs): 
```python3
{
  0: 'Soudní instituce',
  1: 'Reference na rozhodnutí soudu',
  2: 'Účinnost',
  3: 'Reference zákonu'
}
```


## Dataset Source

The dataset is a preprocessed adaptation of existing Czech Court Decisions Dataset [project info](https://ufal.mff.cuni.cz/ccdd), [link to data](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2853). This adaptation contains (almost) same data, but converted to a convenient format and with stripped leaked xml-like tags in the texts.
The category names (verbalizers) were added by a Czech native speaker.


## Citation

Cite authors of the [original dataset](https://ufal.mff.cuni.cz/ccdd):
```bibtex
@misc{11234/1-2853,
  title = {Czech Court Decisions Dataset},
  author = {Kr{\'{\i}}{\v z}, Vincent and Hladk{\'a}, Barbora},
  url = {http://hdl.handle.net/11234/1-2853},
  note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
  copyright = {Creative Commons - Attribution-{NonCommercial}-{ShareAlike} 4.0 International ({CC} {BY}-{NC}-{SA} 4.0)},
  year = {2014}
}
```