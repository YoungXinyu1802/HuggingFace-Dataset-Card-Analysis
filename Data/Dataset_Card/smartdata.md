---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- de
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: SmartData
dataset_info:
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-DATE
          '2': I-DATE
          '3': B-DISASTER_TYPE
          '4': I-DISASTER_TYPE
          '5': B-DISTANCE
          '6': I-DISTANCE
          '7': B-DURATION
          '8': I-DURATION
          '9': B-LOCATION
          '10': I-LOCATION
          '11': B-LOCATION_CITY
          '12': I-LOCATION_CITY
          '13': B-LOCATION_ROUTE
          '14': I-LOCATION_ROUTE
          '15': B-LOCATION_STOP
          '16': I-LOCATION_STOP
          '17': B-LOCATION_STREET
          '18': I-LOCATION_STREET
          '19': B-NUMBER
          '20': I-NUMBER
          '21': B-ORGANIZATION
          '22': I-ORGANIZATION
          '23': B-ORGANIZATION_COMPANY
          '24': I-ORGANIZATION_COMPANY
          '25': B-ORG_POSITION
          '26': I-ORG_POSITION
          '27': B-PERSON
          '28': I-PERSON
          '29': B-TIME
          '30': I-TIME
          '31': B-TRIGGER
          '32': I-TRIGGER
  config_name: smartdata-v3_20200302
  splits:
  - name: train
    num_bytes: 2124312
    num_examples: 1861
  - name: test
    num_bytes: 266529
    num_examples: 230
  - name: validation
    num_bytes: 258681
    num_examples: 228
  download_size: 18880782
  dataset_size: 2649522
---

# Dataset Card for SmartData

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

- **Homepage:** https://www.dfki.de/web/forschung/projekte-publikationen/publikationen-uebersicht/publikation/9427/
- **Repository:** https://github.com/DFKI-NLP/smartdata-corpus
- **Paper:** https://www.dfki.de/fileadmin/user_upload/import/9427_lrec_smartdata_corpus.pdf
- **Leaderboard:**
- **Point of Contact:** 

### Dataset Summary

DFKI SmartData Corpus is a dataset of 2598 German-language documents
which has been annotated with fine-grained geo-entities, such as streets,
stops and routes, as well as standard named entity types. It has also
been annotated with a set of 15 traffic- and industry-related n-ary
relations and events, such as Accidents, Traffic jams, Acquisitions,
and Strikes. The corpus consists of newswire texts, Twitter messages,
and traffic reports from radio stations, police and railway companies.
It allows for training and evaluating both named entity recognition
algorithms that aim for fine-grained typing of geo-entities, as well
as n-ary relation extraction systems.

### Supported Tasks and Leaderboards

NER

### Languages

German

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

    - id: an identifier for the article the text came from
    - tokens: a list of string tokens for the text of the article
    - ner_tags: a corresponding list of NER tags in the BIO format

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

CC-BY 4.0

### Citation Information

```
@InProceedings{SCHIERSCH18.85,
  author = {Martin Schiersch and Veselina Mironova and Maximilian Schmitt and Philippe Thomas and Aleksandra Gabryszak and Leonhard Hennig},
  title = "{A German Corpus for Fine-Grained Named Entity Recognition and Relation Extraction of Traffic and Industry Events}",
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year = {2018},
  month = {May 7-12, 2018},
  address = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {979-10-95546-00-9},
  language = {english}
  }
```

### Contributions

Thanks to [@aseifert](https://github.com/aseifert) for adding this dataset.