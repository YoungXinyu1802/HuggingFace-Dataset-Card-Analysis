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
- 1K<n<10K
source_datasets:
- original
task_categories:
- other
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for ClarinPL Sejm/Senat Speech Corpus

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
- **Repository:** [Needs More Information]
- **Paper:** [System for Automatic Transcription of Sessions of the Polish Senate](https://acoustics.ippt.pan.pl/index.php/aa/article/view/327/pdf_32)
- **Leaderboard:** [Paperswithcode Leaderboard][Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

A collection of 97 hours of parliamentary speeches published on the ClarinPL website.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

The audio is in Polish.

## Dataset Structure

### Data Instances

A typical data point comprises the path to the audio file, usually called `file` and its transcription, called `text`.
An example from the dataset is:
```
{'file': '/root/.cache/huggingface/datasets/downloads/extracted/4143b1d75559b10028c1c7e8800c9ccc05934ca5a8ea15f8f9a92770576a1ee3/SejmSenat/audio/AdamAbramowicz-20130410/file000.wav',
 'id': 'AdamAbramowicz-20130410-file000',
 'speaker_id': 'AdamAbramowicz',
 'text': 'panie marszałku wysoka izbo panie ministrze próbuje się przedstawiać polskę jako zieloną wyspę kraj który się szybko rozwija tymczasem rzeczywistość jest zupełnie inna a widać ją także dzisiaj przed polskim parlamentem próbuje się rząd próbuje zagonić polaków do pracy aż do śmierci przedłużać wiek emerytalny czyliczyli sytuacja gospodarcza polski w tym wypadku jest przedstawiana już zupełnie inaczej pakiet klimatyczny i protokół z kioto jak się zgadzają fachowcy od gospodarki jest szkodliwy dla krajów które są na dorobku a polska właśnie jest takim krajem'}
 ```

### Data Fields

- file: A path to the downloaded audio file in .wav format.
- text: the transcription of the audio file.
- speaker_id: The ID of the speaker of the audio.

### Data Splits

|       | Train | Test |
| ----- | ----- | ---- | 
| dataset | 6622 | 130 |  



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

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]

### Contributions

[Needs More Information]