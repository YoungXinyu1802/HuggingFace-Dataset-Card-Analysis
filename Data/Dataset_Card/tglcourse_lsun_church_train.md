---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          0: '0'
          1: '1'
          2: '2'
          3: '3'
          4: '4'
          5: '5'
          6: '6'
          7: '7'
          8: '8'
          9: '9'
          10: a
          11: b
          12: c
          13: d
          14: e
          15: f
  splits:
  - name: test
    num_bytes: -5033726665.536212
    num_examples: 6312
  - name: train
    num_bytes: -94551870824.9868
    num_examples: 119915
  download_size: 2512548233
  dataset_size: -99585597490.52301
---
# Dataset Card for "lsun_church_train"

Uploading lsun church train dataset for convenience

I've split this into 119915 train and 6312 test but if you want the original test set see https://github.com/fyu/lsun

Notebook that I used to download then upload this dataset: https://colab.research.google.com/drive/1_f-D2ENgmELNSB51L1igcnLx63PkveY2?usp=sharing

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)