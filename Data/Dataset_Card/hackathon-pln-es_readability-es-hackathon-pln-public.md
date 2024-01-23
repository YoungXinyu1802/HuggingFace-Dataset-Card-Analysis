---
annotations_creators:
- found
language_creators:
- found
language:
- es
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: readability-es-sentences
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- text-classification-other-readability
---

# Dataset Card for [readability-es-sentences]


## Dataset Description

Compilation of short Spanish articles for readability assessment.

### Dataset Summary

This dataset is a compilation of short articles from websites dedicated to learn Spanish as a second language. These articles have been compiled from the following sources: 
- **Coh-Metrix-Esp corpus (Quispesaravia, et al., 2016):** collection of 100 parallel texts with simple and complex variants in Spanish. These texts include children's and adult stories to fulfill each category.
- **[kwiziq](https://www.kwiziq.com/):** a language learner assistant
- **[hablacultura.com](https://hablacultura.com/):** Spanish resources for students and teachers. We have downloaded the available content in their websites.


### Languages

Spanish

## Dataset Structure

The dataset includes 1019 text entries between 80 and 8714 characters long. The vast majority (97%) are below 4,000 characters long.

### Data Fields

The dataset is formatted as a json lines and includes the following fields:
- **Category:** when available, this includes the level of this text according to the Common European Framework of Reference for Languages (CEFR).
- **Level:** standardized readability level: complex or simple. 
- **Level-3:** standardized readability level: basic, intermediate or advanced
- **Text:** original text formatted into sentences.

Not all the entries contain usable values for `category`, `level` and `level-3`, but all of them should contain at least one of `level`, `level-3`. When the corresponding information could not be derived, we use the special `"N/A"` value to indicate so.

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

