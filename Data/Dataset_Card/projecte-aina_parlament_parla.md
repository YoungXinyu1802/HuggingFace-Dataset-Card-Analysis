---
annotations_creators:
- found
language_creators:
- found
language:
- ca
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
  clean:
  - 10K<n<100K
  other:
  - 100K<n<1M
source_datasets:
- original
task_categories:
- automatic-speech-recognition
- text-generation
task_ids:
- language-modeling
- speaker-identification
pretty_name: ParlamentParla
---

# Dataset Card for ParlamentParla

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://zenodo.org/record/5541827
- **Repository:** https://github.com/CollectivaT-dev/ParlamentParla
- **Paper:** ParlamentParla: [A Speech Corpus of Catalan Parliamentary Sessions.](http://www.lrec-conf.org/proceedings/lrec2022/workshops/ParlaCLARINIII/2022.parlaclariniii-1.0.pdf#page=135)
- **Point of Contact:** [Baybars Kulebi](mailto:baybars.kulebi@bsc.es)

### Dataset Summary

This is the ParlamentParla speech corpus for Catalan prepared by Col·lectivaT. The audio segments were extracted from recordings the Catalan Parliament (Parlament de Catalunya) plenary sessions, which took place between 2007/07/11 - 2018/07/17. We aligned the transcriptions with the recordings and extracted the corpus. The content belongs to the Catalan Parliament and the data is released conforming their terms of use.

Preparation of this corpus was partly supported by the Department of Culture of the Catalan autonomous government, and the v2.0 was supported by the Barcelona Supercomputing Center, within the framework of Projecte AINA of the Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya.

As of v2.0 the corpus is separated into 211 hours of clean and 400 hours of other quality segments. Furthermore, each speech segment is tagged with its speaker and each speaker with their gender. The statistics are detailed in the readme file.

### Supported Tasks and Leaderboards

The dataset can be used for:
- Language Modeling.
- Automatic Speech Recognition (ASR) transcribes utterances into words.
- Speaker Identification (SI) classifies each utterance for its speaker identity as a multi-class classification, where speakers are in the same predefined set for both training and testing.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'path': 'clean_train/c/c/ccca4790a55aba3e6bcf_63.88_74.06.wav'
  'audio': {
    'path': 'clean_train/c/c/ccca4790a55aba3e6bcf_63.88_74.06.wav',
	'array': array([-6.10351562e-05, -6.10351562e-05, -1.22070312e-04, ...,  
	                -1.22070312e-04,  0.00000000e+00, -3.05175781e-05]),
	'sampling_rate': 16000
  },
  'speaker_id': 167,
  'sentence': "alguns d'ells avui aquí presents un agraïment a aquells que mantenen viva la memòria aquest acte de reparació i dignitat és",
  'gender': 0, 
  'duration': 10.18
}
```

### Data Fields

- `path` (str): The path to the audio file.
- `audio` (dict): A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling
  rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and
  resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might
  take a significant amount of time. Thus, it is important to first query the sample index before the `"audio"` column,
  *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.
- `speaker_id` (int): The speaker ID.
- `sentence` (str): The sentence the user was prompted to speak.
- `gender` (ClassLabel): The gender of the speaker (0: 'F', 1: 'M').
- `duration` (float): Duration of the speech.

### Data Splits

The dataset is split in: "train", "validation" and "test".

## Dataset Creation

The dataset is created by aligning the parliamentary session transcripts
and the audiovisual content. For more detailed information please consult
this [paper](http://www.lrec-conf.org/proceedings/lrec2022/workshops/ParlaCLARINIII/2022.parlaclariniii-1.0.pdf#page=135).

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

The audio segments were extracted from recordings the Catalan Parliament 
(Parlament de Catalunya) plenary sessions, which took place between 2007/07/11 - 
2018/07/17. The cleaning procedures are in the archived repository [Long Audio
Aligner](https://github.com/gullabi/long-audio-aligner)

#### Who are the source language producers?

The parliamentary members of the legislatures between 2007/07/11 - 
2018/07/17

### Annotations

The dataset is unannotated.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

The initial content is publicly available furthermore, the identities of
the parliamentary members are anonymized.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in 
Catalan, a low-resource language.

### Discussion of Biases

This dataset has a gender bias, however since the speakers are tagged according to 
their genders, creating a balanced subcorpus is possible. 

| Subcorpus   | Gender   |  Duration (h) |
|-------------|----------|------------|
| other_test  | F        |   2.516    |
| other_dev   | F        |   2.701    |
| other_train | F        |   109.68   |
| other_test  | M        |   2.631    |
| other_dev   | M        |   2.513    |
| other_train | M        |  280.196   |
|*other total*|          |  400.239   |
| clean_test  | F        |   2.707    |
| clean_dev   | F        |   2.576    |
| clean_train | F        |   77.905   |
| clean_test  | M        |   2.516    |
| clean_dev   | M        |   2.614    |
| clean_train | M        |  123.162   |
|*clean total*|          |   211.48   |
|*Total*      |          |  611.719   |


### Other Known Limitations

The text corpus belongs to the domain of Catalan politics

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

```
@dataset{kulebi_baybars_2021_5541827,
  author       = {Külebi, Baybars},
  title        = {{ParlamentParla - Speech corpus of Catalan 
                   Parliamentary sessions}},
  month        = oct,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v2.0},
  doi          = {10.5281/zenodo.5541827},
  url          = {https://doi.org/10.5281/zenodo.5541827}
}
```

For the paper:
```
@inproceedings{kulebi2022parlamentparla,
  title={ParlamentParla: A Speech Corpus of Catalan Parliamentary Sessions},
  author={K{\"u}lebi, Baybars and Armentano-Oller, Carme and Rodr{\'\i}guez-Penagos, Carlos and Villegas, Marta},
  booktitle={Workshop on Creating, Enriching and Using Parliamentary Corpora},
  volume={125},
  number={130},
  pages={125},
  year={2022}
}
```

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
