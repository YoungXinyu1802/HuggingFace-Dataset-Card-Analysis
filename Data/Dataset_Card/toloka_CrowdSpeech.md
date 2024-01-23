---
annotations_creators:
- found
language_creators:
- crowdsourced
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
- automatic-speech-recognition
- text2text-generation
task_ids: []
paperswithcode_id: crowdspeech
pretty_name: CrowdSpeech
language_bcp47:
- en-US
tags:
- conditional-text-generation
- stuctured-to-text
- speech-recognition
---

# Dataset Card for CrowdSpeech

## Dataset Description
- **Repository:** [GitHub](https://github.com/Toloka/CrowdSpeech)
- **Paper:** [Paper](https://openreview.net/forum?id=3_hgF1NAXU7)
- **Point of Contact:** research@toloka.ai

### Dataset Summary

CrowdSpeech is the first publicly available large-scale dataset of crowdsourced audio transcriptions.
The dataset was constructed by annotation [LibriSpeech](https://www.openslr.org/12) on [Toloka crowdsourcing platform](https://toloka.ai).
CrowdSpeech consists of 22K instances having around 155K annotations obtained from crowd workers.


### Supported Tasks and Leaderboards
Aggregation of crowd transcriptions.

### Languages
English

## Dataset Structure

### Data Instances

A data instance contains a url to the audio recording, a list of transcriptions along with the corresponding performers identifiers and ground truth.
For each data instance, seven crowdsourced transcriptions are provided.

```
{'task': 'https://tlk.s3.yandex.net/annotation_tasks/librispeech/train-clean/0.mp3',
 'transcriptions': "had laid before her a pair of alternatives now of course you're completely your own mistress and are as free as the bird on the bough i don't mean you were not so before but you're at present on a different footing | had laid before her a pair of alternatives now of course you are completely your own mistress and are as free as the bird on the bowl i don't mean you were not so before but you were present on a different footing | had laid before her a pair of alternatives now of course you're completely your own mistress and are as free as the bird on the bow i don't mean you are not so before but you're at present on a different footing | had laid before her a pair of alternatives now of course you're completely your own mistress and are as free as the bird on the bow i don't mean you are not so before but you're at present on a different footing | laid before her a pair of alternativesnow of course you're completely your own mistress and are as free as the bird on the bow i don't mean you're not so before but you're at present on a different footing | had laid before her a peril alternatives now of course your completely your own mistress and as free as a bird as the back bowl i don't mean you were not so before but you are present on a different footing | a lady before her a pair of alternatives now of course you're completely your own mistress and rs free as the bird on the ball i don't need you or not so before but you're at present on a different footing",
 'performers': '1154 | 3449 | 3097 | 461 | 3519 | 920 | 3660',
 'gt': "had laid before her a pair of alternatives now of course you're completely your own mistress and are as free as the bird on the bough i don't mean you were not so before but you're at present on a different footing"}
```

### Data Fields

* task: a string containing a url of the audio recording
* transcriptions: a list of the crowdsourced transcriptions separated by '|'
* performers: the corresponding performers' identifiers.
* gt: ground truth transcription

### Data Splits

There are five splits in the data: train, test, test.other, dev.clean and dev.other.
Splits train, test and dev.clean correspond to *clean* part of LibriSpeech that contains audio recordings of higher quality with accents 
of the speaker being closer to the US English. Splits dev.other and test.other correspond to *other* part of LibriSpeech with 
the recordings more challenging for recognition. The audio recordings are gender-balanced.

## Dataset Creation

### Source Data

[LibriSpeech](https://www.openslr.org/12) is a corpus of approximately 1000 hours of 16kHz read English speech.

### Annotations

Annotation was done on [Toloka crowdsourcing platform](https://toloka.ai) with overlap of 7 (that is, each task was performed by 7 annotators).

Only annotators who self-reported the knowledge of English had access to the annotation task.
Additionally, annotators had to pass *Entrance Exam*. For this, we ask all incoming eligible workers to annotate ten audio
recordings. We then compute our target metric — Word Error Rate (WER) — on these recordings and accept to the main task all workers 
who achieve WER of 40% or less (the smaller the value of the metric, the higher the quality of annotation).

The Toloka crowdsourcing platform associates workers with unique identifiers and returns these identifiers to the requester. 
To further protect the data, we additionally encode each identifier with an integer that is eventually reported in our released datasets.

See more details in the [paper](https://arxiv.org/pdf/2107.01091.pdf).

### Citation Information

```
@inproceedings{CrowdSpeech,
  author    = {Pavlichenko, Nikita and Stelmakh, Ivan and Ustalov, Dmitry},
  title     = {{CrowdSpeech and Vox~DIY: Benchmark Dataset for Crowdsourced Audio Transcription}},
  year      = {2021},
  booktitle = {Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks},
  eprint    = {2107.01091},
  eprinttype = {arxiv},
  eprintclass = {cs.SD},
  url       = {https://openreview.net/forum?id=3_hgF1NAXU7},
  language  = {english},
  pubstate  = {forthcoming},
}
```