---
license: cc-by-4.0
task_categories:
- audio-classification
language:
- bn
pretty_name: SUST BANGLA EMOTIONAL SPEECH CORPUS
size_categories:
- 1K<n<10K
---

# SUST BANGLA EMOTIONAL SPEECH CORPUS

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** [SUBESCO PAPER](https://doi.org/10.1371/journal.pone.0250173)
- **Leaderboard:** 
- **Point of Contact:** [Sadia Sultana](sadia-cse@sust.edu)

### Dataset Summary

SUBESCO is an audio-only emotional speech corpus of 7000 sentence-level utterances of the Bangla language. 20 professional actors (10 males and 10 females) participated in the recordings of 10 sentences for 7 target emotions. The emotions are Anger, Disgust, Fear, Happiness, Neutral, Sadness and Surprise. Total duration of the corpus is 7 hours 40 min 40 sec.  Total size of the dataset is 2.03 GB. The dataset was evaluated by 50 raters (25 males, 25 females). Human perception test achieved a raw accuracy of 71%.  All the details relating to creation, evaluation and analysis of SUBESCO have been described in the corresponding journal paper which has been published in Plos One.

https://doi.org/10.1371/journal.pone.0250173

### Downloading the data

```
from datasets import load_dataset

train = load_dataset("sustcsenlp/bn_emotion_speech_corpus",split="train")

```


### Naming Convention

Each audio file in the dataset has a unique name. There are eight parts in the file name where all the parts are connected by underscores. The order of all the parts is organized as: Gender-Speaker's serial number-Speaker's name-Unit of recording-Unit number- Emotion name- Repeating number and the File format. 

For example, the filename F_02_MONIKA_S_1_NEUTRAL_5.wav refers to:

| Symbol      | Meaning |
| ----------- | ----------- |
|      F      | Speaker Gender       |
| 02   | Speaker Number        |
|   MONIKA   | Speaker Name                     |
|  S_1    |  Sentence Number                    |
|  NEUTRAL     |  Emotion                    |
|    5  |  Take Number                    |

### Languages

This dataset contains Bangla Audio Data.

## Dataset Creation

This database was created as a part of PhD thesis project of the author Sadia Sultana. It was designed and developed by the author in the Department of Computer Science and Engineering of Shahjalal University of Science and Technology. Financial grant was supported by the university. If you use the dataset please cite SUBESCO and the corresponding academic journal publication in Plos One.

### Citation Information

```
@dataset{sadia_sultana_2021_4526477,
  author       = {Sadia Sultana},
  title        = {SUST Bangla Emotional Speech Corpus (SUBESCO)},
  month        = feb,
  year         = 2021,
  note         = {{This database was created as a part of PhD thesis 
                   project of the author Sadia Sultana. It was
                   designed and developed by the author in the
                   Department of Computer Science and Engineering  of
                   Shahjalal University of Science and Technology.
                   Financial grant was supported by the university.
                   If you use the dataset please cite SUBESCO and the
                   corresponding academic journal publication in Plos
                   One.}},
  publisher    = {Zenodo},
  version      = {version - 1.1},
  doi          = {10.5281/zenodo.4526477},
  url          = {https://doi.org/10.5281/zenodo.4526477}
}

```

### Contributors

| Name      | University |
| ----------- | ----------- |
| Sadia Sultana      | Shahjalal University of Science and Technology       |
| Dr. M. Zafar Iqbal   | Shahjalal University of Science and Technology        |
| Dr. M. Shahidur Rahman                    |   Shahjalal University of Science and Technology            |
## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]