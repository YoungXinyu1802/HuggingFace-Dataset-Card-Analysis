---
annotations_creators:
- expert-generated
language:
- pl
license:
- other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- other
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for ClarinPL Studio Speech Corpus

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
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [CLARIN-PL mowa](https://mowa.clarin-pl.eu/)
- **Repository:** [Kaldi Baseline](https://github.com/danijel3/ClarinStudioKaldi)
- **Paper:** [Polish Read Speech Corpus for Speech Tools and Services](https://arxiv.org/abs/1706.00245)
- **Leaderboard:** [Paperswithcode Leaderboard][Needs More Information]
- **Point of Contact:** [Danijel Koržinek](https://github.com/danijel3/)

### Dataset Summary

The corpus consists of 317 speakers recorded in 554
sessions, where each session consists of 20 read sentences and 10 phonetically rich words. The size of
the audio portion of the corpus amounts to around 56 hours, with transcriptions containing 356674 words
from a vocabulary of size 46361.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

The audio is in Polish.

## Dataset Structure

### Data Instances

A typical data point comprises the path to the audio file, usually called `file` and its transcription, called `text`.
An example from the dataset is:
```
{'file': '/root/.cache/huggingface/datasets/downloads/extracted/333ddc746f2df1e1d19b44986992d4cbe28710fde81d533a220e755ee6c5c519/audio/SES0001/rich001.wav',
 'id': 'SES0001_rich001',
 'speaker_id': 'SPK0001',
 'text': 'drożdże dżip gwożdżenie ozimina wędzarz rdzeń wędzonka ingerować kładzenie jutrzenka'}
```

### Data Fields

- file: A path to the downloaded audio file in .wav format.
- text: the transcription of the audio file.
- speaker_id: The ID of the speaker of the audio.

### Data Splits

|       | Train | Test | Valid |
| ----- | ----- | ---- | ----- |
| dataset | 11222 | 1362 | 1229 | 



## Dataset Creation

### Curation Rationale

The purpose of this segment of the project was to develop specific tools that would allow for automatic and semi-automatic processing of large quantities of acoustic speech data. Another purpose of the corpus was to serve as a reference for studies in phonetics and pronunciation.

### Source Data

#### Initial Data Collection and Normalization

The corpus was recorded in a studio environment using two microphones: a high-quality studio microphone and a typical consumer audio headset.

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

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[CLARIN PUB+BY+INF+NORED](https://mowa.clarin-pl.eu/korpusy/LICENSE)

### Citation Information

```
@article{korvzinek2017polish,
  title={Polish read speech corpus for speech tools and services},
  author={Kor{\v{z}}inek, Danijel and Marasek, Krzysztof and Brocki, {\L}ukasz and Wo{\l}k, Krzysztof},
  journal={arXiv preprint arXiv:1706.00245},
  year={2017}
}
```

### Contributions

[Needs More Information]
