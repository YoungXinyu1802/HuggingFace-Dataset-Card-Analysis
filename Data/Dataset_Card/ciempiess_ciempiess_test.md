---
annotations_creators:
- expert-generated
language:
- es
language_creators:
- other
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: 'CIEMPIESS TEST CORPUS: Audio and Transcripts of Mexican Spanish Broadcast Conversations.'
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- ciempiess
- spanish
- mexican spanish
- test set
- ciempiess project
- ciempiess-unam project
- ciempiess test
task_categories:
- automatic-speech-recognition
task_ids: []
---


# Dataset Card for ciempiess_test
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
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
- **Homepage:** [CIEMPIESS-UNAM Project](http://www.ciempiess.org/)
- **Repository:** [CIEMPIESS-TEST is part of LDC2019S07](https://catalog.ldc.upenn.edu/LDC2019S07)
- **Paper:** [Creating Mexican Spanish Language Resources through the Social Service Program](https://aclanthology.org/2022.nidcp-1.4.pdf)
- **Point of Contact:** [Carlos Mena](mailto:carlos.mena@ciempiess.org)

### Dataset Summary

When developing automatic speech recognition engines and any other machine learning system is a good practice to separate the test from the training data and never combined them. So, the CIEMPIESS TEST Corpus was created by this necessity of having an standard test set destined to measure the advances of the community of users of the CIEMPIESS datasets and we strongly recommend not to use the CIEMPIESS TEST for any other purpose.

The CIEMPIESS TEST Corpus is a gender balanced corpus designed to test acoustic models for the speech recognition task. It was created by recordings and human transcripts of 10 male and 10 female speakers.

The CIEMPIESS TEST Corpus is considered a CIEMPIESS dataset because it only contains audio from the same source of the first [CIEMPIESS Corpus](https://catalog.ldc.upenn.edu/LDC2015S07) and it has the word "TEST" in its name, obviously because it is recommended for test purposes only.

### Example Usage
The CIEMPIESS TEST contains only the test split:
```python
from datasets import load_dataset
ciempiess_test = load_dataset("ciempiess/ciempiess_test")
```
It is also valid to do:
```python
from datasets import load_dataset
ciempiess_test = load_dataset("ciempiess/ciempiess_test",split="test")
```

### Supported Tasks
automatic-speech-recognition: The dataset can be used to test a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

### Languages
The language of the corpus is Spanish with the accent of Central Mexico except for the speaker M_09 that comes from El Salvador.

## Dataset Structure

### Data Instances
```python
{
  'audio_id': 'CMPT_M_07_0074', 
  'audio': {
    'path': '/home/carlos/.cache/HuggingFace/datasets/downloads/extracted/86a30fdc762ba3fad1e38fbe6900ea4940d6f0070af8d56aa483701faa050d51/test/male/M_07/CMPT_M_07_0074.flac',  
    'array': array([-0.00192261, -0.00234985, -0.00158691, ..., -0.00839233,
       -0.00900269, -0.00698853], dtype=float32), 
    'sampling_rate': 16000
  }, 
  'speaker_id': 'M_07', 
  'gender': 'male', 
  'duration': 7.510000228881836, 
  'normalized_text': 'pues está la libertá de las posiciones de a ver quién es pasivo quién es activo blablablá muchas cosas no pero'
}
```

### Data Fields
* `audio_id` (string) - id of audio segment
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `speaker_id` (string) - id of speaker
* `gender` (string) - gender of speaker (male or female)
* `duration` (float32) - duration of the audio file in seconds.
* `normalized_text` (string) - normalized audio segment transcription

### Data Splits

The corpus counts just with the test split which has a total of 3558 speech files from 10 male speakers and 10 female speakers with a total duration of 8 hours and 8 minutes.

## Dataset Creation

### Curation Rationale

The CIEMPIESS TEST (CT) Corpus has the following characteristics:

* The CT has a total of 3558 audio files of 10 male speakers and 10 female speakers. It has a total duration of 8 hours and 8 minutes.

* The total number of audio files that come from male speakers is 1694 with a total duration of 4 hours and 3 minutes. The total number of audio files that come from female speakers is 1864 with a total duration of 4 hours and 4 minutes. So CT is perfectly balanced in gender.

* All of the speakers in the CT come from Mexico, except for the speaker M_09 that comes from El Salvador.

* Every audio file in the CT has a duration between 5 and 10 seconds approximately.

* Data in CT is classified by gender and also by speaker, so one can easily select audios from a particular set of speakers to do experiments.

* Audio files in the CT and the first [CIEMPIESS](https://catalog.ldc.upenn.edu/LDC2015S07) are all of the same type. In both, speakers talk about legal and lawyer issues. They also talk about things related to the [UNAM University](https://www.unam.mx/) and the ["Facultad de Derecho de la UNAM"](https://www.derecho.unam.mx/).

* As in the first CIEMPIESS Corpus, transcriptions in the CT were made by humans.

* Speakers in the CT are not present in any other CIEMPIESS dataset.

* Audio files in the CT are distributed in a 16khz@16bit mono format.

### Source Data

#### Initial Data Collection and Normalization

The CIEMPIESS TEST is a Radio Corpus designed to test acoustic models of automatic speech recognition and it is made out of recordings of spontaneous conversations in Spanish between a radio moderator and his guests. Most of the speech in these conversations has the accent of Central Mexico.

All the recordings that constitute the CIEMPIESS TEST come from ["RADIO-IUS"](http://www.derecho.unam.mx/cultura-juridica/radio.php), a radio station belonging to UNAM. Recordings were donated by Lic. Cesar Gabriel Alanis Merchand and Mtro. Ricardo Rojas Arevalo from the "Facultad de Derecho de la UNAM" with the condition that they have to be used for academic and research purposes only.

### Annotations
#### Annotation process

The annotation process is at follows:

* 1. A whole podcast is manually segmented keeping just the portions containing good quality speech.
* 2. A second pass os segmentation is performed; this time to separate speakers and put them in different folders.
* 3. The resulting speech files between 5 and 10 seconds are transcribed by students from different departments (computing, engineering, linguistics). Most of them are native speakers but not with a particular training as transcribers.

#### Who are the annotators?

The CIEMPIESS TEST Corpus was created by the social service program ["Desarrollo de Tecnologías del Habla"](http://profesores.fi-b.unam.mx/carlos_mena/servicio.html) of the ["Facultad de Ingeniería"](https://www.ingenieria.unam.mx/) (FI) in the ["Universidad Nacional Autónoma de México"](https://www.unam.mx/) (UNAM) between 2016 and 2018 by Carlos Daniel Hernández Mena, head of the program.

### Personal and Sensitive Information

The dataset could contain names revealing the identity of some speakers; on the other side, the recordings come from publicly available podcasts, so, there is not a real intent of the participants to be anonymized. Anyway, you agree to not attempt to determine the identity of speakers in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is challenging because it contains spontaneous speech; so, it will be helpful for the ASR community to evaluate their acoustic models in Spanish with it.

### Discussion of Biases

The dataset intents to be gender balanced. It is comprised of 10 male speakers and 10 female speakers. On the other hand the vocabulary is limited to legal issues.

### Other Known Limitations

The transcriptions in this dataset were revised by Mónica Alejandra Ruiz López during 2022 and they are slightly different from the transcriptions found at [LDC](https://catalog.ldc.upenn.edu/LDC2019S07) or at the [CIEMPIESS-UNAM Project](http://www.ciempiess.org/) official website. We strongly recommend to use these updated transcriptions; we will soon update the transcriptions in the rest of the repositories.

### Dataset Curators

The dataset was collected by students belonging to the social service program ["Desarrollo de Tecnologías del Habla"](http://profesores.fi-b.unam.mx/carlos_mena/servicio.html), it was curated by Carlos Daniel Hernández Mena and its transcriptions were manually verified by Mónica Alejandra Ruiz López during 2022.

### Licensing Information
[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)

### Citation Information
```
@misc{carlosmenaciempiesstest2019,
      title={CIEMPIESS TEST CORPUS: Audio and Transcripts of Mexican Spanish Broadcast Conversations.}, 
      ldc_catalog_no={LDC2019S07},
      DOI={https://doi.org/10.35111/xdx5-n815},
      author={Hernandez Mena, Carlos Daniel},
      journal={Linguistic Data Consortium, Philadelphia},
      year={2019},
      url={https://catalog.ldc.upenn.edu/LDC2019S07},
}
```
### Contributions

The authors want to thank to Alejandro V. Mena, Elena Vera and Angélica Gutiérrez for their support to the social service program: "Desarrollo de Tecnologías del Habla." We also thank to the social service students for all the hard work.

We also thank to Lic. Cesar Gabriel Alanis Merchand and Mtro. Ricardo Rojas Arevalo from the "Facultad de Derecho de la UNAM" for donating all the recordings that constitute the CIEMPIESS TEST Corpus.

Special thanks to Mónica Alejandra Ruiz López who performed a meticulous verification of the transcriptions of this dataset during 2022.
