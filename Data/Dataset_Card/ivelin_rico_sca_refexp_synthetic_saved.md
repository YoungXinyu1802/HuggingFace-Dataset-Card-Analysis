---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: image_id
    dtype: string
  - name: labels
    list:
    - name: prompt
      dtype: string
    - name: target_bounding_box
      struct:
      - name: xmin
        dtype: float32
      - name: ymin
        dtype: float32
      - name: xmax
        dtype: float32
      - name: ymax
        dtype: float32
  splits:
  - name: train
    num_bytes: 2604982403.694
    num_examples: 24063
  - name: validation
    num_bytes: 21192787.0
    num_examples: 160
  - name: test
    num_bytes: 22057836.0
    num_examples: 185
  download_size: 2096931333
  dataset_size: 2648233026.694
---
# Dataset Card for "rico_sca_refexp_synthetic_saved"

This is a saved snapshot of the dynamically generated [Rico SCA RefExp dataset](https://huggingface.co/datasets/ivelin/rico_sca_refexp_synthetic)