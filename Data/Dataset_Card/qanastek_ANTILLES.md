---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- fr
language_bcp47:
- fr-FR
pretty_name: ANTILLES
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- part-of-speech-tagging
---

# ANTILLES : An Open French Linguistically Enriched Part-of-Speech Corpus

## Table of Contents
- [Dataset Card for [Needs More Information]](#dataset-card-for-needs-more-information)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
- [sent_id = fr-ud-dev_00005](#sent_id--fr-ud-dev_00005)
- [text = Travail de trés grande qualité exécuté par un imprimeur artisan passionné.](#text--travail-de-trs-grande-qualit-excut-par-un-imprimeur-artisan-passionn)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** https://qanastek.github.io/ANTILLES/
- **Repository:** https://github.com/qanastek/ANTILLES
- **Paper:** https://hal.archives-ouvertes.fr/hal-03696042/document
- **Leaderboard:** https://paperswithcode.com/dataset/antilles
- **Point of Contact:** [Yanis Labrak](mailto:yanis.labrak@univ-avignon.fr)

### Dataset Summary

`ANTILLES` is a part-of-speech tagging corpora based on [UD_French-GSD](https://universaldependencies.org/treebanks/fr_gsd/index.html) which was originally created in 2015 and is based on the [universal dependency treebank v2.0](https://github.com/ryanmcd/uni-dep-tb).

Originally, the corpora consists of 400,399 words (16,341 sentences) and had 17 different classes. Now, after applying our tags augmentation script `transform.py`, we obtain 60 different classes which add semantic information such as: the gender, number, mood, person, tense or verb form given in the different CoNLL-U fields from the original corpora.

We based our tags on the level of details given by the [LIA_TAGG](http://pageperso.lif.univ-mrs.fr/frederic.bechet/download.html) statistical POS tagger written by [Frédéric Béchet](http://pageperso.lif.univ-mrs.fr/frederic.bechet/index-english.html) in 2001.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

### Supported Tasks and Leaderboards

`part-of-speech-tagging`: The dataset can be used to train a model for part-of-speech-tagging. The performance is measured by how high its F1 score is. A Flair Sequence-To-Sequence model trained to tag tokens from Wikipedia passages achieves a F1 score (micro) of 0.952.

### Languages

The text in the dataset is in French, as spoken by [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) users. The associated [BCP-47](https://tools.ietf.org/html/bcp47) code is `fr`.

## Load the dataset

### HuggingFace

```python
from datasets import load_dataset
dataset = load_dataset("qanastek/ANTILLES")
print(dataset)
```

### FlairNLP

```python
from flair.datasets import UniversalDependenciesCorpus
corpus: Corpus = UniversalDependenciesCorpus(
    data_folder='ANTILLES',
    train_file="train.conllu",
    test_file="test.conllu",
    dev_file="dev.conllu"
)
```

## Load the model

### Flair ([model](https://huggingface.co/qanastek/pos-french))

```python
from flair.models import SequenceTagger
tagger = SequenceTagger.load("qanastek/pos-french")
```

## HuggingFace Spaces

<table style="width: fit-content;">
<thead>
  <tr>
    <td>
        <a href="https://huggingface.co/spaces/qanastek/French-Part-Of-Speech-Tagging">
            <img src="https://huggingface.co/datasets/qanastek/ANTILLES/raw/main/imgs/en.png" width="160">
        </a>
    </td>
    <td>
        <a href="https://huggingface.co/spaces/qanastek/Etiqueteur-Morphosyntaxique-Etendu">
            <img src="https://huggingface.co/datasets/qanastek/ANTILLES/raw/main/imgs/fr.png" width="160">
        </a>
    </td>
  </tr>
</thead>
</table>

## Dataset Structure

### Data Instances

```plain
# sent_id = fr-ud-dev_00005
# text = Travail de trés grande qualité exécuté par un imprimeur artisan passionné.
1	Travail	travail	NMS	_	Gender=Masc|Number=Sing	0	root	_	wordform=travail
2	de	de	PREP	_	_	5	case	_	_
3	trés	trés	ADV	_	_	4	advmod	_	_
4	grande	grand	ADJFS	_	Gender=Fem|Number=Sing	5	amod	_	_
5	qualité	qualité	NFS	_	Gender=Fem|Number=Sing	1	nmod	_	_
6	exécuté	exécuter	VPPMS	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	1	acl	_	_
7	par	par	PREP	_	_	9	case	_	_
8	un	un	DINTMS	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	9	det	_	_
9	imprimeur	imprimeur	NMS	_	Gender=Masc|Number=Sing	6	obl:agent	_	_
10	artisan	artisan	NMS	_	Gender=Masc|Number=Sing	9	nmod	_	_
11	passionné	passionné	ADJMS	_	Gender=Masc|Number=Sing	9	amod	_	SpaceAfter=No
12	.	.	YPFOR	_	_	1	punct	_	_
```

### Data Fields

| Abbreviation | Description | Examples | # tokens |
|:--------:|:--------:|:--------:|:--------:|
| PREP | Preposition | de | 63 738 |
| AUX | Auxiliary Verb | est | 12 886 |
| ADV | Adverb | toujours | 14 969 |
| COSUB | Subordinating conjunction | que | 3 007 |
| COCO | Coordinating Conjunction | et | 10 102 |
| PART | Demonstrative particle | -t | 93 |
| PRON | Pronoun | qui ce quoi | 667 |
| PDEMMS | Singular Masculine Demonstrative Pronoun | ce | 1 950 |
| PDEMMP | Plurial Masculine Demonstrative Pronoun | ceux | 108 |
| PDEMFS | Singular Feminine Demonstrative Pronoun | cette | 1 004 |
| PDEMFP | Plurial Feminine Demonstrative Pronoun | celles | 53 |
| PINDMS | Singular Masculine Indefinite Pronoun | tout | 961 |
| PINDMP | Plurial Masculine Indefinite Pronoun | autres | 89 |
| PINDFS | Singular Feminine Indefinite Pronoun | chacune | 136 |
| PINDFP | Plurial Feminine Indefinite Pronoun | certaines | 31 |
| PROPN | Proper noun | houston | 22 135 |
| XFAMIL | Last name | levy | 6 449 |
| NUM | Numerical Adjectives | trentaine vingtaine | 67 |
| DINTMS | Masculine Numerical Adjectives | un | 4 254 |
| DINTFS | Feminine Numerical Adjectives | une | 3 543 |
| PPOBJMS | Singular Masculine Pronoun complements of objects | le lui | 1 425 |
| PPOBJMP | Plurial Masculine Pronoun complements of objects | eux y | 212 |
| PPOBJFS | Singular Feminine Pronoun complements of objects | moi la | 358 |
| PPOBJFP | Plurial Feminine Pronoun complements of objects | en y | 70 |
| PPER1S | Personal Pronoun First Person Singular | je | 571 |
| PPER2S | Personal Pronoun Second Person Singular | tu | 19 |
| PPER3MS | Personal Pronoun Third Person Masculine Singular | il | 3 938 |
| PPER3MP | Personal Pronoun Third Person Masculine Plurial | ils | 513 |
| PPER3FS | Personal Pronoun Third Person Feminine Singular | elle | 992 |
| PPER3FP | Personal Pronoun Third Person Feminine Plurial | elles | 121 |
| PREFS | Reflexive Pronouns First Person of Singular | me m' | 120 |
| PREF | Reflexive Pronouns Third Person of Singular | se s' | 2 337 |
| PREFP | Reflexive Pronouns First / Second Person of Plurial | nous vous | 686 |
| VERB | Verb | obtient | 21 131 |
| VPPMS | Singular Masculine Participle Past Verb | formulé | 6 275 |
| VPPMP | Plurial Masculine Participle Past Verb | classés | 1 352 |
| VPPFS | Singular Feminine Participle Past Verb | appelée | 2 434 |
| VPPFP | Plurial Feminine Participle Past Verb | sanctionnées | 813 |
| VPPRE | Present participle | étant | 2 |
| DET | Determinant | les l' | 25 206 |
| DETMS | Singular Masculine Determinant | les | 15 444 |
| DETFS | Singular Feminine Determinant | la | 10 978 |
| ADJ | Adjective | capable sérieux | 1 075 |
| ADJMS | Singular Masculine Adjective | grand important | 8 338 |
| ADJMP | Plurial Masculine Adjective | grands petits | 3 274 |
| ADJFS | Singular Feminine Adjective | franéaise petite | 8 004 |
| ADJFP | Plurial Feminine Adjective | légéres petites | 3 041 |
| NOUN | Noun | temps | 1 389 |
| NMS | Singular Masculine Noun | drapeau | 29 698 |
| NMP | Plurial Masculine Noun | journalistes | 10 882 |
| NFS | Singular Feminine Noun | téte | 25 414 |
| NFP | Plurial Feminine Noun | ondes | 7 448 |
| PREL | Relative Pronoun | qui dont | 2 976 |
| PRELMS | Singular Masculine Relative Pronoun | lequel | 94 |
| PRELMP | Plurial Masculine Relative Pronoun | lesquels | 29 |
| PRELFS | Singular Feminine Relative Pronoun | laquelle | 70 |
| PRELFP | Plurial Feminine Relative Pronoun | lesquelles | 25 |
| PINTFS | Singular Feminine Interrogative Pronoun | laquelle | 3 |
| INTJ | Interjection | merci bref | 75 |
| CHIF | Numbers | 1979 10 | 10 417 |
| SYM | Symbol | é % | 705 |
| YPFOR | Endpoint | . | 15 088 |
| PUNCT | Ponctuation | : , | 28 918 |
| MOTINC | Unknown words | Technology Lady | 2 022 |
| X | Typos & others | sfeir 3D statu | 175 |

### Data Splits

|                    | Train  |  Dev   | Test  |
|:------------------:|:------:|:------:|:-----:|
|       # Docs       | 14 449 | 1 476  |  416  |
| Avg # Tokens / Doc | 24.54  | 24.19  | 24.08 |

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

The corpora is free of personal or sensitive information since it has been based on `Wikipedia` articles content.

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

The nature of the corpora introduce various biases such as the names of the streets which are temporaly based and can therefore introduce named entity like author or event names. For example, street names such as `Rue Victor-Hugo` or `Rue Pasteur` doesn't exist before the 20's century in France.

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

__ANTILLES__: Labrak Yanis, Dufour Richard

__UD_FRENCH-GSD__: de Marneffe Marie-Catherine, Guillaume Bruno, McDonald Ryan, Suhr Alane, Nivre Joakim, Grioni Matias, Dickerson Carly, Perrier Guy

__Universal Dependency__: Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg, Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang, Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee

### Licensing Information

```plain
For the following languages

  German, Spanish, French, Indonesian, Italian, Japanese, Korean and Brazilian
  Portuguese

we will distinguish between two portions of the data.

1. The underlying text for sentences that were annotated. This data Google
   asserts no ownership over and no copyright over. Some or all of these
   sentences may be copyrighted in some jurisdictions.  Where copyrighted,
   Google collected these sentences under exceptions to copyright or implied
   license rights.  GOOGLE MAKES THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY
   WARRANTY OF ANY KIND, WHETHER EXPRESS OR IMPLIED.

2. The annotations -- part-of-speech tags and dependency annotations. These are
   made available under a CC BY-SA 4.0. GOOGLE MAKES
   THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY WARRANTY OF ANY KIND, WHETHER
   EXPRESS OR IMPLIED. See attached LICENSE file for the text of CC BY-NC-SA.

Portions of the German data were sampled from the CoNLL 2006 Tiger Treebank
data. Hans Uszkoreit graciously gave permission to use the underlying
sentences in this data as part of this release.

Any use of the data should reference the above plus:

  Universal Dependency Annotation for Multilingual Parsing
  Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg,
  Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang,
  Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee
  Proceedings of ACL 2013
```

### Citation Information

Please cite the following paper when using this model.

ANTILLES extended corpus:

```latex
@inproceedings{labrak:hal-03696042,
  TITLE = {{ANTILLES: An Open French Linguistically Enriched Part-of-Speech Corpus}},
  AUTHOR = {Labrak, Yanis and Dufour, Richard},
  URL = {https://hal.archives-ouvertes.fr/hal-03696042},
  BOOKTITLE = {{25th International Conference on Text, Speech and Dialogue (TSD)}},
  ADDRESS = {Brno, Czech Republic},
  PUBLISHER = {{Springer}},
  YEAR = {2022},
  MONTH = Sep,
  KEYWORDS = {Part-of-speech corpus ; POS tagging ; Open tools ; Word embeddings ; Bi-LSTM ; CRF ; Transformers},
  PDF = {https://hal.archives-ouvertes.fr/hal-03696042/file/ANTILLES_A_freNch_linguisTIcaLLy_Enriched_part_of_Speech_corpus.pdf},
  HAL_ID = {hal-03696042},
  HAL_VERSION = {v1},
}
```

UD_French-GSD corpora:

```latex
@misc{
    universaldependencies,
    title={UniversalDependencies/UD_French-GSD},
    url={https://github.com/UniversalDependencies/UD_French-GSD}, journal={GitHub},
    author={UniversalDependencies}
}
```

{U}niversal {D}ependency Annotation for Multilingual Parsing:

```latex
@inproceedings{mcdonald-etal-2013-universal,
    title = "{U}niversal {D}ependency Annotation for Multilingual Parsing",
    author = {McDonald, Ryan  and
      Nivre, Joakim  and
      Quirmbach-Brundage, Yvonne  and
      Goldberg, Yoav  and
      Das, Dipanjan  and
      Ganchev, Kuzman  and
      Hall, Keith  and
      Petrov, Slav  and
      Zhang, Hao  and
      T{\"a}ckstr{\"o}m, Oscar  and
      Bedini, Claudia  and
      Bertomeu Castell{\'o}, N{\'u}ria  and
      Lee, Jungmee},
    booktitle = "Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = aug,
    year = "2013",
    address = "Sofia, Bulgaria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P13-2017",
    pages = "92--97",
}
```

LIA TAGG:

```latex
@techreport{LIA_TAGG,
  author = {Frédéric Béchet},
  title = {LIA_TAGG: a statistical POS tagger + syntactic bracketer},
  institution = {Aix-Marseille University & CNRS},
  year = {2001}
}
```
