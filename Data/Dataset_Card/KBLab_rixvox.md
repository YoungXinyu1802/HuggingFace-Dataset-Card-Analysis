---
language: sv
license: cc-by-4.0
tags: 
- audio
- speech-recognition
task_categories:
  - automatic-speech-recognition
size_categories:
  - 100K<n<1M
multilinguality:
  - monolingual
---

# Dataset Card for RixVox

## Dataset Description

- **Repository:** [Riksdagen anföranden repository](https://github.com/kb-labb/riksdagen_anforanden)
- **Paper:** ["RixVox: A Swedish Speech Corpus with 5500 Hours of Speech from Parliamentary Debates"](https://kb-labb.github.io/posts/2023-03-09-rixvox-a-swedish-speech-corpus/)
- **Point of Contact:** [KBLab](mailto:kblabb@kb.se)
- **Total amount of disk used:** ca. 1.2 TB

### Dataset Summary

RixVox is a speech dataset comprised of speeches from the Riksdag (the Swedish Parliament). It covers speeches from debates during the period 2003-2023. Audio from speeches have been aligned, on the sentence level, with transcripts from written protocols using `aeneas`. An observation may consist of one or several concatenated sentences (up to 30 seconds in duration). Detailed speaker metadata is available for each observation, including the speaker's name, gender, political party, birth year and the electoral district they represent. The dataset contains a total of 5493 hours of speech with transcriptions.

## How to use & Supported Tasks

### Supported Tasks

Tasks are not supported by default (there are no label fields). The dataset may however be suited for:

- Automatic Speech Recognition (ASR).
- Speaker identification and verification.
- Creation of synthetic diarization datasets. 
- Research on bias in ASR systems.

### How to use

To download and extract the files locally you can use `load_dataset()`. We recommend you set the `cache_folder` argument to point to a location that has plenty of disk space (1.2TB+). Here's how to download the `train` split: 

```python
from datasets import load_dataset
# To download/load all splits at once, don't specify a split
rixvox = load_dataset("KBLab/rixvox", split="train", cache_folder="data_rixvox")
```

You can also stream the dataset. This is useful if you want to explore the dataset or if you don't have enough disk space to download the entire dataset. Here's how to stream the `train` split:

```python
from datasets import load_dataset
rixvox = load_dataset("KBLab/rixvox", cache_dir="data_rixvox", split="train", streaming=True)
print(next(iter(rixvox)))

# Grab 5 observations
rixvox_subset = rixvox.take(5)
for example in rixvox_subset:
    print(example)
```

**Create a [PyTorch dataloader](https://huggingface.co/docs/datasets/use_with_pytorch)** with your dataset.

Local mode:

```python
from datasets import load_dataset
from torch.utils.data.sampler import BatchSampler, RandomSampler
# Dataset is not pre-shuffled, recommend shuffling it before training.
rixvox = load_dataset("KBLab/rixvox", split="train", cache_folder="data_rixvox")
batch_sampler = BatchSampler(RandomSampler(rixvox), batch_size=32, drop_last=False)
dataloader = DataLoader(rixvox, batch_sampler=batch_sampler)
```

Streaming mode:

```python
from datasets import load_dataset
from torch.utils.data import DataLoader
rixvox = load_dataset("KBLab/rixvox", split="train", cache_folder="data_rixvox")
dataloader = DataLoader(rixvox, batch_size=32)
```

See Huggingface's guide on [streaming datasets](https://huggingface.co/docs/datasets/v1.11.0/dataset_streaming.html) for more information on how to shuffle in streaming mode. 

### Languages

- Swedish. The BCP 47 language tag for Swedish is `sv`.

## Dataset Structure

### Data Instances

There are a total of `835044` observations from `1194` different speakers. Each observation can be up to 30 seconds in duration. An observation belongs to a debate (`dokid`), is extratected from a speech (`anforande_nummer`), and is numbered according to its order within the speech (`observation_nr`). Here is an example of an observation:

```
{'dokid': 'GR01BOU3',
 'anforande_nummer': 191,
 'observation_nr': 0,
 'audio': {'path': 'GR01BOU3/2442210220028601121_anf191_1_25.wav',
           'array': array([0.01171875, 0.01242065, 0.01071167, ..., 0.00689697, 0.00918579,
       0.00650024]),
           'sampling_rate': 16000},
 'text': 'Kristdemokraterna står bakom alla reservationer med kristdemokratiska förtecken, men jag nöjer mig med att yrka bifall till reservation 1. Jag ska i det här inlägget beröra några av de åtta punkter som är föremål för reservationer från kristdemokratiskt håll, i vissa fall tillsammans med andra partier.',
 'debatedate': datetime.datetime(2003, 12, 4, 0, 0),
 'speaker': 'Göran Hägglund',
 'party': 'KD',
 'gender': 'male',
 'birth_year': 1959,
 'electoral_district': 'Hallands län',
 'intressent_id': '0584659199514',
 'speaker_from_id': True,
 'speaker_audio_meta': 'Göran Hägglund (Kd)',
 'start': 1.4,
 'end': 24.96,
 'duration': 23.560000000000002,
 'bleu_score': 0.7212783273624307,
 'filename': 'GR01BOU3/2442210220028601121_anf191_1_25.wav',
 'path': 'GR01BOU3/2442210220028601121_anf191_1_25.wav',
 'speaker_total_hours': 30.621333333333332}
```

See more examples in the [dataset viewer](https://huggingface.co/datasets/KBLab/rixvox/viewer/default/train).

### Data Fields

* `dokid`: Document id for the debate used by the Riksdag. This is the same for all speeches in a debate.
* `anforande_nummer`: Speech number within the debate, or within the debate sessions on a particular day. Should create a unique primary key for a speech in combination with `dokid` (sometimes there are duplicates, but we removed them from this dataset).
* `observation_nr`: Observation number within the speech. Creates a unique identifier for an observation in combination with `dokid` and `anforande_nummer`.
* `text`: The text transcript from written protocols. The transcripts are not always verbatim. Transcribers have to different degrees adjusted sentence ordering, words and phrasing when they deemed it appropriate. 
* `debatedate`: The date of the debate.
* `start`: The start time of the observation within a speech (in seconds).
* `end`: The end time of the observation within a speech (in seconds).
* `duration`: The duration of the observation (`end` subtracted with `start`).
* `intressent_id`: Unique id for the speaker within the Riksdag's database (see [person.csv.zip](https://data.riksdagen.se/dataset/person/person.csv.zip) from the Riksdag).
* `speaker`: The speaker's name retrieved via the `intressent_id`. 
* `party`: The speaker's party retrieved via the `intressent_id`.
* `gender`: The speaker's gender retrieved via the `intressent_id`.
* `birth_year`: The speaker's bith year retrieved via the `intressent_id`.
* `electoral_district`: The electoral district which the speaker represents if they are/were a member of parliament (retrieved via the `intressent_id`).
* `speaker_audio_meta`: The speaker's name and title as listed in the Riksdag's oroginal text format metadata (sometimes wrong and mismatched against `intressent_id`).
* `speaker_from_id`: Whether the speaker metadata was retrieved via the `intressent_id` or via the Riksdag's original metadata (for those speeches with a missing `intressent_id`).
* `bleu_score`: The BLEU score of the automatic speech recognition (ASR) transcript against the Riksdag's written protocol. Calculated on the entirity of the speech that an observation (30s snippet) is extracted from. A low number for a speech may indicate that either i) the ASR model had trouble transcribing the speaker's accent or dialect, or ii) the transcription took certain liberties in editing and rephrasing the speech. 
* `speaker_total_hours`: The total number of hours of speech from the speaker in the RixVox dataset.
* `filename`: The filename of the observation in the compressed tar.gz files. Useful if you don't want to use Huggingface `datasets`, but would rather manually download and extract the files from the data shards. 
* `path`: Dynamically created variable. Contains the local path to the observation's audio file after you download and extract the files via `load_dataset()` in the `datasets` library.

### Data Splits

Dataset splits were randomly sampled on the speaker level. That is, a speaker is only present in a single split. We sample speakers for each split until the following conditions are met:

- 98% of the total number of hours of speech are included in the train split.
- 1% of the total number of hours of speech are included in the validation split.
- 1% of the total number of hours of speech are included in the test split.

| Dataset Split | Observations      | Total duration of speech (hours) | Average duration obs. (seconds) | Number of speakers |
| ------------- | ----------------: | -------------------------------: | ------------------------------: | -----------------: |
| Train         | 818227            | 5383                             | 23.69                           | 1165               |
| Validation    | 7933              | 52                               | 23.50                           | 18                 |
| Test          | 8884              | 59                               | 23.74                           | 11                 |


## Dataset Creation

For more information about the creation of this dataset, see the article ["Finding Speeches in the Riksdag's Debates"](https://kb-labb.github.io/posts/2023-02-15-finding-speeches-in-the-riksdags-debates/) from our blog. 

### Curation Rationale

Before RixVox, there was only a couple of hundred hours of transcribed speech available to train ASR models for Swedish. ASR models such as Whisper have shown that the performance of models can benefit significantly from adding more supervised data during pretraining or finetuning. Media from debates in the Riksdag are published openly on the web together with transcripts and other metadata. The open data initiatives of the Riksdag presented an opportunity to create a high quality open speech corpus for Swedish.

### Source Data

The Swedish Parliament. 

- [Transcripts of speeches](https://data.riksdagen.se/data/anforanden/).
- Use the `rel_dok_id` of transcripts of speeches to query the Riksdag's media API (e.g. https://data.riksdagen.se/api/mhs-vodapi?H901FiU1 ) for available media and metadata.

#### Initial Data Collection and Normalization

For information on how the speeches were segmented and identified in debate audio files, see the article ["Finding Speeches in the Riksdag's Debates"](https://kb-labb.github.io/posts/2023-02-15-finding-speeches-in-the-riksdags-debates/). 

For information on how the speech segmentations were used to create the final RixVox dataset, see the article ["RixVox: A Swedish Speech Corpus with 5500 Hours of Speech from Parliamentary Debates"](https://kb-labb.github.io/posts/2023-03-09-rixvox-a-swedish-speech-corpus/).

The code to replicate the creation of the dataset is open and available at the GitHub repository [KBLab/riksdagen_anforanden](https://github.com/kb-labb/riksdagen_anforanden). Processing everything can take 1-3 weeks on a workstation with consumer grade GPU. 

#### Who are the source language producers?

The written protocols of speeches are manually produced by the Riksdag. Transcription is not always verbatim, but rather catches the intent of the speaker.

Segmenting speeches to determine when they start and end in a debate was done automatically. Sentence level alignment of the written protocols to the audio files was also done automatically using `aeneas`. See the articles in citation information for more details. 

### Annotations

#### Annotation process

The process of aligning speech to written protocols was automatic. It followed the following general steps:

1. We used ASR to automatically transcribe the debate audio files and get word timestamps for the machine generated transcription.
2. We used fuzzy string matching to determine approximate start/end of a speech, matching the official written protocol of the speech to the machine generated transcription of the debate.
3. We perform speaker diarization using pyannote.audio.
4. We assign speaker diarization segments to speeches by the degree of overlap between approximate start/end from fuzzy string matching and the speaker diarization segments. The start and end of the diarization segment is used as our new adjusted start and end metadata of the speech.
5. Based on adjusted metadata of start/end of as speech, we split and extract the audio of speeches from the debates and then align the segmented speeches to the written protocol using `aeneas` (sentence-level alignment).

#### Who are the annotators?

No manual annotations.

### Personal and Sensitive Information

The speakers are members of parliament or ministers speaking publicly in the Riksdag. The Riksdag is a public institution and the speeches are publicly available on the web as open data.

## Considerations for Using the Data

### Social Impact of Dataset

We except the dataset primarily to be used in training ASR models for Swedish. The performance of Swedish text-to-speech in multillingual ASR models may also benefit from the availability of a large Swedish speech corpus. In turn, improved ASR models can serve to help increase accessibility of audio and video media content for people with hearing impairments.

The dataset can also be used to train models for other audio tasks such as speaker diarization, speaker verification, and speaker recognition. 

Since metadata regarding the age, gender, and electoral district of the speaker is included, the dataset can possibly also be used to study bias in ASR models.

### Discussion of Biases

The dataset includes parliamentary speeches, which are often more formal than everyday speech. 

During the creation of the dataset, we found that speech segmentations based on speaker diarization were more likely to fail when a preceding speaker, the speaker of the house, and the speaker of the following speech were all of the same gender. However, all in all, only a small number of speeches were filtered out of the final RixVox dataset. After quality filtering of the dataset, 5500 out of 5858 hours remained. We do not believe any significant systematic bias was introduced by this filtering.

Only minimal deduplication was performed to weed out commonly repeated phrases. For example, certain phrases such as "Fru talman!", "Herr Talman!", tend to be used a lot as a matter of formality. These phrases tend to be present at the beginning of most transcripts regardless whether it was uttered by the speaker or not. For this reason we have removed the first aligned sentence of each speech when creating RixVox. The aforementioned phrases are repeated frequently in speeches as well, though. As such it might be beneficial to perform more aggressive deduplication of the dataset before training models.

### Other Known Limitations

## Additional Information

### Dataset Curators

KBLab at the the National Library of Sweden. 

### Future updates

There is a possiblity RixVox will be periodically, and irregularly, updated by including both older and newer speeches. Older recordings of parliamentary debates from 1966 to 2002 do exist, but they are not yet part of the Riksdag's open data. KBLab are exploring the possibility of adding metadata to these recordings by applying the existing speech segmentation and alignment pipeline to them. 

Each year also brings new parliamentary debates, with recent years adding 400-500 hours of speech per year.

### Licensing Information

[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

Cite the Swedish Parliament and below articles as sources.

### Citation Information

```
@misc{rekathati2023rixvox:,
  author = {Rekathati, Faton},
  title = {The KBLab Blog: RixVox: A Swedish Speech Corpus with 5500 Hours of Speech from Parliamentary Debates},
  url = {https://kb-labb.github.io/posts/2023-03-09-rixvox-a-swedish-speech-corpus/},
  year = {2023}
}
```

```
@misc{rekathati2023finding,
  author = {Rekathati, Faton},
  title = {The KBLab Blog: Finding Speeches in the Riksdag's Debates},
  url = {https://kb-labb.github.io/posts/2023-02-15-finding-speeches-in-the-riksdags-debates/},
  year = {2023}
}
```

The Swedish Parliament.

### Contributions

Thanks to [@lhoestq](https://huggingface.co/lhoestq) for reviewing the dataset script.