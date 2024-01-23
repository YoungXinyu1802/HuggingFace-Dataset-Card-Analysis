---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 22050
  - name: original_text
    dtype: string
  - name: text
    dtype: string
  - name: duration
    dtype: float64
  splits:
  - name: train
    num_bytes: 3173032948.2
    num_examples: 4515
  download_size: 0
  dataset_size: 3173032948.2
annotations_creators:
  - expert-generated
language:
  - hu
license: cc0-1.0
multilinguality:
  - monolingual
size_categories:
  - 1K<n<10K
source_datasets:
  - original
task_categories:
  - text-to-speech
  - other
task_ids: []
---
# Dataset Card for CSS10 Hungarian: Single Speaker Speech Dataset

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

- **Homepage:** [Hungarian Single Speaker Speech Dataset](https://www.kaggle.com/datasets/bryanpark/hungarian-single-speaker-speech-dataset)
- **Repository:** [CSS10](https://github.com/kyubyong/css10)
- **Paper:** [CSS10: A Collection of Single Speaker Speech Datasets for 10 Languages](https://arxiv.org/abs/1903.11269)

### Dataset Summary

The corpus consists of a single speaker, with 4515 segments extracted
from a single LibriVox audiobook.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

The audio is in Hungarian.

## Dataset Structure

[Needs More Information]

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

CSS10 is a collection of single speaker speech datasets for 10 languages. Each of them consists of audio files recorded by a single volunteer and their aligned text sourced from LibriVox.

### Source Data

#### Initial Data Collection and Normalization

[Egri csillagok](https://librivox.org/egri-csillagok-by-geza-gardonyi/),
read by Diana Majlinger.

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

Kyubyong Park & Tommy Mulc

### Licensing Information

[CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

### Citation Information

```
@article{park2019css10,
  title={CSS10: A Collection of Single Speaker Speech Datasets for 10 Languages},
  author={Park, Kyubyong and Mulc, Thomas},
  journal={Interspeech},
  year={2019}
}
```

### Contributions

[Needs More Information]