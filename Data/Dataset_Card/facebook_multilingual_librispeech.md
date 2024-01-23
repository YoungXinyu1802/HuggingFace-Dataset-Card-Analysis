---
pretty_name: MultiLingual LibriSpeech
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
- expert-generated
language:
- de
- nl
- fr
- it
- es
- pt
- pl
license:
- cc-by-4.0
multilinguality:
- multilingual
paperswithcode_id: multilingual-librispeech
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- automatic-speech-recognition
---

# Dataset Card for MultiLingual LibriSpeech

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
  - [How to use](#how-to-use)
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

- **Homepage:** [MultiLingual LibriSpeech ASR corpus](http://www.openslr.org/94)
- **Repository:** [Needs More Information]
- **Paper:** [MLS: A Large-Scale Multilingual Dataset for Speech Research](https://arxiv.org/abs/2012.03411)
- **Leaderboard:** [🤗 Autoevaluate Leaderboard](https://huggingface.co/spaces/autoevaluate/leaderboards?dataset=facebook%2Fmultilingual_librispeech&only_verified=0&task=automatic-speech-recognition&config=-unspecified-&split=-unspecified-&metric=wer)

### Dataset Summary

This is a streamable version of the Multilingual LibriSpeech (MLS) dataset. 
The data archives were restructured from the original ones from [OpenSLR](http://www.openslr.org/94) to make it easier to stream.

MLS dataset is a large multilingual corpus suitable for speech research. The dataset is derived from read audiobooks from LibriVox and consists of 
8 languages - English, German, Dutch, Spanish, French, Italian, Portuguese, Polish.

### Supported Tasks and Leaderboards

- `automatic-speech-recognition`, `speaker-identification`: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER). The task has an active leaderboard which can be found at https://paperswithcode.com/dataset/multilingual-librispeech and ranks models based on their WER.

### Languages

The dataset is derived from read audiobooks from LibriVox and consists of 8 languages - English, German, Dutch, Spanish, French, Italian, Portuguese, Polish

### How to use

The `datasets` library allows you to load and pre-process your dataset in pure Python, at scale. The dataset can be downloaded and prepared in one call to your local drive by using the `load_dataset` function. 

For example, to download the German config, simply specify the corresponding language config name (i.e., "german" for German):
```python
from datasets import load_dataset

mls = load_dataset("facebook/multilingual_librispeech", "german", split="train")
```

Using the datasets library, you can also stream the dataset on-the-fly by adding a `streaming=True` argument to the `load_dataset` function call. Loading a dataset in streaming mode loads individual samples of the dataset at a time, rather than downloading the entire dataset to disk.
```python
from datasets import load_dataset

mls = load_dataset("facebook/multilingual_librispeech", "german", split="train", streaming=True)

print(next(iter(mls)))
```

*Bonus*: create a [PyTorch dataloader](https://huggingface.co/docs/datasets/use_with_pytorch) directly with your own datasets (local/streamed).

Local:

```python
from datasets import load_dataset
from torch.utils.data.sampler import BatchSampler, RandomSampler

mls = load_dataset("facebook/multilingual_librispeech", "german", split="train")
batch_sampler = BatchSampler(RandomSampler(mls), batch_size=32, drop_last=False)
dataloader = DataLoader(mls, batch_sampler=batch_sampler)
```

Streaming:

```python
from datasets import load_dataset
from torch.utils.data import DataLoader

mls = load_dataset("facebook/multilingual_librispeech", "german", split="train", streaming=True)
dataloader = DataLoader(mls, batch_size=32)
```

To find out more about loading and preparing audio datasets, head over to [hf.co/blog/audio-datasets](https://huggingface.co/blog/audio-datasets).

### Example scripts

Train your own CTC or Seq2Seq Automatic Speech Recognition models on MultiLingual Librispeech with `transformers` - [here](https://github.com/huggingface/transformers/tree/main/examples/pytorch/speech-recognition).

## Dataset Structure

### Data Instances

A typical data point comprises the path to the audio file, usually called `file` and its transcription, called `text`. Some additional information about the speaker and the passage which contains the transcription is provided.

```
{'file': '10900_6473_000030.flac',
 'audio': {'path': '10900_6473_000030.flac',
  'array': array([-1.52587891e-04,  6.10351562e-05,  0.00000000e+00, ...,
          4.27246094e-04,  5.49316406e-04,  4.57763672e-04]),
  'sampling_rate': 16000},
 'text': 'więc czego chcecie odemnie spytałem wysłuchawszy tego zadziwiającego opowiadania broń nas stary człowieku broń zakrzyknęli równocześnie obaj posłowie\n',
 'speaker_id': 10900,
 'chapter_id': 6473,
 'id': '10900_6473_000030'}
```


### Data Fields

- file: A filename .flac format.

- audio: A dictionary containing the audio filename, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- text: the transcription of the audio file.

- id: unique id of the data sample.

- speaker_id: unique id of the speaker. The same speaker id can be found for multiple data samples.

- chapter_id: id of the audiobook chapter which includes the transcription.

### Data Splits

|                             | Train | Train.9h | Train.1h  | Dev | Test |
| -----                       | ------ | ----- | ---- | ---- | ---- | 
| german | 469942 | 2194 | 241 | 3469 | 3394 |
| dutch | 374287 | 2153 | 234 | 3095 | 3075 |
| french | 258213 | 2167 | 241 | 2416 | 2426 |
| spanish | 220701 | 2110 | 233 | 2408 | 2385 |
| italian | 59623 | 2173 | 240 | 1248 | 1262 |
| portuguese | 37533 | 2116 | 236 | 826 | 871 |
| polish | 25043 | 2173 | 238 | 512 | 520 |



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

The dataset consists of people who have donated their voice online. You agree to not attempt to determine the identity of speakers in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

Public Domain, Creative Commons Attribution 4.0 International Public License ([CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

### Citation Information

```
@article{Pratap2020MLSAL,
  title={MLS: A Large-Scale Multilingual Dataset for Speech Research},
  author={Vineel Pratap and Qiantong Xu and Anuroop Sriram and Gabriel Synnaeve and Ronan Collobert},
  journal={ArXiv},
  year={2020},
  volume={abs/2012.03411}
}
```

### Contributions

Thanks to [@patrickvonplaten](https://github.com/patrickvonplaten) 
and [@polinaeterna](https://github.com/polinaeterna) for adding this dataset.
