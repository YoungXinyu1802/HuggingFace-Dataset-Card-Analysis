---
pretty_name: GTZAN
---

# Dataset Card for GTZAN

## Table of Contents
- [Dataset Card for GTZAN](#dataset-card-for-gtzan)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** [http://marsyas.info/downloads/datasets.html](http://marsyas.info/downloads/datasets.html)
- **Paper:** [http://ismir2001.ismir.net/pdf/tzanetakis.pdf](http://ismir2001.ismir.net/pdf/tzanetakis.pdf)
- **Point of Contact:** 

### Dataset Summary

GTZAN is a dataset for musical genre classification of audio signals. The dataset consists of 1,000 audio tracks, each of 30 seconds long. It contains 10 genres, each represented by 100 tracks. The tracks are all 22,050Hz Mono 16-bit audio files in WAV format. The genres are: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, and rock.

### Languages

English

## Dataset Structure

GTZAN is distributed as a single dataset without a predefined training and test split. The information below refers to the single `train` split that is assigned by default.

### Data Instances

An example of GTZAN looks as follows:

```python
{
    "file": "/path/to/cache/genres/blues/blues.00000.wav",
    "audio": {
        "path": "/path/to/cache/genres/blues/blues.00000.wav",
        "array": array(
            [
                0.00732422,
                0.01660156,
                0.00762939,
                ...,
                -0.05560303,
                -0.06106567,
                -0.06417847,
            ],
            dtype=float32,
        ),
        "sampling_rate": 22050,
    },
    "genre": 0,
}
```

### Data Fields

The types associated with each of the data fields is as follows:

* `file`: a `string` feature.
* `audio`: an `Audio` feature containing the `path` of the sound file, the decoded waveform in the `array` field, and the `sampling_rate`.
* `genre`: a `ClassLabel` feature.

### Data Splits

[More Information Needed]

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

[More Information Needed]

### Citation Information

```
@misc{tzanetakis_essl_cook_2001,
author    = "Tzanetakis, George and Essl, Georg and Cook, Perry",
title     = "Automatic Musical Genre Classification Of Audio Signals",
url       = "http://ismir2001.ismir.net/pdf/tzanetakis.pdf",
publisher = "The International Society for Music Information Retrieval",
year      = "2001"
}
```

### Contributions

Thanks to [@lewtun](https://github.com/lewtun) for adding this dataset.