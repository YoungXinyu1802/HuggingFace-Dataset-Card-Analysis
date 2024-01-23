---
annotations_creators: []
language:
- en
- de
- fr
- es
- pl
- it
- ro
- hu
- cs
- nl
- fi
- hr
- sk
- sl
- et
- lt
language_creators: []
license:
- cc0-1.0
- other
multilinguality:
- multilingual
pretty_name: VoxPopuli
size_categories: []
source_datasets: []
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for Voxpopuli

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

- **Homepage:** https://github.com/facebookresearch/voxpopuli
- **Repository:** https://github.com/facebookresearch/voxpopuli
- **Paper:** https://arxiv.org/abs/2101.00390
- **Point of Contact:** [changhan@fb.com](mailto:changhan@fb.com), [mriviere@fb.com](mailto:mriviere@fb.com), [annl@fb.com](mailto:annl@fb.com)

### Dataset Summary

VoxPopuli is a large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation.
The raw data is collected from 2009-2020 [European Parliament event recordings](https://multimedia.europarl.europa.eu/en/home). We acknowledge the European Parliament for creating and sharing these materials.
This implementation contains transcribed speech data for 18 languages.
It also contains 29 hours of transcribed speech data of non-native English intended for research in ASR for accented speech (15 L2 accents)

### Example usage

VoxPopuli contains labelled data for 18 languages. To load a specific language pass its name as a config name:

```python
from datasets import load_dataset

voxpopuli_croatian = load_dataset("facebook/voxpopuli", "hr")
```

To load all the languages in a single dataset use "multilang" config name:

```python
voxpopuli_all = load_dataset("facebook/voxpopuli", "multilang")
```

To load a specific set of languages, use "multilang" config name and pass a list of required languages to `languages` parameter:

```python
voxpopuli_slavic = load_dataset("facebook/voxpopuli", "multilang", languages=["hr", "sk", "sl", "cs", "pl"])
```

To load accented English data, use "en_accented" config name:

```python
voxpopuli_accented = load_dataset("facebook/voxpopuli", "en_accented")
```

**Note that L2 English subset contains only `test` split.**


### Supported Tasks and Leaderboards

* automatic-speech-recognition: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

Accented English subset can also be used for research in ASR for accented speech (15 L2 accents)

### Languages

VoxPopuli contains labelled (transcribed) data for 18 languages:

| Language | Code | Transcribed Hours | Transcribed Speakers | Transcribed Tokens |
|:---:|:---:|:---:|:---:|:---:|
| English | En | 543 | 1313 | 4.8M |
| German | De | 282 | 531 | 2.3M |
| French | Fr | 211 | 534 | 2.1M |
| Spanish | Es | 166 | 305 | 1.6M |
| Polish | Pl | 111 | 282 | 802K |
| Italian | It | 91 | 306 | 757K |
| Romanian | Ro | 89 | 164 | 739K |
| Hungarian | Hu | 63 | 143 | 431K |
| Czech | Cs | 62 | 138 | 461K |
| Dutch | Nl | 53 | 221 | 488K |
| Finnish | Fi | 27 | 84 | 160K |
| Croatian | Hr | 43 | 83 | 337K |
| Slovak | Sk | 35 | 96 | 270K |
| Slovene | Sl | 10 | 45 | 76K |
| Estonian | Et | 3 | 29 | 18K |
| Lithuanian | Lt | 2 | 21 | 10K |
| Total | | 1791 | 4295 | 15M |


Accented speech transcribed data has 15 various L2 accents:

| Accent | Code | Transcribed Hours | Transcribed Speakers |
|:---:|:---:|:---:|:---:|
| Dutch | en_nl | 3.52 | 45 |
| German | en_de | 3.52 | 84 |
| Czech | en_cs | 3.30 | 26 |
| Polish | en_pl | 3.23 | 33 |
| French | en_fr | 2.56 | 27 |
| Hungarian | en_hu | 2.33 | 23 |
| Finnish | en_fi | 2.18 | 20 |
| Romanian | en_ro | 1.85 | 27 |
| Slovak | en_sk | 1.46 | 17 |
| Spanish | en_es | 1.42 | 18 |
| Italian | en_it | 1.11 | 15 |
| Estonian | en_et | 1.08 | 6 |
| Lithuanian | en_lt | 0.65 | 7 |
| Croatian | en_hr | 0.42 | 9 |
| Slovene | en_sl | 0.25 | 7 |

## Dataset Structure

### Data Instances

```python
{
  'audio_id': '20180206-0900-PLENARY-15-hr_20180206-16:10:06_5',
  'language': 11,  # "hr"
  'audio': {
    'path': '/home/polina/.cache/huggingface/datasets/downloads/extracted/44aedc80bb053f67f957a5f68e23509e9b181cc9e30c8030f110daaedf9c510e/train_part_0/20180206-0900-PLENARY-15-hr_20180206-16:10:06_5.wav',
    'array': array([-0.01434326, -0.01055908,  0.00106812, ...,  0.00646973], dtype=float32),
    'sampling_rate': 16000
  },
  'raw_text': '',
  'normalized_text': 'poast genitalnog sakaenja ena u europi tek je jedna od manifestacija takve tetne politike.',
  'gender': 'female',
  'speaker_id': '119431',
  'is_gold_transcript': True,
  'accent': 'None'
}
```

### Data Fields

* `audio_id` (string) - id of audio segment
* `language` (datasets.ClassLabel) - numerical id of audio segment 
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `raw_text` (string) - original (orthographic) audio segment text
* `normalized_text` (string) - normalized audio segment transcription
* `gender` (string) - gender of speaker
* `speaker_id` (string) - id of speaker
* `is_gold_transcript` (bool) - ?
* `accent` (string) - type of accent, for example "en_lt", if applicable, else "None".

### Data Splits

All configs (languages) except for accented English contain data in three splits: train, validation and test. Accented English `en_accented` config contains only test split.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

The raw data is collected from 2009-2020 [European Parliament event recordings](https://multimedia.europarl.europa.eu/en/home)

#### Initial Data Collection and Normalization

The VoxPopuli transcribed set comes from aligning  the full-event source speech audio with the transcripts for plenary sessions. Official timestamps
are available for locating speeches by speaker in the full session, but they are frequently inaccurate, resulting in truncation of the speech or mixture
of fragments from the preceding or the succeeding speeches. To calibrate the original timestamps,
we perform speaker diarization (SD) on the full-session audio using pyannote.audio (Bredin et al.2020) and adopt the nearest SD timestamps (by L1 distance to the original ones) instead for segmentation. 
Full-session audios are segmented into speech paragraphs by speaker, each of which has a transcript available.

The speech paragraphs have an average duration of 197 seconds, which leads to significant. We hence further segment these paragraphs into utterances with a
maximum duration of 20 seconds. We leverage speech recognition (ASR) systems to force-align speech paragraphs to the given transcripts.
The ASR systems are TDS models (Hannun et al., 2019) trained with ASG criterion (Collobert et al., 2016) on audio tracks from in-house deidentified video data.

The resulting utterance segments may have incorrect transcriptions due to incomplete raw transcripts or inaccurate ASR force-alignment. 
We use the predictions from the same ASR systems as references and filter the candidate segments by a maximum threshold of 20% character error rate(CER).

#### Who are the source language producers?

Speakers are participants of the European Parliament events, many of them are EU officials.

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

Gender speakers distribution is imbalanced, percentage of female speakers is mostly lower than 50% across languages, with the minimum of 15% for the Lithuanian language data.

VoxPopuli includes all available speeches from the 2009-2020 EP events without any selections on the topics or speakers.
The speech contents represent the standpoints of the speakers in the EP events, many of which are EU officials.


### Other Known Limitations


## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

The dataset is distributet under CC0 license, see also [European Parliament's legal notice](https://www.europarl.europa.eu/legal-notice/en/) for the raw data.

### Citation Information

Please cite this paper:

```bibtex
@inproceedings{wang-etal-2021-voxpopuli,
    title = "{V}ox{P}opuli: A Large-Scale Multilingual Speech Corpus for Representation Learning, Semi-Supervised Learning and Interpretation",
    author = "Wang, Changhan  and
      Riviere, Morgane  and
      Lee, Ann  and
      Wu, Anne  and
      Talnikar, Chaitanya  and
      Haziza, Daniel  and
      Williamson, Mary  and
      Pino, Juan  and
      Dupoux, Emmanuel",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.80",
    pages = "993--1003",
}
```

### Contributions

Thanks to [@polinaeterna](https://github.com/polinaeterna) for adding this dataset.
