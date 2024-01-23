---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- 'no'
- nb
- nn
license:
- cc0-1.0
multilinguality:
- monolingual
size_categories:
- 2G<n<1B
source_datasets:
- original
task_categories:
- automatic-speech-recognition
- audio-classification
pretty_name: NPSC
tags:
- speech-modeling
---
# Dataset Card for NbAiLab/NPSC


## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Summary](#dataset-summary)
- [Data Fields](#data-fiels)
- [Dataset Creation](#dataset-creation)
- [Statistics](#statistics)
- [Document Types](#document-types)
- [Languages](#languages)
- [Publish Periode](#publish-periode)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Social Impact of Dataset](#social-impact-of-dataset)
- [Discussion of Biases](#discussion-of-biases)
- [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
- [Dataset Curators](#dataset-curators)
- [Licensing Information](#licensing-information)
- [Citation Information](#citation-information)

## Dataset Description
- **Homepage:** https://www.nb.no/sprakbanken/
- **Repository:** https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-58/
- **Paper:** https://www.nb.no/sprakbanken/
- **Point of Contact:** [Per Erik Solberg](mailto:per.solberg@nb.no)

The Norwegian Parliamentary Speech Corpus (NPSC) is a speech corpus made by the Norwegian Language Bank at the National Library of Norway in 2019-2021. The NPSC consists of recordings of speech from Stortinget, the Norwegian parliament, and corresponding orthographic transcriptions to Norwegian Bokmål and Norwegian Nynorsk. All transcriptions are done manually by trained linguists or philologists, and the manual transcriptions are subsequently proofread to ensure consistency and accuracy. Entire days of Parliamentary meetings are transcribed in the dataset.

This repository contains a version of the NPSC in the 🤗 Dataset Format. Note that the official release of the dataset, which can be found in [the repository of the Norwegian Language Bank](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-58/), contains more information than the version found here, including word-level metadata, metadata about the speakers, and detailed documentation.

## How to Use
```python
# Loads the 16K Bokmål corpus in streaming mode
from datasets import load_dataset
data = load_dataset("NbAiLab/NPSC", config="16K_mp3_bokmaal", streaming=True)
```

## Dataset Summary
The NPSC dataset contains JSON lines with language training data. The data loader will add audio data to this structure. Here is an example json object:
```json
{
"sentence_id": 49853,
"sentence_order": 0,
"speaker_id": 32,
"meeting_date": "20170110",
"speaker_name": "Olemic Thommessen",
"sentence_text": "Stortingets møte er lovlig satt",
"sentence_language_code": "nb-NO",
"text": "Stortingets møte er lovlig satt",
"start_time": 320246, 
"end_time": 323590,
"normsentence_text": "Stortingets møte er lovlig satt",
"transsentence_text": "Stortingets møte er lovleg sett",
"translated": 1,
"audio": {"path": "audio/20170110-095504_320246_323590.wav","array": [.......]}
}
```

## Data Fields
|**Key** | **Type** | **Description** |
|:-----------|:------------|:------------|
|**sentence_id:** | Integer | Unique identifier of the sentence |
|**sentence_order** | Integer | A number indicating the order of the sentences in the meeting |
|**speaker_id** | Integer | The ID of the speaker. This can be linked to the original dataset containing thorough demographic and dialectal information about the speaker. |
|**meeting_date** | String | The date for the meeting in the format __yyyymmdd__ |
| **speaker_name** | String  | Name of the speaker. All speakers were members of the Norwegian Parliament or members of the Norwegian Government at the meeting date |
| **sentence_text** | String | The sentence text. The transcribed text string of the sentence in non-normalized form. This is the text of the manual transcriptions, without any postprocessing (apart from corrections of known errors). It may contain interrupted words, non-standard words and function words with a pronunciation deviating from the written form. Detailed metadata about the words in the sentence can be found in the word-tokenized version of the corpus in the official release of the dataset. |
| **sentence_language_code** | String | The language code of the sentence. The following alternatives exists in the file: ['nb-NO'. 'nn-NO', 'en-US']|
| **text** | String | sentence text. This is a copy of "sentence_text". It is included here to make it more convenient to interleave with other datasets.|
| **start_time** | Integer | The start time of the sentence in milliseconds. This time is relative to the start of audiofile of the entire meeting, which can be accessed in the official release  |
| **end_time** | Integer | End time. See comment above. | 
| **normsentence_text** | String | Normalized sentence text. In this version of the transcription, numbers and dates are written in digits on standardized formats, and common abbreviations are used. These modifications to the original transcriptions are produced automatically using normalization grammars |
| **transsentence_text** | String | Translated sentence text. Whenever the original transcription is in Bokmål (nb-NO), this field contains a machine-translated version in Nynorsk (nn-NO), and vice versa |
| **translated** | Integer | A flag indicating  whether a machine-translated version has been produced or not. Sentences in en-US have not been translated |
| **audio** | Array | The dataloader will encode the accociated audio files and provide them as an array containing 'path', 'sound array','sampling_rate' |


#### Initial Data Collection
The procedure for the dataset creation is described in detail in our paper.


## Statistics
|   Feature | Value       |
|:---------|-----------:|
| Duration, pauses included     | 140,3 hours| 
| Duration, pauses not included     | 125,7 hours  | 
| Word count     | 1,2 million | 
| Sentence count     | 64.531 | 
| Language distribution     | Nynorsk: 12,8%| 
|      | Bokmål: 87,2%| 
| Gender distribution     | Female: 38,3% | 
|      | Male: 61.7% | 


## Considerations for Using the Data
This corpus contains speech data. All recordings are of members of Parliament in a public setting, and can be distributed without any restrains.

### Dataset Creators and Curators
The content of the dataset was created by the Norwegian Language Bank (Språkbanken) at the National Library of Norway. [Javier de la Rosa](mailto:versae@nb.no), [Freddy Wetjen](mailto:freddy.wetjen@nb.no), [Per Egil Kummervold](mailto:per.kummervold@nb.no), and [Andre Kaasen](mailto:andre.kasen@nb.no) all contributed in making this into a HuggingFace Dataset. Thanks to the HuggingFace team for assistance.

## License
The sound and the transcriptions are released under the [CC-ZERO-license](https://creativecommons.org/publicdomain/zero/1.0/). The curation of the HuggingFace Dataset is released under [CC-BY-SA-3-license](https://creativecommons.org/licenses/by-sa/3.0/).

### Citation Information
The following article gives detailed information about the corpus. Please refer to the article and this page if you are using this dataset:
```

@misc{solberg2022norwegian,
      title={The Norwegian Parliamentary Speech Corpus},
      author={Per Erik Solberg and Pablo Ortiz},
      year={2022},
      eprint={2201.10881},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
