---
annotations_creators:
- expert-generated
- crowdsourced
- machine-generated
language_creators:
- crowdsourced
- expert-generated
language:
- en
- fr
- it
- es
- pt
- de
- nl
- ru
- pl
- cs
- ko
- zh
language_bcp47:
- en
- en-GB
- en-US
- en-AU
- fr
- it
- es
- pt
- de
- nl
- ru
- pl
- cs
- ko
- zh
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: 'MInDS-14'
size_categories:
- 10K<n<100K
task_categories:
- automatic-speech-recognition
- speech-processing
task_ids:
- speech-recognition
- keyword-spotting
---

# MInDS-14

## Dataset Description

- **Fine-Tuning script:** [pytorch/audio-classification](https://github.com/huggingface/transformers/tree/main/examples/pytorch/audio-classification)
- **Paper:** [Multilingual and Cross-Lingual Intent Detection from Spoken Data](https://arxiv.org/abs/2104.08524)
- **Total amount of disk used:** ca. 500 MB 

MINDS-14 is training and evaluation resource for intent detection task with spoken data. It covers 14 
intents extracted from a commercial system in the e-banking domain, associated with spoken examples in 14 diverse language varieties.

## Example

MInDS-14 can be downloaded and used as follows:

```py
from datasets import load_dataset

minds_14 = load_dataset("PolyAI/minds14", "fr-FR") # for French
# to download all data for multi-lingual fine-tuning uncomment following line
# minds_14 = load_dataset("PolyAI/all", "all")

# see structure
print(minds_14)

# load audio sample on the fly
audio_input = minds_14["train"][0]["audio"]  # first decoded audio sample
intent_class = minds_14["train"][0]["intent_class"]  # first transcription
intent = minds_14["train"].features["intent_class"].names[intent_class]

# use audio_input and language_class to fine-tune your model for audio classification
```

## Dataset Structure

We show detailed information the example configurations `fr-FR` of the dataset.
All other configurations have the same structure.

### Data Instances

**fr-FR**

- Size of downloaded dataset files: 471 MB
- Size of the generated dataset: 300 KB
- Total amount of disk used: 471 MB


An example of a datainstance of the config `fr-FR` looks as follows:

```
{
    "path": "/home/patrick/.cache/huggingface/datasets/downloads/extracted/3ebe2265b2f102203be5e64fa8e533e0c6742e72268772c8ac1834c5a1a921e3/fr-FR~ADDRESS/response_4.wav",
    "audio": {
        "path": "/home/patrick/.cache/huggingface/datasets/downloads/extracted/3ebe2265b2f102203be5e64fa8e533e0c6742e72268772c8ac1834c5a1a921e3/fr-FR~ADDRESS/response_4.wav",
        "array": array(
            [0.0, 0.0, 0.0, ..., 0.0, 0.00048828, -0.00024414], dtype=float32
        ),
        "sampling_rate": 8000,
    },
    "transcription": "je souhaite changer mon adresse",
    "english_transcription": "I want to change my address",
    "intent_class": 1,
    "lang_id": 6,
}
```

### Data Fields
The data fields are the same among all splits.

- **path** (str): Path to the audio file
- **audio** (dict): Audio object including loaded audio array, sampling rate and path ot audio
- **transcription** (str): Transcription of the audio file
- **english_transcription** (str): English transcription of the audio file
- **intent_class** (int): Class id of intent
- **lang_id** (int): Id of language

### Data Splits
Every config only has the `"train"` split containing of *ca.* 600 examples.

## Dataset Creation

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

All datasets are licensed under the [Creative Commons license (CC-BY)](https://creativecommons.org/licenses/).

### Citation Information

```
@article{DBLP:journals/corr/abs-2104-08524,
  author    = {Daniela Gerz and
               Pei{-}Hao Su and
               Razvan Kusztos and
               Avishek Mondal and
               Michal Lis and
               Eshan Singhal and
               Nikola Mrksic and
               Tsung{-}Hsien Wen and
               Ivan Vulic},
  title     = {Multilingual and Cross-Lingual Intent Detection from Spoken Data},
  journal   = {CoRR},
  volume    = {abs/2104.08524},
  year      = {2021},
  url       = {https://arxiv.org/abs/2104.08524},
  eprinttype = {arXiv},
  eprint    = {2104.08524},
  timestamp = {Mon, 26 Apr 2021 17:25:10 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2104-08524.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions

Thanks to [@patrickvonplaten](https://github.com/patrickvonplaten) for adding this dataset
