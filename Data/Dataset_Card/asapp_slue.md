---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- cc0-1.0
- cc-by-4.0
multilinguality:
- monolingual
paperswithcode_id: slue
pretty_name: SLUE (Spoken Language Understanding Evaluation benchmark)
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- automatic-speech-recognition
- audio-classification
- text-classification
- token-classification
task_ids:
- sentiment-analysis
- named-entity-recognition
configs:
- voxpopuli
- voxceleb
---

# Dataset Card for SLUE

## Table of Contents
- [Dataset Card for SLUE](#dataset-card-for-slue)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
      - [Automatic Speech Recognition (ASR)](#automatic-speech-recognition-asr)
      - [Named Entity Recognition (NER)](#named-entity-recognition-ner)
      - [Sentiment Analysis (SA)](#sentiment-analysis-sa)
      - [How-to-submit for your test set evaluation](#how-to-submit-for-your-test-set-evaluation)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
      - [voxpopuli](#voxpopuli)
      - [voxceleb](#voxceleb)
    - [Data Fields](#data-fields)
      - [voxpopuli](#voxpopuli-1)
      - [voxceleb](#voxceleb-1)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
      - [SLUE-VoxPopuli Dataset](#slue-voxpopuli-dataset)
      - [SLUE-VoxCeleb Dataset](#slue-voxceleb-dataset)
        - [Original License of OXFORD VGG VoxCeleb Dataset](#original-license-of-oxford-vgg-voxceleb-dataset)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://asappresearch.github.io/slue-toolkit](https://asappresearch.github.io/slue-toolkit)
- **Repository:** [https://github.com/asappresearch/slue-toolkit/](https://github.com/asappresearch/slue-toolkit/)
- **Paper:** [https://arxiv.org/pdf/2111.10367.pdf](https://arxiv.org/pdf/2111.10367.pdf)
- **Leaderboard:** [https://asappresearch.github.io/slue-toolkit/leaderboard_v0.2.html](https://asappresearch.github.io/slue-toolkit/leaderboard_v0.2.html)
- **Size of downloaded dataset files:** 1.95 GB
- **Size of the generated dataset:** 9.59 MB
- **Total amount of disk used:** 1.95 GB

### Dataset Summary

We introduce the Spoken Language Understanding Evaluation (SLUE) benchmark. The goals of our work are to
- Track research progress on multiple SLU tasks
- Facilitate the development of pre-trained representations by providing fine-tuning and eval sets for a variety of SLU tasks
- Foster the open exchange of research by focusing on freely available datasets that all academic and industrial groups can easily use.

For this benchmark, we provide new annotation of publicly available, natural speech data for training and evaluation. We also provide a benchmark suite including code to download and pre-process the SLUE datasets, train the baseline models, and evaluate performance on SLUE tasks. Refer to [Toolkit](https://github.com/asappresearch/slue-toolkit) and [Paper](https://arxiv.org/pdf/2111.10367.pdf) for more details.

### Supported Tasks and Leaderboards

#### Automatic Speech Recognition (ASR)

Although this is not a SLU task, ASR can help analyze the performance of downstream SLU tasks on the same domain. Additionally, pipeline approaches depend on ASR outputs, making ASR relevant to SLU. ASR is evaluated using word error rate (WER).

#### Named Entity Recognition (NER)

Named entity recognition involves detecting the named entities and their tags (types) in a given sentence. We evaluate performance using micro-averaged F1 and label-F1 scores. The F1 score evaluates an unordered list of named entity phrase and tag pairs predicted for each sentence. Only the tag predictions are considered for label-F1.

#### Sentiment Analysis (SA)

Sentiment analysis refers to classifying a given speech segment as having negative, neutral, or positive sentiment. We evaluate SA using  macro-averaged (unweighted) recall and F1 scores.[More Information Needed]

#### How-to-submit for your test set evaluation

See here https://asappresearch.github.io/slue-toolkit/how-to-submit.html

### Languages

The language data in SLUE is in English.

## Dataset Structure

### Data Instances

#### voxpopuli
- **Size of downloaded dataset files:** 398.45 MB
- **Size of the generated dataset:** 5.81 MB
- **Total amount of disk used:** 404.26 MB
An example of 'train' looks as follows.
```
{'id': '20131007-0900-PLENARY-19-en_20131007-21:26:04_3',
 'audio': {'path': '/Users/username/.cache/huggingface/datasets/downloads/extracted/e35757b0971ac7ff5e2fcdc301bba0364857044be55481656e2ade6f7e1fd372/slue-voxpopuli/fine-tune/20131007-0900-PLENARY-19-en_20131007-21:26:04_3.ogg',
  'array': array([ 0.00132601,  0.00058881, -0.00052187, ...,  0.06857217,
          0.07835515,  0.07845446], dtype=float32),
  'sampling_rate': 16000},
 'speaker_id': 'None',
 'normalized_text': 'two thousand and twelve for instance the new brussels i regulation provides for the right for employees to sue several employers together and the right for employees to have access to courts in europe even if the employer is domiciled outside europe. the commission will',
 'raw_text': '2012. For instance, the new Brussels I Regulation provides for the right for employees to sue several employers together and the right for employees to have access to courts in Europe, even if the employer is domiciled outside Europe. The Commission will',
 'raw_ner': {'type': ['LOC', 'LOC', 'LAW', 'DATE'],
  'start': [227, 177, 28, 0],
  'length': [6, 6, 21, 4]},
 'normalized_ner': {'type': ['LOC', 'LOC', 'LAW', 'DATE'],
  'start': [243, 194, 45, 0],
  'length': [6, 6, 21, 23]},
 'raw_combined_ner': {'type': ['PLACE', 'PLACE', 'LAW', 'WHEN'],
  'start': [227, 177, 28, 0],
  'length': [6, 6, 21, 4]},
 'normalized_combined_ner': {'type': ['PLACE', 'PLACE', 'LAW', 'WHEN'],
  'start': [243, 194, 45, 0],
  'length': [6, 6, 21, 23]}}
```

#### voxceleb
- **Size of downloaded dataset files:** 1.55 GB
- **Size of the generated dataset:** 3.78 MB
- **Total amount of disk used:** 1.55 GB
An example of 'train' looks as follows.
```
{'id': 'id10059_229vKIGbxrI_00004',
 'audio': {'path': '/Users/felixwu/.cache/huggingface/datasets/downloads/extracted/400facb6d2f2496ebcd58a5ffe5fbf2798f363d1b719b888d28a29b872751626/slue-voxceleb/fine-tune_raw/id10059_229vKIGbxrI_00004.flac',
  'array': array([-0.00442505, -0.00204468,  0.00628662, ...,  0.00158691,
          0.00100708,  0.00033569], dtype=float32),
  'sampling_rate': 16000},
 'speaker_id': 'id10059',
 'normalized_text': 'of god what is a creator the almighty that uh',
 'sentiment': 'Neutral',
 'start_second': 0.45,
 'end_second': 4.52}
```


### Data Fields

#### voxpopuli
- `id`: a `string` id of an instance.
- `audio`: audio feature of the raw audio. It is a dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- `speaker_id`: a `string` of the speaker id.
- `raw_text`: a `string` feature that contains the raw transcription of the audio.
- `normalized_text`: a `string` feature that contains the normalized transcription of the audio which is **used in the standard evaluation**.
- `raw_ner`: the NER annotation of the `raw_text` using the same 18 NER classes as OntoNotes.
- `normalized_ner`: the NER annotation of the `normalized_text` using the same 18 NER classes as OntoNotes.
- `raw_combined_ner`: the NER annotation of the `raw_text` using our 7 NER classes (`WHEN`, `QUANT`, `PLACE`, `NORP`, `ORG`, `LAW`, `PERSON`).
- `normalized_combined_ner`: the NER annotation of the `normalized_text` using our 7 NER classes (`WHEN`, `QUANT`, `PLACE`, `NORP`, `ORG`, `LAW`, `PERSON`) which is **used in the standard evaluation**.
Each NER annotation is a dictionary containing three lists: `type`, `start`, and `length`. `type` is a list of the NER tag types. `start` is a list of the start character position of each named entity in the corresponding text. `length` is a list of the number of characters of each named entity.


#### voxceleb
- `id`: a `string` id of an instance.
- `audio`: audio feature of the raw audio. Please use `start_second` and `end_second` to crop the transcribed segment. For example, `dataset[0]["audio"]["array"][int(dataset[0]["start_second"] * dataset[0]["audio"]["sample_rate"]):int(dataset[0]["end_second"] * dataset[0]["audio"]["sample_rate"])]`. It is a dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- `speaker_id`: a `string` of the speaker id.
- `normalized_text`: a `string` feature that contains the transcription of the audio segment.
- `sentiment`: a `string` feature which can be `Negative`, `Neutral`, or `Positive`.
- `start_second`: a `float` feature that specifies the start second of the audio segment.
- `end_second`: a `float` feature that specifies the end second of the audio segment.

### Data Splits

|         |train|validation|test|
|---------|----:|---------:|---:|
|voxpopuli| 5000|      1753|1842|
|voxceleb | 5777|      1454|3553|
Here we use the standard split names in Huggingface's datasets, so the `train` and `validation` splits are the original `fine-tune` and `dev` splits of SLUE datasets, respectively.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

#### SLUE-VoxPopuli Dataset

SLUE-VoxPopuli dataset contains a subset of VoxPopuli dataset and the copyright of this subset remains the same with the original license, CC0. See also European Parliament's legal notice (https://www.europarl.europa.eu/legal-notice/en/)

Additionally, we provide named entity annotation (normalized_ner and raw_ner column in .tsv files) and it is covered with the same license as CC0.

#### SLUE-VoxCeleb Dataset

SLUE-VoxCeleb Dataset contains a subset of OXFORD VoxCeleb dataset and the copyright of this subset remains the same Creative Commons Attribution 4.0 International license as below. Additionally, we provide transcription, sentiment annotation and timestamp (start, end) that follows the same license to OXFORD VoxCeleb dataset.

##### Original License of OXFORD VGG VoxCeleb Dataset 

VoxCeleb1 contains over 100,000 utterances for 1,251 celebrities, extracted from videos uploaded to YouTube.  
VoxCeleb2 contains over a million utterances for 6,112 celebrities, extracted from videos uploaded to YouTube. 

The speakers span a wide range of different ethnicities, accents, professions and ages. 

We provide Youtube URLs, associated face detections, and timestamps, as
well as cropped audio segments and cropped face videos from the
dataset.  The copyright of both the original and cropped versions
of the videos remains with the original owners.

The data is covered under a Creative Commons
Attribution 4.0 International license (Please read the
license terms here. https://creativecommons.org/licenses/by/4.0/).

Downloading this dataset implies agreement to follow the same
conditions for any modification and/or
re-distribution of the dataset in any form.


Additionally any entity using this dataset agrees to the following conditions:

THIS DATASET IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Please cite [1,2] below if you make use of the dataset.

[1] J. S. Chung, A. Nagrani, A. Zisserman  
VoxCeleb2: Deep Speaker Recognition  
INTERSPEECH, 2018.

[2] A. Nagrani, J. S. Chung, A. Zisserman
VoxCeleb: a large-scale speaker identification dataset  
INTERSPEECH, 2017

### Citation Information

```
@inproceedings{shon2022slue,
  title={Slue: New benchmark tasks for spoken language understanding evaluation on natural speech},
  author={Shon, Suwon and Pasad, Ankita and Wu, Felix and Brusco, Pablo and Artzi, Yoav and Livescu, Karen and Han, Kyu J},
  booktitle={ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={7927--7931},
  year={2022},
  organization={IEEE}
}
```

### Contributions

Thanks to [@fwu-asapp](https://github.com/fwu-asapp) for adding this dataset.