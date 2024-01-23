---
annotations_creators:
- expert-generated
language:
- zh
language_creators:
- crowdsourced
license:
- cc-by-nc-nd-4.0
multilinguality:
- monolingual
pretty_name: MAGICDATA_Mandarin_Chinese_Read_Speech_Corpus
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for MMCRSC

## Table of Contents
- [Table of Contents](#table-of-contents)
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

- **Homepage:** [MAGICDATA Mandarin Chinese Read Speech Corpus](https://openslr.org/68/)
- **Repository:**
- **Paper:** 
- **Leaderboard:**
- **Point of Contact:** 

### Dataset Summary

MAGICDATA Mandarin Chinese Read Speech Corpus was developed by MAGIC DATA Technology Co., Ltd. and freely published for non-commercial use.
The contents and the corresponding descriptions of the corpus include:

The corpus contains 755 hours of speech data, which is mostly mobile recorded data.
1080 speakers from different accent areas in China are invited to participate in the recording.
The sentence transcription accuracy is higher than 98%.
Recordings are conducted in a quiet indoor environment.
The database is divided into training set, validation set, and testing set in a ratio of 51: 1: 2.
Detail information such as speech data coding and speaker information is preserved in the metadata file.
The domain of recording texts is diversified, including interactive Q&A, music search, SNS messages, home command and control, etc.
Segmented transcripts are also provided.
The corpus aims to support researchers in speech recognition, machine translation, speaker recognition, and other speech-related fields. Therefore, the corpus is totally free for academic use.
The corpus is a subset of a much bigger data ( 10566.9 hours Chinese Mandarin Speech Corpus ) set which was recorded in the same environment. Please feel free to contact us via business@magicdatatech.com for more details.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

zh-CN

## Dataset Structure

### Data Instances

```json
{
  'file': '14_3466_20170826171404.wav',
  'audio': {
    'path': '14_3466_20170826171404.wav',
    'array': array([0., 0., 0., ..., 0., 0., 0.]),
    'sampling_rate': 16000
  },
  'text': '请搜索我附近的超市',
  'speaker_id': 143466,
  'id': '14_3466_20170826171404.wav'
}
```

### Data Fields

- file: A path to the downloaded audio file in .wav format.
- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- text: the transcription of the audio file.
- id: unique id of the data sample.
- speaker_id: unique id of the speaker. The same speaker id can be found for multiple data samples.

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

Please cite the corpus as "Magic Data Technology Co., Ltd., "http://www.imagicdatatech.com/index.php/home/dataopensource/data_info/id/101", 05/2019".
