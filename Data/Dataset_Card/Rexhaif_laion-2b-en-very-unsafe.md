---
dataset_info:
  features:
  - name: URL
    dtype: string
  - name: TEXT
    dtype: string
  - name: WIDTH
    dtype: int32
  - name: HEIGHT
    dtype: int32
  - name: similarity
    dtype: float64
  - name: hash
    dtype: int64
  - name: punsafe
    dtype: float32
  - name: pwatermark
    dtype: float32
  splits:
  - name: train
    num_bytes: 6799407448
    num_examples: 34607134
  download_size: 5322013902
  dataset_size: 6799407448
---
# Dataset Card for "laion-2b-en-very-unsafe"

A version of laion5b dataset(en subset) with strictly `unsafe` images.
Dataset was filtered to retain only examples with `punsafe` present and > 0.9.
However, due to the way nsfw detector was train, there is a significant amount of false postives.
There is, likely, more false positives than real unsafe images.