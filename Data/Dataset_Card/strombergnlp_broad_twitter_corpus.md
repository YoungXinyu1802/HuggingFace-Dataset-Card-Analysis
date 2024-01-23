---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
paperswithcode_id: broad-twitter-corpus
pretty_name: Broad Twitter Corpus
---

# Dataset Card for broad_twitter_corpus

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [https://github.com/GateNLP/broad_twitter_corpus](https://github.com/GateNLP/broad_twitter_corpus)
- **Repository:** [https://github.com/GateNLP/broad_twitter_corpus](https://github.com/GateNLP/broad_twitter_corpus)
- **Paper:** [http://www.aclweb.org/anthology/C16-1111](http://www.aclweb.org/anthology/C16-1111)
- **Leaderboard:** [Named Entity Recognition on Broad Twitter Corpus](https://paperswithcode.com/sota/named-entity-recognition-on-broad-twitter)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)

### Dataset Summary

This is the Broad Twitter corpus, a dataset of tweets collected over stratified times, places and social uses. The goal is to represent a broad range of activities, giving a dataset more representative of the language used in this hardest of social media formats to process. Further, the BTC is annotated for named entities.

See the paper, [Broad Twitter Corpus: A Diverse Named Entity Recognition Resource](http://www.aclweb.org/anthology/C16-1111), for details.

### Supported Tasks and Leaderboards

* Named Entity Recognition
* On PWC: [Named Entity Recognition on Broad Twitter Corpus](https://paperswithcode.com/sota/named-entity-recognition-on-broad-twitter)

### Languages

English from UK, US, Australia, Canada, Ireland, New Zealand; `bcp47:en`

## Dataset Structure

### Data Instances

Feature |Count
---|---:
Documents |9 551
Tokens |165 739
Person entities |5 271
Location entities |3 114
Organization entities |3 732

### Data Fields

Each tweet contains an ID, a list of tokens, and a list of NER tags


- `id`: a `string` feature.
- `tokens`: a `list` of `strings` 
- `ner_tags`: a `list` of class IDs (`int`s) representing the NER class:

```
  0: O
  1: B-PER
  2: I-PER
  3: B-ORG
  4: I-ORG
  5: B-LOC
  6: I-LOC
```

### Data Splits

Section|Region|Collection period|Description|Annotators|Tweet count
---|---|---|---|---|---:
A | UK| 2012.01| General collection |Expert| 1000
B |UK |2012.01-02 |Non-directed tweets |Expert |2000
E |Global| 2014.07| Related to MH17 disaster| Crowd & expert |200
F |Stratified |2009-2014| Twitterati |Crowd & expert |2000
G |Stratified| 2011-2014| Mainstream news| Crowd & expert| 2351
H |Non-UK| 2014 |General collection |Crowd & expert |2000


The most varied parts of the BTC are sections F and H. However, each of the remaining four sections has some specific readily-identifiable bias. So, we propose that one uses half of section H for evaluation and leaves the other half in the training data. Section H should be partitioned in the order of the JSON-format lines. Note that the CoNLL-format data is readily reconstructible from the JSON format, which is the authoritative data format from which others are derived.

**Test**: Section F

**Development**: Section H (the paper says "second half of Section H" but ordinality could be ambiguous, so it all goes in. Bonne chance)

**Training**: everything else


## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

Creative Commons Attribution 4.0 International (CC BY 4.0)

### Citation Information

```
@inproceedings{derczynski2016broad,
  title={Broad twitter corpus: A diverse named entity recognition resource},
  author={Derczynski, Leon and Bontcheva, Kalina and Roberts, Ian},
  booktitle={Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers},
  pages={1169--1179},
  year={2016}
}
```

### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
