---
pretty_name: Nota

license: 
- cc0-1.0
language:
- da
multilinguality:
- monolingual
task_categories:
- automatic-speech-recognition

---
# Dataset Card Nota Lyd- og tekstdata
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
  - [Disclaimer](#disclaimer)
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
## Dataset Description
- **Homepage:** https://sprogteknologi.dk/dataset/notalyd-ogtekstdata
- **Data Storage Url:** https://sprogtek-ressources.digst.govcloud.dk/nota/
- **Point of Contact:** info@sprogteknologi.dk 
### Dataset Summary
This data was created by the public institution Nota (https://nota.dk/), which is part of the Danish Ministry of Culture. Nota has a library audiobooks and audiomagazines for people with reading or sight disabilities. Nota also produces a number of audiobooks and audiomagazines themselves.  

The dataset consists of .wav and .txt files from Nota's audiomagazines "Inspiration" and "Radio/TV".

The dataset has been published as a part of the initiative sprogteknologi.dk, within the Danish Agency for Digital Government (www.digst.dk). 

336 GB available data, containing voice recordings and accompanying transcripts. 

Each publication has been segmented into bits of 2 - 50 seconds .wav files with an accompanying transcription


### Supported Tasks and Leaderboards
[Needs More Information]
### Languages
Danish
## Dataset Structure
### Data Instances
A typical data point comprises the path to the audio file, called path and its sentence.
`
{'path': '<path_to_clip>.wav', 'sentence': 'Dette er et eksempel', 'audio': {'path': <path_to_clip>.wav', 'array': array([-0.00048828, -0.00018311, -0.00137329, ...,  0.00079346, 0.00091553,  0.00085449], dtype=float32), 'sampling_rate': 44100}
`
### Data Fields
path: The path to the audio file

audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

sentence: The sentence that was read by the speaker
### Data Splits
The material has for now only a train split. As this is very early stage of the dataset, splits might be introduced at a later stage.


## Dataset Creation

### Disclaimer 
There might be smaller discrepancies between the .wav and .txt files. Therefore, there might be issues in the alignment of timestamps, text and sound files. 

There are no strict rules as to how readers read aloud non-letter characters (i.e. numbers, â‚¬, $, !, ?). These symbols can be read differently throughout the dataset. 

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
The dataset is made public and free to use. Recorded individuals has by written contract accepted and agreed to the publication of their recordings. 
Other names appearing in the dataset are already publically known individuals (i.e. TV or Radio host names). Their names are not to be treated as sensitive or personal data in the context of this dataset. 
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed] 
### Discussion of Biases
[More Information Needed] 
### Other Known Limitations
[More Information Needed] 
## Additional Information
### Dataset Curators
https://sprogteknologi.dk/

Contact info@sprogteknologi.dk if you have questions regarding use of data.
They gladly receive inputs and ideas on how to distribute the data.
### Licensing Information
[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/)
### 