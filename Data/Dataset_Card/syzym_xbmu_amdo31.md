---
pretty_name: XBMU-AMDO31
annotations_creators:
- expert-generated
language_creatosr:
- expert-generated
language:
- tib
license: 
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- automatic-speech-recognition
---

# Dataset Card for [XBMU-AMDO31]

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

- **Homepage:**https://github.com/sendream/xbmu_amdo31
- **Repository:**https://github.com/sendream/xbmu_amdo31
- **Paper:**
- **Leaderboard:**https://github.com/sendream/xbmu_amdo31#leaderboard
- **Point of Contact:**[xxlgy@xbmu.edu.cn](mailto:xxlgy@xbmu.edu.cn)

### Dataset Summary

XBMU-AMDO31 dataset is a speech recognition corpus of Amdo Tibetan dialect. The open source corpus contains 31 hours of speech data and resources related to build speech recognition systems, including transcribed texts and a Tibetan pronunciation dictionary.

### Supported Tasks and Leaderboards

automatic-speech-recognition: The dataset can be used to train a model for Amdo Tibetan Automatic Speech Recognition (ASR). It was recorded by 66 native speakers of Amdo Tibetan, and the recorded audio was processed and manually inspected. The most common evaluation metric is the word error rate (WER). The task has an active leaderboard which can be found at https://github.com/sendream/xbmu_amdo31#leaderboard and ranks models based on their WER.

### Languages

XBMU-AMDO31 contains audio, a Tibetan pronunciation dictionary and transcription data in Amdo Tibetan.

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

The dataset has three splits: train, evaluation (dev) and test.Each speaker had approximately 450 sentences, with a small number of individuals having fewer than 200 sen

| Subset | Hours | Male | Female | Remarks                                 |
| ------ | ----- | ---- | ------ | --------------------------------------- |
| Train  | 25.41 | 27   | 27     | 18539 sentences recorded by 54 speakers |
| Dev    | 2.81  | 2    | 4      | 2050 sentences recorded by 6 speakers   |
| Test   | 2.85  | 3    | 3      | 2041 sentences recorded by 6 speakers   |

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

This dataset is distributed under CC BY-SA 4.0.

### Citation Information

[More Information Needed]

### Contributions

Thanks to  [@speechless-z](https://github.com/speechless-z) for adding this dataset.