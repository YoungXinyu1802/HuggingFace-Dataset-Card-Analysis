---
license: cc-by-sa-4.0
task_categories:
- text-classification
language:
- fi
multilinguality:
- translation
tags:
- toxicity, multi-label
source_datasets:
- extended|jigsaw_toxicity_pred
size_categories:
- 100K<n<1M
---


### Dataset Summary

This dataset is a DeepL -based machine translated version of the Jigsaw toxicity dataset for Finnish. The dataset is originally from a Kaggle competition https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data.
The dataset poses a multi-label text classification problem and includes the labels `identity_attack`, `insult`, `obscene`, `severe_toxicity`, `threat` and `toxicity`.

#### Example data

```
{
"id": "879ad7bdba4cedaa",
"label_identity_attack": 0,
"label_insult": 0,
"label_obscene": 0,
"label_severe_toxicity": 0,
"label_threat": 0,
"label_toxicity": 0,
"lang": "fi-deepl",
"text": "\" \n\n Hei Pieter Pietersen, ja tervetuloa Wikipediaan!   \n\n Tervetuloa Wikipediaan! Toivottavasti viihdyt tietosanakirjassa ja haluat jäädä tänne. Ensimmäiseksi voit lukea johdannon. \n\n Jos sinulla on kysyttävää, voit kysyä minulta keskustelusivullani - autan mielelläni. Tai voit kysyä kysymyksesi Uusien avustajien ohjesivulla. \n\n - \n Seuraavassa on lisää resursseja, jotka auttavat sinua tutkimaan ja osallistumaan maailman suurinta tietosanakirjaa.... \n\n  Löydät perille:  \n\n  \n * Sisällysluettelo \n\n * Osastohakemisto \n\n  \n  Tarvitsetko apua?  \n\n  \n * Kysymykset - opas siitä, mistä voi esittää kysymyksiä. \n * Huijausluettelo - pikaohje Wikipedian merkintäkoodeista. \n\n * Wikipedian 5 pilaria - yleiskatsaus Wikipedian perustaan. \n * The Simplified Ruleset - yhteenveto Wikipedian tärkeimmistä säännöistä. \n\n  \n  Miten voit auttaa:  \n\n  \n * Wikipedian avustaminen - opas siitä, miten voit auttaa. \n\n * Yhteisöportaali - Wikipedian toiminnan keskus. \n\n  \n  Lisää vinkkejä...   \n\n  \n * Allekirjoita viestisi keskustelusivuilla neljällä tildillä (~~~~). Tämä lisää automaattisesti \"\"allekirjoituksesi\"\" (käyttäjänimesi ja päivämääräleima). Myös Wikipedian tekstinmuokkausikkunan yläpuolella olevassa työkalupalkissa oleva painike tekee tämän.  \n\n * Jos haluat leikkiä uusilla Wiki-taidoillasi, Hiekkalaatikko on sinua varten.  \n\n  \n  Onnea ja hauskaa. \""
}
```

### Data Fields

Fields marked as `label_` have either `0` to convey *not* having that category of toxicity in the text and `1` to convey having that category of toxicity present in the text.

- `id`: a `string` feature.
- `label_identity_attack`: a `int64` feature. 
- `label_insult`: a `int64` feature.
- `label_obscene`: a `int64` feature.
- `label_severe_toxicity`: a `int64` feature.
- `label_threat`: a `int64` feature.
- `label_toxicity`: a `int64` feature.
- `lang`: a `string` feature.
- `text`: a `string` feature.


### Data Splits

The splits are the same as in the original English data.
| dataset   |  train | test |
| -------- | -----: | ---------: |
| TurkuNLP/wikipedia-toxicity-data-fi| 159571 | 63978 |

### Evaluation Results

Results from fine-tuning [TurkuNLP/bert-large-finnish-cased-v1](https://huggingface.co/TurkuNLP/bert-large-finnish-cased-v1) for multi-label toxicity detection.
| dataset              | F1-micro    | Precision | Recall |
| -------------------- | ----: |  ---: | ----: |
| TurkuNLP/wikipedia-toxicity-data-fi | 0.66 | 0.58 | 0.76 |

<!--- Base results from fine-tuning [bert-large-cased](https://huggingface.co/bert-large-cased) on the original English data for multi-label toxicity detection.
| dataset              | F1-micro    | Precision | Recall |
| -------------------- | ----: | ---: | ----: |
| jigsaw_toxicity_pred | 0.69 | 0.59 | 0.81 | --->

### Considerations for Using the Data
Due to DeepL terms and conditions, this dataset **must not be used for any machine translation work**, namely machine translation 
system development and evaluation of any kind. In general, we wish you do not pair the original English data with the translations 
except when working on research unrelated to machine translation, so as not to infringe on the terms and conditions.
### Licensing Information
Contents of this repository are distributed under the 
[Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). 
Copyright of the dataset contents belongs to the original copyright holders.