---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- af
- am
- ar
- arz
- as
- az
- azb
- ba
- be
- bg
- bn
- bo
- br
- ca
- ce
- ceb
- ckb
- cs
- cv
- cy
- da
- de
- dv
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lb
- lo
- lt
- lv
- mg
- mhr
- mk
- ml
- mn
- mr
- ms
- mt
- my
- nds
- ne
- nl
- nn
- 'no'
- or
- os
- pa
- pl
- pnb
- ps
- pt
- ro
- ru
- sa
- sah
- sd
- sh
- si
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- te
- tg
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
- yi
- zh
license:
- cc0-1.0
multilinguality:
- multilingual
source_datasets:
- oscar
task_categories:
- text-generation
task_ids:
- language-modeling
paperswithcode_id: oscar
pretty_name: OSCAR
---

## WARNING: this dataset is an extract of the OSCAR dataset published here to simulate the use of the full dataset in low-resource contexts.
Using this dataset is equivalent to using a processed version of OSCAR legally speaking. I take no credit for the gathering of the original data and hence refer entirely to the original dataset in the card below.

# Dataset Card for "oscar"

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

- **Homepage:** [https://oscar-corpus.com](https://oscar-corpus.com)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

OSCAR or **O**pen **S**uper-large **C**rawled [**A**LMAnaCH](https://team.inria.fr/almanach/) co**R**pus is a huge multilingual corpus obtained by language classification and filtering of the [Common Crawl](https://commoncrawl.org/) corpus using the [goclassy](https://github.com/pjox/goclassy) architecture. Data is distributed by language in both original and deduplicated form.

### Supported Tasks and Leaderboards

OSCAR is mainly inteded to pretrain language models and word represantations.

### Languages

All the data is distributed by language, both the original and the deduplicated versions of the data are available. 166 different languages are available. The table in subsection [Data Splits Sample Size](#data-splits-sample-size) provides the language code for each subcorpus as well as the number of words (space separated tokens), lines and sizes for both the original and the deduplicated versions of OSCAR.

## Dataset Structure

We show detailed information for all the configurations of the dataset.

## Dataset Creation

### Curation Rationale

OSCAR was constructed new pipeline derived from the [fastText's one](https://github.com/facebookresearch/fastText), called [_goclassy_](https://github.com/pjox/goclassy). Goclassy reuses the [fastText linear classifier](https://fasttext.cc) and the pre-trained fastText model for language recognition, but it completely rewrites and parallelises their pipeline in an asynchronous manner.

The order of operations is more or less the same as in the fastText pre-processing pipeline but instead of clustering multiple operations into a single blocking process, a worker is launched for each operation but bounding the number of possible parallel operations at a given time by the number of available threads instead of the number of CPUs. Goclassy is implemented in the [Go programming language](https://golang.org/) so it lets the [Go runtime](https://golang.org/src/runtime/mprof.go) handle the scheduling of the processes. Thus the goclassy's pipeline one does not have to wait for a whole WET file to download, decompress and classify in order to start downloading and processing the next one, a new file will start downloading and processing as soon as the scheduler is able to allocate a new process.

Filtering and cleaning processes at line level are done before feeding each line to the classifier. Lines shorter than 100 UTF-8 characters and lines containing invalid UTF-8 characters are discarted and are not classified. After all files are proccesed the deduplicated versions are constructed and everything is then splitted in shards and compressed.

### Source Data

#### Initial Data Collection and Normalization

[Common Crawl](https://commoncrawl.org/) is a non-profit foundation which produces and maintains an open repository of web crawled data that is both accessible and analysable. Common Crawl's complete web archive consists of petabytes of data collected over 8 years of web crawling. The repository contains raw web page HTML data (WARC files), metdata extracts (WAT files) and plain text extracts (WET files). The organisation's crawlers has always respected [nofollow](http://microformats.org/wiki/rel-nofollow) and [robots.txt](https://www.robotstxt.org/) policies.

Each monthly Common Crawl snapshot is in itself a massive multilingual corpus, where every single file contains data coming from multiple web pages written in a large variety of languages and covering all possible types of topics.

To construct OSCAR the WET files of Common Crawl were used. These contain the extracted plain texts from the websites mostly converted to UTF-8, as well as headers containing the metatada of each crawled document. Each WET file comes compressed in gzip format and is stored on Amazon Web Services. In the case of OSCAR, the **November 2018** snapshot was used. It surpasses 20TB of uncompressed data and contains more than 50 thousand plain text files where each file consists of the plain text from multiple websites along its metadata header.

#### Who are the source language producers?

The data comes from multiple web pages in a large variety of languages.

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

N/A

#### Who are the annotators?

N/A

### Personal and Sensitive Information

Being constructed from Common Crawl, Personal and sensitive information might be present. This **must** be considered before training deep learning models with OSCAR, specially in the case of text-generation models.

## Considerations for Using the Data

### Social Impact of Dataset

OSCAR is intended to bring more data to a wide variety of lanuages, the aim of the corpus is to make large amounts of data available to lower resource languages in order to facilitate the pre-training of state-of-the-art language modeling architectures.

### Discussion of Biases

OSCAR is not properly filtered yet and this can be reflected on the models trained with it. Care is advised specially concerning biases of the resulting models.

### Other Known Limitations

The [fastText linear classifier](https://fasttext.cc) is limed both in performance and the variety of languages it can recognize, so the quality of some OSCAR sub-corpora might be lower than expected, specially for the lowest-resource langiuages. Some audits have already been done by [third parties](https://arxiv.org/abs/2010.14571).

## Additional Information

### Dataset Curators

The corpus was put together by [Pedro J. Ortiz](https://pjortiz.eu/), [BenoÃ®t Sagot](http://pauillac.inria.fr/~sagot/), and [Laurent Romary](https://cv.archives-ouvertes.fr/laurentromary), during work done at [Inria](https://www.inria.fr/en), particularly at the [ALMAnaCH team](https://team.inria.fr/almanach/).

### Licensing Information

    These data are released under this licensing scheme
    We do not own any of the text from which these data has been extracted.
    We license the actual packaging of these data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/
    To the extent possible under law, Inria has waived all copyright and related or neighboring rights to OSCAR
    This work is published from: France.

    Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:
    * Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
    * Clearly identify the copyrighted work claimed to be infringed.
    * Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

    We will comply to legitimate requests by removing the affected sources from the next release of the corpus.

### Citation Information

```
@inproceedings{ortiz-suarez-etal-2020-monolingual,
    title = "A Monolingual Approach to Contextualized Word Embeddings for Mid-Resource Languages",
    author = "Ortiz Su{'a}rez, Pedro Javier  and
      Romary, Laurent  and
      Sagot, Benoit",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.156",
    pages = "1703--1714",
    abstract = "We use the multilingual OSCAR corpus, extracted from Common Crawl via language classification, filtering and cleaning, to train monolingual contextualized word embeddings (ELMo) for five mid-resource languages. We then compare the performance of OSCAR-based and Wikipedia-based ELMo embeddings for these languages on the part-of-speech tagging and parsing tasks. We show that, despite the noise in the Common-Crawl-based OSCAR data, embeddings trained on OSCAR perform much better than monolingual embeddings trained on Wikipedia. They actually equal or improve the current state of the art in tagging and parsing for all five languages. In particular, they also improve over multilingual Wikipedia-based contextual embeddings (multilingual BERT), which almost always constitutes the previous state of the art, thereby showing that the benefit of a larger, more diverse corpus surpasses the cross-lingual benefit of multilingual embedding architectures.",
}

@inproceedings{OrtizSuarezSagotRomary2019,
  author    = {Pedro Javier {Ortiz Su{'a}rez} and Benoit Sagot and Laurent Romary},
  title     = {Asynchronous pipelines for processing huge corpora on medium to low resource infrastructures},
  series = {Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-7) 2019. Cardiff, 22nd July 2019},
  editor    = {Piotr BaÅ„ski and Adrien Barbaresi and Hanno Biber and Evelyn Breiteneder and Simon Clematide and Marc Kupietz and Harald L{"u}ngen and Caroline Iliadi},
  publisher = {Leibniz-Institut f{"u}r Deutsche Sprache},
  address   = {Mannheim},
  doi       = {10.14618/ids-pub-9021},
  url       = {http://nbn-resolving.de/urn:nbn:de:bsz:mh39-90215},
  pages     = {9 -- 16},
  year      = {2019},
  abstract  = {Common Crawl is a considerably large, heterogeneous multilingual corpus comprised of crawled documents from the internet, surpassing 20TB of data and distributed as a set of more than 50 thousand plain text files where each contains many documents written in a wide variety of languages. Even though each document has a metadata block associated to it, this data lacks any information about the language in which each document is written, making it extremely difficult to use Common Crawl for monolingual applications. We propose a general, highly parallel, multithreaded pipeline to clean and classify Common Crawl by language; we specifically design it so that it runs efficiently on medium to low resource infrastructures where I/O speeds are the main constraint. We develop the pipeline so that it can be easily reapplied to any kind of heterogeneous corpus and so that it can be parameterised to a wide range of infrastructures. We also distribute a 6.3TB version of Common Crawl, filtered, classified by language, shuffled at line level in order to avoid copyright issues, and ready to be used for NLP applications.},
  language  = {en}
}

```

### Contributions

Thanks to [@pjox](https://github.com/pjox) and [@lhoestq](https://github.com/lhoestq) for adding this dataset.
