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
pretty_name: African Accented French
---

## Dataset Description
- **Homepage:** http://www.openslr.org/57/

### Dataset Summary

This corpus consists of approximately 22 hours of speech recordings. Transcripts are provided for all the recordings. The corpus can be divided into 3 parts:

1. Yaounde

Collected by a team from the U.S. Military Academy's Center for Technology Enhanced Language Learning (CTELL) in 2003 in Yaoundé, Cameroon. It has recordings from 84 speakers, 48 male and 36 female.

2. CA16

This part was collected by a RDECOM Science Team who participated in the United Nations exercise Central Accord 16 (CA16) in Libreville, Gabon in June 2016. The Science Team included DARPA's Dr. Boyan Onyshkevich and Dr. Aaron Lawson (SRI International), as well as RDECOM scientists. It has recordings from 125 speakers from Cameroon, Chad, Congo and Gabon.

3. Niger

This part was collected from 23 speakers in Niamey, Niger, Oct. 26-30 2015. These speakers were students in a course for officers and sergeants presented by Army trainers assigned to U.S. Army Africa. The data was collected by RDECOM Science & Technology Advisors Major Eddie Strimel and Mr. Bill Bergen.

### Languages

French

## Dataset Structure
### Data Instances
A typical data point comprises the path to the audio file, called audio and its sentence.


### Data Fields

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- sentence: The sentence the user was prompted to speak

### Data Splits
The speech material has been subdivided into portions for train and test.
The train split consists of 9401 audio clips and the related sentences.
The test split consists of 1985 audio clips and the related sentences.


### Contributions
[@gigant](https://huggingface.co/gigant) added this dataset.