---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- sl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
- 100K<n<1M
source_datasets: []
task_categories:
- text-classification
- token-classification
task_ids: []
pretty_name: Dataset of Slovene idiomatic expressions SloIE
tags:
- idiom-detection
- multiword-expression-detection
---

# Dataset Card for SloIE

### Dataset Summary

SloIE is a manually labelled dataset of Slovene idiomatic expressions. It contains 29399 sentences with 75 different expressions that can occur with either a literal or an idiomatic meaning, with appropriate manual annotations for each token. The idiomatic expressions were selected from the [Slovene Lexical Database]( (http://hdl.handle.net/11356/1030). Only expressions that can occur with both a literal and an idiomatic meaning were selected. The sentences were extracted from the Gigafida corpus.

For a more detailed description of the dataset, please see the paper Škvorc et al. (2022) - see below.

### Supported Tasks and Leaderboards

Idiom detection.

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```json
{
  'sentence': 'Fantje regljajo v enem kotu, deklice pa svoje obrazke barvajo s pisanimi barvami.', 
  'expression': 'barvati kaj s črnimi barvami', 
  'word_order': [11, 10, 12, 13, 14], 
  'sentence_words': ['Fantje', 'regljajo', 'v', 'enem', 'kotu,', 'deklice', 'pa', 'svoje', 'obrazke', 'barvajo', 's', 'pisanimi', 'barvami.'],
  'is_idiom': ['*', '*', '*', '*', '*', '*', '*', '*', 'NE', 'NE', 'NE', 'NE', 'NE']
}
```

In this `sentence`, the words of the expression "barvati kaj s črnimi barvami" are used in a literal sense, as indicated by the "NE" annotations inside `is_idiom`. The "*" annotations indicate the words are not part of the expression.  

### Data Fields

- `sentence`: raw sentence in string form - **WARNING**: this is at times slightly different from the words inside `sentence_words` (e.g., "..." here could be "." in `sentence_words`);  
- `expression`: the annotated idiomatic expression;  
- `word_order`: numbers indicating the positions of tokens that belong to the expression;  
- `sentence_words`: words in the sentence;  
- `is_idiom`: a string denoting whether each word has an idiomatic (`"DA"`), literal (`"NE"`), or ambiguous (`"NEJASEN ZGLED"`) meaning. `"*"` means that the word is not part of the expression.  

## Additional Information

### Dataset Curators

Tadej Škvorc, Polona Gantar, Marko Robnik-Šikonja. 

### Licensing Information

CC BY-NC-SA 4.0.

### Citation Information

```
@article{skvorc2022mice,
  title = {MICE: Mining Idioms with Contextual Embeddings},
  journal = {Knowledge-Based Systems},
  volume = {235},
  pages = {107606},
  year = {2022},
  doi = {https://doi.org/10.1016/j.knosys.2021.107606},
  url = {https://www.sciencedirect.com/science/article/pii/S0950705121008686},
  author = {{\v S}kvorc, Tadej and Gantar, Polona and Robnik-{\v S}ikonja, Marko},
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
