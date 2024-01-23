---
annotations_creators:
- machine-generated
- expert-generated
language:
- sl
language_creators:
- machine-generated
- found
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Semantic lexicon of Slovene sloWNet
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- slownet
- wordnet
- pwn
task_categories:
- other
task_ids: []
---

# Dataset Card for SloWNet

### Dataset Summary

sloWNet is the Slovene WordNet developed in the expand approach: it contains the complete Princeton WordNet 3.0 and over 70 000 Slovene literals. These literals have been added automatically using different types of existing resources, such as bilingual dictionaries, parallel corpora and Wikipedia. 33 000 literals have been subsequently hand-validated.

For a detailed description of the data, please see the paper Fišer et al. (2012).

### Supported Tasks and Leaderboards

Other (the data is a knowledge base).

### Languages

Slovenian.

## Dataset Structure

### Data Instances

Each synset is stored in its own instance. The following instance represents a synset containing the English synonyms `{'able'}` and Slovene synonyms `{'sposoben', 'zmožen'}`:
```
{
  'id': 'eng-30-00001740-a',
  'pos': 'a',
  'bcs': 3,
  'en_synonyms': {
    'words': ['able'],
    'senses': [1],
    'pwnids': ['able%3:00:00::']
  },
  'sl_synonyms': {
    'words': ['sposoben', 'zmožen'],
    'is_validated': [False, False]
  },
  'en_def': "(usually followed by `to') having the necessary means or skill or know-how or authority to do something",
  'sl_def': 'N/A',
  'en_usages': [
    'able to swim', 
    'she was able to program her computer',
    'we were at last able to buy a car',
    'able to get a grant for the project'
  ],
  'sl_usages': [],
  'ilrs': {
    'types': ['near_antonym', 'be_in_state', 'be_in_state', 'eng_derivative', 'eng_derivative'], 
    'id_synsets': ['eng-30-00002098-a', 'eng-30-05200169-n', 'eng-30-05616246-n', 'eng-30-05200169-n', 'eng-30-05616246-n']
  }, 
  'semeval07_cluster': 'able', 
  'domains': ['quality']
}
```

### Data Fields

- `id`: a string ID of the synset;  
- `pos`: part of speech tag of the synset;
- `bcs`: Base Concept Set index (`-1` if not present);  
- `en_synonyms`: the English synonyms in the synset - synonym `i` is described with its form (`words[i]`), sense (`senses[i]`), and Princeton WordNet ID (`pwnids[i]`);  
- `sl_synonyms`: the Slovene synonyms in the synset - synonym `i` is described with its form (`words[i]`) and a flag marking if its correctness has been manually validated (`is_validated[i]`);
- `en_def`: the English definition (`"N/A"` if not present);  
- `sl_def`: the Slovene definition (`"N/A"` if not present);  
- `en_usages`: the English examples of usage;
- `sl_usages`: the Slovene examples of usage;  
- `ilrs`: internal language relations - relation `i` is described by its type (`types[i]`) and the target synset (`id_synsets[i]`);  
- `semeval07_cluster`: string cluster (`"N/A"` if not present);  
- `domains`: domains of the synset.

## Additional Information

### Dataset Curators

Darja Fišer.

### Licensing Information

CC BY-SA 4.0

### Citation Information

```
@inproceedings{fiser2012slownet,
  title={sloWNet 3.0: development, extension and cleaning},
  author={Fi{\v{s}}er, Darja and Novak, Jernej and Erjavec, Toma{\v{z}}},
  booktitle={Proceedings of 6th International Global Wordnet Conference (GWC 2012)},
  pages={113--117},
  year={2012}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
