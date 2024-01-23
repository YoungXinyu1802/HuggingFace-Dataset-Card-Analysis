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
pretty_name: "Samrómur Children Icelandic Speech 1.0"
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- "samromur"
- children's speech
- 'icelandic: iceland'
- icelandic children
- icelandic kids
- kids
task_categories:
- automatic-speech-recognition
task_ids: []
---



# Dataset Card for samromur_children
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
- **Homepage:** [Samrómur Children Icelandic Speech 1.0](https://samromur.is/)
- **Repository:** [LDC](https://catalog.ldc.upenn.edu/LDC2022S11)
- **Paper:** [Samrómur Children: An Icelandic Speech Corpus](https://aclanthology.org/2022.lrec-1.105.pdf)
- **Point of Contact:** [Carlos Mena](mailto:carlos.mena@ciempiess.org), [Jón Guðnason](mailto:jg@ru.is)

### Dataset Summary

The Samrómur Children Corpus consists of audio recordings and metadata files containing prompts read by the participants. It contains more than 137000 validated speech-recordings uttered by Icelandic children.

The corpus is a result of the crowd-sourcing effort run by the Language and Voice Lab (LVL) at the Reykjavik University, in cooperation with Almannarómur, Center for Language Technology. The recording process has started in October 2019 and continues to this day (Spetember 2021). 


### Example Usage
The Samrómur Children Corpus is divided in 3 splits: train, validation and test. To load a specific split pass its name as a config name:
```python
from datasets import load_dataset
samromur_children = load_dataset("language-and-voice-lab/samromur_children")
```
To load an specific split (for example, the validation split) do:
```python
from datasets import load_dataset
samromur_children = load_dataset("language-and-voice-lab/samromur_children",split="validation")
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
  'audio_id': '015652-0717240', 
  'audio': {
    'path': '/home/carlos/.cache/HuggingFace/datasets/downloads/extracted/2c6b0d82de2ef0dc0879732f726809cccbe6060664966099f43276e8c94b03f2/test/015652/015652-0717240.flac', 
    'array': array([ 0.        ,  0.        ,  0.        , ..., -0.00311279,
       -0.0007019 ,  0.00128174], dtype=float32), 
    'sampling_rate': 16000
  }, 
  'speaker_id': '015652', 
  'gender': 'female', 
  'age': '11', 
  'duration': 4.179999828338623, 
  'normalized_text': 'eiginlega var hann hin unga rússneska bylting lifandi komin'
}
```

### Data Fields
* `audio_id` (string) - id of audio segment
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `speaker_id` (string) - id of speaker
* `gender` (string) - gender of speaker (male or female)
* `age` (string) - range of age of the speaker: Younger (15-35), Middle-aged (36-60) or Elderly (61+).
* `duration` (float32) - duration of the audio file in seconds.
* `normalized_text` (string) - normalized audio segment transcription.

### Data Splits
The corpus is split into train, dev, and test portions. Lenghts of every portion are: train = 127h25m, test = 1h50m, dev=1h50m.

To load an specific portion please see the above section "Example Usage".

## Dataset Creation

### Curation Rationale

In the field of Automatic Speech Recognition (ASR) is a known fact that the children's speech is particularly hard to recognise due to its high variability produced by developmental changes in children's anatomy and speech production skills.

For this reason, the criteria of selection for the train/dev/test portions have to take into account the children's age. Nevertheless, the Samrómur Children is an unbalanced corpus in terms of gender and age of the speakers. This means that the corpus has, for example, a total of 1667 female speakers (73h38m) versus 1412 of male speakers (52h26m).

These unbalances impose conditions in the type of the experiments than can be performed with the corpus. For example, a equal number of female and male speakers through certain ranges of age is impossible. So, if one can't have a perfectly balance corpus in the training set, at least one can have it in the test portion.

The test portion of the Samrómur Children was meticulously selected to cover ages between 6 to 16 years in both female and male speakers. Every of these range of age in both genders have a total duration of 5 minutes each.

The development portion of the corpus contains only speakers with an unknown gender information. Both test and dev sets have a total duration of 1h50m each.

In order to perform fairer experiments, speakers in the train and test sets are not shared. Nevertheless, there is only one speaker shared between the train and development set. It can be identified with the speaker ID=010363. However, no audio files are shared between these two sets. 

### Source Data

#### Initial Data Collection and Normalization

The data was collected using the website https://samromur.is, code of which is available at https://github.com/cadia-lvl/samromur. The age range selected for this corpus is between 4 and 17 years.

The original audio was collected at 44.1 kHz or 48 kHz sampling rate as *.wav files, which was down-sampled to 16 kHz and converted to *.flac. Each recording contains one read sentence from a script. The script contains 85.080 unique sentences and 90.838 unique tokens. 

There was no identifier other than the session ID, which is used as the speaker ID. The corpus is distributed with a metadata file with a detailed information on each utterance and speaker. The madata file is encoded as UTF-8 Unicode.

The prompts were gathered from a variety of sources, mainly from The Icelandic Gigaword Corpus, which is available at http://clarin.is/en/resources/gigaword. The corpus includes text from novels, news, plays, and from a list of location names in Iceland. The prompts also came from the [Icelandic Web of Science](https://www.visindavefur.is/).

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
This is the first ASR corpus of Icelandic children.

### Discussion of Biases

* The utterances were recorded by a smartphone or the web app. 

* Participants self-reported their age group, gender, and the native language.

* Participants are aged between 4 to 17 years. 
 
* The corpus contains 137597 utterances from 3175 speakers, totalling 131 hours.

* The amount of data due to female speakers is 73h38m, the amount of data due to male speakers is 52h26m and the amount of data due to speakers with an unknown gender information is 05h02m

* The number of female speakers is 1667, the number of male speakers is 1412. The number of speakers with an unknown gender information is 96.

* The audios due to female speakers are 78993, the audios due to male speakers are 53927 and the audios due to speakers with an unknown gender information are 4677.

### Other Known Limitations
"Samrómur Children: Icelandic Speech 21.09" by the Language and Voice Laboratory (LVL) at the Reykjavik University is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License with the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Additional Information

### Dataset Curators

The corpus is a result of the crowd-sourcing effort run by the Language and Voice Lab (LVL) at the Reykjavik University, in cooperation with Almannarómur, Center for Language Technology. The recording process has started in October 2019 and continues to this day (Spetember 2021). The corpus was curated by Carlos Daniel Hernández Mena in 2021.

### Licensing Information
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information
```
@misc{menasamromurchildren2021,
      title={Samrómur Children Icelandic Speech 1.0}, 
      ldc_catalog_no={LDC2022S11},
      DOI={https://doi.org/10.35111/frrj-qd60},
      author={Hernández Mena, Carlos Daniel and Borsky, Michal and Mollberg, David Erik  and Guðmundsson, Smári Freyr and Hedström, Staffan and Pálsson, Ragnar and Jónsson, Ólafur Helgi and Þorsteinsdóttir, Sunneva and Guðmundsdóttir, Jóhanna Vigdís and Magnúsdóttir, Eydís Huld and Þórhallsdóttir, Ragnheiður and Guðnason, Jón},
      publisher={Reykjavík University}
      journal={Linguistic Data Consortium, Philadelphia},
      year={2019},
      url={https://catalog.ldc.upenn.edu/LDC2022S11},
}
```

### Contributions
This project was funded by the Language Technology Programme for Icelandic 2019-2023. The programme, which is managed and coordinated by Almannarómur, is funded by the Icelandic Ministry of Education, Science and Culture.

The verification for the dataset was funded by the the Icelandic Directorate of Labour's Student Summer Job Program in 2020 and 2021.

Special thanks for the summer students for all the hard work.

