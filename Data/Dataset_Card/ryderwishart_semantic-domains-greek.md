---
dataset_info:
  features:
  - name: tokens
    sequence: string
  - name: tags
    sequence: int64
  - name: labels
    sequence: string
  splits:
  - name: train
    num_bytes: 3694559
    num_examples: 6408
  - name: test
    num_bytes: 444391
    num_examples: 801
  - name: eval
    num_bytes: 366650
    num_examples: 802
  download_size: 1334579
  dataset_size: 4505600
---
# Dataset Card for "semantic-domains-greek"

See dataset card for [semantic-domains-greek-lemmatized](https://huggingface.co/datasets/ryderwishart/semantic-domains-greek-lemmatized). The only difference between these datasets is that this dataset (semantic-domains-greek) does not use lemmatized tokens.