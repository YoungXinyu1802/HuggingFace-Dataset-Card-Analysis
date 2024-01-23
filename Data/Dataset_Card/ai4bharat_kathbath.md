---
annotations_creators:
- expert-generated
language_bcp47:
- bn,gu,kn,hi,ml,mr,or,pa,sn,ta,te,ur
language_creators:
- machine-generated
license:
- mit
multilinguality:
- multilingual
pretty_name: Kathbath
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for Kathbath

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

- **Homepage:https://ai4bharat.org/indic-superb**
- **Repository:https://github.com/AI4Bharat/IndicSUPERB**
- **Paper:https://arxiv.org/pdf/2208.11761.pdf**
- **Point of Contact:tahirjmakhdoomi@gmail.com**

### Dataset Summary

Kathbath is an human-labeled ASR dataset containing 1,684 hours of labelled speech data across 12 Indian languages from 1,218 contributors located in 203 districts in India

### Languages

- Bengali
- Gujarati
- Kannada
- Hindi
- Malayalam
- Marathi
- Odia
- Punjabi
- Sanskrit
- Tamil
- Telugu
- Urdu

## Dataset Structure

```
Audio Data
data
├── bengali
│   ├── <split_name>
│   │   ├── 844424931537866-594-f.m4a
│   │   ├── 844424931029859-973-f.m4a
│   │   ├── ...
├── gujarati
├── ...


Transcripts
data
├── bengali
│   ├── <split_name>
│   │   ├── transcription_n2w.txt
├── gujarati
├── ...
```

### Licensing Information

The IndicSUPERB dataset is released under this licensing scheme:

- We do not own any of the raw text used in creating this dataset.
- The text data comes from the IndicCorp dataset which is a crawl of publicly available websites.
- The audio transcriptions of the raw text and labelled annotations of the datasets have been created by us.
- We license the actual packaging of all this data under the Creative Commons CC0 license (“no rights reserved”).
- To the extent possible under law, AI4Bharat has waived all copyright and related or neighboring rights to the IndicSUPERB dataset.
- This work is published from: India.

### Citation Information

```
@misc{https://doi.org/10.48550/arxiv.2208.11761,
  doi = {10.48550/ARXIV.2208.11761},
  url = {https://arxiv.org/abs/2208.11761},
  author = {Javed, Tahir and Bhogale, Kaushal Santosh and Raman, Abhigyan and Kunchukuttan, Anoop and Kumar, Pratyush and Khapra, Mitesh M.},
  title = {IndicSUPERB: A Speech Processing Universal Performance Benchmark for Indian languages},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

### Contributions

We would like to thank the Ministry of Electronics and Information Technology (MeitY) of the Government of India and the Centre for Development of Advanced Computing (C-DAC), Pune for generously supporting this work and providing us access to multiple GPU nodes on the Param Siddhi Supercomputer. We would like to thank the EkStep Foundation and Nilekani Philanthropies for their generous grant which went into hiring human resources as well as cloud resources needed for this work. We would like to thank DesiCrew for connecting us to native speakers for collecting data. We would like to thank Vivek Seshadri from Karya Inc. for helping setup the data collection infrastructure on the Karya platform. We would like to thank all the members of AI4Bharat team in helping create the Query by Example dataset.