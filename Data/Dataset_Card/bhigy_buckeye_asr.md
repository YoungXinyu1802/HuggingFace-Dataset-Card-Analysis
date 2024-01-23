---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
language_bcp47:
- en-US
license:
- other
multilinguality:
- monolingual
pretty_name: Buckeye Corpus
size_categories:
- unknown
source_datasets:
- original
task_categories:
- automatic-speech-recognition
task_ids:
- speech-recognition
---

# Dataset Card for the Buckeye Corpus (buckeye_asr)

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

- **Homepage:** https://buckeyecorpus.osu.edu/
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The Buckeye Corpus of conversational speech contains high-quality recordings from 40 speakers in Columbus OH conversing freely with an interviewer. The speech has been orthographically transcribed and phonetically labeled.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

American English (en-US)

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

- `file`: filename of the audio file containing the utterance.
- `audio`: filename of the audio file containing the utterance.
- `text`: transcription of the utterance.
- `phonetic_detail`: list of phonetic annotations for the utterance (start, stop and label of each phone).
- `word_detail`: list of word annotations for the utterance (start, stop, label, broad and narrow transcriptions, syntactic class).
- `speaker_id`: string identifying the speaker.
- `id`: string identifying the utterance.

### Data Splits

The data is split in training, validation and test sets with different speakers (32, 4, and 4 speakers respectively) in each set. The sets are all balanced for speaker's gender and age.

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

FREE for noncommercial uses.

### Citation Information

```
@misc{pitt2007Buckeye,
  title = {Buckeye {Corpus} of {Conversational} {Speech} (2nd release).},
  url = {www.buckeyecorpus.osu.edu},
  publisher = {Columbus, OH: Department of Psychology, Ohio State University (Distributor)},
  author = {Pitt, M.A. and Dilley, L. and Johnson, K. and Kiesling, S. and Raymond, W. and Hume, E. and Fosler-Lussier, E.},
  year = {2007},
}
```

### Usage

The first step is to download a copy of the dataset from [the official website](https://buckeyecorpus.osu.edu). Once done, the dataset can be loaded directly through the `datasets` library by running:

```
from datasets import load_dataset

dataset = load_dataset("bhigy/buckeye_asr", data_dir=<path_to_the_dataset>)
```

where `<path_to_the_dataset>` points to the folder where the dataset is stored. An example of path to one of the audio files is then `<path_to_the_dataset>/s01/s0101a.wav`.