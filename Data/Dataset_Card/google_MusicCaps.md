---
license:
- cc-by-sa-4.0
converted_from: kaggle
kaggle_id: googleai/musiccaps
task_categories:
- text-to-speech
language:
- en
---

# Dataset Card for MusicCaps

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

- **Homepage:** https://kaggle.com/datasets/googleai/musiccaps
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The MusicCaps dataset contains **5,521 music examples, each of which is labeled with an English *aspect list* and a *free text caption* written by musicians**. An aspect list is for example *"pop, tinny wide hi hats, mellow piano melody, high pitched female vocal melody, sustained pulsating synth lead"*, while the caption consists of multiple sentences about the music, e.g., 

*"A low sounding male voice is rapping over a fast paced drums playing a reggaeton beat along with a bass. Something like a guitar is playing the melody along. This recording is of poor audio-quality. In the background a laughter can be noticed. This song may be playing in a bar."*

The text is solely focused on describing *how* the music sounds, not the metadata like the artist name.

The labeled examples are 10s music clips from the [**AudioSet**](https://research.google.com/audioset/) dataset (2,858 from the eval and 2,663 from the train split).

Please cite the corresponding paper, when using this dataset: http://arxiv.org/abs/2301.11325 (DOI: `10.48550/arXiv.2301.11325`)

### Dataset Usage

The published dataset takes the form of a `.csv` file that contains the ID of YouTube videos and their start/end stamps. In order to use this dataset, one must download the corresponding YouTube videos and chunk them according to the start/end times.

The following repository has an example script and notebook to load the clips. The notebook also includes a Gradio demo that helps explore some samples: https://github.com/nateraw/download-musiccaps-dataset

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

#### ytid 
YT ID pointing to the YouTube video in which the labeled music segment appears. You can listen to the segment by opening https://youtu.be/watch?v={ytid}&start={start_s}

#### start_s
Position in the YouTube video at which the music starts.

#### end_s
Position in the YouTube video at which the music end. All clips are 10s long.

#### audioset_positive_labels
Labels for this segment from the AudioSet (https://research.google.com/audioset/) dataset.

#### aspect_list
A list of aspects describing the music.

#### caption
A multi-sentence free text caption describing the music.

#### author_id
An integer for grouping samples by who wrote them.

#### is_balanced_subset
If this value is true, the row is a part of the 1k subset which is genre-balanced.

#### is_audioset_eval
If this value is true, the clip is from the AudioSet eval split. Otherwise it is from the AudioSet train split.

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

This dataset was shared by [@googleai](https://ai.google/research/)

### Licensing Information

The license for this dataset is cc-by-sa-4.0

### Citation Information

```bibtex
[More Information Needed]
```

### Contributions

[More Information Needed]