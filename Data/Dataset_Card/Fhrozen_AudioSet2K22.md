---
annotations_creators:
- unknown
language_creators:
- unknown
license: cc-by-sa-4.0
size_categories:
- 100K<n<100M
source_datasets:
- unknown
task_categories:
- audio-classification
task_ids: []
tags:
- audio-slot-filling
---

# Dataset Card for audioset2022
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
- **Homepage:** [AudioSet Ontology](https://research.google.com/audioset/ontology/index.html)
- **Repository:** [Needs More Information]
- **Paper:** [Audio Set: An ontology and human-labeled dataset for audio events](https://research.google.com/pubs/pub45857.html)
- **Leaderboard:** [Paperswithcode Leaderboard](https://paperswithcode.com/dataset/audioset)

### Dataset Summary

The AudioSet ontology is a collection of sound events organized in a hierarchy. The ontology covers a wide range of everyday sounds, from human and animal sounds, to natural and environmental sounds, to musical and miscellaneous sounds.

**This repository only includes audio files for DCASE 2022 - Task 3**

The included labels are limited to:
- Female speech, woman speaking
- Male speech, man speaking
- Clapping
- Telephone
- Telephone bell ringing
- Ringtone
- Laughter
- Domestic sounds, home sounds
- Vacuum cleaner
- Kettle whistle
- Mechanical fan
- Walk, footsteps
- Door
- Cupboard open or close
- Music
- Background music
- Pop music
- Musical instrument
- Acoustic guitar
- Marimba, xylophone
- Cowbell
- Piano
- Electric piano
- Rattle (instrument)
- Water tap, faucet
- Bell
- Bicycle bell
- Chime
- Knock

### Supported Tasks and Leaderboards

- `audio-classification`: The dataset can be used to train a model for Sound Event Detection/Localization.

**The recordings only includes the single channel audio. For Localization tasks, it will required to apply RIR information**

### Languages

None


## Dataset Structure

### Data Instances

**WIP**
```
{
    'file': 

}
```

### Data Fields

- file: A path to the downloaded audio file in .mp3 format.

### Data Splits

This dataset only includes audio file from the unbalance train list.
The data comprises two splits: weak labels and strong labels.

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
The dataset was initially downloaded by Nelson Yalta (nelson.yalta@ieee.org).

### Licensing Information
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

### Citation Information

```
@inproceedings{45857,
title	= {Audio Set: An ontology and human-labeled dataset for audio events},
author	= {Jort F. Gemmeke and Daniel P. W. Ellis and Dylan Freedman and Aren Jansen and Wade Lawrence and R. Channing Moore and Manoj Plakal and Marvin Ritter},
year	= {2017},
booktitle	= {Proc. IEEE ICASSP 2017},
address	= {New Orleans, LA}
}
```
