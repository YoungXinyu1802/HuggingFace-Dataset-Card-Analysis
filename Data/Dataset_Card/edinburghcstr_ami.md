---
annotations_creators: []
language:
- en
language_creators: []
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: AMI
size_categories: []
source_datasets: []
tags: []
task_categories:
- automatic-speech-recognition
---

# Dataset Card for AMI

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
- [Terms of Usage](#terms-of-usage)
  

## Dataset Description

- **Homepage:** https://groups.inf.ed.ac.uk/ami/corpus/
- **Repository:** https://github.com/kaldi-asr/kaldi/tree/master/egs/ami/s5 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** [jonathan@ed.ac.uk](mailto:jonathan@ed.ac.uk)

## Dataset Description

The AMI Meeting Corpus consists of 100 hours of meeting recordings. The recordings use a range of signals
synchronized to a common timeline. These include close-talking and far-field microphones, individual and
room-view video cameras, and output from a slide projector and an electronic whiteboard. During the meetings,
the participants also have unsynchronized pens available to them that record what is written. The meetings
were recorded in English using three different rooms with different acoustic properties, and include mostly
non-native speakers.

**Note**: This dataset corresponds to the data-processing of [KALDI's AMI S5 recipe](https://github.com/kaldi-asr/kaldi/tree/master/egs/ami/s5).
This means text is normalized and the audio data is chunked according to the scripts above!
To make the user experience as simply as possible, we provide the already chunked data to the user here so that the following can be done:


### Example Usage

```python
from datasets import load_dataset
ds = load_dataset("edinburghcstr/ami", "ihm")

print(ds)
```
gives:
```
DatasetDict({
    train: Dataset({
        features: ['meeting_id', 'audio_id', 'text', 'audio', 'begin_time', 'end_time', 'microphone_id', 'speaker_id'],
        num_rows: 108502
    })
    validation: Dataset({
        features: ['meeting_id', 'audio_id', 'text', 'audio', 'begin_time', 'end_time', 'microphone_id', 'speaker_id'],
        num_rows: 13098
    })
    test: Dataset({
        features: ['meeting_id', 'audio_id', 'text', 'audio', 'begin_time', 'end_time', 'microphone_id', 'speaker_id'],
        num_rows: 12643
    })
})
```

```py
ds["train"][0]
```

automatically loads the audio into memory:

```
{'meeting_id': 'EN2001a',
 'audio_id': 'AMI_EN2001a_H00_MEE068_0000557_0000594',
 'text': 'OKAY',
 'audio': {'path': '/cache/dir/path/downloads/extracted/2d75d5b3e8a91f44692e2973f08b4cac53698f92c2567bd43b41d19c313a5280/EN2001a/train_ami_en2001a_h00_mee068_0000557_0000594.wav',
  'array': array([0.        , 0.        , 0.        , ..., 0.00033569, 0.00030518,
         0.00030518], dtype=float32),
  'sampling_rate': 16000},
 'begin_time': 5.570000171661377,
 'end_time': 5.940000057220459,
 'microphone_id': 'H00',
 'speaker_id': 'MEE068'}
```


The dataset was tested for correctness by fine-tuning a Wav2Vec2-Large model on it, more explicitly [the `wav2vec2-large-lv60` checkpoint](https://huggingface.co/facebook/wav2vec2-large-lv60).

As can be seen in this experiments, training the model for less than 2 epochs gives

*Result (WER)*:

| "dev" | "eval" |
|---|---|
| 25.27 | 25.21 |

as can be seen [here](https://huggingface.co/patrickvonplaten/ami-wav2vec2-large-lv60).

The results are in-line with results of published papers:

- [*Hybrid acoustic models for distant and multichannel large vocabulary speech recognition*](https://www.researchgate.net/publication/258075865_Hybrid_acoustic_models_for_distant_and_multichannel_large_vocabulary_speech_recognition)
- [Multi-Span Acoustic Modelling using Raw Waveform Signals](https://arxiv.org/abs/1906.11047)

You can run [run.sh](https://huggingface.co/patrickvonplaten/ami-wav2vec2-large-lv60/blob/main/run.sh) to reproduce the result.

### Supported Tasks and Leaderboards

### Languages

## Dataset Structure

### Data Instances

### Data Fields

### Data Splits

#### Transcribed Subsets Size

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

### Other Known Limitations

## Additional Information

### Dataset Curators


### Licensing Information


### Citation Information


### Contributions

Thanks to [@sanchit-gandhi](https://github.com/sanchit-gandhi), [@patrickvonplaten](https://github.com/patrickvonplaten), 
and [@polinaeterna](https://github.com/polinaeterna) for adding this dataset.

## Terms of Usage


