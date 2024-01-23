---
annotations_creators:
- crowdsourced
language_creators:
- machine-generated
language:
- fr
license:
- wtfpl
multilinguality:
- monolingual
pretty_name: French Wikipedia dataset for Entity Linking
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- token-classification
task_ids: []
---

# Dataset Card for frwiki_good_pages_el

## Dataset Description

- Repository: [frwiki_el](https://github.com/GaaH/frwiki_el)
- Point of Contact: [Gaëtan Caillaut](mailto://g.caillaut@brgm.fr)

### Dataset Summary

This dataset contains articles from the French Wikipédia.
It is intended to be used to train Entity Linking (EL) systems. Links in articles are used to detect named entities.

The dataset `frwiki` contains sentences of each Wikipedia pages.

The dataset `entities` contains description for each Wikipedia pages.

### Languages

- French

## Dataset Structure

### frwiki

```
{
    "name": "Title of the page",
    "wikidata_id": "Identifier of the related Wikidata entity. Can be null.",
    "wikipedia_id": "Identifier of the Wikipedia page",
    "wikipedia_url": "URL to the Wikipedia page",
    "wikidata_url": "URL to the Wikidata page. Can be null.",
    "sentences" : [
        {
            "text": "text of the current sentence",
            "ner": ["list", "of", "ner", "labels"],
            "mention_mappings": [
                (start_of_first_mention, end_of_first_mention),
                (start_of_second_mention, end_of_second_mention)
            ],
            "el_wikidata_id": ["wikidata id of first mention", "wikidata id of second mention"],
            "el_wikipedia_id": [wikipedia id of first mention, wikipedia id of second mention],
            "el_wikipedia_title": ["wikipedia title of first mention", "wikipedia title of second mention"]
        }
    ]
    "words": ["words", "in", "the", "sentence"],
    "ner": ["ner", "labels", "of", "each", "words"],
    "el": ["el", "labels", "of", "each", "words"]
}
```

### entities

```
{
    "name": "Title of the page",
    "wikidata_id": "Identifier of the related Wikidata entity. Can be null.",
    "wikipedia_id": "Identifier of the Wikipedia page",
    "wikipedia_url": "URL to the Wikipedia page",
    "wikidata_url": "URL to the Wikidata page. Can be null.",
    "description": "Description of the entity"
}
```