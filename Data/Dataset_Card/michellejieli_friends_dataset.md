---
language: "en"
tags:
- distilroberta
- sentiment
- emotion
- twitter
- reddit

---

# Dataset Card for friends_data

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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The Friends dataset consists of speech-based dialogue from the Friends TV sitcom. It is extracted from the [SocialNLP EmotionX 2019 challenge](https://sites.google.com/view/emotionx2019/datasets).

### Supported Tasks and Leaderboards
text-classification, sentiment-classification: The dataset is mainly used to predict a sentiment label given text input.

### Languages
The utterances are in English. 

## Dataset Structure

### Data Instances

A data point containing text and the corresponding label.

An example from the friends_dataset looks like this:

{
    'text': 'Well! Well! Well! Joey Tribbiani! So you came back huh?',
    'label': 'surprise'
}

### Data Fields

The field includes a text column and a corresponding emotion label. 

## Dataset Creation

### Curation Rationale

The dataset contains 1000 English-language dialogues originally in JSON files. The JSON file contains an array of dialogue objects. Each dialogue object is an array of line objects, and each line object contains speaker, utterance, emotion, and annotation strings.
        {
            "speaker": "Chandler",
            "utterance": "My duties?  All right.",
            "emotion": "surprise",
            "annotation": "2000030"
        }

Utterance and emotion were extracted from the original files into a CSV file. The dataset was cleaned to remove non-neutral labels. This dataset was created to be used in fine-tuning an emotion sentiment classifier that can be useful to teach individuals with autism how to read facial expressions.