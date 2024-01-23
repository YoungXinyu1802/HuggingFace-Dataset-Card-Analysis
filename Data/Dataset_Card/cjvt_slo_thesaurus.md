---
annotations_creators:
- machine-generated
language:
- sl
language_creators:
- machine-generated
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Thesaurus of Modern Slovene 1.0
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- sopomenke
- synonyms
task_categories:
- other
task_ids: []
---

# Dataset Card for Thesaurus of Modern Slovene 1.0

Also known as "Sopomenke 1.0". Available in application form online: https://viri.cjvt.si/sopomenke/slv/.

### Dataset Summary

This is an automatically created Slovene thesaurus from Slovene data available in a comprehensive English–Slovenian dictionary, a monolingual dictionary, and a corpus. A network analysis on the bilingual dictionary word co-occurrence graph was used, together with additional information from the distributional thesaurus data available as part of the Sketch Engine tool and extracted from the 1.2 billion word Gigafida corpus and the monolingual dictionary.

For a detailed description of the data, please see the paper Krek et al. (2017).

### Supported Tasks and Leaderboards

Other (the data is a knowledge base).

### Languages

Slovenian.

## Dataset Structure

### Data Instances

Each entry is stored in its own instance. The following instance contains the metadata for the `headword` "abeceda" (EN: "alphabet").
```
{
  'id_headword': 'th.12',
  'headword': 'abeceda',
  'groups_core': [],
  'groups_near': [
    {
      'id_words': ['th.12.1', 'th.12.2'], 
      'words': ['pisava', 'črkopis'], 
      'scores': [0.3311710059642792, 0.3311710059642792],
      'domains': [['jezikoslovje'], ['jezikoslovje']]
    }
  ]
}
```

### Data Fields

- `id_headword`: a string ID of the word;
- `headword`: the word whose synonyms are grouped in the instance;
- `groups_core`: groups of likely synonyms - each group contains the IDs of the words (`id_words`), the synonyms (`words`), and how strong the synonym relation (`scores`) is. Some groups also have domains annotated (`domains`, >= 1 per word, i.e. `domains` is a list of lists);
- `groups_near`: same as `groups_near`, but the synonyms here are typically less likely to be exact synonyms and more likely to be otherwise similar. 

## Additional Information

### Dataset Curators

Simon Krek; et al. (please see http://hdl.handle.net/11356/1166 for the full list).

### Licensing Information

CC BY-SA 4.0

### Citation Information

```
@article{krek2017translation,
  title={From translation equivalents to synonyms: creation of a Slovene thesaurus using word co-occurrence network analysis},
  author={Krek, Simon and Laskowski, Cyprian and Robnik-{\v{S}}ikonja, Marko},
  journal={Proceedings of eLex},
  pages={93--109},
  year={2017}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
