---
license:
- other
kaggle_id: rtatman/stopword-lists-for-african-languages
---

# Dataset Card for Stopword Lists for African Languages

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://kaggle.com/datasets/rtatman/stopword-lists-for-african-languages
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

### Context: 
Some words, like “the” or “and” in English, are used a lot in speech and writing. For most Natural Language Processing applications, you will want to remove these very frequent words. This is usually done using a list of “stopwords” which has been complied by hand.

### Content: 
This project uses the source texts provided by the African Storybook Project as a corpus and provides a number of tools to extract frequency lists and lists of stopwords from this corpus for the 60+ languages covered by ASP.

Included in this dataset are the following languages:

* Afrikaans: stoplist and word frequency
* Hausa: stoplist and word frequency
* Lugbarati: word frequency only
* Lugbarati (Official): word frequency only
* Somali: stoplist and word frequency
* Sesotho: stoplist and word frequency
* Kiswahili: stoplist and word frequency
* Yoruba: stoplist and word frequency
* isiZulu: stoplist and word frequency

Files are named using the language’s ISO code. For each language, code.txt is the list of stopwords, and code_frequency_list.txt is word frequency information. A list of ISO codes the the languages associated with them may be found in ISO_codes.csv.

### Acknowledgements: 
This project therefore attempts to fill in the gap in language coverage for African language stoplists by using the freely-available and open-licensed ASP Source project as a corpus.
Dual-licensed under CC-BY and Apache-2.0 license. Compiled by Liam Doherty. More information and the scripts used to generate these files are available [here](https://github.com/dohliam/more-stoplists).

### Inspiration: 
This dataset is mainly helpful for use during NLP analysis, however there may some interesting insights in the data.

* What qualities do stopwords share across languages? Given a novel language, could you predict what its stopwords should be?
* What stopwords are shared across languages?
* Often, related languages will have words with the same meaning and similar spellings. Can you automatically identify any of these pairs of words?

### You may also like:

* [Stopword Lists for 19 Languages (mainly European and South Asian)](https://www.kaggle.com/rtatman/stopword-lists-for-19-languages)

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset was shared by [@rtatman](https://kaggle.com/rtatman)

### Licensing Information

The license for this dataset is other

### Citation Information

```bibtex
[More Information Needed]
```

### Contributions

[More Information Needed]