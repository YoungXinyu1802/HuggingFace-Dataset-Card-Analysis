---
annotations_creators:
- expert-generated
language:
- ko
language_creators:
- crowdsourced
license: []
multilinguality:
- monolingual
pretty_name: KsponSpeech
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for KsponSpeech

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

- **Homepage:** [AIHub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=123)
- **Repository:**
- **Paper:** [KsponSpeech](https://www.mdpi.com/2076-3417/10/19/6936)
- **Leaderboard:**
- **Point of Contact:** 

### Dataset Summary

This corpus contains 969 h of general open-domain dialog utterances, spoken by about 2000 native Korean speakers in a clean environment. All data were constructed by recording the dialogue of two people freely conversing on a variety of topics and manually transcribing the utterances. The transcription provides a dual transcription consisting of orthography and pronunciation, and disfluency tags for spontaneity of speech, such as filler words, repeated words, and word fragments. This paper also presents the baseline performance of an end-to-end speech recognition model trained with KsponSpeech. In addition, we investigated the performance of standard end-to-end architectures and the number of sub-word units suitable for Korean. We investigated issues that should be considered in spontaneous speech recognition in Korean. KsponSpeech is publicly available on an open data hub site of the Korea government.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Korean

## Dataset Structure

### Data Instances

```json
{
  'id': 'KsponSpeech_E00001',
  'audio': {'path': None,
  'array': array([0.0010376 , 0.00085449, 0.00097656, ..., 0.00250244, 0.0022583 ,
          0.00253296]),
  'sampling_rate': 16000},
  'text': '어 일단은 억지로 과장해서 이렇게 하는 것보다 진실된 마음으로 이걸 어떻게 전달할 수 있을까 공감을 시킬 수 있을까 해서 좀'
}
```

### Data Fields

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- text: the transcription of the audio file.
- id: unique id of the data sample.

### Data Splits

|                             | Train | Valid | eval.clean  | eval.other | 
| -----                       | ------ | ----- | ---- | ---- |
| #samples | 620000 | 2545 | 3000 | 3000 |

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
```bibtex
@Article{app10196936,
AUTHOR = {Bang, Jeong-Uk and Yun, Seung and Kim, Seung-Hi and Choi, Mu-Yeol and Lee, Min-Kyu and Kim, Yeo-Jeong and Kim, Dong-Hyun and Park, Jun and Lee, Young-Jik and Kim, Sang-Hun},
TITLE = {KsponSpeech: Korean Spontaneous Speech Corpus for Automatic Speech Recognition},
JOURNAL = {Applied Sciences},
VOLUME = {10},
YEAR = {2020},
NUMBER = {19},
ARTICLE-NUMBER = {6936},
URL = {https://www.mdpi.com/2076-3417/10/19/6936},
ISSN = {2076-3417},
ABSTRACT = {This paper introduces a large-scale spontaneous speech corpus of Korean, named KsponSpeech. This corpus contains 969 h of general open-domain dialog utterances, spoken by about 2000 native Korean speakers in a clean environment. All data were constructed by recording the dialogue of two people freely conversing on a variety of topics and manually transcribing the utterances. The transcription provides a dual transcription consisting of orthography and pronunciation, and disfluency tags for spontaneity of speech, such as filler words, repeated words, and word fragments. This paper also presents the baseline performance of an end-to-end speech recognition model trained with KsponSpeech. In addition, we investigated the performance of standard end-to-end architectures and the number of sub-word units suitable for Korean. We investigated issues that should be considered in spontaneous speech recognition in Korean. KsponSpeech is publicly available on an open data hub site of the Korea government.},
DOI = {10.3390/app10196936}
}
```
