---
annotations_creators:
- expert-generated
language:
- mt
language_creators:
- other
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'MASRI-TEST CORPUS: Audio and Transcriptions in Maltese extracted from the YouTube channel of the University of Malta.'
size_categories:
- n<1K
source_datasets:
- original
tags:
- masri
- maltese
- masri-project
- malta
- test corpus
task_categories:
- automatic-speech-recognition
task_ids: []
---
# Dataset Card for masri_test
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
- **Homepage:** [MASRI Project](https://www.um.edu.mt/projects/masri/)
- **Repository:** [MASRI Data Repo](https://github.com/UMSpeech/)
- **Point of Contact:** [Carlos Mena](mailto:carlos.mena@ciempiess.org), [Andrea De Marco](mailto:andrea.demarco@um.edu.mt), [Claudia Borg](mailto:claudia.borg@um.edu.mt)
### Dataset Summary
The MASRI-TEST CORPUS was created out of YouTube videos belonging to the channel of the [University of Malta](www.youtube.com/user/universityofmalta). It has a length of 1 hour and it is gender balanced, as it has the same number of male and female speakers.
### Example Usage
The MASRI-TEST contains only the test split:
```python
from datasets import load_dataset
masri_test = load_dataset("MLRS/masri_test")
```
It is also valid to do:
```python
from datasets import load_dataset
masri_test = load_dataset("MLRS/masri_test",split="test")
```
### Supported Tasks
automatic-speech-recognition: The dataset can be used to test a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).
### Languages
The language of the corpus is Maltese.
## Dataset Structure
### Data Instances
```python
{
  'audio_id': 'MSRTS_M_17_TS_00001', 
  'audio': {
    'path': '/home/carlos/.cache/HuggingFace/datasets/downloads/extracted/9158ecbeeb3532038f3fe3d53e0adda1f790c9363a613bac32c454a39d9c682c/test/male/M_17/MSRTS_M_17_TS_00001.flac', 
    'array': array([ 0.0020752 ,  0.00283813,  0.00167847, ..., -0.0010376 ,
       -0.00091553, -0.00100708], dtype=float32), 
    'sampling_rate': 16000
  }, 
  'speaker_id': 'M_17', 
  'gender': 'male', 
  'duration': 5.920000076293945, 
  'normalized_text': 'ignazio saverio mifsud kien qed jippjana kien qed iħejji tliet volumi tal-biblijoteka maltese'
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
The corpus counts just with the test split which has a total of 668 speech files from 17 male speakers and 17 female speakers with a total duration of 1 hour.
## Dataset Creation
### Curation Rationale
The MASRI-TEST CORPUS (MTSC) has the following characteristics:
* The MTSC has an exact duration of 1 hours and 0 minutes. It has 668 audio files.
* The MTSC has recordings from 34 different speakers: 17 men and 17 women.
* Data in MTSC is classified by speaker. Therefore, all the recordings of each individual speaker are stored in one single directory.
* Data is also classified according to the gender (male/female) of the speakers.
* Every audio file in the MTSC has a duration between 3 and 10 seconds approximately.
* Audio files in the MTSC are distributed in a 16khz@16bit mono format.
* Transcriptions in MTSC are in lowercase. No punctuation marks are permitted except for dashes (-) and apostrophes (') due to their importance in Maltese orthography.
### Source Data
#### Initial Data Collection and Normalization
The MASRI-TEST CORPUS was possible due to a collaboration of two different Universities. The data selection and audio segmentation was performed by the [CIEMPIESS-UNAM Project](http://www.ciempiess.org/) at the [Universidad Nacional Autónoma de México (UNAM)](https://www.unam.mx/) in Mexico City. The audio transcription and corpus edition was performed by the [MASRI Team](https://www.um.edu.mt/projects/masri/) at the [University of Malta](https://www.um.edu.mt/) in the Msida Campus.
### Annotations
#### Annotation process
Proper nouns and other words pronounced in languages other than Maltese (mainly from English, Italian, French and German) were transcribed in their respective orthographic system.
#### Who are the annotators?
The audio transcription was performed by expert native speakers at the [University of Malta](https://www.um.edu.mt/) in the Msida Campus.
### Personal and Sensitive Information
The dataset could contain names revealing the identity of some speakers; on the other side, the recordings come from a publicly repository (YouTube), so, there is not a real intent of the participants to be anonymized. Anyway, you agree to not attempt to determine the identity of speakers in this dataset.
**Notice:** Should you consider that our data contains material that is owned by you and should therefore not be reproduced here?, please:
* Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
* Clearly identify the copyrighted work claimed to be infringed.
* Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.
* Send the request to [Carlos Mena](mailto:carlos.mena@ciempiess.org)
Take down: We will comply to legitimate requests by removing the affected sources from the corpus.
## Considerations for Using the Data
### Social Impact of Dataset
This dataset is challenging because it contains spontaneous speech; so, it will be helpful for the ASR community to evaluate their acoustic models in Maltese with it.
### Discussion of Biases
The dataset intents to be gender balanced. It is comprised of 17 male speakers and 17 female speakers.
### Other Known Limitations
Neither the MASRI Team or the CIEMPIESS-UNAM Project guarantee the accuracy of this corpus, nor its suitability for any specific purpose. As a matter of fact, a number of errors, omissions and inconsistencies are expected to be found within the corpus.
### Dataset Curators
The audio recordings were collected and segmented by students belonging to the social service program ["Desarrollo de Tecnologías del Habla"](http://profesores.fi-b.unam.mx/carlos_mena/servicio.html), it was curated by Carlos Daniel Hernández Mena and its transcriptions were manually performed by Ayrton-Didier Brincat during 2020.
### Licensing Information
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). The copyright remains with the original owners of the video.
As the data is taken from YouTube, we invoke the same argument of "fair use" as in the [Voxlingua107](http://bark.phon.ioc.ee/voxlingua107/) dataset, which is:
**"While YouTube users own the copyright to their own videos, using the audio in the videos for training speech recognition models has very limited and transformative purpose and qualifies thus as "fair use" of copyrighted materials. YouTube’s terms of service forbid downloading, storing and distribution of videos. However, the aim of this rule is clearly to forbid unfair monetization of the content by third-party sites and applications. Our dataset contains the videos in segmented audio-only form that makes the monetization of the actual distributed content extremely difficult."**
### Citation Information
```
@misc{carlosmenamasritest2020,
      title={MASRI-TEST CORPUS: Audio and Transcriptions in Maltese extracted from the YouTube channel of the University of Malta.}, 
      author={Hernandez Mena, Carlos Daniel and  Brincat, Ayrton-Didier and Gatt, Albert and DeMarco, Andrea and Borg, Claudia and van der Plas, Lonneke and Meza Ruiz, Iván Vladimir},
      journal={MASRI Project, Malta},
      year={2020},
      url={https://huggingface.co/datasets/MLRS/masri_test},
}
```
### Contributions
The authors would like to thank to Alberto Templos Carbajal, Elena Vera and Angélica Gutiérrez for their support to the social service program ["Desarrollo de Tecnologías del Habla"](http://profesores.fi-b.unam.mx/carlos_mena/servicio.html) at the ["Facultad de Ingeniería (FI)"](https://www.ingenieria.unam.mx/) of the [Universidad Nacional Autónoma de México (UNAM)](https://www.unam.mx/). We also thank to the social service students for all the hard work during the audio segmentation.
