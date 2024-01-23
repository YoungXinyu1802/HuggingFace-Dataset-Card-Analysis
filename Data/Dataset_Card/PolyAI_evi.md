---
annotations_creators:
- crowdsourced
- machine-generated
language_creators:
- crowdsourced
- expert-generated
language:
- en
- fr
- pl
license:
- cc-by-4.0
multilinguality:
- multilingual
paperswithcode_id: evi-multilingual-spoken-dialogue-tasks-and-1
language_bcp47:
- en
- en-GB
- fr
- fr-FR
- pl
---

# EVI

## Dataset Description
- **Paper:** [EVI: Multilingual Spoken Dialogue Tasks and Dataset for Knowledge-Based Enrolment, Verification, and Identification](https://arxiv.org/abs/2204.13496)
- **Repository:** [Github](https://github.com/PolyAI-LDN/evi-paper)

EVI is a challenging spoken multilingual dataset
with 5,506 dialogues in English, Polish, and French
that can be used for benchmarking and developing
knowledge-based enrolment, identification, and identification for spoken dialogue systems.

## Example
EVI can be downloaded and used as follows:

```py
from datasets import load_dataset
evi = load_dataset("PolyAI/evi", "en-GB") # for British English

# to download data from all locales use:
# evi = load_dataset("PolyAI/evi", "all")

# see structure
print(evi)
```

## Dataset Structure

We show detailed information of the example for the `en-GB` configuration of the dataset.
All other configurations have the same structure.

### Data Instances

An example of a data instance of the config `en-GB` looks as follows:

```
{
    "language": 0,
    "dialogue_id": "CA0007220161df7be23f4554704c8720f5",
    "speaker_id": "e80e9bdd33eda593f16a1b6f2fb228ff",
    "turn_id": 0,
    "target_profile_id": "en.GB.608",
    "asr_transcription": "w20 a b",
    "asr_nbest'": ["w20 a b", "w20 a bee", "w20 a baby"],
    "path": "audios/en/CA0007220161df7be23f4554704c8720f5/0.wav",
    "audio": {
        "path": "/home/georgios/.cache/huggingface/datasets/downloads/extracted/0335ebc25feace53243133b49ba17ba18e26f0f97cb083ffdf4e73dd7427b443/audios/en/CA0007220161df7be23f4554704c8720f5/0.wav",
        "array": array([ 0.00024414,  0.00024414,  0.00024414, ...,  0.00024414,
       -0.00024414,  0.00024414], dtype=float32),
       "sampling_rate": 8000,
    }
}
```

### Data Fields
The data fields are the same among all splits.
- **language** (int): ID of language
- **dialogue_id** (str): the ID of the dialogue
- **speaker_id** (str): the ID of the speaker
- **turn_id** (int)": the ID of the turn
- **target_profile_id** (str): the ID of the target profile
- **asr_transcription** (str): ASR transcription of the audio file
- **asr_nbest** (list): n-best ASR transcriptions of the audio file
- **path** (str): Path to the audio file
- **audio** (dict): Audio object including loaded audio array, sampling rate and path of audio


### Data Splits
Every config only has the `"test"` split containing *ca.* 1,800 dialogues.

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
@inproceedings{Spithourakis2022evi,
    author      = {Georgios P. Spithourakis and
                   Ivan Vuli\'{c} and
                   Micha\l{} Lis and
                   I\~{n}igo Casanueva
                   and Pawe\l{} Budzianowski},
    title       = {{EVI}: Multilingual Spoken Dialogue Tasks and Dataset for Knowledge-Based Enrolment, Verification, and Identification},
    year        = {2022},
    note        = {Data available at https://github.com/PolyAI-LDN/evi-paper},
    url         = {https://arxiv.org/abs/2204.13496},
    booktitle   = {Findings of NAACL (publication pending)}
}
```

### Contributions
Thanks to [@polinaeterna](https://github.com/polinaeterna) for helping with adding this dataset