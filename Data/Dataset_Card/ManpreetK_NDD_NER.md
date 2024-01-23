---
viewer: true
dataset_info:
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': I-CONDITION
          '1': I-TEST
          '2': B-CONDITION
          '3': I-PATIENT_GROUP
          '4': B-ASSOCIATED_PROBLEM
          '5': O
          '6': I-ASSOCIATED_PROBLEM
          '7': B-INTERVENTION
          '8': B-PATIENT_GROUP
          '9': I-INTERVENTION
          '10': B-TEST
  splits:
  - name: train
    num_bytes: 156151
    num_examples: 341
  - name: validation
    num_bytes: 68495
    num_examples: 177
  - name: test
    num_bytes: 67949
    num_examples: 160
  download_size: 78315
  dataset_size: 292595
---
# Dataset Card for "NDD_NER"
## Dataset Summary
This Named Entity Recognition dataset is created for Neurodevelopmental disorders domain to detected domain specific entities. Initially, pubmed abstracts were annotated
with SciSpaCy UMLS entity linker and specific semantic types were mapped to required domain specific labels, which were further validated during manual curation process
using Label Studio (an open source data labeling tool).
  | Label Category  | UMLS semantic types |
|-----|-----|
|CONDITION|  Mental or Behavioral Dysfunction, Disease or Syndrome,  Neoplastic Process, Congenital Abnormality |
|ASSOCIATED_PROBLEM| Sign or Symptom, Mental Process, Injury or Poisoning |
|PATIENT_GROUP|  Age Group, Population Group, Patient or Disabled Group |
|INTERVENTION| Therapeutic or Preventive Procedure, Health Care Activity |
|TEST| Diagnostic Procedure, Intellectual Product, Research Activity, Laboratory Procedure |
## Dataset Splits
|split name|number of examples|CONDITION|ASSOCIATED_PROBLEM|PATIENT_GROUP|INTERVENTION|TEST|
|-----|-----|-----|-----|-----|-----|-----|
|train| 341 | 320 | 189 | 240 | 273 | 228 |
|test| 160 | 139 | 68 | 87 | 98 | 82 | 
|validation| 177 | 147 | 82 | 104 | 117 | 98 |

## Source Data
Pubmed abstracts for ("Neurodevelopmental Disorders"[Mesh]) AND "Behavioral Disciplines and Activities"[Mesh] query using NCBI E-utilities API.

