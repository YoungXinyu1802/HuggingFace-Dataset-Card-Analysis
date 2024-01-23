---
pretty_name: RyanSpeech
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- automatic-speech-recognition
- audio-classification
- speech-synthesis
---

# Dataset Card for librispeech_asr

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

- **Homepage:** [RyanSpeech corpus](http://mohammadmahoor.com/ryanspeech/)
- **Repository:** [Ryan TTS](https://github.com/roholazandie/ryan-tts)
- **Paper:** [RyanSpeech: A Corpus for Conversational Text-to-Speech Synthesis](https://arxiv.org/abs/2106.08468)
- **Leaderboard:** [RyanTTS](https://huggingface.co/spaces/Roh/RyanSpeech)
- **Point of Contact:** [Rohola Zandie](mailto:rohola.zandie@gmail.com)

### Dataset Summary

RyanSpeech is a speech corpus for research on automated text-to-speech (TTS) systems. Publicly available TTS corpora are often noisy, recorded with multiple speakers, or lack quality male speech data. In order to meet the need for a high-quality, publicly available male speech corpus within the field of speech recognition, we have designed and created RyanSpeech which contains textual materials from real-world conversational settings. These materials contain over 10 hours of a professional male voice actor's speech recorded at 44.1 kHz. This corpus's design and pipeline make RyanSpeech ideal for developing TTS systems in real-world applications. To provide a baseline for future research, protocols, and benchmarks, we trained 4 state-of-the-art speech models and a vocoder on RyanSpeech. The results show 3.36 in mean opinion scores (MOS) in our best model. We have made both the corpus and trained models for public use.

### Supported Tasks and Leaderboards

- `speech-synthesis`, `automatic-speech-recognition`: The dataset can be used to train a model for Speech Synthesis (TTS) or Automatic Speech Recognition (ASR). We have trained 4 different models based on this dataset: [tacotron](https://huggingface.co/espnet/english_male_ryanspeech_tacotron), [fastspeech](https://huggingface.co/espnet/english_male_ryanspeech_fastspeech), [fastspeech2](https://huggingface.co/espnet/english_male_ryanspeech_fastspeech2) and [conformer](https://huggingface.co/espnet/english_male_ryanspeech_conformer_fastspeech2) all of which are available on 🤗 huggingface spaces.

### Languages

The audio is in English.

## Dataset Structure

### Data Instances

A typical data point comprises the 'id', the audio file and the path to the audio file 'audio' and its transcription, called `text`

```
{'id': 'RY0002-1498', 
'audio': {'path': '/home/downloads/extracted/95ae28dc9210201ceed4e37e4e7758eca933beb002f7291cbdeea0c61c586514/train/wavs/RY0002-1498.wav', 
'array': array([ 1.4025815e-06,  8.8169247e-05,  1.5270278e-04, ...,
       -1.5984153e-04, -7.7941244e-05,  0.0000000e+00], dtype=float32), 'sampling_rate': 22500},
'text': 'The first PC computers appeared around 1975,'}
```


### Data Fields

- id: unique id of the data sample.
- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- text: the transcription of the audio file.


### Data Splits

The data has been split into three parts: train (7895), test (2256), and validation(1123). 



## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

The dataset consists of people who have donated their voice online. You agree to not attempt to determine the identity of speakers in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[Needs More Information]



### Licensing Information

[CC by NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

### Citation Information

```
@inproceedings{Zandie2021RyanSpeechAC,
  title={RyanSpeech: A Corpus for Conversational Text-to-Speech Synthesis},
  author={Rohola Zandie and Mohammad H. Mahoor and Julia Madsen and Eshrat S. Emamian},
  booktitle={Interspeech},
  year={2021}
}
```

