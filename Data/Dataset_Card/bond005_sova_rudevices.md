---
pretty_name: RuDevices
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- ru
license:
- cc-by-4.0
multilinguality:
- monolingual
paperswithcode_id: 
size_categories:
- 10K<n<100k
source_datasets:
- extended
task_categories:
- automatic-speech-recognition
- audio-classification
---
# Dataset Card for sova_rudevices
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
- **Homepage:** [SOVA RuDevices](https://github.com/sovaai/sova-dataset)
- **Repository:** [SOVA Dataset](https://github.com/sovaai/sova-dataset)
- **Leaderboard:** [The 🤗 Speech Bench](https://huggingface.co/spaces/huggingface/hf-speech-bench)
- **Point of Contact:** [SOVA.ai](mailto:support@sova.ai)
### Dataset Summary
SOVA Dataset is free public STT/ASR dataset. It consists of several parts, one of them is SOVA RuDevices. This part is an acoustic corpus of approximately 100 hours of 16kHz Russian live speech with manual annotating, prepared by [SOVA.ai team](https://github.com/sovaai).

Authors do not divide the dataset into train, validation and test subsets. Therefore, I was compelled to prepare this splitting. The training subset includes more than 82 hours, the validation subset includes approximately 6 hours, and the test subset includes approximately 6 hours too.

### Supported Tasks and Leaderboards
- `automatic-speech-recognition`: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER). The task has an active Hugging Face leaderboard which can be found at https://huggingface.co/spaces/huggingface/hf-speech-bench. The leaderboard ranks models uploaded to the Hub based on their WER.
### Languages
The audio is in Russian.
## Dataset Structure
### Data Instances
A typical data point comprises the audio data, usually called `audio` and its transcription, called `transcription`. Any additional information about the speaker and the passage which contains the transcription is not provided.
```
{'audio': {'path': '/home/bond005/datasets/sova_rudevices/data/train/00003ec0-1257-42d1-b475-db1cd548092e.wav',
  'array': array([  0.00787354,  0.00735474,  0.00714111, ...,
                   -0.00018311, -0.00015259, -0.00018311]), dtype=float32),
  'sampling_rate': 16000},
 'transcription': 'мне получше стало'}
```
### Data Fields
- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- transcription: the transcription of the audio file.
### Data Splits
This dataset consists of three splits: training, validation, and test. This splitting was realized with accounting of internal structure of SOVA RuDevices (the validation split is based on the subdirectory `0`, and the test split is based on the subdirectory `1` of the original dataset), but audio recordings of the same speakers can be in different splits at the same time (the opposite is not guaranteed).
|                             | Train  | Validation |  Test |
| -----                       | ------ | ---------- | ----- |
| examples                    |  81607 |       5835 |  5799 |
| hours                       |  82.4h |       5.9h |  5.8h |
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
All recorded audio files were manually annotated.
#### Who are the annotators?
[Needs More Information]
### Personal and Sensitive Information
The dataset consists of people who have donated their voice. You agree to not attempt to determine the identity of speakers in this dataset.
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed]
### Discussion of Biases
[More Information Needed]
### Other Known Limitations
[Needs More Information]
## Additional Information
### Dataset Curators
The dataset was initially created by Egor Zubarev, Timofey Moskalets, and SOVA.ai team.
### Licensing Information
[Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/)
### Citation Information
```
@misc{sova2021rudevices,
  author = {Zubarev, Egor and Moskalets, Timofey and SOVA.ai},
  title = {SOVA RuDevices Dataset: free public STT/ASR dataset with manually annotated live speech},
  publisher = {GitHub},
  journal = {GitHub repository},
  year = {2021},
  howpublished = {\url{https://github.com/sovaai/sova-dataset}},
}
```
### Contributions
Thanks to [@bond005](https://github.com/bond005) for adding this dataset.