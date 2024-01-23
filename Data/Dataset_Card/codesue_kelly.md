---
annotations_creators:
- expert-generated
language:
- sv
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: kelly
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- lexicon
- swedish
- CEFR
task_categories:
- text-classification
task_ids:
- text-scoring
---

# Dataset Card for Kelly

Keywords for Language Learning for Young and adults alike

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://spraakbanken.gu.se/en/resources/kelly
- **Paper:** https://link.springer.com/article/10.1007/s10579-013-9251-2

### Dataset Summary

The Swedish Kelly list is a freely available frequency-based vocabulary list
that comprises general-purpose language of modern Swedish. The list was
generated from a large web-acquired corpus (SweWaC) of 114 million words
dating from the 2010s. It is adapted to the needs of language learners and
contains 8,425 most frequent lemmas that cover 80% of SweWaC.

### Languages

Swedish (sv-SE)

## Dataset Structure

### Data Instances

Here is a sample of the data:

```python
{
    'id': 190,
    'raw_frequency': 117835.0,
    'relative_frequency': 1033.61,
    'cefr_level': 'A1',
    'source': 'SweWaC',
    'marker': 'en',
    'lemma': 'dag',
    'pos': 'noun-en',
    'examples': 'e.g. god dag'
}
```

This can be understood as:

> The common noun "dag" ("day") has a rank of 190 in the list. It was used 117,835
times in SweWaC, meaning it occured 1033.61 times per million words. This word
is among the most important vocabulary words for Swedish language learners and
should be learned at the A1 CEFR level. An example usage of this word is the
phrase "god dag" ("good day").


### Data Fields

- `id`: The row number for the data entry, starting at 1. Generally corresponds
  to the rank of the word.
- `raw_frequency`: The raw frequency of the word.
- `relative_frequency`: The relative frequency of the word measured in
  number of occurences per million words.
- `cefr_level`: The CEFR level (A1, A2, B1, B2, C1, C2) of the word.
- `source`: Whether the word came from SweWaC, translation lists (T2), or
  was manually added (manual).
- `marker`: The grammatical marker of the word, if any, such as an article or
  infinitive marker.
- `lemma`: The lemma of the word, sometimes provided with its spelling or
  stylistic variants.
- `pos`: The word's part-of-speech.
- `examples`: Usage examples and comments. Only available for some of the words.

Manual entries were prepended to the list, giving them a higher rank than they
might otherwise have had. For example, the manual entry "Göteborg ("Gothenberg")
has a rank of 20, while the first non-manual entry "och" ("and") has a rank of
87. However, a conjunction and common stopword is far more likely to occur than
the name of a city.

### Data Splits

There is a single split, `train`.

## Dataset Creation

Please refer to the article [Corpus-based approaches for the creation of a frequency
based vocabulary list in the EU project KELLY – issues on reliability, validity and
coverage](https://gup.ub.gu.se/publication/148533?lang=en) for information about how
the original dataset was created and considerations for using the data.

**The following changes have been made to the original dataset**:

- Changed header names.
- Normalized the large web-acquired corpus name to "SweWac" in the `source` field.
- Set the relative frequency of manual entries to null rather than 1000000.


## Additional Information

### Licensing Information

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0)

### Citation Information

Please cite the authors if you use this dataset in your work:

```bibtex
@article{Kilgarriff2013,
  doi = {10.1007/s10579-013-9251-2},
  url = {https://doi.org/10.1007/s10579-013-9251-2},
  year = {2013},
  month = sep,
  publisher = {Springer Science and Business Media {LLC}},
  volume = {48},
  number = {1},
  pages = {121--163},
  author = {Adam Kilgarriff and Frieda Charalabopoulou and Maria Gavrilidou and Janne Bondi Johannessen and Saussan Khalil and Sofie Johansson Kokkinakis and Robert Lew and Serge Sharoff and Ravikiran Vadlapudi and Elena Volodina},
  title = {Corpus-based vocabulary lists for language learners for nine languages},
  journal = {Language Resources and Evaluation}
}
```

### Contributions

Thanks to [@spraakbanken](https://github.com/spraakbanken) for creating this dataset
and to [@codesue](https://github.com/codesue) for adding it.
