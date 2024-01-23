---
annotations_creators:
- machine-generated
language_creators: []
language:
- fr-FR
- fr
license:
- wtfpl
multilinguality:
- monolingual
pretty_name: test
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
---

# Dataset Card for frwiki_good_pages_el

## Dataset Description

- Repository: [frwiki_good_pages_el](https://github.com/GaaH/frwiki_good_pages_el)
- Point of Contact: [Gaëtan Caillaut](mailto://g.caillaut@brgm.fr)

### Dataset Summary

This dataset contains _featured_ and _good_ articles from the French Wikipédia. Pages are downloaded, as HTML files, from the [French Wikipedia website](https://fr.wikipedia.org).

It is intended to be used to train Entity Linking (EL) systems. Links in articles are used to detect named entities.

### Languages

- French

## Dataset Structure

```
{
    "title": "Title of the page",
    "qid": "QID of the corresponding Wikidata entity",
    "words": ["tokens"],
    "wikipedia": ["Wikipedia description of each entity"],
    "wikidata": ["Wikidata description of each entity"],
    "labels": ["NER labels"],
    "titles": ["Wikipedia title of each entity"],
    "qids": ["QID of each entity"],
}
```

The `words` field contains the article’s text splitted on white-spaces. The other fields are list with same length as `words` and contains data only when the respective token in `words` is the __start of an entity__. For instance, if the _i-th_ token in `words` is an entity, then the _i-th_ element of `wikipedia` contains a description, extracted from Wikipedia, of this entity. The same applies for the other fields. If the entity spans multiple words, then only the index of the first words contains data.

The only exception is the `labels` field, which is used to delimit entities. It uses the IOB encoding: if the token is not part of an entity, the label is `"O"`; if it is the first word of a multi-word entity, the label is `"B"`; otherwise the label is `"I"`.