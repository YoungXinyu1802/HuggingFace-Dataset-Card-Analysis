---
dataset_info:
  features:
    - name: text
      dtype: string
    - name: tokens
      sequence: string
    - name: tokens_offsets
      sequence:
        sequence: int32
    - name: clinical_entity_tags
      sequence:
        class_label:
          names:
            "0": O
            "1": B-CLINENTITY
            "2": I-CLINENTITY
    - name: temporal_information_tags
      sequence:
        class_label:
          names:
            "0": O
            "1": B-EVENT
            "2": B-ACTOR
            "3": B-BODYPART
            "4": B-TIMEX3
            "5": B-RML
            "6": I-EVENT
            "7": I-ACTOR
            "8": I-BODYPART
            "9": I-TIMEX3
            "10": I-RML
  config_name: e3c
  splits:
    - name: en.layer1
      num_bytes: 1273610
      num_examples: 1520
    - name: en.layer2
      num_bytes: 2550153
      num_examples: 2873
    - name: en.layer2.validation
      num_bytes: 290108
      num_examples: 334
    - name: es.layer1
      num_bytes: 1252571
      num_examples: 1134
    - name: es.layer2
      num_bytes: 2498266
      num_examples: 2347
    - name: es.layer2.validation
      num_bytes: 275770
      num_examples: 261
    - name: eu.layer1
      num_bytes: 1519021
      num_examples: 3126
    - name: eu.layer2
      num_bytes: 839955
      num_examples: 1594
    - name: eu.layer2.validation
      num_bytes: 220097
      num_examples: 468
    - name: fr.layer1
      num_bytes: 1258738
      num_examples: 1109
    - name: fr.layer2
      num_bytes: 2628628
      num_examples: 2389
    - name: fr.layer2.validation
      num_bytes: 282527
      num_examples: 293
    - name: it.layer1
      num_bytes: 1276534
      num_examples: 1146
    - name: it.layer2
      num_bytes: 2641257
      num_examples: 2436
    - name: it.layer2.validation
      num_bytes: 286702
      num_examples: 275
  download_size: 230213492
  dataset_size: 19093937
---

# Dataset Card for E3C

## Dataset Description

- **Homepage:** https://github.com/hltfbk/E3C-Corpus
- **Public:** True
- **Tasks:** NER,RE

The European Clinical Case Corpus (E3C) project aims at collecting and \
annotating a large corpus of clinical documents in five European languages (Spanish, \
Basque, English, French and Italian), which will be freely distributed. Annotations \
include temporal information, to allow temporal reasoning on chronologies, and \
information about clinical entities based on medical taxonomies, to be used for semantic reasoning.

## Citation Information

```
@report{Magnini2021,
    author = {Bernardo Magnini and Begoña Altuna and Alberto Lavelli and Manuela Speranza
    and Roberto Zanoli and Fondazione Bruno Kessler},
    keywords = {Clinical data,clinical enti-ties,corpus,multilingual,temporal information},
    title = {The E3C Project:
    European Clinical Case Corpus El proyecto E3C: European Clinical Case Corpus},
    url = {https://uts.nlm.nih.gov/uts/umls/home},
    year = {2021},
}
```
