---
Tasks:
- Text2Text Generation
Fine-Grained Tasks:
- paraphrase
- query-paraphrasing
Languages:
- Persian
Multilinguality:
- monolingual
- fa
- fa-IR
Sizes:
- n>1M
dataset_info:
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  splits:
  - name: train
    num_bytes: 139373682.4
    num_examples: 881408
  - name: test
    num_bytes: 17421710.3
    num_examples: 110176
  - name: validation
    num_bytes: 17421710.3
    num_examples: 110176
  download_size: 98032993
  dataset_size: 174217103.00000003
---
# Dataset Card for "fa-paraphrase"

This dataset contains over 1.1 million rows. Each row contains a pair of Farsi sentences which are a paraphrase of each other. The datasets used to create this dataset can be found here:

* [tapaco](https://huggingface.co/datasets/tapaco)
* [kaggle](https://www.kaggle.com/datasets/armannikkhah/persian-paraphrase-dataset)

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)