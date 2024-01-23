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
    num_bytes: 140620332.25
    num_examples: 2822
  - name: train
    num_bytes: 608597323.625
    num_examples: 11291
  download_size: 711464914
  dataset_size: 749217655.875
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
license:
- cc-by-nc-sa-4.0
---

# Dataset Card for UWB-ATCC corpus

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
- **Homepage:** [UWB-ATCC corpus homepage](https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0)
- **Repository:** [GitHub repository (used in research)](https://github.com/idiap/w2v2-air-traffic)
- **Paper:** [Air traffic control communication (ATCC) speech corpora and their use for ASR and TTS development](https://link.springer.com/article/10.1007/s10579-019-09449-5)
- **Paper of this research:** [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](https://arxiv.org/abs/2203.16822)

### Dataset Summary

The UWB-ATCC Corpus is provided provided by University of West Bohemia, Department of Cybernetics. The corpus contains recordings of communication between air traffic controllers and pilots. The speech is manually transcribed and labeled with the information about the speaker (pilot/controller, not the full identity of the person). The corpus is currently small (20 hours) but we plan to search for additional data next year. The audio data format is: 8kHz, 16bit PCM, mono.

Important, from the `<id (string)>` field, you can obtain the speaker roles. For instance:
- `_PI`: segment with only pilot speech
- `_AT`: segment with only ATCO speech
- `PIAT`: segment with both, ATCO and pilot speech

### Supported Tasks and Leaderboards

- `automatic-speech-recognition`. Already adapted/fine-tuned models are available here --> [XLS-R-300m](https://huggingface.co/Jzuluaga/wav2vec2-large-960h-lv60-self-en-atc-atcosim).

### Languages and other details

The text and the recordings are in English. The authors took advantage of the fact that one of their industrial partners develops complex IT solutions for several ATC authorities and airports and, as such, has access to the ATC communication recordings collected in the Czech airspace. This partner was able to secure the following data:

- Ground control—communication before takeoff and after landing—19.2 h of data.
- Tower control—communication during takeoff, landing and landing standby—22.5 h.
- Approach control—communication during landing approach—25.5 h.
- Area control—communication during overflights and cruises—71.3 h.

(Not all data is released. Check their website [here](https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0))
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

The licensing status of the dataset hinges on the legal status of the [UWB-ATCC corpus](https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0) creators.

They used [Creative Commons - Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) licensing.

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

Authors of the dataset:
```
@article{vsmidl2019air,
  title={Air traffic control communication (ATCC) speech corpora and their use for ASR and TTS development},
  author={{\v{S}}m{\'\i}dl, Lubo{\v{s}} and {\v{S}}vec, Jan and Tihelka, Daniel and Matou{\v{s}}ek, Jind{\v{r}}ich and Romportl, Jan and Ircing, Pavel},
  journal={Language Resources and Evaluation},
  volume={53},
  number={3},
  pages={449--464},
  year={2019},
  publisher={Springer}
}
```
