---
annotations_creators:
- machine-generated
language:
- is
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Althingi Parliamentary Speech
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- icelandic
- parliamentary speech
- parlament
- althingi
task_categories:
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for althingi_asr
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Data](#data)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Other Known Limitations](#other-known-limitations)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
  
## Dataset Description
- **Homepage:** Althingi Parliamentary Speech
- **Repository:** [LDC](https://catalog.ldc.upenn.edu/LDC2021S01)
- **Paper:** [Building an ASR corpus using Althingi’s Parliamentary Speeches](https://www.researchgate.net/profile/Jon-Gudnason/publication/319185185_Building_an_ASR_Corpus_Using_Althingi's_Parliamentary_Speeches/links/5d1dbdd3a6fdcc2462bdda0f/Building-an-ASR-Corpus-Using-Althingis-Parliamentary-Speeches.pdf)
- **Point of Contact:** [Jón Guðnason](mailto:jg@ru.is)

### Dataset Summary

Althingi Parliamentary Speech consists of approximately 542 hours of recorded speech from Althingi, the Icelandic Parliament, along with corresponding transcripts, a pronunciation dictionary and two language models. Speeches date from 2005-2016.

This dataset was collected in 2016 by the ASR for Althingi project at [Reykjavik University](https://en.ru.is/) in collaboration with the Althingi speech department. The purpose of that project was to develop an ASR (automatic speech recognition) system for parliamentary speech to replace the procedure of manually transcribing performed speeches.

### Data

The mean speech length is six minutes, with speeches ranging from under one minute to around thirty minutes. The corpus features 197 speakers (105 male, 92 female) and is split into training, development and evaluation sets. The language models are of two types: a pruned trigram model, used in decoding, and an unpruned constant ARPA 5-gram model, used for re-scoring decoding results.

Audio data is presented as single channel 16-bit mp3 files; the majority of these files have a sample rate of 44.1 kHz. Transcripts and other text data are plain text encoded in UTF-8.

### Example Usage
The Althingi Corpus is divided in 3 splits: train, validation and test. To load a specific split pass its name as a config name:
```python
from datasets import load_dataset
althingi_asr = load_dataset("language-and-voice-lab/althingi_asr")
```
To load an specific split (for example, the validation split) do:
```python
from datasets import load_dataset
althingi_asr = load_dataset("language-and-voice-lab/althingi_asr",split="validation")
```

### Supported Tasks
automatic-speech-recognition: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

### Languages
The audio is in Icelandic.

## Dataset Structure

### Data Instances
```python
{
  'audio_id': 'rad20160602T000219_00083', 
  'audio': {
    'path': '/home/inga/.cache/HuggingFace/datasets/downloads/extracted/52607f9db9e3394263070575d29323213b99a06a996c43d4fe75bca115827d12/dev/EyH/rad20160602T000219/rad20160602T000219_00083.flac', 
    'array': array([-0.01098633, -0.01489258, -0.01040649, ...,  0.00314331,
        0.00186157,  0.00527954], dtype=float32), 
    'sampling_rate': 16000
  }, 
  'speaker_id': 'rad20160602T000219', 
  'duration': 12.67199993133545, 
  'normalized_text': 'og má svo sannarlega segja að landslagið sé nokkuð breytt frá því þrjú komma tvö prósent þjóðarinnar töldust vera innflytjendur árið tvö þúsund en nú teljast tíu prósent þjóðarinnar vera fyrsta og önnur kynslóð innflytjenda'
}
```

### Data Fields
* `audio_id` (string) - id of audio segment
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `speaker_id` (string) - id of speaker
* `duration` (float32) - duration of the audio file in seconds.
* `normalized_text` (string) - normalized audio segment transcription.

### Data Splits
The corpus is split into train, evaluation, and test portions. Lenghts of every portion are: train = 514h29m, test = 13h52m, evaluation=14h02m.

To load an specific portion please see the above section "Example Usage".

## Additional Information

### Other Known Limitations
"Althingi Parliamentary Speech" by the Language and Voice Laboratory (LVL) at the Reykjavik University is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License with the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

### Licensing Information
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information
```
@misc{helgadottiralthingi2021,
      title={Althingi Parliamentary Speech}, 
      ldc_catalog_no={LDC2021S01},
      DOI={https://doi.org/10.35111/695b-6697},
      author={Helgadóttir, Inga Rún and Kjaran, Róbert and Nikulásdóttir, Anna Björk and Guðnason, Jón},
      publisher={Reykjavík University}
      journal={Linguistic Data Consortium, Philadelphia},
      year={2021},
      url={https://catalog.ldc.upenn.edu/LDC2021S01},
}
```

### Contributions

This project was made possible through the support of Althingi’s information and publications departments. The authors would like to thank Solveig K. Jónsdóttir, Þorbjörg Árnadóttir and Ingvi Stígsson for their valuable help.

