---
license: apache-2.0
---

---
dataset_info:
- config_name: train
  features:
  - name: filename
    dtype: string
  - name: height
    dtype: int64
  - name: width
    dtype: int64
  - name: ann
    struct:
    - name: bboxes
      sequence:
        sequence: float64
    - name: bboxes_ignore
      sequence:
        sequence: int64
    - name: label_ignore
      sequence: int64
    - name: labels
      sequence: int64
  splits:
  - name: train
    num_bytes: 211748
    num_examples: 500
  download_size: 89624346
  dataset_size: 211748
- config_name: val
  features:
  - name: filename
    dtype: string
  - name: height
    dtype: int64
  - name: width
    dtype: int64
  - name: ann
    struct:
    - name: bboxes
      sequence:
        sequence: float64
    - name: bboxes_ignore
      sequence:
        sequence: int64
    - name: label_ignore
      sequence: int64
    - name: labels
      sequence: int64
  splits:
  - name: val
    num_bytes: 209868
    num_examples: 500
  download_size: 82654443
  dataset_size: 209868
---
