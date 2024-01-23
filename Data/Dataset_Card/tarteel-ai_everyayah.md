---
pretty_name: Tarteel AI - EveryAyah Dataset
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: duration
    dtype: float64
  - name: text
    dtype: string
  - name: reciter
    dtype: string
  splits:
  - name: train
    num_bytes: 262627688145.3
    num_examples: 187785
  - name: test
    num_bytes: 25156009734.72
    num_examples: 23473
  - name: validation
    num_bytes: 23426886730.218
    num_examples: 23474
  download_size: 117190597305
  dataset_size: 311210584610.23804
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- ar
license:
- mit
multilinguality:
- monolingual
paperswithcode_id: tarteel-everyayah
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- automatic-speech-recognition
task_ids: []
train-eval-index:
- config: clean
  task: automatic-speech-recognition
  task_id: speech_recognition
  splits:
    train_split: train
    eval_split: test
    validation_split: validation
  col_mapping:
    audio: audio
    text: text
    reciter: text
  metrics:
  - type: wer
    name: WER
  - type: cer
    name: CER
---

﷽

# Dataset Card for Tarteel AI's EveryAyah Dataset

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [Tarteel AI](https://www.tarteel.ai/)
- **Repository:** [Needs More Information]
- **Point of Contact:** [Mohamed Saad Ibn Seddik](mailto:ms.ibnseddik@tarteel.ai)

### Dataset Summary

This dataset is a collection of Quranic verses and their transcriptions, with diacritization, by different reciters.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

The audio is in Arabic.

## Dataset Structure

### Data Instances

A typical data point comprises the audio file `audio`, and its transcription called `text`.
The `duration` is in seconds, and the author is `reciter`.

An example from the dataset is:
```
{
  'audio': {
    'path': None,
    'array': array([ 0.        ,  0.        ,  0.        , ..., -0.00057983,
       -0.00085449, -0.00061035]),
    'sampling_rate': 16000
  },
  'duration': 6.478375,
  'text': 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ',
  'reciter': 'abdulsamad'
}
```

### Data Fields

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- text: The transcription of the audio file.

- duration: The duration of the audio file. 

- reciter: The reciter of the verses. 

### Data Splits

|       | Train | Test | Validation |
| ----- | ----- | ---- | ---------- |
| dataset | 187785 | 23473 | 23474 |



## Dataset Creation

### Curation Rationale


### Source Data

#### Initial Data Collection and Normalization


#### Who are the source language producers?


### Annotations

#### Annotation process


#### Who are the annotators?



### Personal and Sensitive Information



## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators



### Licensing Information

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

```
```

### Contributions

This dataset was created by:
