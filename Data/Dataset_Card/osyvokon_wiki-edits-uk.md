---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- uk-UA
license:
- cc-by-3.0
multilinguality:
- monolingual
- translation
pretty_name: 'Ukrainian Wikipedia edits '
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- other
task_ids: []
---

# Ukrainian Wikipedia Edits

### Dataset summary

A collection of over 5M sentence edits extracted from Ukrainian Wikipedia history revisions.

Edits were filtered by edit distance and sentence length. This makes them usable for grammatical error correction (GEC) or spellchecker models pre-training.


### Supported Tasks and Leaderboards

* Ukrainian grammatical error correction (GEC) - see [UA-GEC](https://github.com/grammarly/ua-gec)
* Ukrainian spelling correction

### Languages

Ukrainian

## Dataset Structure

### Data Fields

* `src` - sentence before edit
* `tgt` - sentence after edit

### Data Splits

* `full/train` contains all the data (5,243,376 samples)
* `tiny/train` contains a 5000 examples sample.

## Dataset Creation

Latest full Ukrainian Wiki dump were used as of 2022-04-30.

It was processed with the [wikiedits](https://github.com/snukky/wikiedits) and custom scripts.

### Source Data

#### Initial Data Collection and Normalization

Wikipedia

#### Who are the source language producers?

Wikipedia writers

### Annotations

#### Annotation process

Annotations inferred by comparing two subsequent page revisions.

#### Who are the annotators?

People who edit Wikipedia pages.

### Personal and Sensitive Information

No

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

The data is noisy. In addition to GEC and spelling edits, it contains a good chunk of factual changes and vandalism.

More task-specific filters could help.

## Additional Information

### Dataset Curators

[Oleksiy Syvokon](https://github.com/asivokon)

### Licensing Information

CC-BY-3.0

### Citation Information

```
@inproceedings{wiked2014,
    author = {Roman Grundkiewicz and Marcin Junczys-Dowmunt},
    title = {The WikEd Error Corpus: A Corpus of Corrective Wikipedia Edits and its Application to Grammatical Error Correction},
    booktitle = {Advances in Natural Language Processing -- Lecture Notes in Computer Science},
    editor = {Adam Przepiórkowski and Maciej Ogrodniczuk},
    publisher = {Springer},
    year = {2014},
    volume = {8686},
    pages = {478--490},
    url = {http://emjotde.github.io/publications/pdf/mjd.poltal2014.draft.pdf}
}
```

### Contributions

[@snukky](https://github.com/snukky) created tools for dataset processing.

[@asivokon](https://github.com/asivokon) generated this dataset.
