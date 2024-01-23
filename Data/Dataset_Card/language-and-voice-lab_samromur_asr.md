---
annotations_creators:
- crowdsourced
language:
- is
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: "Samrómur Icelandic Speech 1.0."
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- crowd-sourced icelandic
- "samrómur"
- icelandic speech
- samromur
- iceland
task_categories:
- automatic-speech-recognition
task_ids: []
---



# Dataset Card for samromur_asr
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
- **Homepage:** [Samrómur 21.05]
- **Repository:** [OpenSLR](http://www.openslr.org/112/)
- **Paper:** [Samrómur: Crowd-sourcing Data Collection for Icelandic Speech Recognition](https://aclanthology.org/2020.lrec-1.425.pdf)
- **Point of Contact:** [Jón Guðnason](mailto:jg@ru.is)

### Dataset Summary
This is the first release of the Samrómur Icelandic Speech corpus that contains 100.000 validated utterances.

The corpus is a result of the crowd-sourcing effort run by the Language and Voice Lab at the Reykjavik University, in cooperation with Almannarómur, Center for Language Technology.


### Example Usage
The Samrómur Corpus is divided in 3 splits: train, validation and test. To load a specific split pass its name as a config name:
```python
from datasets import load_dataset
samromur_asr = load_dataset("language-and-voice-lab/samromur_asr")
```
To load an specific split (for example, the validation split) do:
```python
from datasets import load_dataset
samromur_asr = load_dataset("language-and-voice-lab/samromur_asr",split="validation")
```

### Supported Tasks
automatic-speech-recognition: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

### Languages
The audio is in Icelandic.
The reading prompts were gathered from a variety of sources, mainly from the [Icelandic Gigaword Corpus](http://clarin.is/en/resources/gigaword). The corpus includes text from novels, news, plays, and from a list of location names in Iceland. The prompts also came from the [Icelandic Web of Science](https://www.visindavefur.is/).

## Dataset Structure

### Data Instances
```python
{
  'audio_id': '009123-0150695', 
  'audio': {
    'path': '/home/david/.cache/HuggingFace/datasets/downloads/extracted/cb428a7f1e46b058d76641ef32f36b49d28b73aea38509983170495408035a10/dev/009123/009123-0150695.flac', 
    'array': array([0., 0., 0., ..., 0., 0., 0.], dtype=float32), 
    'sampling_rate': 16000
  }, 
  'speaker_id': '009123', 
  'gender': 'female', 
  'age': '18-19', 
  'duration': 3.299999952316284, 
  'normalized_text': 'það skipti heldur engu'
}
```

### Data Fields
* `audio_id` (string) - id of audio segment
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `speaker_id` (string) - id of speaker
* `gender` (string) - gender of speaker (male or female)
* `age` (string) - range of age of the speaker.
* `duration` (float32) - duration of the audio file in seconds.
* `normalized_text` (string) - normalized audio segment transcription.

### Data Splits
The corpus is split into train, validation, and test subsets with no speaker overlap. Each subset contains folders that correspond to speaker IDs, and the audio files inside use the following naming convention: {speaker_ID}-{utterance_ID}.flac. Lenghts of each portion are: train=114h/34m, test=15h51m, validation=15h16m.

To load an specific portion please see the above section "Example Usage".

## Dataset Creation

### Curation Rationale

* The recording has started in October 2019 and continues to this day (May 2021). 

* This release has been authorized for release in May 2021. 

* The aim is to create an open-source speech corpus to enable research and development for Icelandic Language Technology. 

* The corpus contains audio recordings and a metadata file that contains the prompts the participants read. 

* A Kaldi based script using this data can be found on the Language and Voice Lab gitHub page https://github.com/cadia-lvl/samromur-asr 

### Source Data

#### Initial Data Collection and Normalization

* The utterances were recorded by a smartphone or the web app.

* The data was collected using the website https://samromur.is, code of which is available at https://github.com/cadia-lvl/samromur. 

* Each recording contains one read sentence from a script. 

* The script contains 85.080 unique sentences and 90.838 unique tokens. 

### Annotations

#### Annotation process

Prompts were pulled from these corpora if they met the criteria of having only letters which are present in the Icelandic alphabet, and if they are listed in the [DIM: Database Icelandic Morphology](https://aclanthology.org/W19-6116.pdf). 

There are also synthesised prompts consisting of a name followed by a question or a demand, in order to simulate a dialogue with a smart-device. 

#### Who are the annotators?
The audio files content was manually verified against the prompts by one or more listener (summer students mainly).

### Personal and Sensitive Information
The dataset consists of people who have donated their voice. You agree to not attempt to determine the identity of speakers in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset
This contribution describes an ongoing project of speech data collection, using the web application Samrómur which is built upon Common Voice, Mozilla Foundation's web platform for open-source voice collection. The goal of the project is to build a large-scale speech corpus for Automatic Speech Recognition (ASR) for Icelandic. Upon completion, Samrómur will be the largest open speech corpus for Icelandic collected from the public domain.

### Discussion of Biases

* The participants are aged between 18 to 90, 59,782 recordings are from female speakers and 40,218 are from male, recorded by a smartphone or the web app. 

* Participants self-reported their age group, gender, and the native language.

* The corpus contains 100 000 utterance from 8392 speaker, totalling 145 hours.

### Other Known Limitations
"Samromur 21.05" by the Language and Voice Laboratory (LVL) at the Reykjavik University is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License with the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Additional Information

### Dataset Curators

The corpus is a result of the crowd-sourcing effort run by the Language and Voice Lab at the Reykjavik University, in cooperation with Almannarómur, Center for Language Technology. 

### Licensing Information
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information
```
@inproceedings{mollberg-etal-2020-samromur,
    title = "{S}amr{\'o}mur: Crowd-sourcing Data Collection for {I}celandic Speech Recognition",
    author = "Mollberg, David Erik  and
      J{\'o}nsson, {\'O}lafur Helgi  and
      {\TH}orsteinsd{\'o}ttir, Sunneva  and
      Steingr{\'\i}msson, Stein{\th}{\'o}r  and
      Magn{\'u}sd{\'o}ttir, Eyd{\'\i}s Huld  and
      Gudnason, Jon",
    booktitle = "Proceedings of the 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.425",
    pages = "3463--3467",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
```

### Contributions
This project was funded by the Language Technology Programme for Icelandic 2019-2023. The programme, which is managed and coordinated by Almannarómur, is funded by the Icelandic Ministry of Education, Science and Culture.

The verification for the dataset was funded by the the Icelandic Directorate of Labour's Student Summer Job Program.

Special thanks for the summer students for all the hard work.
