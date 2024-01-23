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
pretty_name: "Málrómur: A manually verified corpus of recorded Icelandic speech"
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- crowd-sourced icelandic
- "málrómur"
- icelandic speech
- malromur
- iceland
task_categories:
- automatic-speech-recognition
task_ids: []
---



# Dataset Card for malromur_asr
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [About the project](#about-the-project)
  - [About the Malromur corpus](#about-the-malromur-corpus)
  - [The Almannaromur project](#the-almannaromur-project)
  - [The data opened](#the-data-opened)
- [Additional Information](#additional-information)
  - [Other Known Limitations](#other-known-limitations)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
  
## Dataset Description
- **Homepage:** The Málrómur Corpus
- **Repository:** [Clarin.is](https://clarin.is/en/resources/malromur/)
- **Paper:** [Málrómur: A Manually Verified Corpus of Recorded Icelandic Speech](https://ep.liu.se/ecp/131/029/ecp17131029.pdf)
- **Point of Contact:** [Jón Guðnason](mailto:jg@ru.is)

### Dataset Summary

The Málrómur corpus, an open, manually verified, Icelandic speech corpus. The recordings were collected in 2011–2012 by Reykjavik University and the Icelandic Center for Language Technology in cooperation with Google.

### Example Usage
The Málrómur Corpus is divided in 3 splits: train, validation and test. To load a specific split pass its name as a config name:
```python
from datasets import load_dataset
malromur_asr = load_dataset("language-and-voice-lab/malromur_asr")
```
To load an specific split (for example, the validation split) do:
```python
from datasets import load_dataset
malromur_asr = load_dataset("language-and-voice-lab/malromur_asr",split="validation")
```

### Supported Tasks
automatic-speech-recognition: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

### Languages
The audio is in Icelandic.

## Dataset Structure

### Data Instances
```python
{
  'audio_id': 'is_is-mrn_07_06-2012-02-01T16:23:40.207297', 
  'audio': {
    'path': '/home/jon/.cache/HuggingFace/datasets/downloads/extracted/11c85f8d1098257da3161566b6b80bdf30b8512c8eeea357947c02620ba70b8a/dev/is_is-mrn_07_06-2012-02-01T16:23:40.207297.flac', 
    'array': array([0.00042725, 0.00030518, 0.00033569, ..., 0.00030518, 0.00015259,
       0.00054932], dtype=float32), 
    'sampling_rate': 16000
  }, 
  'speaker_id': 'is_is-mrn_07_06', 
  'gender': 'male', 
  'age': '50_59', 
  'duration': 3.9000000953674316, 
  'normalized_text': 'hrólfsskálavör'
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
The corpus is split into train, validation, and test portions. Lenghts of every portion are: train=119h03m, test=13h41m, validation=3h22m.

To load an specific portion please see the above section "Example Usage".

## About the project

### About the Malromur corpus

[Reykjavík University](http://en.ru.is/) and [The Icelandic Centre for Language Technology](http://iclt.is/) collected data for an Icelandic speech corpus in collaboration with Google. The data is available on this webpage for everybody, and presents an opportunity to develop language technology tools for Icelandic such as a speech recognizer. Voice samples from 563 individuals were recorded with Android G1 smartphones for a total of 152 hours of speech. In total 127,286 voice samples were recorded. Of those 108,568 were considered useful and 18,718 were discarded. The 108,568 good voice samples can be downloaded from this webpage.

### The Almannaromur project

The Almannarómur project was performed during the years 2011 and 2012. With the support of Google, work was performed at that time to collect voice samples for various languages in order to develop speech recognition tools, and to make the data available for the research and development of language technology tools. The goal of the Almannarómur project was to develop a database of spoken sentences to aid the development of automatic speech recognition for Icelandic. The database can also be used in the development of many other types of spoken language technologies. 

Google cooperated with [Reykjavík University](http://en.ru.is/) and [The Icelandic Centre for Language Technology](http://iclt.is/) in collecting voice samples for Icelandic. During the first phase of the project a text corpus with sentences was generated. About 50% of the texts in the corpus are news stories from the website mbl.is (the website of the newspaper Morgunblaðið), 10% are rare tri-phones, 10% are street names, 10% are names of people, 10% are miscellaneous, 5% are names of countries and capitals and 5% are URLs. The corpus contains 55,000 sentences. A list containing numbers, dates, times of day, names of days and months, simple questions, and common greetings was also included in the corpus.

Headlines were extracted from the text obtained from [mbl.is](https://www.mbl.is/frettir/) and then processed by the [IceNLP](https://clarin.is/en/resources/icenlp/) sentence segmentizer in order to obtain a complete sentence list. The length of each sentence was limited to six words, in order to make reading easier and to ensure that the sentence would fit on the screen of the Android G1 device. Each sentence was checked for spelling, using the [Database of Modern Icelandic Inflection](https://clarin.is/en/resources/dmii/) (BÍN). Any sentences containing words not found in the dictionary were deleted from the final list. Sentences were then ordered randomly to ensure that the sample of sentences that each participant was to read was representative of the text in the corpus. 

The data was recorded using Android G1 smartphones. Each participant was asked to read for 30 minutes or up to 250 utterances. The people donating their voice were non-paid participants of the project and signed a [special agreement](https://clarin.is/media/uploads/google_samthykki_en.pdf) about the use of the voice samples in spoken language technologies operated by Google and other spoken language tools. Google provided ten Android G1 smartphones that were used in the project. 

The voice samples were collected in three phases. The first phase started on July 15, 2011. Ten volunteers each received smartphones and had the responsibility of obtaining participants, i.e. asking them to donate a voice sample by reading sentences for 30 minutes. This phase ended in August and the approach was not as effective as anticipated. It turned out to be difficult to get people to volunteer. The volunteers that did help out also had a hard time getting participants. The total number of people participating in this phase was 59. The second phase was carried out from September and October 2011, and was based on organized events around the data collection effort. A series of events were advertised within the capital's universities (Reykjavík University and University of Iceland) where two to three volunteers collected voices from participants, using all ten phones. This approach lasted for four weeks and was considerably more effective than the first approach, as 104 people participated in the project. The last phase was carried out from November 2011 to January 2012, and was based on organized visits to companies and institutions. The preparation for this phase took some time as key individuals in the workplace were identified and approached and asked to organize the data collection. Each workplace received a set number of smartphones for a set number of days. The phones were then sent to the next workplace. Two to five volunteers were recruited and the duration of the collection was deliberately kept low, usually lasting only three to four days. Nineteen total workplaces were visited and the total number of participants in this phase was 430. The total number of read sentences was thus 123,227 from 593 individuals.

A client-software was set up on the smartphones that enabled downloading of Icelandic utterances and the uploading of speech recordings. Google technical staff used the voice samples together with other Icelandic language resources (large text corpora to make a language model) to develop a speech recognizer for Icelandic for Android smartphones and the Google search engine. These tools were announced in the fall of 2012.

### The data opened

It was decided to make the database with the voice samples open source to be used for the development of speech recognizers and other speech technology tools. To make the voice samples as useful as possible, it was considered necessary to validate them. In the summer of 2014, a student at the [University of Iceland](https://english.hi.is/) listened to 69,000 voice samples to determine whether the spoken text agreed with the text to be read. At the end of the summer, 57,000 voice samples had been validated to be good and were made available on this webpage. During the summer of 2015, another student listened to more voice samples, and during the year 2016, employees at the [Árni Magnússon Institute for Icelandic Studies](https://english.arnastofnun.is/) finished listening to the voice samples.

In total, 127,286 voice samples were recorded, with 5,401 failed recordings, resulting in 121,885 voice samples that were evaluated. Before the verification process started, new sound files were created by trimming long periods of silence at the beginning and end of the recordings. The total duration of the untrimmed files is about 152 hours, but this was reduced to about 90 hours. During this process, 2,795 files were found to comprise only silence. Therefore, in the first stage of the verification process, 119,090 voice samples were evaluated. 100,020 recordings were accepted as correct, and 19,070 were rejected. During the second stage in the winter of 2016–2017, two evaluators listened to untrimmed versions of the 19,070 recordings that were rejected in stage one and classified them further. Of these samples, 8,548 were classified as correct. In total, it is considered that 108,568 voice samples are good and are available through this webpage.

Four evaluators listened to 3000 voice samples selected randomly from all samples evaluated in the first stage. All evaluators listened to all the 3000 samples. Results are in-line with results obtained during the second stage of the verification process.

An Icelandic NGO, Almannrómur, was established April 1st 2013. The aim of the NGO is to develop language technology tools for Icelandic. The database made available here has therefore been given the name Málrómur (“voice”).

For further information see the articles [“Almannarómur: An Open Icelandic Speech Corpus”](http://www.mica.edu.vn/sltu2012/files/proceedings/15.pdf) and [“Málrómur: A Manually Verified Corpus of Recorded Icelandic Speech”](http://www.ep.liu.se/ecp/131/029/ecp17131029.pdf) (see above).

## Aditional information

### Other Known Limitations
"The Málrómur Corpus" by the Language and Voice Laboratory (LVL) at the Reykjavik University is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License with the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

### Licensing Information
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information
```
@inproceedings{steingrimsson2017malromur,
  title={Málrómur: A manually verified corpus of recorded Icelandic speech},
  author={Steingrímsson, Steinþór and Guðnason, Jón and Helgadóttir, Sigrún and Rögnvaldsson, Eiríkur},
  booktitle={Proceedings of the 21st Nordic Conference on Computational Linguistics},
  pages={237--240},
  year={2017}
}
```

### Contributions
The Almannarómur project was partially realized because of the generous help received from Google and its employees. Google provided the smart-phones for the data recording effort and the server technology used to host the database.

