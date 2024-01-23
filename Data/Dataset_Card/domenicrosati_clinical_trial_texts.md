---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: trial_id
    dtype: string
  - name: input_ids
    sequence: int32
  - name: token_type_ids
    sequence: int8
  - name: attention_mask
    sequence: int8
  splits:
  - name: train
    num_bytes: 22784316806
    num_examples: 434977
  download_size: 5376659326
  dataset_size: 22784316806
---
# Dataset Card for "clinical_trial_texts"

These are the text of clinical trials dowloaded from https://ClinicalTrials.gov/AllAPIJSON.zip on Dec 3rd 2022.

Total trials is 434977
Number of tokens is 2,184,397,556 (2.1bn tokens).

The tokens here are from the default BERT tokenizer in hugginface.

This data can be used for pretraining in the clinical trial and biomedical domains.

If you use this data please acknowledge @domenicrosati and link to this dataset

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)