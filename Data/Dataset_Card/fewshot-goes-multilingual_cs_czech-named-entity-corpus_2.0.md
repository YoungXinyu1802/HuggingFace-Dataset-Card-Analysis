---
annotations_creators:
- expert-generated
language:
- cs
language_creators:
- found
license:
- cc-by-nc-sa-3.0
multilinguality:
- monolingual
pretty_name: Czech Named Entity Corpus 2.0
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- czech NER
- CNEC
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---


# Dataset Card for Czech Named Entity Corpus 2.0


## Dataset Description
The dataset contains Czech sentences and annotated named entities. Total number of sentences is around 9,000 and total number of entities is around 34,000. (Total means train + validation + test)

## Dataset Features
Each sample contains:
- `text`: source sentence
- `entities`: list of selected entities. Each entity contains:
  - `category_id`: string identifier of the entity category
  - `category_str`: human-friendly category name in Czech (verbalizer)
  - `start`: index on which the entity starts in the source sentence
  - `end`: index on which the entity ends in the source sentence
  - `content`: entity content, it was created as `text[start:end]`
  - `entity_id`: unique entity string identifier
  - `parent_id`: If entity was selected inside another entity (e.g. house number inside address), `parent_id` is the identifier of the parent entity. None otherwise.

The `entity_id` field was checked to be globally unique (across data samples and dataset splits.)


## Entity categories
The list of the recognized entities (`category_id`, `category_str` pairs): 

```python3
{
 'A': 'číslo v adrese / kontaktním údaji',
 'ah': 'číslo domu',
 'at': 'telefonní číslo / fax',
 'az': 'PSČ (poštovní směrovací číslo)',
 'C': 'reference/bibliografie',
 'f': 'cizí výraz',
 'g_': 'geografický název - jiný',
 'gc': 'stát/země',
 'gh': 'jméno vodstva',
 'gl': 'přírodní oblast/útvar',
 'gq': 'městská čtvrť',
 'gr': 'území',
 'gs': 'ulice/náměstí',
 'gt': 'kontinent',
 'gu': 'město/zámek',
 'i_': 'instituce - jiná',
 'ia': 'konference/soutěž',
 'ic': 'kulturní/vzdělávací/vědecká instituce',
 'if': 'komerční instituce',
 'io': 'vládní/politická instituce',
 'me': 'emailová adresa',
 'mi': 'URL / internetový odkaz',
 'mn': 'časopis',
 'ms': 'radio/televizní stanice',
 'n_': 'číselný výraz - jiný',
 'na': 'věk',
 'nb': 'číslo stránky/kapitoly/sekce/objektu',
 'nc': 'množství/počet',
 'ni': 'číslo položky',
 'no': 'pořadí',
 'ns': 'sportovní skóre',
 'o_': 'artefakt - jiný',
 'oa': 'umělecké dílo / kulturní artefakt',
 'oe': 'jednotka',
 'om': 'měna',
 'op': 'produkt/výrobek',
 'or': 'zákon/směrnice/listina',
 'P': 'celé jméno',
 'p_': 'jméno - jiné',
 'pc': 'národnost',
 'pd': '(akademický) titul',
 'pf': 'křestní jméno',
 'pm': 'prostřední jméno',
 'pp': 'mýtická/historická postava',
 'ps': 'příjmení',
 's': 'zkratka',
 'T': 'čas/datum',
 'td': 'den',
 'tf': 'svátky',
 'th': 'hodiny/minuty',
 'tm': 'měsíc',
 'ty': 'rok',
}
```

## Dataset Source

The dataset is a preprocessed adaptation of existing CNEC 2.0 dataset [project info](https://ufal.mff.cuni.cz/cnec/cnec2.0), [link to data](https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0023-1B22-8). This adaptation contains (almost) same data, but converted to a convenient format. In addition, we inspected and decided to remove entity categories: `?`, `segm`, `cap`, `lower`, `upper`, which were either undocumented and/or carried little semantic meaning.

The category names (verbalizers) are not in the original dataset. They were added by a Czech native speaker using the available [documentation](https://ufal.mff.cuni.cz/cnec/cnec2.0) and by looking at several occurrences in the data.


## Citation

Cite authors of the [original dataset](https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0023-1B22-8):

```bibtex
@misc{11858/00-097C-0000-0023-1B22-8,
 title = {Czech Named Entity Corpus 2.0},
 author = {{\v S}ev{\v c}{\'{\i}}kov{\'a}, Magda and {\v Z}abokrtsk{\'y}, Zden{\v e}k and Strakov{\'a}, Jana and Straka, Milan},
 url = {http://hdl.handle.net/11858/00-097C-0000-0023-1B22-8},
 note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
 copyright = {Attribution-{NonCommercial}-{ShareAlike} 3.0 Unported ({CC} {BY}-{NC}-{SA} 3.0)},
 year = {2014}
}
```

