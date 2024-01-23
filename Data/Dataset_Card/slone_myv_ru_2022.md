---
annotations_creators:
- found
- machine-generated
language:
- myv
- ru
language_creators:
- found
- machine-generated
license:
- cc-by-sa-4.0
multilinguality:
- translation
pretty_name: Erzya-Russian parallel corpus
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- erzya
- mordovian
task_categories:
- translation
task_ids: []
---

# Dataset Card for **slone/myv_ru_2022**

## Dataset Description

- **Repository:** https://github.com/slone-nlp/myv-nmt
- **Paper:**: https://arxiv.org/abs/2209.09368
- **Point of Contact:** @cointegrated

### Dataset Summary

This is a corpus of parallel Erzya-Russian words, phrases and sentences, collected in the paper [The first neural machine translation system for the Erzya language](https://arxiv.org/abs/2209.09368).

Erzya (`myv`) is a language from the Uralic family. It is spoken primarily in the Republic of Mordovia and some other regions of Russia and other post-Soviet countries. We use the Cyrillic version of its script. 

The corpus consists of the following parts:

| name | size | composition | 
| -----| ---- | -------|
|train | 74503 | parallel words, phrases and sentences, mined from dictionaries, books and web texts | 
| dev  | 1500  | parallel sentences mined from books and web texts | 
| test | 1500  | parallel sentences mined from books and web texts | 
| mono | 333651| Erzya sentences mined from books and web texts, translated to Russian by a neural model | 

The dev and test splits contain sentences from the following sources

| name | size | description| 
| ---------------|----| -------|
|wiki            |600 | Aligned sentences from linked Erzya and Russian Wikipedia articles |
|bible           |400 | Paired verses from the Bible (https://finugorbib.com) |
|games           |250 | Aligned sentences from the book *"Сказовые формы мордовской литературы", И.И. Шеянова, 2017, НИИ гуманитарых наук при Правительстве Республики Мордовия, Саранск* |
|tales           |100 | Aligned sentences from the book *"Мордовские народные игры", В.С. Брыжинский, 2009, Мордовское книжное издательство, Саранск* |
|fiction         |100 | Aligned sentences from modern Erzya prose and poetry (https://rus4all.ru/myv) |
|constitution    | 50 | Aligned sentences from the Soviet 1938 constitution |

To load the first three parts (train, validation and test), use the code:

```Python
from datasets import load_dataset
data = load_dataset('slone/myv_ru_2022')
```

To load all four parts (included the back-translated data), please specify the data files explicitly:
```Python
from datasets import load_dataset
data_extended = load_dataset(
    'slone/myv_ru_2022',
    data_files={'train':'train.jsonl', 'validation': 'dev.jsonl', 'test': 'test.jsonl', 'mono': 'back_translated.jsonl'}
)
```

### Supported Tasks and Leaderboards

- `translation`: the dataset may be used to train `ru-myv` translation models. There are no specific leaderboards for it yet, but if you feel like discussing it, welcome to the comments!

### Languages

The main part of the dataset (`train`, `dev` and `test`) consists of "natural" Erzya (Cyrillic) and Russian sentences, translated to the other language by humans. There is also a larger Erzya-only part of the corpus (`mono`), translated to Russian automatically.

## Dataset Structure

### Data Instances

All data instances have three string fields: `myv`, `ru` and `src` (the last one is currently meaningful only for dev and test splits), for example:
```
{'myv': 'Сюкпря Пазонтень, кие кирвазтизе Титэнь седейс тынк кисэ секе жо бажамонть, кона палы минек седейсэяк!',
 'ru': 'Благодарение Богу, вложившему в сердце Титово такое усердие к вам.',
 'src': 'bible'}
```

### Data Fields

- `myv`: the Erzya text (word, phrase, or sentence)
- `ru`: the corresponding Russian text
- `src`: the source of data (only for dev and test splits)

### Data Splits

- train: parallel sentences, words and phrases, collected from various sources. Most of them are aligned automatically. Noisy.
- dev: 1500 parallel sentences, selected from the 6 most reliable and diverse sources.
- test: same as dev. 
- mono: Erzya sentences collected from various sources, with the Russian counterpart generated by a neural machine translation model.

## Dataset Creation

### Curation Rationale

This is, as far as we know, the first publicly available parallel Russian-Erzya corpus, and the first medium-sized translation corpus for Erzya. 
We hope that it sets a meaningful baseline for Erzya machine translation.

### Source Data

#### Initial Data Collection and Normalization

The dataset was collected from various sources (see below). 

The texts were spit in sentences using the [razdel]() package. 
For some sources, sentences were filtered by language using the [slone/fastText-LID-323](https://huggingface.co/slone/fastText-LID-323) model.
For most of the sources, `myv` and `ru` sentences were aligned automatically using the [slone/LaBSE-en-ru-myv-v1](https://huggingface.co/slone/LaBSE-en-ru-myv-v1) sentence encoder 
and the code from [the paper repository](https://github.com/slone-nlp/myv-nmt).

#### Who are the source language producers?

The dataset comprises parallel `myv-ru` and monolingual `myv` texts from diverse sources:
- 12K parallel sentences from the Bible (http://finugorbib.com);
- 3K parallel Wikimedia sentences from OPUS;
- 42K parallel words or short phrases collected from various online dictionaries ();
- the Erzya Wikipedia and the corresponding articles from the Russian Wikipedia;
- 18 books, including 3 books with Erzya-Russian bitexts (http://lib.e-mordovia.ru);
- Soviet-time books and periodicals (https://fennougrica.kansalliskirjasto.fi);
- The Erzya part of Wikisource (https://wikisource.org/wiki/Main_Page/?oldid=895127);
- Short texts by modern Erzya authors (https://rus4all.ru/myv/);
- News articles from the Erzya Pravda website (http://erziapr.ru);
- Texts found in LiveJournal (https://www.livejournal.com) by searching with the 100 most frequent Erzya words.

### Annotations

No human annotation was involved in the data collection.

### Personal and Sensitive Information

All data was collected from public sources, so no sensitive information is expected in them. 
However, some sentences collected, for example, from news articles or LiveJournal posts, can contain personal data.

## Considerations for Using the Data

### Social Impact of Dataset

Publication of this dataset may attract some attention to the endangered Erzya language.

### Discussion of Biases

Most of the dataset has been collected by automatical means, so it may contain errors and noise. 
Some types of these errors are systemic: for example, the words for "Erzya" and "Russian" are often aligned together, 
because they appear in the corresponding Wikipedias on similar positions.

### Other Known Limitations

The dataset is noisy: some texts in it may be ungrammatical, in a wrong language, or poorly aligned.

## Additional Information

### Dataset Curators

The data was collected by David Dale (https://huggingface.co/cointegrated). 

### Licensing Information

The status of the dataset is not final, but after we check everything, we hope to be able to distribute it under the [CC-BY-SA license](http://creativecommons.org/licenses/by-sa/4.0/).

### Citation Information

[TBD]