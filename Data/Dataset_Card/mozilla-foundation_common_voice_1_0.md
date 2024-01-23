---
pretty_name: Common Voice Corpus 1
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language_bcp47:
- br
- ca
- cnh
- cv
- cy
- de
- en
- eo
- et
- fr
- ga-IE
- it
- kab
- ky
- nl
- sl
- tr
- tt
- zh-TW
license:
- cc0-1.0
multilinguality:
- multilingual
size_categories:
  br:
  - 1K<n<10K
  ca:
  - 10K<n<100K
  cnh:
  - 1K<n<10K
  cv:
  - 1K<n<10K
  cy:
  - 10K<n<100K
  de:
  - 100K<n<1M
  en:
  - 100K<n<1M
  eo:
  - 1K<n<10K
  et:
  - n<1K
  fr:
  - 10K<n<100K
  ga-IE:
  - 1K<n<10K
  it:
  - 10K<n<100K
  kab:
  - 100K<n<1M
  ky:
  - 1K<n<10K
  nl:
  - 10K<n<100K
  sl:
  - 1K<n<10K
  tr:
  - 1K<n<10K
  tt:
  - 10K<n<100K
  zh-TW:
  - 10K<n<100K
source_datasets:
- extended|common_voice
task_categories:
- speech-processing
task_ids:
- automatic-speech-recognition
paperswithcode_id: common-voice
extra_gated_prompt: "By clicking on “Access repository” below, you also agree to not attempt to determine the identity of speakers in the Common Voice dataset."
---

# Dataset Card for Common Voice Corpus 1

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

- **Homepage:** https://commonvoice.mozilla.org/en/datasets
- **Repository:** https://github.com/common-voice/common-voice
- **Paper:** https://arxiv.org/abs/1912.06670
- **Leaderboard:** https://paperswithcode.com/dataset/common-voice
- **Point of Contact:** [Anton Lozhkov](mailto:anton@huggingface.co)

### Dataset Summary

The Common Voice dataset consists of a unique MP3 and corresponding text file. 
Many of the 1368 recorded hours in the dataset also include demographic metadata like age, sex, and accent 
that can help improve the accuracy of speech recognition engines.

The dataset currently consists of 1096 validated hours in 19 languages, but more voices and languages are always added. 
Take a look at the [Languages](https://commonvoice.mozilla.org/en/languages) page to request a language or start contributing.

### Supported Tasks and Leaderboards

The results for models trained on the Common Voice datasets are available via the 
[🤗 Speech Bench](https://huggingface.co/spaces/huggingface/hf-speech-bench)

### Languages

```
Breton, Catalan, Chinese (Taiwan), Chuvash, Dutch, English, Esperanto, Estonian, French, German, Hakha Chin, Irish, Italian, Kabyle, Kyrgyz, Slovenian, Tatar, Turkish, Welsh
```

## Dataset Structure

### Data Instances

A typical data point comprises the `path` to the audio file and its `sentence`. 
Additional fields include `accent`, `age`, `client_id`, `up_votes`, `down_votes`, `gender`, `locale` and `segment`.

```python
{
  'client_id': 'd59478fbc1ee646a28a3c652a119379939123784d99131b865a89f8b21c81f69276c48bd574b81267d9d1a77b83b43e6d475a6cfc79c232ddbca946ae9c7afc5', 
  'path': 'et/clips/common_voice_et_18318995.mp3', 
  'audio': {
    'path': 'et/clips/common_voice_et_18318995.mp3', 
    'array': array([-0.00048828, -0.00018311, -0.00137329, ...,  0.00079346, 0.00091553,  0.00085449], dtype=float32), 
    'sampling_rate': 48000
  }, 
  'sentence': 'Tasub kokku saada inimestega, keda tunned juba ammust ajast saati.', 
  'up_votes': 2, 
  'down_votes': 0, 
  'age': 'twenties', 
  'gender': 'male', 
  'accent': '', 
  'locale': 'et', 
  'segment': ''
}
```

### Data Fields

`client_id` (`string`): An id for which client (voice) made the recording

`path` (`string`): The path to the audio file

`audio` (`dict`): A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

`sentence` (`string`): The sentence the user was prompted to speak

`up_votes` (`int64`): How many upvotes the audio file has received from reviewers

`down_votes` (`int64`): How many downvotes the audio file has received from reviewers

`age` (`string`): The age of the speaker (e.g. `teens`, `twenties`, `fifties`)

`gender` (`string`): The gender of the speaker

`accent` (`string`): Accent of the speaker

`locale` (`string`): The locale of the speaker

`segment` (`string`): Usually an empty field

### Data Splits

The speech material has been subdivided into portions for dev, train, test, validated, invalidated, reported and other.

The validated data is data that has been validated with reviewers and received upvotes that the data is of high quality.

The invalidated data is data has been invalidated by reviewers
and received downvotes indicating that the data is of low quality.

The reported data is data that has been reported, for different reasons.

The other data is data that has not yet been reviewed.

The dev, test, train are all data that has been reviewed, deemed of high quality and split into dev, test and train.

## Data Preprocessing Recommended by Hugging Face

The following are data preprocessing steps advised by the Hugging Face team. They are accompanied by an example code snippet that shows how to put them to practice. 

Many examples in this dataset have trailing quotations marks, e.g _“the cat sat on the mat.“_. These trailing quotation marks do not change the actual meaning of the sentence, and it is near impossible to infer whether a sentence is a quotation or not a quotation from audio data alone. In these cases, it is advised to strip the quotation marks, leaving: _the cat sat on the mat_.

In addition, the majority of training sentences end in punctuation ( . or ? or ! ), whereas just a small proportion do not. In the dev set, **almost all** sentences end in punctuation. Thus, it is recommended to append a full-stop ( . ) to the end of the small number of training examples that do not end in punctuation.

```python
from datasets import load_dataset

ds = load_dataset("mozilla-foundation/common_voice_1_0", "en", use_auth_token=True)

def prepare_dataset(batch):
  """Function to preprocess the dataset with the .map method"""
  transcription = batch["sentence"]
  
  if transcription.startswith('"') and transcription.endswith('"'):
    # we can remove trailing quotation marks as they do not affect the transcription
    transcription = transcription[1:-1]
  
  if transcription[-1] not in [".", "?", "!"]:
    # append a full-stop to sentences that do not end in punctuation
    transcription = transcription + "."
  
  batch["sentence"] = transcription
  
  return batch

ds = ds.map(prepare_dataset, desc="preprocess dataset")
```

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

The dataset consists of people who have donated their voice online.  You agree to not attempt to determine the identity of speakers in the Common Voice dataset.

## Considerations for Using the Data

### Social Impact of Dataset

The dataset consists of people who have donated their voice online.  You agree to not attempt to determine the identity of speakers in the Common Voice dataset.

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
@inproceedings{commonvoice:2020,
  author = {Ardila, R. and Branson, M. and Davis, K. and Henretty, M. and Kohler, M. and Meyer, J. and Morais, R. and Saunders, L. and Tyers, F. M. and Weber, G.},
  title = {Common Voice: A Massively-Multilingual Speech Corpus},
  booktitle = {Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020)},
  pages = {4211--4215},
  year = 2020
}
```
