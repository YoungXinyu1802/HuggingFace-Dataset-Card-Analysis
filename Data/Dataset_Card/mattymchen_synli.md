---
license: odc-by
dataset_info:
  features:
  - name: sent0
    dtype: string
  - name: sent1
    dtype: string
  - name: hard_neg
    dtype: string
  splits:
  - name: train
    num_bytes: 11441750654
    num_examples: 60939492
  download_size: 6904073153
  dataset_size: 11441750654
---

# Dataset Card for SyNLI
A synthetic NLI datasets from open domain sentences using T5 as data synthesizer. The data can be used to train sentence embedding models.

## Data Fields
The data have several fields:
- `sent0`: premise as a string
- `sent1`: entailment hypothesis as a string
- `hard_neg`: contradiction hypothesis as a string
