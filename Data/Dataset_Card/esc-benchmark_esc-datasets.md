---
annotations_creators:
- expert-generated
- crowdsourced
- machine-generated
language:
- en
language_creators:
- crowdsourced
- expert-generated
license:
- cc-by-4.0
- apache-2.0
- cc0-1.0
- cc-by-nc-3.0
- other
multilinguality:
- monolingual
pretty_name: esc-datasets
size_categories:
- 100K<n<1M
- 1M<n<10M
source_datasets:
- original
- extended|librispeech_asr
- extended|common_voice
tags:
- asr
- benchmark
- speech
- esc
task_categories:
- automatic-speech-recognition
task_ids: []
extra_gated_prompt: |- 
    Three of the ESC datasets have specific terms of usage that must be agreed to before using the data. 
    To do so, fill in the access forms on the specific datasets' pages:
      * Common Voice: https://huggingface.co/datasets/mozilla-foundation/common_voice_9_0
      * GigaSpeech: https://huggingface.co/datasets/speechcolab/gigaspeech
      * SPGISpeech: https://huggingface.co/datasets/kensho/spgispeech
extra_gated_fields:
 I hereby confirm that I have registered on the original Common Voice page and agree to not attempt to determine the identity of speakers in the Common Voice dataset: checkbox
 I hereby confirm that I have accepted the terms of usages on GigaSpeech page: checkbox
 I hereby confirm that I have accepted the terms of usages on SPGISpeech page: checkbox
---

All eight of datasets in ESC can be downloaded and prepared in just a single line of code through the Hugging Face Datasets library:

```python
from datasets import load_dataset

librispeech = load_dataset("esc-benchmark/esc-datasets", "librispeech", split="train")
```

- `"esc-benchmark"`: the repository namespace. This is fixed for all ESC datasets.

- `"librispeech"`: the dataset name. This can be changed to any of any one of the eight datasets in ESC to download that dataset.

-  `split="train"`: the split. Set this to one of train/validation/test to generate a specific split. Omit the `split` argument to generate all splits for a dataset.


The datasets are full prepared, such that the audio and transcription files can be used directly in training/evaluation scripts.


## Dataset Information

A data point can be accessed by indexing the dataset object loaded through `load_dataset`:

```python
print(librispeech[0])
```

A typical data point comprises the path to the audio file and its transcription. Also included is information of the dataset from which the sample derives and a unique identifier name:

```python
{
  'dataset': 'librispeech', 
  'audio': {'path': '/home/esc-bencher/.cache/huggingface/datasets/downloads/extracted/d2da1969fe9e7d06661b5dc370cf2e3c119a14c35950045bcb76243b264e4f01/374-180298-0000.flac',
      'array': array([ 7.01904297e-04,  7.32421875e-04,  7.32421875e-04, ...,
             -2.74658203e-04, -1.83105469e-04, -3.05175781e-05]),
      'sampling_rate': 16000},
    'text': 'chapter sixteen i might have told you of the beginning of this liaison in a few lines but i wanted you to see every step by which we came i to agree to whatever marguerite wished',
    'id': '374-180298-0000'
}
 ```
 
### Data Fields

- `dataset`: name of the ESC dataset from which the sample is taken.

- `audio`: a dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate.

- `text`: the transcription of the audio file.

- `id`: unique id of the data sample.

### Data Preparation
#### Audio
The audio for all ESC datasets is segmented into sample lengths suitable for training ASR systems. The Hugging Face datasets library decodes audio files on the fly, reading the segments and converting them to a Python arrays. Consequently, no further preparation of the audio is required to be used in training/evaluation scripts.

Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, i.e. `dataset[0]["audio"]` should always be preferred over `dataset["audio"][0]`.

#### Transcriptions
The transcriptions corresponding to each audio file are provided in their 'error corrected' format. No transcription pre-processing is applied to the text, only necessary 'error correction' steps such as removing junk tokens (_&lt;unk>_) or converting symbolic punctuation to spelled out form (_&lt;comma>_  to  _,_). As such, no further preparation of the transcriptions is required to be used in training/evaluation scripts.

Transcriptions are provided for training and validation splits. The transcriptions are **not** provided for the test splits. The ESC benchmark requires you to generate predictions for the test sets and upload them to https://huggingface.co/spaces/esc-benchmark/esc for scoring.

### Access
All eight of the datasets in ESC are accessible and licensing is freely available. Three of the ESC datasets have specific terms of usage that must be agreed to before using the data. To do so, fill in the access forms on the specific datasets' pages:
* Common Voice: https://huggingface.co/datasets/mozilla-foundation/common_voice_9_0
* GigaSpeech: https://huggingface.co/datasets/speechcolab/gigaspeech
* SPGISpeech: https://huggingface.co/datasets/kensho/spgispeech

## LibriSpeech

The LibriSpeech corpus is a standard large-scale corpus for assessing ASR systems. It consists of approximately 1,000 hours of narrated audiobooks from the [LibriVox](https://librivox.org) project. It is licensed under CC-BY-4.0.

Example Usage:

```python
librispeech = load_dataset("esc-benchmark/esc-datasets", "librispeech")
```

Train/validation splits:
- `train` (combination of `train.clean.100`, `train.clean.360` and `train.other.500`)
- `validation.clean`
- `validation.other`

Test splits:
- `test.clean`
- `test.other`

Also available are subsets of the train split, which can be accessed by setting the `subconfig` argument:
```python
librispeech = load_dataset("esc-benchmark/esc-datasets", "librispeech", subconfig="clean.100")
```

- `clean.100`: 100 hours of training data from the 'clean' subset
- `clean.360`: 360 hours of training data from the 'clean' subset
- `other.500`: 500 hours of training data from the 'other' subset

## Common Voice
Common Voice is a series of crowd-sourced open-licensed speech datasets where speakers record text from Wikipedia in various languages. The English subset of contains approximately 1,400 hours of audio data from speakers of various nationalities, accents and different recording conditions. It is licensed under CC0-1.0.

Example usage:

```python
common_voice = load_dataset("esc-benchmark/esc-datasets", "common_voice", use_auth_token=True)
```

Training/validation splits:
- `train`
- `validation`

Test splits:
- `test`

## VoxPopuli
VoxPopuli s a large-scale multilingual speech corpus consisting of political data sourced from 2009-2020 European Parliament event recordings. The English subset contains approximately 550 hours of speech largely from non-native English speakers. It is licensed under CC0.

Example usage:

```python
voxpopuli = load_dataset("esc-benchmark/esc-datasets", "voxpopuli")
```

Training/validation splits:
- `train`
- `validation`

Test splits:
- `test`

## TED-LIUM
TED-LIUM consists of English-language TED Talk conference videos covering a range of different cultural, political, and academic topics. It contains approximately 450 hours of transcribed speech data. It is licensed under CC-BY-NC-ND 3.0.

Example usage:

```python
tedlium = load_dataset("esc-benchmark/esc-datasets", "tedlium")
```

Training/validation splits:
- `train`
- `validation`

Test splits:
- `test`

## GigaSpeech
GigaSpeech is a multi-domain English speech recognition corpus created from audiobooks, podcasts and YouTube. We provide the large train set (2,500 hours) and the standard validation and test splits. It is licensed under apache-2.0.

Example usage:

```python
gigaspeech = load_dataset("esc-benchmark/esc-datasets", "gigaspeech", use_auth_token=True)
```

Training/validation splits:
- `train` (`l` subset of training data (2,500 h))
- `validation`

Test splits:
- `test`

Also available are subsets of the train split, which can be accessed by setting the `subconfig` argument:
```python
gigaspeech = load_dataset("esc-benchmark/esc-datasets", "spgispeech", subconfig="xs", use_auth_token=True)
```
- `xs`: extra-small subset of training data (10 h)
- `s`: small subset of training data (250 h)
- `m`: medium subset of training data (1,000 h)
- `xl`: extra-large subset of training data (10,000 h)

## SPGISpeech
SPGISpeech consists of company earnings calls that have been manually transcribed by S&P Global, Inc according to a professional style guide. We provide the large train set (5,000 hours) and the standard validation and test splits. It is licensed under a Kensho user agreement.

Loading the dataset requires authorization.

Example usage:

```python
spgispeech = load_dataset("esc-benchmark/esc-datasets", "spgispeech", use_auth_token=True)
```

Training/validation splits:
- `train` (`l` subset of training data (~5,000 h))
- `validation`

Test splits:
- `test`

Also available are subsets of the train split, which can be accessed by setting the `subconfig` argument:
```python
spgispeech = load_dataset("esc-benchmark/esc-datasets", "spgispeech", subconfig="s", use_auth_token=True)
```
- `s`: small subset of training data (~200 h)
- `m`: medium subset of training data (~1,000 h)


## Earnings-22
Earnings-22 is a 119-hour corpus of English-language earnings calls collected from global companies, with speakers of many different nationalities and accents. It is licensed under CC-BY-SA-4.0. 

Example usage:

```python
earnings22 = load_dataset("esc-benchmark/esc-datasets", "earnings22")
```

Training/validation splits:
- `train`
- `validation`

Test splits:
- `test`

## AMI
The AMI Meeting Corpus consists of 100 hours of meeting recordings from multiple recording devices synced to a common timeline. It is licensed under CC-BY-4.0.

Example usage:

```python
ami = load_dataset("esc-benchmark/esc-datasets", "ami")
```

Training/validation splits:
- `train`
- `validation`

Test splits:
- `test`
