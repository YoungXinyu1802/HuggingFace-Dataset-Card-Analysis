---
task_categories:
- summarization
- text2text-generation
language:
- 'no'
- nb
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: title
    dtype: string
  - name: url
    dtype: string
  - name: published
    dtype: string
  - name: classes
    dtype: string
  - name: article
    dtype: string
  - name: ingress
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 482362411.09144986
    num_examples: 157038
  - name: validation
    num_bytes: 36309721.60567524
    num_examples: 11821
  - name: test
    num_bytes: 57632967.30287493
    num_examples: 18763
  download_size: 364433583
  dataset_size: 576305100.0
---
Articles and ingresses from VG news articles extracted from Norsk Aviskorpus

187622 samples