---
pretty_name: ScandiWiki
language:
- da
- sv
- no
- nb
- nn
- is
- fo
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
size_categories:
- 1M<n<10M
source_datasets:
- wikipedia
task_categories:
- fill-mask
- text-generation
- feature-extraction
task_ids:
- language-modeling
---

# Dataset Card for ScandiWiki

## Dataset Description

- **Point of Contact:** [Dan Saattrup Nielsen](mailto:dan.nielsen@alexandra.dk)
- **Total amount of disk used:** 4485.90 MB

### Dataset Summary

ScandiWiki is a parsed and deduplicated Wikipedia dump in Danish, Norwegian Bokmål,
Norwegian Nynorsk, Swedish, Icelandic and Faroese.

### Supported Tasks and Leaderboards

This dataset is intended for general language modelling.


### Languages

The dataset is available in Danish (`da`), Swedish (`sv`), Norwegian Bokmål (`nb`),
Norwegian Nynorsk (`nn`), Icelandic (`is`) and Faroese (`fo`).


## Dataset Structure

### Data Instances

- **Total amount of disk used:** 4485.90 MB

An example from the `train` split of the `fo` subset looks as follows.
```
{
    'id': '3380',
    'url': 'https://fo.wikipedia.org/wiki/Enk%C3%B6pings%20kommuna',
    'title': 'Enköpings kommuna',
    'text': 'Enköpings kommuna (svenskt: Enköpings kommun), er ein kommuna í Uppsala län í Svøríki. Enköpings kommuna hevur umleið 40.656 íbúgvar (2013).\n\nKeldur \n\nKommunur í Svøríki'
}
```

### Data Fields

The data fields are the same among all splits.

- `id`: a `string` feature.
- `url`: a `string` feature.
- `title`: a `string` feature.
- `text`: a `string` feature.

### Data Subsets

|   name   | samples   |
|----------|----------:|
| sv       | 2,469,978 |
| nb       | 596,593   |
| da       | 287,216   |
| nn       | 162,776   |
| is       | 55,418    |
| fo       | 12,582    |


## Dataset Creation

### Curation Rationale

It takes quite a long time to parse the Wikipedia dump as well as to deduplicate it, so
this dataset is primarily for convenience.

### Source Data

The original data is from the [wikipedia
dataset](https://huggingface.co/datasets/wikipedia).


## Additional Information

### Dataset Curators

[Dan Saattrup Nielsen](https://saattrupdan.github.io/) from the [The Alexandra
Institute](https://alexandra.dk/) curated this dataset.

### Licensing Information

The dataset is licensed under the [CC BY-SA 4.0
license](https://creativecommons.org/licenses/by-sa/4.0/), in accordance with the same
license of the [wikipedia dataset](https://huggingface.co/datasets/wikipedia).
