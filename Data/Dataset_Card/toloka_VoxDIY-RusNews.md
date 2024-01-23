---
annotations_creators:
- found
language_creators:
- crowdsourced
language:
- ru
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
pretty_name: VoxDIY RusNews
language_bcp47:
- ru-RU
tags:
- conditional-text-generation
- stuctured-to-text
- speech-recognition
---

# Dataset Card for VoxDIY RusNews

## Dataset Description
- **Repository:** [GitHub](https://github.com/Toloka/CrowdSpeech)
- **Paper:** [Paper](https://openreview.net/forum?id=3_hgF1NAXU7)
- **Point of Contact:** research@toloka.ai

### Dataset Summary

VoxDIY RusNews is the first publicly available large-scale dataset of crowdsourced audio transcriptions in Russian language.
The dataset was constructed by annotating audio recordings of Russian sentences from news domain on [Toloka crowdsourcing platform](https://toloka.ai).
VoxDIY RusNews consists of 3091 instances having around 21K annotations obtained from crowd workers.

### Supported Tasks and Leaderboards
Aggregation of crowd transcriptions.

### Languages
Russian

## Dataset Structure

### Data Instances

A data instance contains a url to the audio recording, a list of transcriptions along with the corresponding performers identifiers and 
ground truth. For each data instance, seven crowdsourced transcriptions are provided.

```
{'task': 'https://tlk.s3.yandex.net/annotation_tasks/russian/1003.wav',
 'transcriptions': 'в список так же попали мэрлин монро джон ленон и альберт эйнштейн | в список также попали мерлин монро джон ленон и альберт энштейн | в список также попали мерилин монро джон леннон и альберт энтштейн | в список также попали мэрилин монро джон леннон и альберт эпштейн | в список также попали мэрилин монро джон леннон и альберт эйнштейн | в список так же попали мерелин монро джон ленон и альберт нштейн | в список также попали мэрилин монро джон леннон и альберт эйнштейн',
 'performers': '1743 | 784 | 1014 | 1572 | 744 | 2187 | 1208',
 'gt': 'в список также попали мэрилин монро джон леннон и альберт эйнштейн'}
```

### Data Fields

* task: a string containing a url of the audio recording
* transcriptions: a list of the crowdsourced transcriptions separated by '|'
* performers: the corresponding performers' identifiers.
* gt: ground truth transcription

## Dataset Creation

### Source Data

The audio recordings were obtained using a [speech synthesis tool](https://cloud.yandex.com/en-ru/services/speechkit).
The source sentences come from the Russian test set of the machine translation shared task executed as a part of the 
Eights and Ninth Workshops on Statistical Machine Translation ([WMT 2013](https://www.statmt.org/wmt13/) and [WMT 2014](https://www.statmt.org/wmt14/)).

### Annotations

Annotation was done on [Toloka crowdsourcing platform](https://toloka.ai) with overlap of 7 (that is, each task was performed by 7 annotators).

Only annotators who self-reported the knowledge of Russian had access to the annotation task.
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