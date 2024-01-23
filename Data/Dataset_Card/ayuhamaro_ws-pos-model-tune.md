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
paperswithcode_id: ws-pos-model-tune
pretty_name: WS POS Model Tune
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
  - name: ws_tags
    sequence:
      class_label:
        names:
          '0': B,
          '1': I
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': A,
          '1': Caa,
          '2': Cab,
          '3': Cba,
          '4': Cbb,
          '5': D,
          '6': Da,
          '7': Dfa,
          '8': Dfb,
          '9': Di,
          '10': Dk,
          '11': DM,
          '12': I,
          '13': Na,
          '14': Nb,
          '15': Nc,
          '16': Ncd,
          '17': Nd,
          '18': Nep,
          '19': Neqa,
          '20': Neqb,
          '21': Nes,
          '22': Neu,
          '23': Nf,
          '24': Ng,
          '25': Nh,
          '26': Nv,
          '27': P,
          '28': T,
          '29': VA,
          '30': VAC,
          '31': VB,
          '32': VC,
          '33': VCL,
          '34': VD,
          '35': VF,
          '36': VE,
          '37': VG,
          '38': VH,
          '39': VHC,
          '40': VI,
          '41': VJ,
          '42': VK,
          '43': VL,
          '44': V_2,
          '45': DE,
          '46': SHI,
          '47': FW,
          '48': COLONCATEGORY,
          '49': COMMACATEGORY,
          '50': DASHCATEGORY,
          '51': DOTCATEGORY,
          '52': ETCCATEGORY,
          '53': EXCLAMATIONCATEGORY,
          '54': PARENTHESISCATEGORY,
          '55': PAUSECATEGORY,
          '56': PERIODCATEGORY,
          '57': QUESTIONCATEGORY,
          '58': SEMICOLONCATEGORY,
          '59': SPCHANGECATEGORY
  splits:
  - name: train
    num_bytes: 1024
    num_examples: 1
  download_size: 1024
  dataset_size: 1024
---

# Dataset Card for "WS POS Model Tune"

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