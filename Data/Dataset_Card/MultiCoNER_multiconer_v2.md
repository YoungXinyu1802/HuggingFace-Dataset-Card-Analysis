---
license: cc-by-4.0
task_categories:
- token-classification
language:
- bn
- zh
- de
- en
- es
- fa
- fr
- hi
- it
- pt
- sv
- uk
tags:
- multiconer
- ner
- multilingual
- named entity recognition
- fine-grained ner
size_categories:
- 100K<n<1M
---
# Dataset Card for Multilingual Complex Named Entity Recognition (MultiCoNER)

## Dataset Description

- **Homepage:**  https://multiconer.github.io
- **Repository:** 
- **Paper:** 
- **Leaderboard:** https://multiconer.github.io/results, https://codalab.lisn.upsaclay.fr/competitions/10025
- **Point of Contact:** https://multiconer.github.io/organizers

### Dataset Summary

The tagset of MultiCoNER is a fine-grained tagset.
The fine to coarse level mapping of the tags are as follows:

* Location (LOC) : Facility, OtherLOC, HumanSettlement, Station
* Creative Work (CW) : VisualWork, MusicalWork, WrittenWork, ArtWork, Software
* Group (GRP) : MusicalGRP, PublicCORP, PrivateCORP, AerospaceManufacturer, SportsGRP, CarManufacturer, ORG
* Person (PER) : Scientist, Artist, Athlete, Politician, Cleric, SportsManager, OtherPER
* Product (PROD) : Clothing, Vehicle, Food, Drink, OtherPROD
* Medical (MED) : Medication/Vaccine, MedicalProcedure, AnatomicalStructure, Symptom, Disease



### Supported Tasks and Leaderboards

The final leaderboard of the shared task is available <a href="https://multiconer.github.io/results" target="_blank">here</a>.

### Languages
Supported languages are Bangla, Chinese, English, Spanish, Farsi, French, German, Hindi, Italian, Portuguese, Swedish, Ukrainian.

## Dataset Structure
The dataset follows CoNLL format.

### Data Instances

Here are some examples in different languages:

* Bangla: [লিটল মিক্স | MusicalGrp] এ যোগদানের আগে তিনি [পিৎজা হাট | ORG] এ ওয়েট্রেস হিসাবে কাজ করেছিলেন।
* Chinese: 它的纤维穿过 [锁骨 | AnatomicalStructure] 并沿颈部侧面倾斜向上和内侧.
* English: [wes anderson | Artist]'s film [the grand budapest hotel | VisualWork] opened the festival .
* Farsi:     است] ناگویا |HumanSettlement] مرکزاین استان شهر
* French: l [amiral de coligny | Politician] réussit à s y glisser .
* German: in [frühgeborenes | Disease] führt dies zu [irds | Symptom] .
* Hindi: १७९६ में उन्हें [शाही स्वीडिश विज्ञान अकादमी | Facility] का सदस्य चुना गया।
* Italian: è conservato nel [rijksmuseum | Facility] di [amsterdam | HumanSettlement] .
* Portuguese: também é utilizado para se fazer [licor | Drink] e [vinhos | Drink].
* Spanish: fue superado por el [aon center | Facility] de [los ángeles | HumanSettlement] .
* Swedish: [tom hamilton | Artist] amerikansk musiker basist i [aerosmith | MusicalGRP] .
* Ukrainian: назва альбому походить з роману « [кінець дитинства | WrittenWork] » англійського письменника [артура кларка | Artist] .

### Data Fields

The data has two fields. One is the token and another is the label. Here is an example from the English data.

```
# id f5458a3a-cd23-4df4-8384-4e23fe33a66b	domain=en
doris _ _ B-Artist
day _ _ I-Artist
included _ _ O
in _ _ O
the _ _ O
album _ _ O
billy _ _ B-MusicalWork
rose _ _ I-MusicalWork
's _ _ I-MusicalWork
jumbo _ _ I-MusicalWork
```


### Data Splits

Train, Dev, and Test splits are provided

## Dataset Creation
TBD


### Licensing Information
CC BY 4.0

### Citation Information
```
@inproceedings{multiconer2-report,
    title={{SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)}},
    author={Fetahu, Besnik and Kar, Sudipta and Chen, Zhiyu and Rokhlenko, Oleg and Malmasi, Shervin},
    booktitle={Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023)},
    year={2023},
    publisher={Association for Computational Linguistics},
}

@article{multiconer2-data,
    title={{MultiCoNER v2: a Large Multilingual dataset for Fine-grained and Noisy Named Entity Recognition}},
    author={Fetahu, Besnik and Chen, Zhiyu and Kar, Sudipta and Rokhlenko, Oleg and Malmasi, Shervin},
    year={2023},
}
```

