---
annotations_creators:
- expert-generated
language:
- bm
- bbj
- ee
- fon
- ha
- ig
- rw
- lg
- luo
- mos
- ny
- pcm
- sn
- sw
- tn
- tw
- wo
- xh
- yo
- zu
language_creators:
- expert-generated
license:
- afl-3.0
multilinguality:
- multilingual
pretty_name: masakhaner2.0
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- ner
- masakhaner
- masakhane
task_categories:
- token-classification
task_ids:
- named-entity-recognition

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

- **Homepage:** [homepage](https://github.com/masakhane-io/masakhane-ner)
- **Repository:** [github](https://github.com/masakhane-io/masakhane-ner)
- **Paper:** [paper](https://arxiv.org/abs/2103.11811)
- **Point of Contact:** [Masakhane](https://www.masakhane.io/) or didelani@lsv.uni-saarland.de

### Dataset Summary

MasakhaNER 2.0 is the largest publicly available high-quality dataset for named entity recognition (NER) in 20 African languages created by the Masakhane community.

Named entities are phrases that contain the names of persons, organizations, locations, times and quantities. Example:

[PER Wolff] , currently a journalist in [LOC Argentina] , played with [PER Del Bosque] in the final years of the seventies in [ORG Real Madrid] .

MasakhaNER 2.0 is a named entity dataset consisting of PER, ORG, LOC, and DATE entities annotated by Masakhane for 20 African languages

The train/validation/test sets are available for all the 20 languages.

For more details see https://arxiv.org/abs/2210.12391


### Supported Tasks and Leaderboards

[More Information Needed]

- `named-entity-recognition`: The performance in this task is measured with [F1](https://huggingface.co/metrics/f1) (higher is better). A named entity is correct only if it is an exact match of the corresponding entity in the data.

### Languages

There are 20 languages available :
- Bambara (bam)
- Ghomala (bbj)
- Ewe (ewe)
- Fon (fon)
- Hausa (hau)
- Igbo (ibo)
- Kinyarwanda (kin)
- Luganda (lug)
- Dholuo (luo) 
- Mossi (mos)
- Chichewa (nya)
- Nigerian Pidgin
- chShona (sna)
- Kiswahili (swą)
- Setswana (tsn)
- Twi (twi)
- Wolof (wol)
- isiXhosa (xho)
- Yorùbá (yor)
- isiZulu (zul)

## Dataset Structure

### Data Instances

The examples look like this for Yorùbá:

```
from datasets import load_dataset
data = load_dataset('masakhane/masakhaner2', 'yor') 

# Please, specify the language code

# A data point consists of sentences seperated by empty line and tab-seperated tokens and tags. 
{'id': '0',
 'ner_tags': [B-DATE, I-DATE, 0, 0, 0, 0, 0, B-PER, I-PER, I-PER, O, O, O, O],
 'tokens': ['Wákàtí', 'méje', 'ti', 'ré', 'kọjá', 'lọ', 'tí', 'Luis', 'Carlos', 'Díaz', 'ti', 'di', 'awati', '.']
}
```

### Data Fields

- `id`: id of the sample
- `tokens`: the tokens of the example text
- `ner_tags`: the NER tags of each token

The NER tags correspond to this list:
```
"O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-DATE", "I-DATE",
```

In the NER tags, a B denotes the first item of a phrase and an I any non-initial word. There are four types of phrases: person names (PER), organizations (ORG), locations (LOC) and dates & time (DATE).

It is assumed that named entities are non-recursive and non-overlapping. In case a named entity is embedded in another named entity usually, only the top level entity is marked.

### Data Splits

For all languages, there are three splits.

The original splits were named `train`, `dev` and `test` and they correspond to the `train`, `validation` and `test` splits.

The splits have the following sizes :

| Language        | train | validation | test  |
|-----------------|------:|-----------:|------:|
| Bambara         |  4463 |        638 |  1274 |
| Ghomala         |  3384 |        483 |   966 |
| Ewe             |  3505 |        501 |  1001 |
| Fon.            |  4343 |        621 |  1240 |
| Hausa           |  5716 |        816 |  1633 |
| Igbo            |  7634 |       1090 |  2181 |
| Kinyarwanda     |  7825 |       1118 |  2235 |
| Luganda         |  4942 |        706 |  1412 |
| Luo             |  5161 |        737 |  1474 |
| Mossi           |  4532 |        648 |  1613 |
| Nigerian-Pidgin |  5646 |        806 |  1294 |
| Chichewa        |  6250 |        893 |  1785 |
| chiShona        |  6207 |        887 |  1773 |
| Kiswahili       |  6593 |        942 |  1883 |
| Setswana        |  3289 |        499 |   996 |
| Akan/Twi        |  4240 |        605 |  1211 |
| Wolof           |  4593 |        656 |  1312 |
| isiXhosa        |  5718 |        817 |  1633 |
| Yoruba          |  6877 |        983 |  1964 |
| isiZulu         |  5848 |        836 |  1670 |

## Dataset Creation

### Curation Rationale

The dataset was introduced to introduce new resources to 20 languages that were under-served for natural language processing.

[More Information Needed]

### Source Data

The source of the data is from the news domain, details can be found here https://arxiv.org/abs/2210.12391

#### Initial Data Collection and Normalization

The articles were word-tokenized, information on the exact pre-processing pipeline is unavailable.

#### Who are the source language producers?

The source language was produced by journalists and writers employed by the news agency and newspaper mentioned above.

### Annotations

#### Annotation process

Details can be found here https://arxiv.org/abs/2103.11811

#### Who are the annotators?

Annotators were recruited from [Masakhane](https://www.masakhane.io/)

### Personal and Sensitive Information

The data is sourced from newspaper source and only contains mentions of public figures or individuals

## Considerations for Using the Data

### Social Impact of Dataset
[More Information Needed]


### Discussion of Biases
[More Information Needed]


### Other Known Limitations

Users should keep in mind that the dataset only contains news text, which might limit the applicability of the developed systems to other domains.

## Additional Information

### Dataset Curators


### Licensing Information

The licensing status of the data is CC 4.0 Non-Commercial

### Citation Information

Provide the [BibTex](http://www.bibtex.org/)-formatted reference for the dataset. For example:
```
@article{Adelani2022MasakhaNER2A,
  title={MasakhaNER 2.0: Africa-centric Transfer Learning for Named Entity Recognition},
  author={David Ifeoluwa Adelani and Graham Neubig and Sebastian Ruder and Shruti Rijhwani and Michael Beukman and Chester Palen-Michel and Constantine Lignos and Jesujoba Oluwadara Alabi and Shamsuddeen Hassan Muhammad and Peter Nabende and Cheikh M. Bamba Dione and Andiswa Bukula and Rooweither Mabuya and Bonaventure F. P. Dossou and Blessing K. Sibanda and Happy Buzaaba and Jonathan Mukiibi and Godson Kalipe and Derguene Mbaye and Amelia Taylor and Fatoumata Kabore and Chris C. Emezue and Anuoluwapo Aremu and Perez Ogayo and Catherine W. Gitau and Edwin Munkoh-Buabeng and Victoire Memdjokam Koagne and Allahsera Auguste Tapo and Tebogo Macucwa and Vukosi Marivate and Elvis Mboning and Tajuddeen R. Gwadabe and Tosin P. Adewumi and Orevaoghene Ahia and Joyce Nakatumba-Nabende and Neo L. Mokono and Ignatius M Ezeani and Chiamaka Ijeoma Chukwuneke and Mofetoluwa Adeyemi and Gilles Hacheme and Idris Abdulmumin and Odunayo Ogundepo and Oreen Yousuf and Tatiana Moteu Ngoli and Dietrich Klakow},
  journal={ArXiv},
  year={2022},
  volume={abs/2210.12391}
}
```

### Contributions

Thanks to [@dadelani](https://github.com/dadelani) for adding this dataset.