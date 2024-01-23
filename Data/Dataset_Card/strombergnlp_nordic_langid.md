---
annotations_creators:
- found
language_creators:
- found
language:
- da
- nn
- nb
- fo
- is
- sv
license:
- cc-by-sa-3.0
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
task_ids: []
paperswithcode_id: nordic-langid
pretty_name: Nordic Language ID for Distinguishing between Similar Languages
tags:
- language-identification
---

# Dataset Card for nordic_langid

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

- **Homepage:** [https://github.com/StrombergNLP/NordicDSL](https://github.com/StrombergNLP/NordicDSL)
- **Repository:** [https://github.com/StrombergNLP/NordicDSL](https://github.com/StrombergNLP/NordicDSL)
- **Paper:** [https://aclanthology.org/2021.vardial-1.8/](https://aclanthology.org/2021.vardial-1.8/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [René Haas](mailto:renha@itu.dk)

### Dataset Summary

Automatic language identification is a challenging problem. Discriminating
between closely related languages is especially difficult. This paper presents
a machine learning approach for automatic language identification for the
Nordic languages, which often suffer miscategorisation by existing 
state-of-the-art tools. Concretely we will focus on discrimination between six 
Nordic language: Danish, Swedish, Norwegian (Nynorsk), Norwegian (Bokmål), 
Faroese and Icelandic.

This is the data for the tasks. Two variants are provided: 10K and 50K, with
holding 10,000 and 50,000 examples for each language respectively.

For more info, see the paper: [Discriminating Between Similar Nordic Languages](https://aclanthology.org/2021.vardial-1.8/).

### Supported Tasks and Leaderboards

*

### Languages

This dataset is in six similar Nordic language:

- Danish, `da`
- Faroese, `fo`
- Icelandic, `is`
- Norwegian Bokmål, `nb`
- Norwegian Nynorsk, `nn`
- Swedish, `sv`

## Dataset Structure

The dataset has two parts, one with 10K samples per language and another with 50K per language.
The original splits and data allocation used in the paper is presented here.

### Data Instances

[Needs More Information]

### Data Fields

- `id`: the sentence's unique identifier, `string`
- `sentence`: the test to be classifier, a `string`
- `language`: the class, one of `da`, `fo`, `is`, `nb`, `no`, `sv`.

### Data Splits

Train and Test splits are provided, divided using the code provided with the paper.

## Dataset Creation

### Curation Rationale

Data is taken from Wikipedia and Tatoeba from each of these six languages.

### Source Data

#### Initial Data Collection and Normalization

**Data collection** Data was scraped from Wikipedia. We downloaded summaries for randomly chosen Wikipedia
articles in each of the languages, saved as raw text
to six .txt files of about 10MB each.
The 50K section is extended with Tatoeba data, which provides a different register to Wikipedia text, and then topped up with more Wikipedia data.

**Extracting Sentences** The first pass in sentence
tokenisation is splitting by line breaks. We then extract shorter sentences with the sentence tokenizer
(sent_tokenize) function from NLTK (Loper
and Bird, 2002). This does a better job than just
splitting by ’.’ due to the fact that abbreviations,
which can appear in a legitimate sentence, typically
include a period symbol.

**Cleaning characters** The initial data set has
many characters that do not belong to the alphabets of the languages we work with. Often the
Wikipedia pages for people or places contain names
in foreign languages. For example a summary
might contain Chinese or Russian characters which
are not strong signals for the purpose of discriminating between the target languages.
Further, it can be that some characters in the
target languages are mis-encoded. These misencodings are also not likely to be intrinsically
strong or stable signals.
To simplify feature extraction, and to reduce the
size of the vocabulary, the raw data is converted
to lowercase and stripped of all characters which
are not part of the standard alphabet of the six
languages using a character whitelist.

#### Who are the source language producers?

The source language is from Wikipedia contributors and Tatoeba contributors.

### Annotations

#### Annotation process

The annotations were found. 

#### Who are the annotators?

The annotations were found. They are determined by which language section a contributor posts their content to.

### Personal and Sensitive Information

The data hasn't been checked for PII, and is already all public. Tatoeba is is based on translations of synthetic conversational turns and is unlikely to bear personal or sensitive information.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is intended to help correctly identify content in the languages of six minority languages. Existing systems often confuse these, especially Bokmål and Danish or Icelandic and Faroese. However, some dialects are missed (for example Bornholmsk) and the closed nature of the classification task thus excludes speakers of these languages without recognising their existence.

### Discussion of Biases

The text comes from only two genres, so might not transfer well to other domains.

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

The data here is licensed CC-BY-SA 3.0. If you use this data, you MUST state its origin.

### Citation Information

````
@inproceedings{haas-derczynski-2021-discriminating,
    title = "Discriminating Between Similar Nordic Languages",
    author = "Haas, Ren{\'e}  and
      Derczynski, Leon",
    booktitle = "Proceedings of the Eighth Workshop on NLP for Similar Languages, Varieties and Dialects",
    month = apr,
    year = "2021",
    address = "Kiyv, Ukraine",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.vardial-1.8",
    pages = "67--75",
}
```
