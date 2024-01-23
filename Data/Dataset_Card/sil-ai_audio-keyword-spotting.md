---
annotations_creators:
- machine-generated
language_creators:
- other
language:
- eng
- en
- spa
- es
- ind
- id
license: cc-by-4.0
multilinguality:
- multilingual
source_datasets:
- extended|common_voice
- MLCommons/ml_spoken_words
task_categories:
- automatic-speech-recognition
task_ids: []
pretty_name: Audio Keyword Spotting
tags:
- other-keyword-spotting
---

# Dataset Card for Audio Keyword Spotting

## Table of Contents
- [Table of Contents](#table-of-contents)

## Dataset Description

- **Homepage:** https://sil.ai.org
- **Point of Contact:** [SIL AI email](mailto:idx_aqua@sil.org)
- **Source Data:** [MLCommons/ml_spoken_words](https://huggingface.co/datasets/MLCommons/ml_spoken_words), [trabina GitHub](https://github.com/wswu/trabina) 

![sil-ai logo](https://s3.amazonaws.com/moonup/production/uploads/1661440873726-6108057a823007eaf0c7bd10.png) 

## Dataset Summary

The initial version of this dataset is a subset of [MLCommons/ml_spoken_words](https://huggingface.co/datasets/MLCommons/ml_spoken_words), which is derived from Common Voice, designed for easier loading. Specifically, the subset consists of `ml_spoken_words` files filtered by the names and placenames transliterated in Bible translations, as found in [trabina](https://github.com/wswu/trabina). For our initial experiment, we have focused only on English, Spanish, and Indonesian, three languages whose name spellings are frequently used in other translations. We anticipate growing this dataset in the future to include additional keywords and other languages as the experiment progresses.

### Data Fields

* file: strinrelative audio path inside the archive
* is_valid: if a sample is valid
* language: language of an instance. 
* speaker_id: unique id of a speaker. Can be "NA" if an instance is invalid
* gender: speaker gender. Can be one of `["MALE", "FEMALE", "OTHER", "NAN"]`
* keyword: word spoken in a current sample
* audio: a dictionary containing the relative path to the audio file, 
the decoded audio array, and the sampling rate. 
Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically 
decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of 
a large number of audio files might take a significant amount of time. 
Thus, it is important to first query the sample index before the "audio" column, 
i.e. `dataset[0]["audio"]` should always be preferred over `dataset["audio"][0]`

### Data Splits

The data for each language is splitted into train / validation / test parts.

## Supported Tasks
Keyword spotting and spoken term search

### Personal and Sensitive Information

The dataset consists of people who have donated their voice online. 
You agree to not attempt to determine the identity of speakers.

### Licensing Information

The dataset is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) and can be used for academic
research and commercial applications in keyword spotting and spoken term search.

