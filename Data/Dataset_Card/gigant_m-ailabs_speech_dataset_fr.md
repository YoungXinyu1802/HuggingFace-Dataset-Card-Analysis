---
language:
- fr
license: cc
size_categories:
  fr:
  - 10K<n<100K
task_categories:
- automatic-speech-recognition
task_ids: []
pretty_name: M-AILABS Speech Dataset (French)
---

## Dataset Description
- **Homepage:** https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/

### Dataset Summary

The M-AILABS Speech Dataset is the first large dataset that we are providing free-of-charge, freely usable as training data for speech recognition and speech synthesis.

Most of the data is based on LibriVox and Project Gutenberg. The training data consist of nearly thousand hours of audio and the text-files in prepared format.

A transcription is provided for each clip. Clips vary in length from 1 to 20 seconds and have a total length of approximately shown in the list (and in the respective info.txt-files) below.


The texts were published between 1884 and 1964, and are in the public domain. The audio was recorded by the LibriVox project and is also in the public domain – except for Ukrainian.

Ukrainian audio was kindly provided either by Nash Format or Gwara Media for machine learning purposes only (please check the data info.txt files for details).


### Languages

French

## Dataset Structure
### Data Instances
A typical data point comprises the path to the audio file, called audio and its sentence.


### Data Fields

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- sentence: The sentence the user was prompted to speak

### Data Splits
The speech material has not been subdivided into portions, everything is in the "train" split.
The train split consists of 82825 audio clips and the related sentences.


### Contributions
[@gigant](https://huggingface.co/gigant) added this dataset.