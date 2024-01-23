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
- 1K<n<10K
source_datasets: []
task_categories:
- token-classification
task_ids:
- named-entity-recognition
paperswithcode_id: ipm-nel
pretty_name: IPM NEL (Derczynski)
tags:
- named-entity-linking
---

# Dataset Card for "ipm-nel"

## Table of Contents
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

- **Homepage:** []()
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [http://www.derczynski.com/papers/ner_single.pdf](http://www.derczynski.com/papers/ner_single.pdf)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 120 KB
- **Size of the generated dataset:** 
- **Total amount of disk used:** 

### Dataset Summary

This data is for the task of named entity recognition and linking/disambiguation over tweets. It comprises
the addition of an entity URI layer on top of an NER-annotated tweet dataset. The task is to detect entities
and then provide a correct link to them in DBpedia, thus disambiguating otherwise ambiguous entity surface
forms; for example, this means linking "Paris" to the correct instance of a city named that (e.g. Paris, 
France vs. Paris, Texas).

The data concentrates on ten types of named entities: company, facility, geographic location, movie, musical
artist, person, product, sports team, TV show, and other.

The file is tab separated, in CoNLL format, with line breaks between tweets.

* Data preserves the tokenisation used in the Ritter datasets.
* PoS labels are not present for all tweets, but where they could be found in the Ritter data, they're given. 
* In cases where a URI could not be agreed, or was not present in DBpedia, the linking URI is `NIL`.

See the paper, [Analysis of Named Entity Recognition and Linking for Tweets](http://www.derczynski.com/papers/ner_single.pdf) for a full description of the methodology.


### Supported Tasks and Leaderboards

* Dataset leaderboard on PWC: [Entity Linking on Derczynski](https://paperswithcode.com/sota/entity-linking-on-derczynski-1)

### Languages

English of unknown region (`bcp47:en`)

## Dataset Structure

### Data Instances

#### ipm_nel

- **Size of downloaded dataset files:** 120 KB
- **Size of the generated dataset:** 
- **Total amount of disk used:**

An example of 'train' looks as follows.

```
{
  'id': '0', 
  'tokens': ['#Astros', 'lineup', 'for', 'tonight', '.', 'Keppinger', 'sits', ',', 'Downs', 'plays', '2B', ',', 'CJ', 'bats', '5th', '.', '@alysonfooter', 'http://bit.ly/bHvgCS'], 
  'ner_tags': [9, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0],
  'uris': "['http://dbpedia.org/resource/Houston_Astros', '', '', '', '', 'http://dbpedia.org/resource/Jeff_Keppinger', '', '', 'http://dbpedia.org/resource/Brodie_Downs', '', '', '', 'NIL', '', '', '', '', '']" 
}
```


### Data Fields

- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels (`int`). Full tagset with indices:
- `uris`: a `list` of URIs (`string`) that disambiguate entities. Set to `NIL` when an entity has no DBpedia entry, or blank for outside-of-entity tokens.

### Data Splits

|  name   |train|
|---------|----:|
|ipm_nel|183 sentences|

## Dataset Creation

### Curation Rationale

To gather a social media benchmark for named entity linking that is sufficiently different from newswire data.

### Source Data

#### Initial Data Collection and Normalization

The data is partly harvested from that distributed by [Ritter / Named Entity Recognition in Tweets: An Experimental Study](https://aclanthology.org/D11-1141/),
and partly taken from Twitter by the authors.

#### Who are the source language producers?

English-speaking Twitter users, between October 2011 and September 2013

### Annotations

#### Annotation process

The authors were allocated documents and marked them for named entities (where these were not already present) and then attempted to find
the best-fitting DBpedia entry for each entity found. Each entity mention was labelled by a random set of three volunteers. 
The annotation task was mediated using Crowdflower (Biewald, 2012). Our interface design was to show each volunteer the text of the tweet, any URL links contained
therein, and a set of candidate targets from DBpedia. The volunteers were encouraged to click on the URL links from the
tweet, to gain addition context and thus ensure that the correct DBpedia URI is chosen by them. Candidate entities were
shown in random order, using the text from the corresponding DBpedia abstracts (where available) or the actual DBpedia
URI otherwise. In addition, the options ‘‘none of the above’’, ‘‘not an entity’’ and ‘‘cannot decide’’ were added, to allow the
volunteers to indicate that this entity mention has no corresponding DBpedia URI (none of the above), the highlighted text
is not an entity, or that the tweet text (and any links, if available) did not provide sufficient information to reliably disambiguate the entity mention.

#### Who are the annotators?

The annotators are 10 volunteer NLP researchers, from the authors and the authors' institutions.

### Personal and Sensitive Information

The data was public at the time of collection. User names are preserved.

## Considerations for Using the Data

### Social Impact of Dataset

There's a risk of user-deleted content being in this data. The data has NOT been vetted for any content, so there's a risk of harmful text.

### Discussion of Biases

The data is annotated by NLP researchers; we know that this group has high agreement but low recall on English twitter text [C16-1111](https://aclanthology.org/C16-1111/).

### Other Known Limitations

The above limitations apply.

## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. You must
acknowledge the author if you use this data, but apart from that, you're quite
free to do most things. See https://creativecommons.org/licenses/by/4.0/legalcode .


### Citation Information

```
@article{derczynski2015analysis,
  title={Analysis of named entity recognition and linking for tweets},
  author={Derczynski, Leon and Maynard, Diana and Rizzo, Giuseppe and Van Erp, Marieke and Gorrell, Genevieve and Troncy, Rapha{\"e}l and Petrak, Johann and Bontcheva, Kalina},
  journal={Information Processing \& Management},
  volume={51},
  number={2},
  pages={32--49},
  year={2015},
  publisher={Elsevier}
}
```


### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
