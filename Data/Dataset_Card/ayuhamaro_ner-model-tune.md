---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- zh
license:
- unknown
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
paperswithcode_id: nlp-model-tune
pretty_name: NER Model Tune
train-eval-index:
- config: default
  task: token-classification
  task_id: entity_extraction
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    tokens: tokens
    ner_tags: tags
  metrics:
  - type: seqeval
    name: seqeval
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
          '0': O,
          '1': B-CARDINAL,
          '2': B-DATE,
          '3': B-EVENT,
          '4': B-FAC,
          '5': B-GPE,
          '6': B-LANGUAGE,
          '7': B-LAW,
          '8': B-LOC,
          '9': B-MONEY,
          '10': B-NORP,
          '11': B-ORDINAL,
          '12': B-ORG,
          '13': B-PERCENT,
          '14': B-PERSON,
          '15': B-PRODUCT,
          '16': B-QUANTITY,
          '17': B-TIME,
          '18': B-WORK_OF_ART,
          '19': I-CARDINAL,
          '20': I-DATE,
          '21': I-EVENT,
          '22': I-FAC,
          '23': I-GPE,
          '24': I-LANGUAGE,
          '25': I-LAW,
          '26': I-LOC,
          '27': I-MONEY,
          '28': I-NORP,
          '29': I-ORDINAL,
          '30': I-ORG,
          '31': I-PERCENT,
          '32': I-PERSON,
          '33': I-PRODUCT,
          '34': I-QUANTITY,
          '35': I-TIME,
          '36': I-WORK_OF_ART,
          '37': E-CARDINAL,
          '38': E-DATE,
          '39': E-EVENT,
          '40': E-FAC,
          '41': E-GPE,
          '42': E-LANGUAGE,
          '43': E-LAW,
          '44': E-LOC,
          '45': E-MONEY,
          '46': E-NORP,
          '47': E-ORDINAL,
          '48': E-ORG,
          '49': E-PERCENT,
          '50': E-PERSON,
          '51': E-PRODUCT,
          '52': E-QUANTITY,
          '53': E-TIME,
          '54': E-WORK_OF_ART,
          '55': S-CARDINAL,
          '56': S-DATE,
          '57': S-EVENT,
          '58': S-FAC,
          '59': S-GPE,
          '60': S-LANGUAGE,
          '61': S-LAW,
          '62': S-LOC,
          '63': S-MONEY,
          '64': S-NORP,
          '65': S-ORDINAL,
          '66': S-ORG,
          '67': S-PERCENT,
          '68': S-PERSON,
          '69': S-PRODUCT,
          '70': S-QUANTITY,
          '71': S-TIME,
          '72': S-WORK_OF_ART
  splits:
  - name: train
    num_bytes: 568
    num_examples: 1
  download_size: 568
  dataset_size: 568
---

# Dataset Card for "NER Model Tune"

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

- **Homepage:** None
- **Repository:** https://huggingface.co/datasets/ayuhamaro/nlp-model-tune
- **Paper:** [More Information Needed]
- **Leaderboard:** [If the dataset supports an active leaderboard, add link here]()
- **Point of Contact:** [More Information Needed]

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]
## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

[More Information Needed]

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

[More Information Needed]

### Citation Information

[More Information Needed]
### Contributions