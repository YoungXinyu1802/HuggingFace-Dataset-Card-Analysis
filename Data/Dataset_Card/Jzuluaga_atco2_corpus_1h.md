---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: text
    dtype: string
  - name: segment_start_time
    dtype: float32
  - name: segment_end_time
    dtype: float32
  - name: duration
    dtype: float32
  splits:
  - name: test
    num_bytes: 113872168.0
    num_examples: 871
  download_size: 113467762
  dataset_size: 113872168.0
tags:
- audio
- automatic-speech-recognition
- en-atc
- en
- noisy-speech-recognition
- speech-recognition
task_categories:
- automatic-speech-recognition  
language:
- en
multilinguality:
- monolingual
---

# Dataset Card for ATCO2 test set corpus (1hr set)

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages and Other Details](#languages-and-other-details)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)


## Dataset Description
- **Homepage:** [ATCO2 project homepage](https://www.atco2.org/)
- **Repository:** [ATCO2 corpus](https://github.com/idiap/atco2-corpus)
- **Paper:** [ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications](https://arxiv.org/abs/2211.04054)

### Dataset Summary

ATCO2 project aims at developing a unique platform allowing to collect, organize and pre-process air-traffic control (voice communication) data from air space. This project has received funding from the Clean Sky 2 Joint Undertaking (JU) under grant agreement No 864702. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and the Clean Sky 2 JU members other than the Union.

The project collected the real-time voice communication between air-traffic controllers and pilots available either directly through publicly accessible radio frequency channels or indirectly from air-navigation service providers (ANSPs). In addition to the voice communication data, contextual information is available in a form of metadata (i.e. surveillance data). The dataset consists of two distinct packages:

- A corpus of 5000+ hours (pseudo-transcribed) of air-traffic control speech collected across different airports (Sion, Bern, Zurich, etc.) in .wav format for speech recognition. Speaker distribution is 90/10% between males and females and the group contains native and non-native speakers of English.
- A corpus of 4 hours (transcribed) of air-traffic control speech collected across different airports (Sion, Bern, Zurich, etc.) in .wav format for speech recognition. Speaker distribution is 90/10% between males and females and the group contains native and non-native speakers of English. This corpus has been transcribed with orthographic information in XML format with speaker noise information, SNR values and others. Read Less
- A free sample of the 4 hours transcribed data is in [ATCO2 project homepage](https://www.atco2.org/data)

### Supported Tasks and Leaderboards

- `automatic-speech-recognition`. Already adapted/fine-tuned models are available here --> [Wav2Vec 2.0 LARGE mdel](https://huggingface.co/Jzuluaga/wav2vec2-large-960h-lv60-self-en-atc-uwb-atcc-and-atcosim).

### Languages and other details

The text and the recordings are in English. For more information see Table 3 and Table 4 of [ATCO2 corpus paper](https://arxiv.org/abs/2211.04054)

## Dataset Structure

### Data Fields

- `id (string)`: a string of recording identifier for each example, corresponding to its.
- `audio (audio)`: audio data for the given ID
- `text (string)`: transcript of the file already normalized. Follow these repositories for more details [w2v2-air-traffic](https://github.com/idiap/w2v2-air-traffic) and [bert-text-diarization-atc](https://github.com/idiap/bert-text-diarization-atc)
- `segment_start_time (float32)`: segment start time (normally 0)
- `segment_end_time (float32): segment end time
- `duration (float32)`: duration of the recording, compute as segment_end_time - segment_start_time

## Additional Information

### Licensing Information

The licensing status of the ATCO2-test-set-1h corpus is in the file **ATCO2-ASRdataset-v1_beta - End-User Data Agreement** in the data folder. Download the data in [ATCO2 project homepage](https://www.atco2.org/data)

### Citation Information

Contributors who prepared, processed, normalized and uploaded the dataset in HuggingFace:

```
@article{zuluaga2022how,
    title={How Does Pre-trained Wav2Vec2. 0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications},
    author={Zuluaga-Gomez, Juan and Prasad, Amrutha and Nigmatulina, Iuliia and Sarfjoo, Saeed and others},
    journal={IEEE Spoken Language Technology Workshop (SLT), Doha, Qatar},
    year={2022}
  }
@article{zuluaga2022bertraffic,
  title={BERTraffic: BERT-based Joint Speaker Role and Speaker Change Detection for Air Traffic Control Communications},
  author={Zuluaga-Gomez, Juan and Sarfjoo, Seyyed Saeed and Prasad, Amrutha and others},
  journal={IEEE Spoken Language Technology Workshop (SLT), Doha, Qatar},
  year={2022}
  }
@article{zuluaga2022atco2,
  title={ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications},
  author={Zuluaga-Gomez, Juan and Vesel{\`y}, Karel and Sz{\"o}ke, Igor and Motlicek, Petr and others},
  journal={arXiv preprint arXiv:2211.04054},
  year={2022}
}
```

