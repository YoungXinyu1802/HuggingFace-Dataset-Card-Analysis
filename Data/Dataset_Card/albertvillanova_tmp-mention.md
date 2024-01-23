---
license: cc-by-4.0
tags:
- zenodo
---

# Dataset Card for MultiLingual LibriSpeech

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

- **Homepage:** [MultiLingual LibriSpeech ASR corpus](http://www.openslr.org/94)
- **Repository:** [Needs More Information]
- **Paper:** [MLS: A Large-Scale Multilingual Dataset for Speech Research](https://arxiv.org/abs/2012.03411)
- **Leaderboard:** [Paperswithcode Leaderboard](https://paperswithcode.com/dataset/multilingual-librispeech)

### Dataset Summary

<div class="course-tip course-tip-orange bg-gradient-to-br dark:bg-gradient-to-r before:border-orange-500 dark:before:border-orange-800 from-orange-50 dark:from-gray-900 to-white dark:to-gray-950 border border-orange-50 text-orange-700 dark:text-gray-400"><p><b>Deprecated:</b> Not every model supports a fast tokenizer. Take a look at this <a href="index#supported-frameworks">table</a> to check if a model has fast tokenizer support.</p></div>

Multilingual LibriSpeech (MLS) dataset is a large multilingual corpus suitable for speech research. The dataset is derived from read audiobooks from LibriVox and consists of 8 languages - English, German, Dutch, Spanish, French, Italian, Portuguese, Polish.

### Supported Tasks and Leaderboards

- `automatic-speech-recognition`, `audio-speaker-identification`: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER). The task has an active leaderboard which can be found at https://paperswithcode.com/dataset/multilingual-librispeech and ranks models based on their WER.


<div class="course-tip course-tip-orange bg-gradient-to-br dark:bg-gradient-to-r before:border-orange-500 dark:before:border-orange-800 from-orange-50 dark:from-gray-900 to-white dark:to-gray-950 border border-orange-50 text-orange-700 dark:text-gray-400"><p><b>Deprecated:</b> Not every model supports a fast tokenizer. Take a look at this <a href="index#supported-frameworks">table</a> to check if a model has fast tokenizer support.</p></div>


<div class="alert alert-danger d-flex align-items-center" role="alert">
  <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
  <div>
    An example danger alert with an icon
  </div>
</div>

<div class="alert alert-block alert-warning"> ⚠ In general, just avoid the red boxes. </div>
<div class="alert alert-block alert-danger"> In general, just avoid the red boxes. </div>
<div class="alert alert-danger" role="alert"> In general, just avoid the red boxes. </div>
<div class="alert" role="alert"> In general, just avoid the red boxes. </div>

<div class="course-tip-orange">
<strong>Error:</strong>
</div>

<div class="alert alert-danger" role="alert">
    <div class="row vertical-align">
        <div class="col-xs-1 text-center">
            <i class="fa fa-exclamation-triangle fa-2x"></i>
        </div>
        <div class="col-xs-11">
                <strong>Error:</strong>                   
        </div>   
    </div> 
</div>

>[!WARNING]
>This is a warning

_**Warning:** Be very careful here._

<Deprecated>
This is a warning
</Deprecated>

<Tip warning>
This is a warning
</Tip>

<Tip warning={true}>
This is a warning
</Tip>


> **Warning**
> This is a warning