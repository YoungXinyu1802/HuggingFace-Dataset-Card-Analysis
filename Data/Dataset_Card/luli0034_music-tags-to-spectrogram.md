---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12031171376.431
    num_examples: 1543
  download_size: 12061543955
  dataset_size: 12031171376.431
---
# Dataset Card for "music-tags-to-spectrogram"

This dataset is extracted from the [MTG-Jamendo Datase](https://github.com/MTG/mtg-jamendo-dataset/tree/ef1248f0fc295a4bd2189531b0e2b4d158d219dc)

### We applied the following transformation:
- Convert audio to spectrogram diagram.
- Join tagging list into one-line text.
  For example, there is a genre list that has three tags: chillout, downtempo, and easylistening.
  The raw text of this example will be `"chillout downtempo easylistening"`.