---
annotations_creators: []
language:
- ha
language_creators:
- expert-generated
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: BibleTTS Hausa
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- bible
task_categories:
- automatic-speech-recognition
- text-to-speech
task_ids: []
---

# Dataset Card for BibleTTS Hausa

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://masakhane-io.github.io/bibleTTS/
- **Repository:** http://www.openslr.org/129/
- **Paper:** https://arxiv.org/abs/2207.03546

### Dataset Summary

BibleTTS is a large high-quality open Text-to-Speech dataset with up to 80 hours of single speaker, studio quality 48kHz recordings.
This is a Hausa part of the dataset. Aligned hours: 86.6, aligned verses: 40,603.

### Languages

Hausa

## Dataset Structure

### Data Fields

- `audio`: audio path
- `sentence`: transcription of the audio
- `locale`: always set to `ha`
- `book`: 3-char book encoding
- `verse`: verse id

### Data Splits

- `dev`: Book of Ezra (264 verses)
- `test`: Book of Colossians (124 verses)
- `train`: all other books (40215 verses)

## Additional Information

*See [this notebook](https://github.com/seads-org/hausa-speech-recognition/blob/6993c5c74379c93a2416acac6126b60ce6e52df8/notebooks/prepare_bible_dataset.ipynb) for the code on how the dataset was processed.

### Dataset Curators

The dataset uploaded by [vpetukhov](https://github.com/VPetukhov/) who is not connected to the dataset authors. Please, see the project page for more info.

### Licensing Information

The data is released under a commercial-friendly [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license.

### Citation Information

Meyer, Josh, et al. "BibleTTS: a large, high-fidelity, multilingual, and uniquely African speech corpus." arXiv preprint arXiv:2207.03546 (2022).
