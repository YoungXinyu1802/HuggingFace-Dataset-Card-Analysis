---
language:
- ro
license:
- unknown
size_categories:
  ro:
  - 1K<n<10K
task_categories:
- automatic-speech-recognition
task_ids: []
pretty_name: Romanian Speech Synthesis
---

## Dataset Description
- **Homepage:** https://romaniantts.com/rssdb/
- **Paper:** https://www.sciencedirect.com/science/article/abs/pii/S0167639310002074

### Dataset Summary

The Romanian speech synthesis (RSS) corpus was recorded in a hemianechoic chamber (anechoic walls and ceiling; floor partially anechoic) at the University of Edinburgh. We used three high quality studio microphones: a Neumann u89i (large diaphragm condenser), a Sennheiser MKH 800 (small diaphragm condenser with very wide bandwidth) and a DPA 4035 (headset-mounted condenser). Although the current release includes only speech data recorded via Sennheiser MKH 800, we may release speech data recorded via other microphones in the future. All recordings were made at 96 kHz sampling frequency and 24 bits per sample, then downsampled to 48 kHz sampling frequency. For recording, downsampling and bit rate conversion, we used ProTools HD hardware and software. We conducted 8 sessions over the course of a month, recording about 500 sentences in each session. At the start of each session, the speaker listened to a previously recorded sample, in order to attain a similar voice quality and intonation.


### Languages

Romanian

## Dataset Structure
### Data Instances
A typical data point comprises the path to the audio file, called audio and its sentence.


### Data Fields

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- sentence: The sentence the user was prompted to speak

### Data Splits
The speech material has been subdivided into portions for train and test.
The train split consists of 3180 audio clips and the related sentences.
The test split consists of 536 audio clips and the related sentences.

### Citation Information

```
@article{Stan2011442,
  author = {Adriana Stan and Junichi Yamagishi and Simon King and
                   Matthew Aylett},
  title = {The {R}omanian speech synthesis ({RSS}) corpus:
                   Building a high quality {HMM}-based speech synthesis
                   system using a high sampling rate},
  journal = {Speech Communication},
  volume = {53},
  number = {3},
  pages = {442--450},
  note = {},
  abstract = {This paper first introduces a newly-recorded high
                   quality Romanian speech corpus designed for speech
                   synthesis, called ''RSS'', along with Romanian
                   front-end text processing modules and HMM-based
                   synthetic voices built from the corpus. All of these
                   are now freely available for academic use in order to
                   promote Romanian speech technology research. The RSS
                   corpus comprises 3500 training sentences and 500 test
                   sentences uttered by a female speaker and was recorded
                   using multiple microphones at 96 kHz sampling
                   frequency in a hemianechoic chamber. The details of the
                   new Romanian text processor we have developed are also
                   given. Using the database, we then revisit some basic
                   configuration choices of speech synthesis, such as
                   waveform sampling frequency and auditory frequency
                   warping scale, with the aim of improving speaker
                   similarity, which is an acknowledged weakness of
                   current HMM-based speech synthesisers. As we
                   demonstrate using perceptual tests, these configuration
                   choices can make substantial differences to the quality
                   of the synthetic speech. Contrary to common practice in
                   automatic speech recognition, higher waveform sampling
                   frequencies can offer enhanced feature extraction and
                   improved speaker similarity for HMM-based speech
                   synthesis.},
  doi = {10.1016/j.specom.2010.12.002},
  issn = {0167-6393},
  keywords = {Speech synthesis, HTS, Romanian, HMMs, Sampling
                   frequency, Auditory scale},
  url = {http://www.sciencedirect.com/science/article/pii/S0167639310002074},
  year = 2011
}
```


### Contributions
[@gigant](https://huggingface.co/gigant) added this dataset.