---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: link
    dtype: string
  - name: transcript
    dtype: string
  - name: segments
    list:
    - name: end
      dtype: float64
    - name: start
      dtype: float64
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 4845076
    num_examples: 39
  download_size: 2633561
  dataset_size: 4845076
task_categories:
- text-classification
- text-generation
- summarization
language:
- en
size_categories:
- n<1K
pretty_name: TalkRL Podcast
---
# Dataset Card for "talkrl-podcast"

This dataset is sourced from the [TalkRL Podcast website](https://www.talkrl.com/) and contains English transcripts of wonderful TalkRL podcast episodes. The transcripts were generated using OpenAI's base Whisper model