---
dataset_info:
  features:
  - name: did
    dtype: int64
  - name: query
    dtype: string
  - name: name
    dtype: string
  - name: datatype
    dtype: string
  - name: unit
    dtype: string
  - name: IRDI
    dtype: string
  - name: metalabel
    dtype: int64
  splits:
  - name: train
    num_bytes: 137123
    num_examples: 672
  download_size: 48203
  dataset_size: 137123
---
# Dataset Card for "eclassCorpus"

This Dataset consists of names and descriptions from ECLASS-standard pump-properties. It can be used to evaluate models on the task of matching paraphrases to the ECLASS-standard pump-properties based on their semantics.