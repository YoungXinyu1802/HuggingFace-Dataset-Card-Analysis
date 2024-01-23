---
annotations_creators:
- other
language_creators:
- other
language:
- en
license:
- odc-by
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- extended|vctk
task_categories:
- audio-classification
task_ids: []
pretty_name: asvspoof2019
tags:
- voice-anti-spoofing
---

# Dataset Card for asvspoof2019

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://datashare.ed.ac.uk/handle/10283/3336
- **Repository:** [Needs More Information]
- **Paper:** https://arxiv.org/abs/1911.01601
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This is a database used for the Third Automatic Speaker Verification Spoofing
and Countermeasuers Challenge, for short, ASVspoof 2019 (http://www.asvspoof.org)
organized by Junichi Yamagishi, Massimiliano Todisco, Md Sahidullah, Héctor
Delgado, Xin Wang, Nicholas Evans, Tomi Kinnunen, Kong Aik Lee, Ville Vestman,
and Andreas Nautsch in 2019.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

English

## Dataset Structure

### Data Instances

```
{'speaker_id': 'LA_0091',
 'audio_file_name': 'LA_T_8529430',
 'audio': {'path': 'D:/Users/80304531/.cache/huggingface/datasets/downloads/extracted/8cabb6d5c283b0ed94b2219a8d459fea8e972ce098ef14d8e5a97b181f850502/LA/ASVspoof2019_LA_train/flac/LA_T_8529430.flac',
  'array': array([-0.00201416, -0.00234985, -0.0022583 , ...,  0.01309204,
          0.01339722,  0.01461792], dtype=float32),
  'sampling_rate': 16000},
 'system_id': 'A01',
 'key': 1}
```

### Data Fields

Logical access (LA):
- `speaker_id`: `LA_****`, a 4-digit speaker ID
- `audio_file_name`: name of the audio file
- `audio`: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- `system_id`: ID of the speech spoofing system (A01 - A19),  or, for bonafide speech SYSTEM-ID is left blank ('-')
- `key`: 'bonafide' for genuine speech, or, 'spoof' for spoofing speech

Physical access (PA):
- `speaker_id`: `PA_****`, a 4-digit speaker ID

- `audio_file_name`: name of the audio file

- `audio`: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- `environment_id`: a triplet (S,R,D_s), which take one letter in the set {a,b,c} as categorical value, defined as

  |                                  | a      | b       | c        |
  | -------------------------------- | ------ | ------- | -------- |
  | S: Room size (square meters)     | 2-5    | 5-10    | 10-20    |
  | R: T60 (ms)                      | 50-200 | 200-600 | 600-1000 |
  | D_s: Talker-to-ASV distance (cm) | 10-50  | 50-100  | 100-150  |

- `attack_id`: a duple (D_a,Q), which take one letter in the set {A,B,C} as categorical value, defined as

  |                                     | A       | B      | C     |
  | ----------------------------------- | ------- | ------ | ----- |
  | Z: Attacker-to-talker distance (cm) | 10-50   | 50-100 | > 100 |
  | Q: Replay device quality            | perfect | high   | low   |

  for bonafide speech, `attack_id` is left blank ('-')

- `key`: 'bonafide' for genuine speech, or, 'spoof' for spoofing speech

### Data Splits

|          | Training set | Development set | Evaluation set |
| -------- | ------------ | --------------- | -------------- |
| Bonafide | 2580         | 2548            | 7355           |
| Spoof    | 22800        | 22296           | 63882          |
| Total    | 25380        | 24844           | 71237          |

## Dataset Creation

### Curation Rationale

[Needs More Information]

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

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

This ASVspoof 2019 dataset is made available under the Open Data Commons Attribution License: http://opendatacommons.org/licenses/by/1.0/

### Citation Information

```
@InProceedings{Todisco2019,
  Title     = {{ASV}spoof 2019: {F}uture {H}orizons in {S}poofed and {F}ake {A}udio {D}etection},
  Author    = {Todisco, Massimiliano and
               Wang, Xin and
               Sahidullah, Md and
               Delgado, H ́ector and
               Nautsch, Andreas and
               Yamagishi, Junichi and
               Evans, Nicholas and
               Kinnunen, Tomi and
               Lee, Kong Aik},
  booktitle = {Proc. of Interspeech 2019},
  Year      = {2019}
}
```
