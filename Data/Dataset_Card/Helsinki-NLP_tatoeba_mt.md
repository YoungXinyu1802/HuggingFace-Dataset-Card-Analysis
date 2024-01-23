---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- af
- ar
- az
- be
- bg
- bn
- br
- bs
- ca
- ch
- cs
- cv
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fo
- fr
- fy
- ga
- gd
- gl
- gn
- he
- hi
- hr
- hu
- hy
- ia
- id
- ie
- io
- is
- it
- ja
- jv
- ka
- kk
- km
- ko
- ku
- kw
- la
- lb
- lt
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- nb
- nl
- nn
- 'no'
- oc
- pl
- pt
- qu
- rn
- ro
- ru
- sh
- sl
- sq
- sr
- sv
- sw
- ta
- te
- th
- tk
- tl
- tr
- tt
- ug
- uk
- ur
- uz
- vi
- vo
- yi
- zh
license:
- cc-by-2.0
multilinguality:
- translation
pretty_name: The Tatoeba Translation Challenge
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
---

# Dataset Card for [Dataset Name]

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

- **Homepage:** https://github.com/Helsinki-NLP/Tatoeba-Challenge/
- **Repository:** https://github.com/Helsinki-NLP/Tatoeba-Challenge/
- **Paper:** [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/)
- **Leaderboard:**
- **Point of Contact:** [Jörg Tiedemann](mailto:jorg.tiedemann@helsinki.fi)

### Dataset Summary

The Tatoeba Translation Challenge is a multilingual data set of machine translation benchmarks derived from user-contributed translations collected by [Tatoeba.org](https://tatoeba.org/) and provided as parallel corpus from [OPUS](https://opus.nlpl.eu/). This dataset includes test and development data sorted by language pair. It includes test sets for hundreds of language pairs and is continuously updated. Please, check the version number tag to refer to the release that your are using.

### Supported Tasks and Leaderboards

The translation task is described in detail in the [Tatoeba-Challenge repository](https://github.com/Helsinki-NLP/Tatoeba-Challenge) and covers various sub-tasks with different data coverage and resources. [Training data](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/data/README.md) is also available from the same repository and [results](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/results/tatoeba-results-all.md) are published and collected as well. [Models](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/results/tatoeba-models-all.md) are also released for public use and are also partially available from the [huggingface model hub](https://huggingface.co/Helsinki-NLP).


### Languages

The data set covers hundreds of languages and language pairs and are organized by ISO-639-3 languages. The current release covers the following language: Afrikaans, Arabic, Azerbaijani, Belarusian, Bulgarian, Bengali, Breton, Bosnian, Catalan, Chamorro, Czech, Chuvash, Welsh, Danish, German, Modern Greek, English, Esperanto, Spanish, Estonian, Basque, Persian, Finnish, Faroese, French, Western Frisian, Irish, Scottish Gaelic, Galician, Guarani, Hebrew, Hindi, Croatian, Hungarian, Armenian, Interlingua, Indonesian, Interlingue, Ido, Icelandic, Italian, Japanese, Javanese, Georgian, Kazakh, Khmer, Korean, Kurdish, Cornish, Latin, Luxembourgish, Lithuanian, Latvian, Maori, Macedonian, Malayalam, Mongolian, Marathi, Malay, Maltese, Burmese, Norwegian Bokmål, Dutch, Norwegian Nynorsk, Norwegian, Occitan, Polish, Portuguese, Quechua, Rundi, Romanian, Russian, Serbo-Croatian, Slovenian, Albanian, Serbian, Swedish, Swahili, Tamil, Telugu, Thai, Turkmen, Tagalog, Turkish, Tatar, Uighur, Ukrainian, Urdu, Uzbek, Vietnamese, Volapük, Yiddish, Chinese


## Dataset Structure

### Data Instances

Data instances are given as translation units in TAB-separated files with four columns: source and target language ISO-639-3 codes, source language text and target language text. Note that we do not imply a translation direction and consider the data set to be symmetric and to be used as a test set in both directions. Language-pair-specific subsets are only provided under the label of one direction using sorted ISO-639-3 language IDs.

Some subsets contain several sub-languages or language variants. They may refer to macro-languages such as Serbo-Croatian languages that are covered by the ISO code `hbs`. Language variants may also include different writing systems and in that case the ISO15924 script codes are attached to the language codes. Here are a few examples from the English to Serbo-Croation test set including examples for Bosnian, Croatian and Serbian in Cyrillic and in Latin scripts:

```
eng	bos_Latn	Children are the flowers of our lives.	Djeca su cvijeće našeg života.
eng	hrv	A bird was flying high up in the sky.	Ptica je visoko letjela nebom.
eng	srp_Cyrl	A bird in the hand is worth two in the bush.	Боље врабац у руци, него голуб на грани.
eng	srp_Latn	Canada is the motherland of ice hockey.	Kanada je zemlja-majka hokeja na ledu.
```

There are also data sets with sentence pairs in the same language. In most cases, those are variants with minor spelling differences but they also include rephrased sentences. Here are a few examples from the English test set:

```
eng     eng     All of us got into the car.     We all got in the car.
eng     eng     All of us hope that doesn't happen.     All of us hope that that doesn't happen.
eng     eng     All the seats are booked.       The seats are all sold out.
```


### Data Splits

Test and development data sets are disjoint with respect to sentence pairs but may include overlaps in individual source or target language sentences. Development data should not be used in training directly. The goal of the data splits is to create test sets of reasonable size with a large language coverage. Test sets include at most 10,000 instances. Development data do not exist for all language pairs.

To be comparable with other results, models should use the training data distributed from the [Tatoeba MT Challenge Repository](https://github.com/Helsinki-NLP/Tatoeba-Challenge/) including monolingual data sets also listed there.


## Dataset Creation

### Curation Rationale


The Tatoeba MT data set will be updated continuously and the data preparation procedures are also public and released on [github](https://github.com/Helsinki-NLP/Tatoeba-Challenge/). High language coverage is the main goal of the project and data sets are prepared to be consistent and systematic with standardized language labels and distribution formats.


### Source Data

#### Initial Data Collection and Normalization

The Tatoeba data sets are collected from user-contributed translations submitted to [Tatoeba.org](https://tatoeba.org/) and compiled into a multi-parallel corpus in [OPUS](https://opus.nlpl.eu/Tatoeba.php). The test and development sets are incrementally updated with new releases of the Tatoeba data collection at OPUS. New releases extend the existing data sets. Test sets should not overlap with any of the released development data sets.


#### Who are the source language producers?

The data sets come from [Tatoeba.org](https://tatoeba.org/), which provides a large database of sentences and their translations into a wide varity of languages. Its content is constantly growing as a result of voluntary contributions of thousands of users.
The original project was founded by Trang Ho in 2006, hosted on Sourceforge under the codename of multilangdict. 


### Annotations

#### Annotation process

Sentences are translated by volunteers and the Tatoeba database also provides additional metadata about each record including user ratings etc. However, the metadata is currently not used in any way for the compilation of the MT benchmark. Language skills of contributors naturally vary quite a bit and not all translations are done by native speakers of the target language. More information about the contributions can be found at [Tatoeba.org](https://tatoeba.org/).


#### Who are the annotators?

### Personal and Sensitive Information

For information about handling personal and sensitive information we refer to the [original provider](https://tatoeba.org/) of the data. This data set has not been processed in any way to detect or remove potentially sensitve or personal information.

## Considerations for Using the Data

### Social Impact of Dataset

The language coverage is high and with that it represents a highly valuable resource for machine translation development especially for lesser resourced languages and language pairs. The constantly growing database also represents a dynamic resource and its value wil grow further.


### Discussion of Biases

The original source lives from its contributors and there interest and background will to certain subjective and cultural biases. Language coverage and translation quality is also biased by the skills of the contributors.


### Other Known Limitations

The sentences are typically quite short and, therefore, rather easy to translate. For high-resource languages, this leads to results that will be less useful than more challenging benchmarks. For lesser resource language pairs, the limited complexity of the examples is actually a good thing to measure progress even in very challenging setups.


## Additional Information

### Dataset Curators

The data set is curated by the University of Helsinki and its [language technology research group](https://blogs.helsinki.fi/language-technology/). Data and tools used for creating and using the resource are [open source](https://github.com/Helsinki-NLP/Tatoeba-Challenge/) and will be maintained as part of the [OPUS ecosystem](https://opus.nlpl.eu/) for parallel data and machine translation research.


### Licensing Information

The data sets are distributed under the same licence agreement as the original Tatoeba database using a
[CC-BY 2.0 license](https://creativecommons.org/licenses/by/2.0/fr/). More information about the terms of use of the original data sets is listed [here](https://tatoeba.org/eng/terms_of_use).


### Citation Information

If you use the data sets then, please, cite the following paper: [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/)

```
@inproceedings{tiedemann-2020-tatoeba,
    title = "The Tatoeba Translation Challenge {--} Realistic Data Sets for Low Resource and Multilingual {MT}",
    author = {Tiedemann, J{\"o}rg},
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.wmt-1.139",
    pages = "1174--1182",
}
```

### Contributions

Thanks to [@jorgtied](https://github.com/jorgtied) and [@Helsinki-NLP](https://github.com/Helsinki-NLP) for adding this dataset.
Thanks also to [CSC Finland](https://www.csc.fi/en/solutions-for-research) for providing computational resources and storage space for the work on OPUS and other MT projects.
