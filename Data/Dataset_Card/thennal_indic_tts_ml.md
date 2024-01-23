---
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: text
    dtype: string
  - name: gender
    dtype: string
  splits:
  - name: train
    num_bytes: 4830182115.4
    num_examples: 8600
  download_size: 3966895730
  dataset_size: 4830182115.4
annotations_creators: []
language:
- ml
language_creators: []
license:
- other
multilinguality:
- monolingual
pretty_name: Indic TTS Malayalam Speech Corpus
size_categories:
- 1K<n<10K
source_datasets: []
tags: []
task_categories:
- text-to-speech
- automatic-speech-recognition
task_ids: []
---
# Indic TTS Malayalam Speech Corpus
The Malayalam subset of [Indic TTS Corpus](https://www.iitm.ac.in/donlab/tts/index.php), taken from
[this Kaggle database.](https://www.kaggle.com/datasets/kavyamanohar/indic-tts-malayalam-speech-corpus) The corpus contains
one male and one female speaker, with a 2:1 ratio of samples due to missing files for the female speaker. The license is given
in the repository.