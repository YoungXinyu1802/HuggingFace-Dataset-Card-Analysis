---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: sentiment-classification-reviews-with-drift
size_categories:
- 10K<n<100K
source_datasets:
- extended|imdb
task_categories:
- text-classification
task_ids:
- sentiment-classification
---

# Dataset Card for `reviews_with_drift`

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

### Dataset Summary

This dataset was crafted to be used in our tutorial [Link to the tutorial when ready]. It consists on a large Movie Review Dataset mixed with some reviews from a Hotel Review Dataset. The training/validation set are purely obtained from the Movie Review Dataset while the production set is mixed. Some other features have been added (`age`, `gender`, `context`) as well as a made up timestamp `prediction_ts` of when the inference took place.

### Supported Tasks and Leaderboards

`text-classification`, `sentiment-classification`: The dataset is mainly used for text classification: given the text, predict the sentiment (positive or negative).

### Languages

Text is mainly written in english.

## Dataset Structure

### Data Instances

#### default

An example of `training` looks as follows:

```json
{
 'prediction_ts': 1650092416.0,
 'age': 44,
 'gender': 'female',
 'context': 'movies',
 'text': "An interesting premise, and Billy Drago is always good as a dangerous nut-bag (side note: I'd love to see Drago, Stephen McHattie and Lance Hendrikson in a flick together; talk about raging cheekbones!). The soundtrack wasn't terrible, either.<br /><br />But the acting--even that of such professionals as Drago and Debbie Rochon--was terrible, the directing worse (perhaps contributory to the former), the dialog chimp-like, and the camera work, barely tolerable. Still, it was the SETS that got a big 10 on my oy-vey scale. I don't know where this was filmed, but were I to hazard a guess, it would be either an open-air museum, or one of those re-enactment villages, where everything is just a bit too well-kept to do more than suggest the real Old West. Okay, so it was shot on a college kid's budget. That said, I could have forgiven one or two of the aforementioned faults. But taken all together, and being generous, I could not see giving it more than three stars.",
 'label': 0
 }
```

### Data Fields

#### default

The data fields are the same among all splits. An example of `training` looks as follows:

- `prediction_ts`: a `float` feature.
- `age`: an `int` feature.
- `gender`: a `string` feature.
- `context`: a `string` feature.
- `text`: a `string` feature.
- `label`: a `ClassLabel` feature, with possible values including negative(0) and positive(1).

### Data Splits

|   name   |training|validation|production |
|----------|-------:|---------:|----------:|
|  default |  9916  |   2479   |   40079   |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Contributions

Thanks to [@fjcasti1](https://github.com/fjcasti1) for adding this dataset.