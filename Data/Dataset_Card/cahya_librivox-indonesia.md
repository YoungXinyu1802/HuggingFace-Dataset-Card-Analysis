---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- ace
- bal
- bug
- id
- min
- jav
- sun
license: cc
multilinguality:
- multilingual
size_categories:
  ace:
  - 1K<n<10K
  bal:
  - 1K<n<10K
  bug:
  - 1K<n<10K
  id:
  - 1K<n<10K
  min:
  - 1K<n<10K
  jav:
  - 1K<n<10K
  sun:
  - 1K<n<10K
source_datasets:
- librivox
task_categories:
- automatic-speech-recognition
task_ids: []
pretty_name: LibriVox Indonesia 1.0
---
# Dataset Card for LibriVox Indonesia 1.0

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
- **Homepage:** https://huggingface.co/datasets/indonesian-nlp/librivox-indonesia
- **Repository:** https://huggingface.co/datasets/indonesian-nlp/librivox-indonesia
- **Point of Contact:** [Cahya Wirawan](mailto:cahya.wirawan@gmail.com)

### Dataset Summary
The LibriVox Indonesia dataset consists of MP3 audio and a corresponding text file we generated from the public 
domain audiobooks [LibriVox](https://librivox.org/). We collected only languages in Indonesia for this dataset. 
The original LibriVox audiobooks or sound files' duration varies from a few minutes to a few hours. Each audio 
file in the speech dataset now lasts from a few seconds to a maximum of 20 seconds. 

We converted the audiobooks to speech datasets using the forced alignment software we developed. It supports 
multilingual, including low-resource languages, such as Acehnese, Balinese, or Minangkabau. We can also use it 
for other languages without additional work to train the model.

The dataset currently consists of 8 hours in 7 languages from Indonesia. We will add more languages or audio files
as we collect them.

### Languages
```
Acehnese, Balinese, Bugisnese, Indonesian, Minangkabau, Javanese, Sundanese
```

## Dataset Structure
### Data Instances
A typical data point comprises the `path` to the audio file and its `sentence`. Additional fields include 
`reader` and `language`.
```python
{
  'path': 'librivox-indonesia/sundanese/universal-declaration-of-human-rights/human_rights_un_sun_brc_0000.mp3',
  'language': 'sun',
  'reader': '3174',
  'sentence': 'pernyataan umum ngeunaan hak hak asasi manusa sakabeh manusa',
  'audio': {
    'path': 'librivox-indonesia/sundanese/universal-declaration-of-human-rights/human_rights_un_sun_brc_0000.mp3', 
    'array': array([-0.00048828, -0.00018311, -0.00137329, ...,  0.00079346, 0.00091553,  0.00085449], dtype=float32), 
    'sampling_rate': 44100
  }, 
}
```

### Data Fields
`path` (`string`): The path to the audio file

`language` (`string`): The language of the audio file

`reader` (`string`): The reader Id in LibriVox

`sentence` (`string`): The sentence the user read from the book.

`audio` (`dict`): A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

### Data Splits
The speech material has only train split.

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
[More Information Needed] 
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed] 
### Discussion of Biases
[More Information Needed] 
### Other Known Limitations
[More Information Needed] 
## Additional Information
### Dataset Curators
[More Information Needed] 
### Licensing Information
Public Domain, [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)
### Citation Information
```

```