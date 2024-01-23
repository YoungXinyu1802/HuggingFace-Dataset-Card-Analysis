---
language:
- zh
multilinguality:
- monolingual
pretty_name: Genshin Voice
source_datasets:
- original
task_categories:
  - text-to-speech
  - automatic-speech-recognition
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: language
    dtype: string
  - name: npcName
    dtype: string
  - name: text
    dtype: string
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 36412736429.25
    num_examples: 75033
  download_size: 18251937481
  dataset_size: 36412736429.25
---
# Dataset Card for Genshin Voice

## Dataset Description

### Dataset Summary

The Genshin Voice dataset is a text-to-voice dataset of different Genshin Impact characters unpacked from the game.

### Languages

The text in the dataset is in Mandarin.

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The data was obtained by unpacking the [Genshin Impact](https://genshin.hoyoverse.com/) game.

#### Who are the source language producers?

The language producers are the employee of [Hoyoverse](https://hoyoverse.com/) and contractors from [EchoSky Studio](http://qx.asiacu.com/).

### Annotations

The dataset contains official annotations from the game, including ingame speaker name and transcripts.

## Additional Information

### Dataset Curators

The dataset was created by [w4123](https://github.com/w4123) initially in his [GitHub repository](https://github.com/w4123/GenshinVoice).

### Licensing Information

Copyright © COGNOSPHERE. All Rights Reserved.