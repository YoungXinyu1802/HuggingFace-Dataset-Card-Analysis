---
annotations_creators:
- other
language_creators:
- other
language:
- es
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: readability-es-caes
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- text-classification-other-readability
---

# Dataset Card for [readability-es-caes]


## Dataset Description


### Dataset Summary

This dataset is a compilation of short articles from websites dedicated to learn Spanish as a second language. These articles have been compiled from the following sources:
- [CAES corpus](http://galvan.usc.es/caes/) (Martínez et al., 2019): the "Corpus de Aprendices del Español" is a collection of texts produced by Spanish L2 learners from Spanish learning centers and universities. These text are produced by students of all levels (A1 to C1), with different backgrounds (11 native languages) and levels of experience.  
### Languages

Spanish

## Dataset Structure

Texts are tokenized to create a paragraph-based dataset

### Data Fields

The dataset is formatted as a json lines and includes the following fields:
- **Category:** when available, this includes the level of this text according to the Common European Framework of Reference for Languages (CEFR).
- **Level:** standardized readability level: simple or complex.
- **Level-3:** standardized readability level: basic, intermediate or advanced.
- **Text:** original text formatted into sentences.


## Additional Information

### Licensing Information

https://creativecommons.org/licenses/by-nc-sa/4.0/

### Citation Information

Please cite this page to give credit to the authors :)

### Team
- [Laura Vásquez-Rodríguez](https://lmvasque.github.io/)
- [Pedro Cuenca](https://twitter.com/pcuenq)
- [Sergio Morales](https://www.fireblend.com/)
- [Fernando Alva-Manchego](https://feralvam.github.io/)

