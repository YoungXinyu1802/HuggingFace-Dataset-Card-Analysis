---
pretty_name: 'Snow Mountain'
language:
- hi
- bgc
- kfs
- dgo
- bhd
- gbk
- xnr
- kfx
- mjl
- kfo
- bfz
annotations_creators:
- ?
language_creators:
- ?
license: []
multilinguality:
- multilingual
size_categories:
- 
source_datasets:
- Snow Mountain
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
configs:
  - hi
  - bgc
dataset_info:
  - config_name: hi
    features:
      - name: Unnamed
        dtype: int64
      - name: sentence
        dtype: string
      - name: path
        dtype: string
    splits:
      - name: train_500
        num_examples: 400
      - name: val_500  
        num_examples: 100
      - name: train_1000
        num_examples: 800
      - name: val_1000
        num_examples: 200
      - name: test_common
        num_examples: 500
    dataset_size: 71.41 hrs
  - config_name: bgc
    features:
      - name: Unnamed
        dtype: int64
      - name: sentence
        dtype: string
      - name: path
        dtype: string
    splits:
      - name: train_500
        num_examples: 400
      - name: val_500  
        num_examples: 100
      - name: train_1000
        num_examples: 800
      - name: val_1000
        num_examples: 200
      - name: test_common
        num_examples: 500
    dataset_size: 27.41 hrs

---

# Dataset Card for [Dataset Name]

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

- **Homepage:**
- **Repository:https://gitlabdev.bridgeconn.com/software/research/datasets/snow-mountain**
- **Paper:https://arxiv.org/abs/2206.01205**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The Snow Mountain dataset contains the audio recordings (in .mp3 format) and the corresponding text of The Bible in 11 Indian languages. The recordings were done in a studio setting by native speakers. Each language has a single speaker in the dataset. Most of these languages are geographically concentrated in the Northern part of India around the state of Himachal Pradesh. Being related to Hindi they all use the Devanagari script for transcription. 

We have used this dataset for experiments in ASR tasks. But these could be used for other applications in speech domain, like speaker recognition, language identification or even as unlabelled corpus for pre-training.

### Supported Tasks and Leaderboards

Atomatic speech recognition, Speaker recognition, Language identification

### Languages

Hindi, Haryanvi, Bilaspuri, Dogri, Bhadrawahi, Gaddi, Kangri, Kulvi, Mandeali, Kulvi Outer Seraji, Pahari Mahasui 

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

The Bible recordings were done in a studio setting by native speakers. 

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

The data is licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (CC BY-SA 4.0)


### Citation Information

@inproceedings{Raju2022SnowMD,
  title={Snow Mountain: Dataset of Audio Recordings of The Bible in Low Resource Languages},
  author={Kavitha Raju and V. Anjaly and R. Allen Lish and Joel Mathew},
  year={2022}
}



### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
