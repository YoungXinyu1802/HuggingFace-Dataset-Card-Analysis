---
language:
- multilingual
license:
- cc-by-4.0 
multilinguality:
- multilingual
source_datasets:
- nluplusplus
task_categories:
- text-classification
pretty_name: multi3-nlu

---

# Dataset Card for Multi<sup>3</sup>NLU++

## Table of Contents
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
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contact](#contact)
  
## Dataset Description

- **Paper:** [arXiv](https://arxiv.org/abs/2212.10455)


### Dataset Summary
Please note the dataset is not being loaded currently in the dataset loader - but you can access the raw files of the dataset in the folder where the dataset gets downloaded. We will fix this ASAP. 

Multi<sup>3</sup>NLU++ consists of 3080 utterances per language representing challenges in building multilingual multi-intent multi-domain task-oriented dialogue systems. The domains include banking and hotels. There are 62 unique intents. 

### Supported Tasks and Leaderboards

- multi-label intent detection
- slot filling
- cross-lingual language understanding for task-oriented dialogue

### Languages

The dataset covers four language pairs in addition to the source dataset in English: 
Spanish, Turkish, Marathi, Amharic

## Dataset Structure

### Data Instances

Each data instance contains the following features: _text_, _intents_, _uid_, _lang_, and ocassionally _slots_ and _values_

See the [Multi<sup>3</sup>NLU++ corpus viewer](https://huggingface.co/datasets/uoe-nlp/multi3-nlu/viewer/uoe-nlp--multi3-nlu/train) to explore more examples.

An example from the Multi<sup>3</sup>NLU++ looks like the following:
```
{
        "text": "माझे उद्याचे रिझर्वेशन मला रद्द का करता येणार नाही?",
        "intents": [
            "why",
            "booking",
            "cancel_close_leave_freeze",
            "wrong_notworking_notshowing"
        ],
        "slots": {
            "date_from": {
                "text": "उद्याचे",
                "span": [
                    5,
                    12
                ],
                "value": {
                    "day": 16,
                    "month": 3,
                    "year": 2022
                }
            }
        },
        "uid": "hotel_1_1",
        "lang": "mr"

}
```

### Data Fields

- 'text': a string containing the utterance for which the intent needs to be detected
- 'intents': the corresponding intent labels
- 'uid': unique identifier per language
- 'lang': the language of the dataset 
- 'slots': annotation of the span that needs to be extracted for value extraction with its label and _value_


### Data Splits

The experiments are done on different k-fold validation setups. The dataset has multiple types of data splits. Please see Section 4 of the paper. 

## Dataset Creation

### Curation Rationale
Existing task-oriented dialogue datasets are 1) predominantly limited to detecting a single intent, 2) focused on a single domain, and 3) include a small set of slot types. Furthermore, the success of task-oriented dialogue is 4) often evaluated on a small set of higher-resource languages (i.e., typically English) which does not test how generalisable systems are to the diverse range of the world's languages.
Our proposed dataset addresses all these limitations


### Source Data


#### Initial Data Collection and Normalization
Please see Section 3 of the paper 

#### Who are the source language producers?
The source language producers are authors of [NLU++ dataset](https://arxiv.org/abs/2204.13021). The dataset was professionally translated into our chosen four languages. We used Blend Express and Proz.com to recruit these translators. 


### Personal and Sensitive Information

None. Names are fictional



### Discussion of Biases

We have carefully vetted the examples to exclude the problematic examples.

### Other Known Limitations
The dataset comprises utterances extracted from real dialogues between users and conversational agents as well as synthetic human-authored utterances constructed with the aim of introducing additional combinations of intents and slots. The utterances therefore lack the wider context that would be present in a complete dialogue. As such the dataset cannot be used to evaluate systems with respect to discourse-level phenomena present in dialogue.

## Additional Information
N/A

### Licensing Information

The dataset is Creative Commons Attribution 4.0 International (cc-by-4.0) 

### Citation Information

Coming soon

### Contact
[Nikita Moghe](mailto:nikita.moghe@ed.ac.uk) and [Evgeniia Razumovskaia](er563@cam.ac.uk) and [Liane Guillou](mailto:lguillou@ed.ac.uk)

Dataset card based on [Allociné](https://huggingface.co/datasets/allocine) 