---
annotations_creators:
- expert-generated
- machine-generated
language:
- sl
language_creators:
- found
- machine-generated
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Collocations Dictionary of Modern Slovene 1.0
size_categories:
- 1M<n<10M
source_datasets: []
tags:
- kolokacije
- gigafida
task_categories:
- other
task_ids: []
---

# Dataset Card for Collocations Dictionary of Modern Slovene KSSS 1.0

Also known as "Kolokacije 1.0". Available in application form online: https://viri.cjvt.si/kolokacije/eng/.

### Dataset Summary

The database of the Collocations Dictionary of Modern Slovene 1.0 contains entries for 35,862 headwords (18,043 nouns, 5,148 verbs, 10,259 adjectives and 2,412 adverbs) and 7,310,983 collocations that were automatically extracted from the Gigafida 1.0 corpus. 
For the automatic extraction via the Sketch Engine API the authors used a specially adapted Sketch grammar for Slovene, and, based on manual evaluation, a set of parameters that determined: maximum number of collocates per grammatical relation, 
minimum frequency of a collocate, minimum frequency of a grammatical relation, minimum salience (logDice) score of a collocate, and minimum salience of a grammatical relation.  
  
The procedure of automatic extraction, which produced a list of collocates (lemmas) in a particular relation, was followed by a set of post-processing steps:
- removal of collocations that were represented by repetitions of the same sentence
- preparation of full collocations by the addition of the headword, and, if needed, the third element in the grammatical relation (such as preposition). The headwords/collocates were also put in the correct case, depending on the grammatical relation.
- addition of IDs from the Slovenian morphological lexicon [Sloleks](http://hdl.handle.net/11356/1230) to every element in the collocation.

For a detailed description of the data, please see the paper Kosem et al. (2018).

### Supported Tasks and Leaderboards

Other (the data is a knowledge base).

### Languages

Slovenian.

## Dataset Structure

### Data Instances

The structure of the original data is flattened, meaning that each collocation is its own instance.
The following example shows the entry for collocation `"idealizirati preteklost"` (*to idealize the past*), which is a collocation of the lexical unit `"idealizirati"` (*to idealize*).
```
{
  'collocation': 'idealizirati preteklost',
  'cluster': 1,
  'words': ['idealizirati', 'preteklost'],
  'sloleks_ids': ['LE_08e2de61d9f23f949a21f37639afdff2', 'LE_92b3b802fe9baeff25bdd6deafde10ca'],
  'gramrel': 'GBZ sbz4',
  'sense': 0,
  'id_lex_unit': '1372',
  'lex_unit': 'idealizirati',
  'lex_unit_category': 'verb'
}
```

### Data Fields

- `collocation`: the string form of the collocation;
- `cluster`: cluster of the collocation - sometimes, but not always, corresponds to the sense;
- `words`: tokenized collocation;
- `sloleks_ids`: [Sloleks](http://hdl.handle.net/11356/1230) IDs of collocation words;
- `gramrel`: grammatical relation;  
- `sense`: sense of the collocation - curently constant (see `cluster` for a slightly better approximate division);
- `id_lex_unit`: ID of the lexical unit that the collocation belongs to;
- `lex_unit`: lexical unit;
- `lex_unit_category`: category of the lexical unit.

## Additional Information

### Dataset Curators

Iztok Kosem; et al. (please see http://hdl.handle.net/11356/1250 for the full list).

### Licensing Information

CC BY-SA 4.0

### Citation Information

```
@inproceedings{kosem2018collocations,
  title={Collocations dictionary of modern Slovene},
  author={Kosem, Iztok and Krek, Simon and Gantar, Polona and Arhar Holdt, {\v{S}}pela and {\v{C}}ibej, Jaka and Laskowski, Cyprian},
  booktitle={Proceedings of the XVIII EURALEX International Congress: Lexicography in Global Contexts},
  pages={989--997},
  year={2018},
  organization={Znanstvena zalo{\v{z}}ba Filozofske fakultete Univerze v Ljubljani}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
