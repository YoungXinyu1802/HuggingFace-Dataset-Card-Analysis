---
annotations_creators:
- no-annotation
language:
- en
- es
- pt
- ja
- ar
- in
- ko
- tr
- fr
- tl
- ru
- it
- th
- de
- hi
- pl
- nl
- fa
- et
- ht
- ur
- sv
- ca
- el
- fi
- cs
- iw
- da
- vi
- zh
- ta
- ro
- no
- uk
- cy
- ne
- hu
- eu
- sl
- lv
- lt
- bn
- sr
- bg
- mr
- ml
- is
- te
- gu
- kn
- ps
- ckb
- si
- hy
- or
- pa
- am
- sd
- my
- ka
- km
- dv
- lo
- ug
- bo
language_creators:
- found
license:
- mit
multilinguality:
- multilingual
pretty_name: Bernice Pretrain Data
size_categories:
- 1B<n<10B
source_datasets:
- original
tags:
- twitter
- slang
- code switch
- social
- social media
task_categories:
- other
task_ids: []
---

# Dataset Card for Bernice Pre-train Data

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

- **Homepage:** N/A
- **Repository:** https://github.com/JHU-CLSP/Bernice-Twitter-encoder
- **Paper:** _Bernice: A Multilingual Pre-trained Encoder for Twitter_ at [EMNLP 2022](https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.415)
- **Leaderboard:** N/A
- **Point of Contact:** Alexandra DeLucia aadelucia (at) jhu.edu

### Dataset Summary

Tweet IDs for the 2.5 billion multilingual tweets used to train Bernice, a Twitter encoder.
Read the paper [here](https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.415).
The tweets are from the public 1% Twitter API stream from January 2016 to December 2021. 
Twitter-provided language metadata is provided with the tweet ID. The data contains 66 unique languages, as identified by [ISO 639 language codes](https://www.wikiwand.com/en/List_of_ISO_639-1_codes), including `und` for undefined languages.
Tweets need to be re-gathered via the Twitter API. We suggest [Hydrator](https://github.com/DocNow/hydrator) or [tweepy](https://www.tweepy.org/).

To load with HuggingFace:

```python
from datasets import load_dataset
dataset = load_dataset("jhu-clsp/bernice-pretrain-data")

for i, row in enumerate(dataset["train"]):
    print(row)
    if i > 10:
        break
```

If you only want Indic languages, use

```python
dataset = load_dataset("jhu-clsp/bernice-pretrain-data", "indic")
```


### Supported Tasks and Leaderboards

N/A

### Languages

65 languages (ISO 639 codes shown below), plus an `und` (undefined) category. 
All language identification provided by Twitter API.

|    |     |    |    |    |     |    |
|----|-----|----|----|----|-----|----|
| en |  ru | ht | zh | bn |  ps | lt |
| es | bo  | ur | ta | sr | ckb | km |
| pt |  it | sv | ro | bg |  si | dv |
| ja |  th | ca | no | mr |  hy | lo |
| ar |  de | el | uk | ml |  or | ug |
| in |  hi | fi | cy | is |  pa |    |
| ko |  pl | cs | ne | te |  am |    |
| tr |  nl | iw | hu | gu |  sd |    |
| fr |  fa | da | eu | kn |  my |    |
| tl |  et | vi | sl | lv |  ka |    |

## Dataset Structure

### Data Instances

Data is provided in gzip'd files organized by year and month of tweet origin. 
Tweets are one per line, with fields separated by tabs.

### Data Fields

* `tweet ID`: ID of tweet
* `lang`: ISO 639 code of language, provided by Twitter metadata. Accuracy of label is not known.
* `year`: Year tweet was created. Year is also provided in the file names.

### Data Splits

[More Information Needed]


## Dataset Creation

### Curation Rationale

Data was gathered to support the training of Bernice, a multilingual pre-trained Twitter encoder.

### Source Data

#### Initial Data Collection and Normalization

Data was gathered via the Twitter API public 1% stream from January 2016 through December 2021. 
Tweets with less than three non-username or URL space-delimited words were removed.
All usernames and URLs were replaced with `@USER` and `HTTPURL`, respectively.

#### Who are the source language producers?

Data was produced by users on Twitter.

### Annotations

N/A

### Personal and Sensitive Information

As per Twitter guidelines, only tweet IDs and not full tweets are shared.
Tweets will only be accessible if user has not removed their account (or been banned), tweets were deleted or removed, or a user changed their account access to private.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]


## Additional Information

### Dataset Curators

Dataset gathered and processed by Mark Dredze, Alexandra DeLucia, Shijie Wu, Aaron Mueller, Carlos Aguirre, and Philip Resnik.

### Licensing Information

MIT

### Citation Information

Please cite the Bernice paper if you use this dataset:

> Alexandra DeLucia, Shijie Wu, Aaron Mueller, Carlos Aguirre, Philip Resnik, and Mark Dredze. 2022. Bernice: A Multilingual Pre-trained Encoder for Twitter. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 6191–6205, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

### Contributions

Dataset uploaded by [@AADeLucia](https://github.com/AADeLucia).
