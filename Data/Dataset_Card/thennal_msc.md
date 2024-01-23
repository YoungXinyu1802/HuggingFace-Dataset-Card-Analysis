---
annotations_creators:
- crowdsourced
language:
- ml
language_creators:
- crowdsourced
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Swathanthra Malayalam Computing Malayalam Speech Corpus
size_categories:
- 1K<n<10K
source_datasets: []
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
dataset_info:
  features:
  - name: speechid
    dtype: string
  - name: speaker_id
    dtype: string
  - name: review_score
    dtype: int64
  - name: transcript
    dtype: string
  - name: category
    dtype: string
  - name: speaker_gender
    dtype: string
  - name: speaker_age
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 48000
  splits:
  - name: train
    num_bytes: 581998721.306
    num_examples: 1541
  download_size: 422643542
  dataset_size: 581998721.306
---

# SMC Malayalam Speech Corpus

Malayalam Speech Corpus (MSC) is a repository of curated speech samples collected using MSC web application, released by Swathanthra Malayalam Computing. 
The official blog post and source data can be found at [https://blog.smc.org.in/malayalam-speech-corpus/](https://blog.smc.org.in/malayalam-speech-corpus/).

## Dataset Description

- **Homepage:** [https://blog.smc.org.in/malayalam-speech-corpus/](https://blog.smc.org.in/malayalam-speech-corpus/)

### Dataset Summary

The first version of Malayalam Speech Corpus contains 1541 speech samples from 75 contributors amounting to 1:38:16 hours of speech. It has 482 unique sentences, 1400 unique words, 553 unique syllables and 48 unique phonemes.
