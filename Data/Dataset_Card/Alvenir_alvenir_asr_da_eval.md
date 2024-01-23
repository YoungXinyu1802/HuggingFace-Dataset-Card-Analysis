---
license: cc-by-4.0
---

# Dataset Card alvenir_asr_da_eval
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Prompts/sentence selection](#prompts/sentence-selection)
  - [Recording](#recording)
  - [Evaluation](#evaluation)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Licensing Information](#licensing-information)

## Dataset Description

- **Homepage:** https://alvenir.ai
- **Repository:** https://github.com/danspeech/alvenir-asr-da-eval/

### Dataset Summary

This dataset was created by Alvenir in order to evaluate ASR models in Danish. It can also be used for training but the amount is very limited.

The dataset consists of .wav files with corresponding reference text. The amount of data is just above 5 hours spread across 50 speakers with age in the interval 20-60 years old. The data was collected by a third party vendor through their software and people. All recordings have been validated.  

## Dataset Structure
### Data Instances

A data point consists of a path to the audio file, called path and its sentence. Additional fields will eventually be added such as age and gender.

`
{'audio': {'path': `some_path.wav', 'array': array([-0.044223, -0.00031411, -0.00435671, ...,  0.00612312, 0.00014581,  0.00091009], dtype=float32), 'sampling_rate': 16000}}
`

### Data Fields

audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

sentence: The sentence the user was prompted to speak

### Data Splits
Since the idea behind the dataset is for it to be used as a test/eval ASR dataset for Danish, there is only test split.

## Dataset Creation

### Prompts/sentence selection

The sentences used for prompts were gathered from the danish part of open subtitles (OSS) (need reference) and wikipedia (WIKI). The OSS prompts sampled randomly across the dataset making sure that all prompts are unique. The WIKI prompts were selected by first training a topic model with 30 topics on wikipedia and than randomly sampling an equal amount of unique sentences from each topic. All sentences were manually inspected.

### Recording 

50 unique speakers were all sent 20 WIKI sentences and 60 sentences from OSS. The recordings took place through third party recording software. 

### Evaluation

All recordings were evaluated by third party to confirm alignment between audio and text.

### Personal and Sensitive Information

The dataset consists of people who have given their voice to the dataset for ASR purposes. You agree to not attempt to determine the identity of any of the speakers in the  dataset.

### Licensing Information

[cc-by-4.0](https://creativecommons.org/licenses/by/4.0/)



