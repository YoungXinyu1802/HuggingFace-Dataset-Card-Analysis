---
annotations_creators:
- found
language_creators:
- found
language:
- ca
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- automatic-speech-recognition
- text-generation
task_ids:
- language-modeling
pretty_name: TV3Parla
---

# Dataset Card for TV3Parla

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

- **Homepage:** https://collectivat.cat/asr#tv3parla
- **Repository:**
- **Paper:** [Building an Open Source Automatic Speech Recognition System for Catalan](https://www.isca-speech.org/archive/iberspeech_2018/kulebi18_iberspeech.html)
- **Point of Contact:** [Col·lectivaT](mailto:info@collectivat.cat)

### Dataset Summary

This corpus includes 240 hours of Catalan speech from broadcast material.
The details of segmentation, data processing and also model training are explained in Külebi, Öktem; 2018.
The content is owned by Corporació Catalana de Mitjans Audiovisuals, SA (CCMA);
we processed their material and hereby making it available under their terms of use.

This project was supported by the Softcatalà Association.

### Supported Tasks and Leaderboards

The dataset can be used for:
- Language Modeling.
- Automatic Speech Recognition (ASR) transcribes utterances into words.

### Languages

The dataset is in Catalan (`ca`).

## Dataset Structure

### Data Instances

```
{
  'path': 'tv3_0.3/wav/train/5662515_1492531876710/5662515_1492531876710_120.180_139.020.wav',
  'audio': {'path': 'tv3_0.3/wav/train/5662515_1492531876710/5662515_1492531876710_120.180_139.020.wav',
   'array': array([-0.01168823,  0.01229858,  0.02819824, ...,  0.015625  ,
          0.01525879,  0.0145874 ]),
   'sampling_rate': 16000},
  'text': 'algunes montoneres que que et feien anar ben col·locat i el vent també hi jugava una mica de paper bufava vent de cantó alguns cops o de cul i el pelotón el vent el porta molt malament hi havia molts nervis'
}
```

### Data Fields

- `path` (str): Path to the audio file.
- `audio` (dict): A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling
  rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and
  resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might
  take a significant amount of time. Thus, it is important to first query the sample index before the `"audio"` column,
  *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- `text` (str): Transcription of the audio file.

### Data Splits

The dataset is split into "train" and "test".

|                    |  train | test |
|:-------------------|-------:|-----:|
| Number of examples | 159242 | 2220 |

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

[Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/).

### Citation Information

```
@inproceedings{kulebi18_iberspeech,
  author={Baybars Külebi and Alp Öktem},
  title={{Building an Open Source Automatic Speech Recognition System for Catalan}},
  year=2018,
  booktitle={Proc. IberSPEECH 2018},
  pages={25--29},
  doi={10.21437/IberSPEECH.2018-6}
}
```

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
