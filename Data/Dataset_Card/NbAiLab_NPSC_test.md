---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- nb
- 'no'
- nn
license:
- cc0-1.0
multilinguality:
- monolingual
size_categories:
- 2G<n<1B
source_datasets:
- original
task_categories:
- automatic-speech-recognition
- audio-classification
task_ids:
- speech-modeling
pretty_name: NPSC
tags:
- speech-modeling
---
# Dataset Card for NBAiLab/NPSC


## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Summary](#dataset-summary)
- [Data Fields](#data-fiels)
- [Dataset Creation](#dataset-creation)
- [Statistics](#statistics)
- [Document Types](#document-types)
- [Languages](#languages)
- [Publish Periode](#publish-periode)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Social Impact of Dataset](#social-impact-of-dataset)
- [Discussion of Biases](#discussion-of-biases)
- [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
- [Dataset Curators](#dataset-curators)
- [Licensing Information](#licensing-information)
- [Citation Information](#citation-information)

## Dataset Description
- **Homepage:** https://www.nb.no/sprakbanken/
- **Repository:** https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-58/
- **Paper:** https://www.nb.no/sprakbanken/
- **Point of Contact:** [Per Erik Solberg](mailto:per.solberg@nb.no)

The Norwegian Parliament Speech Corpus (NPSC) is a corpus for training a Norwegian ASR (Automatic Speech Recognition) models. The corpus is created by Språkbanken at the National Library in Norway. 

NPSC is based on sound recording from meeting in the Norwegian Parliament. These talks are orthographically transcribed to either Norwegian Bokmål or Norwegian Nynorsk. In addition to the data actually included in this dataset, there is a significant amount of metadata that is included in the original corpus. Through the speaker id there is additional information about the speaker, like gender, age, and place of birth (ie dialect). Through the proceedings id the corpus can be linked to the official proceedings from the meetings. 

The corpus is in total sound recordings from 40 entire days of meetings. This amounts to 140 hours of speech, 65,000 sentences or 1.2 million words. 

This corpus is an adaption of the original corpus made for efficiant ASR training. For simplicity and portability, a few of the original datasets features, like the token transcription, is ommitted. You can find the complete dataset at [the Resource Catalogue at Språkbanken](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-58/).

## How to Use (This needs to be edited of course)
```python
from datasets import load_dataset
data = load_dataset("nb/NPSC", streaming=True)
```

## Data Fields
Currently there are two versions included in this repo.

### Version A
This verison has a short list of the metadata and includes the audio (48k mp3) encoded as a float32 array in the dataset itself.

The current dataloader script is associated with this version.

One line in train.json looks like this:

```json
{
  "sentence_id": 7309,
  "sentence_order": 0,
  "speaker_id": 1,
  "speaker_name": "Marit Nybakk",
  "sentence_text": "Stortingets møte er lovlig satt",
  "sentence_language_code": "nb-NO",
  "text": "Stortingets møte er lovlig satt",
  "start_time": 302650,
  "end_time": 306000,
  "normsentence_text": "Stortingets møte er lovlig satt",
  "transsentence_text": "Stortingets møte er lovleg sett",
  "translated": 1,
  "audio": {
    "path": "audio/20170207-095506_302650_306000.wav",
    "array": [
      24,
      25,
      50,
      (...)
          ],
    "sampling_rate": 48000
  }
}
```

### Version B
This verison does not contain the audio encoded in the dataset. Instead it has the audio files placed in sub-directories. There are currently both samples in clips_48k_wav and clips_16k_mp3. Only the base filename is referred in the dataset. Please not that there are both sentence-based audio clips as well at meeting-based audio clips. The dataset contains referrals to both, the latter referral has start and stop time as well.

One line in the train/metadata.json looks like this:
```json
{
  "meeting_date": "20170207",
  "full_audio_file": "20170207-095506",
  "proceedings_file": "20170207-095506.ref",
  "duration": 4442474,
  "transcriber_id": 1,
  "reviewer_id": 2,
  "data_split": "test",
  "speaker_name": "Marit Nybakk",
  "speaker_id": 1,
  "sentence_id": 7309,
  "sentence_language_code": "nb-NO",
  "sentence_text": "Stortingets møte er lovlig satt",
  "sentence_order": 0,
  "audio_file": "20170207-095506_302650_306000",
  "start_time": 302650,
  "end_time": 306000,
  "normsentence_text": "Stortingets møte er lovlig satt",
  "transsentence_text": "Stortingets møte er lovleg sett",
  "translated": 1
}
```


### Dataset Creation
We are providing a **train**, **dev** and **test** split. These are the same as in the orginal corpus.

Build date: 20012022

#### Initial Data Collection and Curation
The procedure for the dataset creation is described in detail in the paper.


## Statistics
|   Feature | Value       |
|:---------|-----------:|
| Duration, pauses included     | 140,3 hours| 
| Duration, pauses not included     | 125,7 hours  | 
| Word count     | 1,2 million | 
| Sentence count     | 64.531 | 
| Language distribution     | Nynorsk: 12,8%| 
|      | Bokmål: 87,2%%| 
| Gender distribution     | Female: 38,3% | 
|      | Male: 61.7% | 

## Considerations for Using the Data
This corpus contains speech data and is allowed to be used outside the National Library of Norway for speech recognition technology purposes.

### Discussion of Biases
Please refer to our paper.

### Dataset Curators
[Per Erik Solberg](mailto:per.solberg@nb.no)

[Freddy Wetjen](mailto:Freddy.wetjen@nb.no), [Andre Kaasen](mailto:andre.kasen@nb.no) and [Per Egil Kummervold](mailto:per.kummervold@nb.no) has contributed to porting it to the Hugging Face Dataset format.

### Licensing Information
Licensed for use outside the National Library of Norway.

## License
CC-ZERO(https://creativecommons.org/publicdomain/zero/1.0/)

### Citation Information
We are preparing an article with detailed information about this corpus. Until it is published, please cite out paper discussing the first version of this corpus:
```
ANDRE: TO BE DONE

```
