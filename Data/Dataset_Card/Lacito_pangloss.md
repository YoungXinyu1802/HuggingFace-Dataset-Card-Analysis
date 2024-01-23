---
pretty_name: Pangloss
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- jya
- nru
language_bcp47:
- x-japh1234
- x-yong1288
language_details: jya consists of japh1234 (Glottolog code); nru consists of yong1288 (Glottolog code)
license: cc-by-nc-sa-4.0
multilinguality:
- multilingual
- translation
size_categories:
  yong1288:
  - 10K<n<100K
  japh1234:
  - 10K<n<100K
source_datasets:
- original
task_categories:
- automatic-speech-recognition
task_ids:
- speech-recognition
---

# Dataset Card for [Needs More Information]

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [Web interface of the Pangloss Collection, which hosts the data sets](https://pangloss.cnrs.fr/)
- **Repository:** [GithHub repository of the Pangloss Collection, which hosts the data sets](https://github.com/CNRS-LACITO/Pangloss/)
- **Paper:** [A paper about the Pangloss Collection, including a presentation of the Document Type Definition](https://halshs.archives-ouvertes.fr/halshs-01003734)
[A paper in French about the deposit in Zenodo](https://halshs.archives-ouvertes.fr/halshs-03475436)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Benjamin Galliot](mailto:b.g01lyon@gmail.com)

### Dataset Summary

Two audio corpora of minority languages of China (Japhug and Na), with transcriptions, proposed as reference data sets for experiments in Natural Language Processing. The data, collected and transcribed in the course of immersion fieldwork, amount to a total of about 1,900 minutes in Japhug and 200 minutes in Na. By making them available in an easily accessible and usable form, we hope to facilitate the development and deployment of state-of-the-art NLP tools for the full range of human languages. There is an associated tool for assembling datasets from the Pangloss Collection (an open archive) in a way that ensures full reproducibility of experiments conducted on these data.
The Document Type Definition for the XML files is available here:
http://cocoon.huma-num.fr/schemas/Archive.dtd

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

Japhug (ISO 639-3 code: jya, Glottolog language code: japh1234) and Yongning Na (ISO 639-3 code: nru, Glottolog language code: yong1288) are two minority languages of China. The documents in the dataset have a transcription in the endangered language. Some of the documents have translations into French, English, and Chinese.

## Dataset Structure

### Data Instances

A typical data row includes the path, audio, sentence, document type and several translations (depending on the sub-corpus).

`
{
  "path": "cocoon-db3cf0e1-30bb-3225-b012-019252bb4f4d_C1/Tone_BodyPartsOfAnimals_12_F4_2008_withEGG_069.wav",
  "audio": "{'path': 'na/cocoon-db3cf0e1-30bb-3225-b012-019252bb4f4d_C1/Tone_BodyPartsOfAnimals_12_F4_2008_withEGG_069.wav', 'array': array([0.00018311, 0.00015259, 0.00021362, ..., 0.00030518, 0.00030518, 0.00054932], dtype=float32), 'sampling_rate': 16000}",
  "sentence": "ʈʂʰɯ˧ | ɖɤ˧mi˧-ɬi˧pi˩ ɲi˩",
  "doctype": "WORDLIST",
  "translation:zh": "狐狸的耳朵",
  "translation:fr": "oreilles de renard",
  "translation:en": "fox's ears",
}
`

### Data Fields

path: the path to the audio file;;

audio: a dictionary containing the path to the audio file, the audio array and the sampling rate;

sentence: the sentence the native has pronunced;

doctype: the document type (a text or a word list);

translation:XX: the translation of the sentence in the language XX.

### Data Splits

The train, test and validation splits have all been reviewed and were splitted randomly (ratio 8:1:1) at sentence level (after the extraction from various files).

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

The dataset was collected in immersion fieldwork for language documentation. It contributes to the documentation and study of the world's languages by providing documents of connected, spontaneous speech recorded in their cultural context and transcribed in consultation with native speakers. The impacts concern research, and society at large: a guiding principle of the Pangloss Collection, which hosts the data sets, is that a close association between documentation and research is highly profitable to both. A range of possibilities for uses exist, for the scientific and speaker communities and for the general public.

### Discussion of Biases

The corpora are single-speaker and hence clearly do not reflect the sociolinguistic and dialectal diversity of the languages. No claim is made that the language variety described constitutes a 'standard'.

### Other Known Limitations

The translations are entirely hand-made by experts working on these languages; the amount and type of translations available varies from document to document, as not all documents have translations and not all translated documents have the same translation languages (Chinese, French, English...).

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]
