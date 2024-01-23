---
annotations_creators:
- crowdsourced
language: []
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: VoxCeleb
size_categories:
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
source_datasets: []
tags: []
task_categories:
- automatic-speech-recognition
- audio-classification
- image-classification
task_ids:
- speaker-identification
---

# Dataset Card for VoxCeleb

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

### Dataset Summary

VoxCeleb is an audio-visual dataset consisting of short clips of human speech, extracted from interview videos uploaded to YouTube.

NOTE: Although this dataset can be automatically downloaded, you must manually request credentials to access it from the creators' website.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

Each datapoint has a path to the audio/video clip along with metadata about the speaker.

```
{
  'file': '/datasets/downloads/extracted/[hash]/wav/id10271/_YimahVgI1A/00003.wav',
  'file_format': 'wav',
  'dataset_id': 'vox1',
  'speaker_id': 'id10271',
  'speaker_gender': 'm',
  'speaker_name': 'Ed_Westwick',
  'speaker_nationality': 'UK',
  'video_id': '_YimahVgI1A',
  'clip_id': '00003',
  'audio': {
    'path': '/datasets/downloads/extracted/[hash]/wav/id10271/_YimahVgI1A/00003.wav',
    'array': array([...], dtype=float32),
    'sampling_rate': 16000
  }
}
```

### Data Fields

Each row includes the following fields:
- `file`: The path to the audio/video clip
- `file_format`: The file format in which the clip is stored (e.g. `wav`, `aac`, `mp4`)
- `dataset_id`: The ID of the dataset this clip is from (`vox1`, `vox2`)
- `speaker_id`: The ID of the speaker in this clip
- `speaker_gender`: The gender of the speaker (`m`/`f`)
- `speaker_name` (VoxCeleb1 only): The full name of the speaker in the clip
- `speaker_nationality` (VoxCeleb1 only): The speaker's country of origin
- `video_id`: The ID of the video from which this clip was taken
- `clip_index`: The index of the clip for this specific video
- `audio` (Audio dataset only): The audio signal data

### Data Splits

The dataset has a predefined dev set and test set. The dev set has been renamed to a "train" split.

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

The dataset includes recordings of clips (mostly of celebrities and public figures) from public YouTube videos. The names of speakers in VoxCeleb1 are provided.

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

The VoxCeleb authors request that anyone who uses VoxCeleb1 or VoxCeleb2 includes the following three citations:
```
@Article{Nagrani19,
    author = "Arsha Nagrani and Joon~Son Chung and Weidi Xie and Andrew Zisserman",
    title = "Voxceleb: Large-scale speaker verification in the wild",
    journal = "Computer Science and Language",
    year = "2019",
    publisher = "Elsevier",
}

@InProceedings{Chung18b,
    author = "Chung, J.~S. and Nagrani, A. and Zisserman, A.",
    title = "VoxCeleb2: Deep Speaker Recognition",
    booktitle = "INTERSPEECH",
    year = "2018",
}

@InProceedings{Nagrani17,
    author = "Nagrani, A. and Chung, J.~S. and Zisserman, A.",
    title = "VoxCeleb: a large-scale speaker identification dataset",
    booktitle = "INTERSPEECH",
    year = "2017",
}
```

### Contributions

Thanks to [@101arrowz](https://github.com/101arrowz) for adding this dataset.
