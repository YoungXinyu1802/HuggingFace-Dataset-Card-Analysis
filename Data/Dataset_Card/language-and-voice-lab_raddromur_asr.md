---
annotations_creators:
- machine-generated
language:
- is
language_creators:
- machine-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: "Raddr\xF3mur Icelandic Speech 22.09"
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- icelandic podcasts
- spontaneous icelandic
- forced-aligned
- ruv.is
- mafia aligner
task_categories:
- automatic-speech-recognition
task_ids: []
---



# Dataset Card for raddromur_asr
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
- **Homepage:** Raddrómur Icelandic Speech 22.09
- **Repository:** [Clarin.is](http://hdl.handle.net/20.500.12537/286)
- **Point of Contact:** [Carlos Mena](mailto:carlos.mena@ciempiess.org), [Jón Guðnason](mailto:jg@ru.is)

### Dataset Summary

The "Raddrómur Icelandic Speech 22.09" ("Raddrómur Corpus" for short) is an Icelandic corpus created by the Language and Voice Laboratory (LVL) at Reykjavík University (RU) in 2022. It is made out of radio podcasts mostly taken from RÚV (ruv.is).

### Example Usage
The Raddrómur Corpus counts with the train split only. To load the training split pass its name as a config name:
```python
from datasets import load_dataset
raddromur_asr = load_dataset("language-and-voice-lab/raddromur_asr")
```
To load the specific "train" split do:
```python
from datasets import load_dataset
raddromur_asr = load_dataset("language-and-voice-lab/raddromur_asr",split="train")
```

### Supported Tasks
automatic-speech-recognition: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

### Languages
The audio is in Icelandic.

## Dataset Structure

### Data Instances
```python
{
  'audio_id': 'leikfangavelin_007-0066-00:18:5686-00:00:0392', 
  'audio': {
    'path': '/home/carlos/.cache/HuggingFace/datasets/downloads/extracted/f9a8b6e2ea4539571f6e88659a63aa485daa99d47d9c1c95e968fce7ab96664a/train/leikfangavelin/leikfangavelin_007/leikfangavelin_007-0066-00:18:5686-00:00:0392.flac', 
    'array': array([-0.03311157, -0.08340454, -0.11801147, ...,  0.        ,
        0.00033569,  0.00054932], dtype=float32), 
    'sampling_rate': 16000
  },
  'podcast_id': 'leikfangavelin_007', 
  'segment_num': 66, 
  'start_time': '00:18:56.86', 
  'duration': 3.9679999351501465, 
  'mafia_score': 0.0, 
  'normalized_text': 'hætti í bandinu skömmu eftir að platan sem ekki kom út var tekin upp'
}
```

### Data Fields
* `audio_id` (string) - id of audio segment
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `podcast_id` (string) - id of the podcast
* `segment_num` (int32) - integer identifing the number of segment
* `duration` (float32) - duration of the audio file in seconds.
* `mafia_score` (float32) - In order to distinguish the transcriptions with fewer expected mistakes, a quality measure called "MAFIA Score" was added. A MAFIA Score close to zero implies a better quality transcription.
* `normalized_text` (string) - normalized audio segment transcription.

### Data Splits
The corpus is split into train only. The lenght of the train portion is 49h09m in 13030 utterances.

## Dataset Creation

### Curation Rationale

* The corpus was automatically segmented using the tool [inaSpeechSegmenter](https://pypi.org/project/inaSpeechSegmenter/).
  
* The forced alignment was performed using the tool [MAFIA aligner](http://hdl.handle.net/20.500.12537/215).
  
* The corpus comes with a metadata file wich is in TSV format. This file contain the normalized transcription of the corpus and the filenames among other relevant information.
 
* The corpus contains 13030 utterances, totalling 49 hours and 09 minutes.

* The corpus is not split into train/dev/test portions.

* The corpus is distrubuted in the following format: flac, 16kHz@16bits mono.

* The column "mafia_score" in the metadata file indicates the expected precision of the transcription. Zero is the highest precision.

### Source Data

#### Initial Data Collection and Normalization

The Raddrómur Corpus is composed of different radio podcasts in Icelandic. More information about the origin of these podcasts comes as follows:

* Rokkland | Author: Ólafur Páll Gunnarsson | Podcast/Radio show hosted by RUV.

* A Tonsvidinu | Author: Una Margrét Jónsdóttir | Podcast/Radio show hosted by RUV.

* I ljosu Sogunnar | Author: Vera Illugadóttir | Podcast/Radio show hosted by RUV.

* Nedanmals | Authors: Elísabet Rún Þorsteinsdóttir and Marta Eir Sigurðardóttir. | Elísabet Rún Þorsteinsdóttir og Marta Eir Sigurðardóttir.

* Leikfangavelin | Author: Atla Hergeirssonar | Independent Podcast/Radio show.

### Annotations

#### Annotation process

The podcasts from https://www.ruv.is/ were selected because they count with a text script that matches with certain 
fidelity what is said during the show. After automatic segmentation of the episodes, the transcriptions were inferred using the scripts along with a forced alignment technique.

#### Who are the annotators?

The corpus was automatically segmented and aligned by the [MAFIA aligner](http://hdl.handle.net/20.500.12537/215).

The MAFIA aligner is designed to take a podcast episode along with a text script reflecting what is spoken in the podcast, then segment the podcast and find a transcription that better fits what is in the script. When the script is not accurate, MAFIA is able to infer a transcription using Automatic Speech Recognition. 

### Personal and Sensitive Information
The corpus is comprised of speech utterances from professional podcasters. Nevertheless, you agree to not attempt to determine the identity of speakers in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset
This ASR corpus is one of the few available Icelandic copora with spontaneous speech.

### Discussion of Biases

In order to distinguish the transcriptions with fewer expected mistakes, a quality measure called "MAFIA Score" was added in the metadata file included with the corpus. A MAFIA Score close to zero implies a better quality transcription.

To infer a transcription using the vocabulary of the text script, MAFIA creates a 3-gram language model with SRILM [4] using the text of all the podcasts available at the moment of running it. After this, MAFIA transcribes all the segments using a speech recognizer based on [NVIDIA-NeMo](https://developer.nvidia.com/nvidia-nemo).

In order to calculate the MAFIA Score, a second round of speech recognition is passed to all the segments but using a way more robust [6-gram language model](http://hdl.handle.net/20.500.12537/226) with a size of 5GB. The MAFIA score is then obtained by measuring the Word Error Rate bewteen the first pass transcriptions (reference) and the second pass transcriptions (hyphotesis). According to this, a MAFIA score of 0 reflects a transcription that is equal in both passes and therefore, it is a high quality transcription.


### Other Known Limitations
"Raddrómur Icelandic Speech 22.09" by the Language and Voice Laboratory (LVL) from Reykjavík University (RU) is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License with the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Additional Information

### Dataset Curators

The corpus was curated by Carlos Daniel Hernández Mena in 2022.

### Licensing Information
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information
```
@misc{carlosmenaraddromur2022,
      title={Raddrómur Icelandic Speech 22.09}, 
      author={Hernández Mena, Carlos Daniel and Hedström, Staffan and Þórhallsdóttir, Ragnheiður and Fong, Judy Y. and Gunnarsson, Þorsteinn Daði and Sigurðardóttir, Helga Svala and Þorsteinsdóttir, Helga Lára and Guðnason, Jón},
      year={2022},
      url={http://hdl.handle.net/20.500.12537/286},
}
```

### Contributions

This project was funded by the Language Technology Programme for Icelandic 2019-2022. The programme, which is managed and coordinated by Almannarómur, is funded by the Icelandic Ministry of Education, Science and Culture.

Special thanks to the podcasters and to Aron Berg from RÚV.
