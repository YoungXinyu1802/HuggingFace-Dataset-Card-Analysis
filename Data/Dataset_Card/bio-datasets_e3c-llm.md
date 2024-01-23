---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: tokens_offsets
    sequence:
      sequence: int32
  - name: clinical_entity_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-CLINENTITY
          '2': I-CLINENTITY
  config_name: e3c-llm
  splits:
  - name: fr.layer2
    num_bytes: 1583560
    num_examples: 2389
  - name: fr.layer2.validation
    num_bytes: 170233
    num_examples: 293
  - name: fr.layer1
    num_bytes: 758368
    num_examples: 1109
  download_size: 0
  dataset_size: 2512161
---
# Dataset Card for E3C

## Dataset Description

- **Public:** True
- **Tasks:** NER

This dataset is an annotated corpus of clinical texts from E3C using Large Language Models (LLM).