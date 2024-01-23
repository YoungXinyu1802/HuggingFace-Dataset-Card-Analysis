---
license: cc-by-sa-4.0
---

# Dataset Card for Sloleks 3

**Important**: this is a minimal script for processing Sloleks 3. Most notably, some word form properties (accentuation, pronounciation) and frequencies are not exposed here. 
Please see the [CLARIN repository](https://www.clarin.si/repository/xmlui/handle/11356/1745) for full details on what the dataset contains, and open an issue or a pull request if you require some other information from the raw data.   


### Dataset Summary

Sloleks is a reference morphological lexicon of Slovene that was developed to be used in various NLP applications and language manuals. 
It contains Slovene lemmas, their inflected or derivative word forms and the corresponding grammatical description. 
In addition to the approx. 100,000 entries already available in [Sloleks 2.0](http://hdl.handle.net/11356/1230), Sloleks 3.0 contains an additional 
cca. 265,000 newly generated entries from the most frequent lemmas in [Gigafida 2.0](http://hdl.handle.net/11356/1320) not yet included in previous versions of Sloleks. 
For verbs, adjectives, adverbs, and common nouns, the lemmas were checked manually by three annotators and included in Sloleks only if confirmed as legitimate by at 
least one annotator. No manual checking was performed on proper nouns. Lemmatization rules, part-of-speech categorization and the set of feature-value pairs follow the 
[MULTEXT-East morphosyntactic specifications for Slovenian](https://nl.ijs.si/ME/V6/msd/html/msd-sl.html).  

### Supported Tasks and Leaderboards

Other (the data is a knowledge base - lexicon).  

### Languages

Slovenian.

## Dataset Structure

### Data Instances

Entry for the verb `absorbirati` (English: *to absorb*):
```
{
	'headword_lemma': 'absorbirati', 
	'pos': 'verb',
	'lex_unit': {'id': 'LE_a293f9ab871299f116dff2cc1421367a', 'form': 'absorbirati', 'key': 'G_absorbirati', 'type': 'single'}, 
	'word_forms': 
		[
			{'forms': ['absorbirati'], 'msd': 'Ggvn'}, 
			{'forms': ['absorbirat'], 'msd': 'Ggvm'}, 
			{'forms': ['absorbiral'], 'msd': 'Ggvd-em'}, 
			{'forms': ['absorbirala'], 'msd': 'Ggvd-dm'}, 
			{'forms': ['absorbirali'], 'msd': 'Ggvd-mm'}, 
			{'forms': ['absorbirala'], 'msd': 'Ggvd-ez'}, 
			{'forms': ['absorbirali'], 'msd': 'Ggvd-dz'}, 
			{'forms': ['absorbirale'], 'msd': 'Ggvd-mz'}, 
			{'forms': ['absorbiralo'], 'msd': 'Ggvd-es'}, 
			{'forms': ['absorbirali'], 'msd': 'Ggvd-ds'}, 
			{'forms': ['absorbirala'], 'msd': 'Ggvd-ms'}, 
			{'forms': ['absorbiram'], 'msd': 'Ggvspe'}, 
			{'forms': ['absorbiraš'], 'msd': 'Ggvsde'}, 
			{'forms': ['absorbira'], 'msd': 'Ggvste'}, 
			{'forms': ['absorbirava'], 'msd': 'Ggvspd'}, 
			{'forms': ['absorbirata'], 'msd': 'Ggvsdd'}, 
			{'forms': ['absorbirata'], 'msd': 'Ggvstd'}, 
			{'forms': ['absorbiramo'], 'msd': 'Ggvspm'}, 
			{'forms': ['absorbirate'], 'msd': 'Ggvsdm'}, 
			{'forms': ['absorbirajo'], 'msd': 'Ggvstm'}, 
			{'forms': ['absorbirajva'], 'msd': 'Ggvvpd'}, 
			{'forms': ['absorbirajmo'], 'msd': 'Ggvvpm'}, 
			{'forms': ['absorbiraj'], 'msd': 'Ggvvde'}, 
			{'forms': ['absorbirajta'], 'msd': 'Ggvvdd'}, 
			{'forms': ['absorbirajte'], 'msd': 'Ggvvdm'}
		], 
	'is_manually_checked': True
}
```

### Data Fields

- `headword_lemma`: lemma of the headword;
- `pos`: coarse-grained part-of-speech tag (one of `{"noun", "verb", "adjective", "adverb", "pronoun", "numeral", "preposition", "conjunction", "particle", "interjection", "abbreviation", "residual"}`);  
- `lex_unit`: properties of the lexical unit corresponding to the headword (`id`, `form`, `key` and `type`);
- `word_forms`: forms of the headword, each with its own list of possible forms and the morphosyntactic description of the form;
- `is_manually_checked`: whether the headword was manually validated or not.


## Additional Information

### Dataset Curators

Jaka Čibej; et al. (please see http://hdl.handle.net/11356/1745 for the full list).

### Licensing Information

CC BY-SA 4.0.

### Citation Information

```
@misc{sloleks3,
    title = {Morphological lexicon Sloleks 3.0},
    author = {{\v C}ibej, Jaka and Gantar, Kaja and Dobrovoljc, Kaja and Krek, Simon and Holozan, Peter and Erjavec, Toma{\v z} and Romih, Miro and Arhar Holdt, {\v S}pela and Krsnik, Luka and Robnik-{\v S}ikonja, Marko},
    url = {http://hdl.handle.net/11356/1745},
    note = {Slovenian language resource repository {CLARIN}.{SI}},
    copyright = {Creative Commons - Attribution-{ShareAlike} 4.0 International ({CC} {BY}-{SA} 4.0)},
    year = {2022}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
