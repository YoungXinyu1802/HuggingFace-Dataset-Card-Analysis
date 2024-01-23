---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- fa
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: Sharif Emotional Speech Dataset (ShEMO)
size_categories:
- 1K<n<10K
source_datasets:
- radio-plays
task_categories:
- automatic-speech-recognition
task_ids:
- speech-recognition
---

## Sharif Emotional Speech Dataset (ShEMO)

## Dataset Summary
The dataset includes 3000 semi-natural utterances, equivalent to 3 hours and 25 minutes of speech data extracted from online Persian radio plays. The ShEMO covers speech samples of 87 native-Persian speakers for five basic emotions including <i>anger</i>, <i>fear</i>, <i>happiness</i>, <i>sadness</i> and <i>surprise</i>, as well as neutral state. Twelve annotators label the underlying emotional state of utterances and majority voting is used to decide on the final labels. According to the kappa measure, 
the inter-annotator agreement is 64% which is interpreted as "substantial agreement".

## Languages
Persian (fa)

## Overview of ShEMO
Feature                      | Status   
-------------                | ----------
**license**                  | apache-2.0
**language**                 | Persian (fa)
**modality**                 | Speech
**duration**                 | 3 hours and 25 minutes
**#utterances**              | 3000
**#speakers**                | 87 (31 females, 56 males)
**#emotions**                | 5 basic emotions (anger, fear, happiness, sadness and surprise) and neutral state
**orthographic transcripts** | Available
**phonetic transcripts**     | Available

## Data Instances
Here is a sample of data instances:
```json
"F21N37": {
    "speaker_id": "F21", 
    "gender": "female", 
    "emotion": "neutral", 
    "transcript": "مگه من به تو نگفته بودم که باید راجع به دورانت سکوت کنی؟", 
    "ipa": "mӕge mæn be to nægofte budӕm ke bɑyæd rɑdʒeʔ be dorɑnt sokut koni"
 }
```

## Citation
If you use this dataset, please cite the following paper:
~~~~
@Article{MohamadNezami2019,
author  = {Mohamad Nezami, Omid and Jamshid Lou, Paria and Karami, Mansoureh},
title = {ShEMO: a large-scale validated database for Persian speech emotion detection},
journal = {Language Resources and Evaluation},
year  = {2019},
volume  = {53},
number  = {1},
pages = {1--16},
issn  = {1574-0218},
doi = {10.1007/s10579-018-9427-x},
url = {https://doi.org/10.1007/s10579-018-9427-x}
}
~~~~

## Download Dataset
To download the dataset, please check the [ShEMO repo](https://github.com/pariajm/sharif-emotional-speech-database)!