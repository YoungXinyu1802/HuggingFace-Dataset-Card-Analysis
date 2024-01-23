---
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: speaker_id_str
    dtype: int64
  - name: speaker_id
    dtype: int64
  - name: question_id
    dtype: int64
  - name: total_score
    dtype: int64
  - name: accuracy
    dtype: int64
  - name: completeness
    dtype: float64
  - name: fluency
    dtype: int64
  - name: prosodic
    dtype: int64
  - name: text
    dtype: string
  - name: audio
    dtype: audio
  - name: path
    dtype: string
  splits:
  - name: test
    num_bytes: 288402967.0
    num_examples: 2500
  - name: train
    num_bytes: 290407029.0
    num_examples: 2500
  download_size: 0
  dataset_size: 578809996.0
---
# Dataset Card for "speechocean762"

The datasets introduced in
- Zhang, Junbo, et al. "speechocean762: An open-source non-native english speech corpus for pronunciation assessment." arXiv preprint arXiv:2104.01378 (2021).
- Currently, phonetic-level evaluation is omitted (total sentence-level scores are just used.)
- The original full data link: https://github.com/jimbozhang/speechocean762 


[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)