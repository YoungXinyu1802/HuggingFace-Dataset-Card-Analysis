---
dataset_info:
  features:
  - name: original_speech
    dtype: string
  - name: original_language
    dtype: string
  - name: audio_path
    dtype: string
  - name: segment_start
    dtype: float32
  - name: segment_end
    dtype: float32
  - name: transcriptions
    struct:
    - name: de
      dtype: string
    - name: en
      dtype: string
    - name: es
      dtype: string
    - name: fr
      dtype: string
    - name: it
      dtype: string
    - name: nl
      dtype: string
    - name: pl
      dtype: string
    - name: pt
      dtype: string
    - name: ro
      dtype: string
  splits:
  - name: train
    num_bytes: 147857910
    num_examples: 116138
  - name: valid
    num_bytes: 21318985
    num_examples: 17538
  - name: test
    num_bytes: 22580968
    num_examples: 18901
  download_size: 109205144
  dataset_size: 191757863
task_categories:
- translation
- text-to-speech
language:
- es
- de
- en
- fr
- nl
- pl
- pt
- ro
- it
size_categories:
- 100K<n<1M
license: cc-by-nc-4.0
---
# Dataset Card for "Europarl-ST"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://www.mllp.upv.es/europarl-st/
- **Paper:** https://ieeexplore.ieee.org/document/9054626
- **Point of Contact:** https://www.mllp.upv.es/

### Dataset Summary

Europarl-ST is a Multilingual Speech Translation Corpus, that contains paired audio-text samples for Speech Translation, constructed using the debates carried out in the European Parliament in the period between 2008 and 2012.

### Languages

Spanish, German, English, French, Dutch, Polish, Portuguese, Romanian, Italian

## Dataset Structure

### Data Fields

- **original_audio:** The original speech that is heard on the recording. 
- **original_language:** The language of the audio
- **audio_path:** Path to the audio file
- **segment_start:** Second in which the speech begins
- **segment_end:** Second in which the speech ends
- **transcriptions:** Dictionary containing transcriptions into different languages

### Data Splits

- **train split:** 116138 samples
- **valid split:** 17538 samples
- **test split:** 18901 samples

Train set (hours):

| src/tgt | en | fr | de | it | es | pt | pl | ro | nl |
|---------|----|----|----|----|----|----|----|----|----|
| en      | -  | 81 | 83 | 80 | 81 | 81 | 79 | 72 | 80 |
| fr      | 32 | -  | 21 | 20 | 21 | 22 | 20 | 18 | 22 |
| de      | 30 | 18 | -  | 17 | 18 | 18 | 17 | 17 | 18 |
| it      | 37 | 21 | 21 | -  | 21 | 21 | 21 | 19 | 20 |
| es      | 22 | 14 | 14 | 14 | -  | 14 | 13 | 12 | 13 |
| pt      | 15 | 10 | 10 | 10 | 10 | -  | 9  | 9  | 9  |
| pl      | 28 | 18 | 18 | 17 | 18 | 18 | -  | 16 | 18 |
| ro      | 24 | 12 | 12 | 12 | 12 | 12 | 12 | -  | 12 |
| nl      | 7  | 5  | 5  | 4  | 5  | 4  | 4  | 4  | -  |

Valid/Test sets are all between 3 and 6 hours.

## Additional Information

### Licensing Information

* The work carried out for constructing the Europarl-ST corpus is released under a Creative Commons Attribution-NonCommercial 4.0 International license (CC BY-NC 4.0)
       
* All rights of the data belong to the European Union and respective copyright holders.

### Citation Information

If you use the corpus in your research please cite the following reference:

  @INPROCEEDINGS{jairsan2020a,
  author={J. {Iranzo-Sánchez} and J. A. {Silvestre-Cerdà} and J. {Jorge} and N. {Roselló} and A. {Giménez} and A. {Sanchis} and J. {Civera} and A. {Juan}},
  booktitle={ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={Europarl-ST: A Multilingual Corpus for Speech Translation of Parliamentary Debates}, 
  year={2020},
  pages={8229-8233},}