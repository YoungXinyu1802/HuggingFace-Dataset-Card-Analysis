---
annotations_creators:
- expert-generated
language:
- ml
language_creators:
- found
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: ICFOSS Malayalam Speech Corpus
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- text-to-speech
- automatic-speech-recognition
task_ids: []
---

# IMaSC: ICFOSS Malayalam Speech Corpus

**IMaSC** is a Malayalam text and speech corpus made available by [ICFOSS](https://icfoss.in/) for the purpose of developing speech technology for Malayalam, particularly text-to-speech. The corpus contains 34,473 text-audio pairs of Malayalam sentences spoken by 8 speakers, totalling in approximately 50 hours of audio.

## Dataset Description

- **Paper:** [IMaSC — ICFOSS Malayalam Speech Corpus](https://arxiv.org/abs/2211.12796)
- **Point of Contact:** [Thennal D K](mailto:thennal10@gmail.com)

## Dataset Structure
The dataset consists of 34,473 instances with fields `text`, `speaker`, and `audio`. The audio is mono, sampled at 16kH. The transcription is normalized and only includes Malayalam characters and common punctuation. The table given below specifies how the 34,473 instances are split between the speakers, along with some basic speaker info:


| Speaker | Gender | Age | Time (HH:MM:SS) | Sentences |
| --- | --- | --- | --- | --- |
| Joji | Male | 28 | 06:08:55 | 4,332 |  
| Sonia | Female | 43 | 05:22:39 | 4,294 |  
| Jijo | Male | 26 | 05:34:05 | 4,093 |  
| Greeshma | Female | 22 | 06:32:39 | 4,416 |  
| Anil | Male | 48 | 05:58:34 | 4,239 |  
| Vidhya | Female | 23 | 04:21:56 | 3,242 |  
| Sonu | Male | 25 | 06:04:43 | 4,219 |  
| Simla | Female | 24 | 09:34:21 | 5,638 |
| **Total** | | | **49:37:54** | **34,473** |

### Data Instances
An example instance is given below:
```json
{'text': 'സർവ്വകലാശാല വൈസ് ചാൻസലർ ഡോ. ചന്ദ്രബാബുവിനും സംഭവം തലവേദനയാവുകയാണ്',
 'speaker': 'Sonia',
 'audio': {'path': None,
  'array': array([ 0.00921631,  0.00930786,  0.00939941, ..., -0.00497437,
         -0.00497437, -0.00497437]),
  'sampling_rate': 16000}}
 ```

### Data Fields
- **text** (str): Transcription of the audio file
- **speaker** (str): The name of the speaker
- **audio** (dict): Audio object including loaded audio array, sampling rate and path to audio (always None)

### Data Splits

We provide all the data in a single `train` split. The loaded dataset object thus looks like this:
```json
DatasetDict({
     train: Dataset({
         features: ['text', 'speaker', 'audio'],
         num_rows: 34473
     })
 })
```

### Dataset Creation

The text is sourced from [Malayalam Wikipedia](https://ml.wikipedia.org), and read by our speakers in studio conditions. Extensive error correction was conducted to provide a clean, accurate database. Further details are given in our paper, accessible at [https://arxiv.org/abs/2211.12796](https://arxiv.org/abs/2211.12796).


## Additional Information

### Licensing
The corpus is made available under the [Creative Commons license (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

### Citation
```
@misc{gopinath2022imasc,
    title={IMaSC -- ICFOSS Malayalam Speech Corpus},
    author={Deepa P Gopinath and Thennal D K and Vrinda V Nair and Swaraj K S and Sachin G},
    year={2022},
    eprint={2211.12796},
    archivePrefix={arXiv},
    primaryClass={cs.SD}
}
```
