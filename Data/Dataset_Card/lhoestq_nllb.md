# Dataset Card for No Language Left Behind (NLLB - 200vo)

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

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** https://arxiv.org/pdf/2207.0467
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset was created based on [metadata](https://github.com/facebookresearch/fairseq/tree/nllb) for mined bitext released by Meta AI.  It contains bitext for 148 English-centric and 1465 non-English-centric language pairs using the stopes mining library and the LASER3 encoders (Heffernan et al., 2022). 


#### How to use the data
There are two ways to access the data:
* Via the Hugging Face Python datasets library 
```
from datasets import load_dataset
dataset = load_dataset("allenai/nllb")
```

For accessing a particular [language pair]((https://huggingface.co/datasets/allenai/nllb/blob/main/nllb_lang_pairs.py)):
```
from datasets import load_dataset
dataset = load_dataset("allenai/nllb", "ace_Latn-ban_Latn")
```

* Clone the git repo
```
git lfs install
git clone https://huggingface.co/datasets/allenai/nllb
```

### Supported Tasks and Leaderboards

N/A

### Languages

Language pairs can be found [here](https://huggingface.co/datasets/allenai/nllb/blob/main/nllb_lang_pairs.py).

## Dataset Structure

The dataset contains gzipped tab delimited text files for each direction.  Each text file contains lines with parallel sentences.


### Data Instances

[More Information Needed]

### Data Fields

Every instance for a language pair contains the following fields: 'translation' (containing sentence pairs), 'laser_score', 'source_sentence_lid', 'target_sentence_lid', where 'lid' is language classification probability, 'source_sentence_source', 'source_sentence_url', 'target_sentence_source', 'target_sentence_url'.

* Sentence in first language
* Sentence in second language
* LASER score
* Language ID score for first sentence
* Language ID score for second sentence
* First sentence source (https://github.com/facebookresearch/LASER/tree/main/data/nllb200) 
* First sentence URL if the source is crawl-data/\*; _ otherwise
* Second sentence source
* Second sentence URL if the source is crawl-data/\*; _ otherwise

The lines are sorted by LASER3 score in decreasing order.

Example:
```
{'translation': {'ace_Latn': 'Gobnyan hana geupeukeucewa gata atawa geutinggai meunan mantong gata."',
  'ban_Latn': 'Ida nenten jaga manggayang wiadin ngutang semeton."'},
 'laser_score': 1.2499876022338867,
 'source_sentence_lid': 1.0000100135803223,
 'target_sentence_lid': 0.9991400241851807,
 'source_sentence_source': 'paracrawl9_hieu',
 'source_sentence_url': '_',
 'target_sentence_source': 'crawl-data/CC-MAIN-2020-10/segments/1581875144165.4/wet/CC-MAIN-20200219153707-20200219183707-00232.warc.wet.gz',
 'target_sentence_url': 'https://alkitab.mobi/tb/Ula/31/6/\n'}
```

### Data Splits

The data is not split.  Given the noisy nature of the overall process, we recommend using the data only for training and use other datasets like [Flores-200](https://github.com/facebookresearch/flores) for the evaluation. The data includes some development and test sets from other datasets, such as xlsum.  In addition, sourcing data from multiple web crawls is likely to produce incidental overlap with other test sets.


## Dataset Creation

### Curation Rationale

Data was filtered based on language identification, emoji based filtering, and for some high-resource languages using a language model. For more details on data filtering please refer to Section 5.2 (NLLB Team et al., 2022).


### Source Data


#### Initial Data Collection and Normalization

Monolingual data was collected from the following sources: 

| Name in data     | Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| afriberta        | https://github.com/castorini/afriberta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| americasnlp      | https://github.com/AmericasNLP/americasnlp2021/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| bho_resources    | https://github.com/shashwatup9k/bho-resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| crawl-data/*     | WET files from https://commoncrawl.org/the-data/get-started/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| emcorpus         | http://lepage-lab.ips.waseda.ac.jp/en/projects/meiteilon-manipuri-language-resources/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| fbseed20220317   | https://github.com/facebookresearch/flores/tree/main/nllb_seed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| giossa_mono      | https://github.com/sgongora27/giossa-gongora-guarani-2021                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| iitguwahati      | https://github.com/priyanshu2103/Sanskrit-Hindi-Machine-Translation/tree/main/parallel-corpus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| indic            | https://indicnlp.ai4bharat.org/corpora/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| lacunaner        | https://github.com/masakhane-io/lacuna_pos_ner/tree/main/language_corpus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| leipzig          | Community corpora from https://wortschatz.uni-leipzig.de/en/download for each year available                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| lowresmt2020     | https://github.com/panlingua/loresmt-2020                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| masakhanener     | https://github.com/masakhane-io/masakhane-ner/tree/main/MasakhaNER2.0/data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| nchlt            | https://repo.sadilar.org/handle/20.500.12185/299 <br>https://repo.sadilar.org/handle/20.500.12185/302 <br>https://repo.sadilar.org/handle/20.500.12185/306 <br>https://repo.sadilar.org/handle/20.500.12185/308 <br>https://repo.sadilar.org/handle/20.500.12185/309 <br>https://repo.sadilar.org/handle/20.500.12185/312 <br>https://repo.sadilar.org/handle/20.500.12185/314 <br>https://repo.sadilar.org/handle/20.500.12185/315 <br>https://repo.sadilar.org/handle/20.500.12185/321 <br>https://repo.sadilar.org/handle/20.500.12185/325 <br>https://repo.sadilar.org/handle/20.500.12185/328 <br>https://repo.sadilar.org/handle/20.500.12185/330 <br>https://repo.sadilar.org/handle/20.500.12185/332 <br>https://repo.sadilar.org/handle/20.500.12185/334 <br>https://repo.sadilar.org/handle/20.500.12185/336 <br>https://repo.sadilar.org/handle/20.500.12185/337 <br>https://repo.sadilar.org/handle/20.500.12185/341 <br>https://repo.sadilar.org/handle/20.500.12185/343 <br>https://repo.sadilar.org/handle/20.500.12185/346 <br>https://repo.sadilar.org/handle/20.500.12185/348 <br>https://repo.sadilar.org/handle/20.500.12185/353 <br>https://repo.sadilar.org/handle/20.500.12185/355 <br>https://repo.sadilar.org/handle/20.500.12185/357 <br>https://repo.sadilar.org/handle/20.500.12185/359 <br>https://repo.sadilar.org/handle/20.500.12185/362 <br>https://repo.sadilar.org/handle/20.500.12185/364  |
| paracrawl-2022-* | https://data.statmt.org/paracrawl/monolingual/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| paracrawl9*      | https://paracrawl.eu/moredata the monolingual release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pmi              | https://data.statmt.org/pmindia/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| til              | https://github.com/turkic-interlingua/til-mt/tree/master/til_corpus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| w2c              | https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0022-6133-9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| xlsum            | https://github.com/csebuetnlp/xl-sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

#### Who are the source language producers?

Text was collected from the web and various monolingual data sets, many of which are also web crawls.  This may have been written by people, generated by templates, or in some cases be machine translation output. 

### Annotations

#### Annotation process

Parallel sentences in the monolingual data were identified using LASER3 encoders. (Heffernan et al., 2022)

#### Who are the annotators?

The data was not human annotated.

### Personal and Sensitive Information

Data may contain personally identifiable information, sensitive content, or toxic content that was publicly shared on the Internet.  

## Considerations for Using the Data

### Social Impact of Dataset

This dataset provides data for training machine learning systems for many languages that have low resources available for NLP.

### Discussion of Biases

Biases in the data have not been specifically studied, however as the original source of data is World Wide Web it is likely that the data has biases similar to those prevalent in the Internet. The data may also exhibit biases introduced by language identification and data filtering techniques; lower resource languages generally have lower accuracy.  

### Other Known Limitations

Some of the translations are in fact machine translations.  While some website machine translation tools are identifiable from HTML source, these tools were not filtered out en mass because raw HTML was not available from some sources and CommonCrawl processing started from WET files. 

## Additional Information

### Dataset Curators

The data was not curated.

### Licensing Information

The dataset is released under the terms of [ODC-BY](https://opendatacommons.org/licenses/by/1-0/). By using this, you are also bound to the respective Terms of Use and License of the original source.


### Citation Information

Hefferman et al, Bitext Mining Using Distilled Sentence Representations for Low-Resource Languages. Arxiv https://arxiv.org/abs/2205.12654, 2022.<br>
NLLB Team et al, No Language Left Behind: Scaling Human-Centered Machine Translation, Arxiv https://arxiv.org/abs/2207.04672, 2022.

### Contributions

We thank the NLLB Meta AI team for open sourcing the meta data and instructions on how to use it with special thanks to  Bapi Akula, Pierre Andrews, Onur Çelebi, Sergey Edunov, Kenneth Heafield, Philipp Koehn, Alex Mourachko, Safiyyah Saleem, Holger Schwenk, and Guillaume Wenzek. We also thank the AllenNLP team at AI2 for hosting and releasing this data, including Akshita Bhagia (for engineering efforts to host the data, and create the huggingface dataset), and Jesse Dodge (for organizing the connection).