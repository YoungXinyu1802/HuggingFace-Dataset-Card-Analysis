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
    num_bytes: 471628915.76
    num_examples: 1901
  - name: train
    num_bytes: 1934757106.88
    num_examples: 7638
  download_size: 0
  dataset_size: 2406386022.6400003
tags:
- audio
- automatic-speech-recognition
- en-atc
- en
- robust-speech-recognition
- noisy-speech-recognition
- speech-recognition
task_categories:
- automatic-speech-recognition  
language:
- en  
multilinguality:
- monolingual
---

# Dataset Card for ATCOSIM corpus
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
- **Homepage:** [ATCOSIM homepage](https://www.spsc.tugraz.at/databases-and-tools/atcosim-air-traffic-control-simulation-speech-corpus.html)
- **Repository:** [GitHub repository (used in research)](https://github.com/idiap/w2v2-air-traffic)
- **Paper:** [The ATCOSIM Corpus of Non-Prompted Clean Air Traffic Control Speech](https://aclanthology.org/L08-1507/)
- **Paper of this research:** [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](https://arxiv.org/abs/2203.16822)

### Dataset Summary

The ATCOSIM Air Traffic Control Simulation Speech corpus is a speech database of air traffic control (ATC) operator speech, provided by Graz University of Technology (TUG) and Eurocontrol Experimental Centre (EEC). It consists of ten hours of speech data, which were recorded during ATC real-time simulations using a close-talk headset microphone. The utterances are in English language and pronounced by ten non-native speakers. The database includes orthographic transcriptions and additional information on speakers and recording sessions. It was recorded and annotated by Konrad Hofbauer ([description here](https://www.spsc.tugraz.at/databases-and-tools/atcosim-air-traffic-control-simulation-speech-corpus.html)).

### Supported Tasks and Leaderboards

- `automatic-speech-recognition`. Already adapted/fine-tuned models are available here --> [XLS-R-300m](https://huggingface.co/Jzuluaga/wav2vec2-large-960h-lv60-self-en-atc-atcosim).

### Languages and other details
The text and the recordings are in English. The participating controllers were all actively employed air traffic controllers and possessed professional experience in the simulated sectors. The six male and four female controllers were of either German or Swiss nationality and had German, Swiss German or Swiss French native tongue. The controllers had agreed to the recording of their voice for the purpose of language analysis as well as for research and development in speech technologies, and were asked to show their normal working behaviour.

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

The licensing status of the dataset hinges on the legal status of the [ATCOSIM corpus](https://www.spsc.tugraz.at/databases-and-tools/atcosim-air-traffic-control-simulation-speech-corpus.html) creators.

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
@inproceedings{hofbauer-etal-2008-atcosim,
    title = "The {ATCOSIM} Corpus of Non-Prompted Clean Air Traffic Control Speech",
    author = "Hofbauer, Konrad  and
      Petrik, Stefan  and
      Hering, Horst",
    booktitle = "Proceedings of the Sixth International Conference on Language Resources and Evaluation ({LREC}'08)",
    month = may,
    year = "2008",
    address = "Marrakech, Morocco",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2008/pdf/545_paper.pdf",
}
```
