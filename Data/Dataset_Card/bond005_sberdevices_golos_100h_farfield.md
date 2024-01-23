---
pretty_name: Golos
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
- expert-generated
language:
- ru
license:
- other
multilinguality:
- monolingual
paperswithcode_id: golos
size_categories:
- 10K<n<100k
source_datasets:
- extended
task_categories:
- automatic-speech-recognition
- audio-classification
---
# Dataset Card for sberdevices_golos_100h_farfield
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
- **Homepage:** [Golos ASR corpus](https://www.openslr.org/114)
- **Repository:** [Golos dataset](https://github.com/sberdevices/golos)
- **Paper:** [Golos: Russian Dataset for Speech Research](https://arxiv.org/pdf/2106.10161.pdf)
- **Leaderboard:** [The 🤗 Speech Bench](https://huggingface.co/spaces/huggingface/hf-speech-bench)
- **Point of Contact:** [Nikolay Karpov](mailto:karpnv@gmail.com)
### Dataset Summary
Sberdevices Golos is a corpus of approximately 1200 hours of 16kHz Russian speech from crowd (reading speech) and farfield (communication with smart devices) domains, prepared by SberDevices Team (Alexander Denisenko, Angelina Kovalenko, Fedor Minkin, and Nikolay Karpov). The data is derived from the crowd-sourcing platform, and has been manually annotated.
Authors divide all dataset into train and test subsets. The training subset includes approximately 1000 hours. For experiments with a limited number of records, authors identified training subsets of shorter length: 100 hours, 10 hours, 1 hour, 10 minutes.
This dataset is a simpler version of the above mentioned Golos:
- it includes the farfield domain only (without any sound from the crowd domain);
- validation split is built on the 10-hour training subset;
- training split corresponds to the 100-hour training subset without sounds from the 10-hour training subset;
- test split is a full original test split.
### Supported Tasks and Leaderboards
- `automatic-speech-recognition`: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER). The task has an active Hugging Face leaderboard which can be found at https://huggingface.co/spaces/huggingface/hf-speech-bench. The leaderboard ranks models uploaded to the Hub based on their WER.
### Languages
The audio is in Russian.
## Dataset Structure
### Data Instances
A typical data point comprises the audio data, usually called `audio` and its transcription, called `transcription`. Any additional information about the speaker and the passage which contains the transcription is not provided.
```
{'audio': {'path': None,
  'array': array([ 1.22070312e-04,  1.22070312e-04,  9.15527344e-05, ...,
                   6.10351562e-05,  6.10351562e-05,  3.05175781e-05]), dtype=float64),
  'sampling_rate': 16000},
 'transcription': 'джой источники истории турции'}
```
### Data Fields
- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- transcription: the transcription of the audio file.
### Data Splits
This dataset is a simpler version of the original Golos:
- it includes the farfield domain only (without any sound from the crowd domain);
- validation split is built on the 10-hour training subset;
- training split corresponds to the 100-hour training subset without sounds from the 10-hour training subset;
- test split is a full original test split.
|                             | Train  | Validation |  Test |
| -----                       | ------ | ---------- | ----- |
| examples                    |  9570  |        933 |  1916 |
| hours                       | 10.3h  |       1.0h |  1.4h |
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
All recorded audio files were manually annotated on the crowd-sourcing platform.
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
The dataset was initially created by Alexander Denisenko, Angelina Kovalenko, Fedor Minkin, and Nikolay Karpov.
### Licensing Information
[Public license with attribution and conditions reserved](https://github.com/sberdevices/golos/blob/master/license/en_us.pdf)
### Citation Information
```
@misc{karpov2021golos,
  author = {Karpov, Nikolay and Denisenko, Alexander and Minkin, Fedor},
  title = {Golos: Russian Dataset for Speech Research},
  publisher = {arXiv},
  year = {2021},
  url = {https://arxiv.org/abs/2106.10161}
}
```
### Contributions
Thanks to [@bond005](https://github.com/bond005) for adding this dataset.
