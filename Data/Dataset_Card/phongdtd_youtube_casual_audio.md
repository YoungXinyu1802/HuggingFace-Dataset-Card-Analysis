---
multilinguality:
  vi:
  - 190K<n<200K
source_datasets:
- extended|youtube
task_categories:
- automatic-speech-recognition
task_ids: []
Pretty_name: Youtube Casual Audio
Annotations_creators:
- crowdsourced
Language_creators:
- datlq
Languages:
- vi
Licenses:
- cc0-1.0
---

# Dataset Card for common_voice

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

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

[Needs More Information]

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

Vietnamese

## Dataset Structure

### Data Instances

A typical data point comprises the path to the audio file, called path and its sentence. Additional fields include accent, age, client_id, up_votes down_votes, gender, locale and segment.

`
{
'file_path': 'audio/_1OsFqkFI38_34.304_39.424.wav', 
'script': 'Ik vind dat een dubieuze procedure.', 
'audio': {'path': 'audio/_1OsFqkFI38_34.304_39.424.wav', 
          'array': array([-0.00048828, -0.00018311, -0.00137329, ...,  0.00079346, 0.00091553,  0.00085449], dtype=float32), 
          'sampling_rate': 16000}
`

### Data Fields

file_path: The path to the audio file

audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

script: The sentence the user was prompted to speak

### Data Splits

The speech material has been subdivided into portions for train, test, validated.

The val, test, train are all data that has been reviewed, deemed of high quality and split into val, test and train.

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

[More Information Needed] 

### Other Known Limitations

[More Information Needed] 

## Additional Information

### Dataset Curators

[More Information Needed] 

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]

### Contributions

Thanks to [@datlq](https://github.com/datlq98) for adding this dataset.
