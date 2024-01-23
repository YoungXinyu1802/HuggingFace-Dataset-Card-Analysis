---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
- fr
license:
- cc-by-sa-4.0
multilinguality:
- translation
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- translation
task_ids: []
pretty_name: DiaBLa
language_bcp47:
- en-UK
- fr-FR
---

# Dataset Card for DiaBLa: Bilingual dialogue parallel evaluation set

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

- **Homepage:** [almanach.inria.fr/software_and_resources/custom/DiaBLa-en.html](http://almanach.inria.fr/software_and_resources/custom/DiaBLa-en.html)
- **Repository:** [github.com/rbawden/DiaBLa-dataset](https://github.com/rbawden/DiaBLa-dataset)
- **Paper:** [Bawden et al. (2021). DiaBLa: A Corpus of Bilingual Spontaneous Written Dialogues for Machine Translation. Language Resources and Evaluation(55). Pages 635–660. Springer Verlag. 10.1007/s10579-020-09514-4.](https://hal.inria.fr/hal-03021633)
- **Point of contact:** rachel.bawden[at]inria.fr

### Dataset Summary

The dataset is an English-French dataset for the evaluation of Machine Translation (MT) for informal, written bilingual dialogue.

The dataset contains 144 spontaneous dialogues (5,700+ sentences) between native English and French speakers, mediated by one of two neural MT systems in a range of role-play settings. See below for some basic statistics. The dialogues are accompanied by fine-grained sentence-level judgments of MT quality, produced by the dialogue participants themselves, as well as by manually normalised versions and reference translations produced a posteriori. See here for information about evaluation.

The motivation for the corpus is two-fold: to provide:

- a unique resource for evaluating MT models for dialogue (i.e. in context)
- a corpus for the analysis of MT-mediated communication

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English (mainly UK) and French

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 37 MB
- **Number of parallel utterances:** 5748

Each example is highly annotated and is associated with dialogue context. An example from the test set looks as follows (only the first and last utterances of the dialogue history are shown for readability purposes):

```
{

  "id": "dialogue-2018-04-25T16-20-36.087170_french_english_1_2_25",
  "mt": "Tu m'en veux pour \u00e7a ?",
  "norm": "",
  "orig": "Are you blaming me for this?",
  "ref": "C'est moi que vous critiquez pour \u00e7a\u00a0?",
  "utterance_meta": {
    "eval_judgment": "medium",
    "eval_verbatim": "",
    "eval_problems": [
      "coherence"
    ],
    "lang": "english"
  },
  "dialogue_meta": {
    "start_time": "2018-04-25T16:20:36.087170",
    "end_time": "",
    "translation_model": "baseline",
    "final_evaluation_user1": {
      "style": "average",
      "coherence": "average",
      "grammaticality": "good",
      "meaning": "average",
      "word_choice": "average"
    },
    "final_evaluation_user2": {
      "style": "",
      "coherence": "",
      "grammaticality": "",
      "meaning": "",
      "word_choice": ""
    },
    "scenario": [
      [
        "You are both stuck in a lift at work.",
        "Vous \u00eates tous les deux bloqu\u00e9(e)s dans un ascenseur au travail."
      ],
      [
        "You are an employee and you are with your boss.",
        "Vous \u00eates un(e) employ\u00e9(e) et vous \u00eates avez votre patron(ne)"
      ],
      [
        "You are the boss and are with an employee.",
        "Vous \u00eates le ou la patron(ne) et vous \u00eates avec un(e) employ\u00e9(e)"
      ]
    ],
    "user1": {
      "role_num": 1,
      "role": [
        "You are an employee and you are with your boss.",
        "Vous \u00eates un(e) employ\u00e9(e) et vous \u00eates avez votre patron(ne)"
      ],
      "initiated_dialogue": true,
      "turn_number": 2,
      "lang": "french"
    },
    "user2": {
      "role_num": 2,
      "role": [
        "You are the boss and are with an employee.",
        "Vous \u00eates le ou la patron(ne) et vous \u00eates avec un(e) employ\u00e9(e)"
      ],
      "initiated_dialogue": false,
      "turn_number": 1,
      "lang": "english"
    }
  },
  "dialogue_history": [
    {
      "id": "dialogue-2018-04-25T16-20-36.087170_french_english_1_2_0",
      "orig": "We appear to have stopped moving.",
      "norm": "",
      "mt": "On semble avoir arr\u00eat\u00e9 de bouger.",
      "ref": "J'ai l'impression qu'on s'est arr\u00eat\u00e9s.",
      "utterance_meta": {
        "eval_judgment": "medium",
        "eval_verbatim": "",
        "eval_problems": [
          "style"
        ],
        "lang": "english"
      }
    },

    [...]

    {
      "id": "dialogue-2018-04-25T16-20-36.087170_french_english_1_2_24",
      "orig": "La sonnerie s'est arr\u00eat\u00e9, je pense que personne ne va nous r\u00e9pondre.",
      "norm": "",
      "mt": "The ringing stopped, and I don't think anyone's gonna answer us.",
      "ref": "It stopped ringing. I don't think anybody's going to reply.",
      "utterance_meta": {
        "eval_judgment": "perfect",
        "eval_verbatim": "",
        "eval_problems": [],
        "lang": "french"
      }
    }
  ]
}
```

### Data Fields

#### plain_text

- `id`: a `string` feature.
- `orig`: a `string` feature.
- `norm`: a `string` feature.
- `mt`: a `string` feature.
- `ref`: a `string` feature.
- `utterance_meta`: a dictionary feature containing:
  - `eval_judgment`: a `string` feature.
  - `eval_verbatim`: a `string` feature.
  - `eval_problems`: a list feature containing:
    - up to 5 `string` features.
  - `lang`: a `string` feature.
- `dialogue_meta`: a dictionary feature containing:   
  - `start_time` : a `string` feature.
  - `end_time`: a `string` feature.
  - `translation_model`: a `string` feature.
  - `final_evaluation_user1`: a dictionary feature containing:
    - `style`: a `string` feature.
    - `coherence`: a `string` feature.
    - `grammaticality`: a `string` feature.
    - `meaning`: a `string` feature.
    - `word_choice`: a `string` feature.
  - `final_evaluation_user2`: a dictionary feature containing:
    - `style`: a `string` feature.
    - `coherence`: a `string` feature.
    - `grammaticality`: a `string` feature.
    - `meaning`: a `string` feature.
    - `word_choice`: a `string` feature.     
  - `scenario`: a list feature containing
    - 3 lists each containing 2 `string` features.
  - `user1`: a dictionary feature containing:
    - `role_num`: an `int` feature.
    - `role`: a list feature containing:
      - 2 `string` features.
    - `initiated_dialogue`: a `bool` feature.
    - `turn_number`: an `int` value.
    - `lang`: a `string` value.   
  - `user2`: a dictionary feature containing:
    - `role_num`: an `int` feature.
    - `role`: a list feature containing:
      - 2 `string` features.
    - `initiated_dialogue`: a `bool` feature.
    - `turn_number`: an `int` value.
    - `lang`: a `string` value.
- `dialogue_history`: a list feature containing:
  - dictionary features containing:
    - `id`: a `string` feature.
    - `orig`: a `string` feature.
    - `norm`: a `string` feature.
    - `mt`: a `string` feature.
    - `ref`: a `string` feature.
    - `utterance_meta`: a dictionary feature containing:
      - `eval_judgment`: a `string` feature.
      - `eval_verbatim`: a `string` feature.
      - `eval_problems`: a list feature containing:
        - up to 5 `string` features.
      - `lang`: a `string` feature.

### Data Splits

DiaBLa is a test set only.

|   name   |test   |
|----------|------:|
|plain_text|   5748|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Original data was collected through a [dedicated online chat platform](https://github.com/rbawden/diabla-chat-interface) and involved native speakers of English and of French. As well as producing the original text, participants also annotated the quality of the machine-translated outputs of their partners' utterances (which they saw instead of their partners' original text) based on their monolingual intuitions and the dialogue context.

Each dialogue is assigned one of 12 role-play scenarios and where appropriate each participant is assigned a role to play in the dialogue. 

#### Who are the source language producers?

The source text producers were native French and native English volunteers (mainly British English). See the paper for very basic information concerning their backgrounds (age categories and experience in NLP).

### Annotations

#### Annotation process

On top of the original dialogue text (a mixture of utterances in English and in French), the following "annotations" are provided:

- machine translated version of the original text (produced in real time and presented during the dialogue), produced by one of two MT systems, both trained using [Marian](https://github.com/marian-nmt/marian).
- judgments of MT quality by participants (overall quality, particular problems, verbatim comments)
- manually produced normalised version of the original text (for spelling mistakes, grammatical errors, missing punctuation, etc.)
- manually produced reference translations

#### Who are the annotators?

The judgments of MT quality were produced by the dialogue participants themselves in real time. The normalised version of the text and the reference translations were manually produced by the authors of the paper. Translations were always done into the translator's native language and all translations were verified and post-edited by a bilingual English-French speaker.

### Personal and Sensitive Information

A priori the dataset does not contain personal and sensitive information. Participants were instructed not to give any personal information and to assume the roles assigned in the role play scenario. Usernames were anonymised prior to distribution and any mention of either usernames or real names in the dialogues were replaced by generic names of the same gender as the participant. Only basic user information was collected to get an idea of the distribution of participants and to potentially see how multilingual ability influences quality judgments (rough age categories, experience in NLP or research, native languages, familiarity with the other language (either English or French), other languages spoken and gender). Gender was included because it is an important factor in translation (particularly for the direction English-to-French), and this was explained in advance to the participants in the FAQs.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The dataset was collected by Rachel Bawden, Eric Bilinski, Thomas Lavergne and Sophie Rosset (see citation below).

### Licensing Information

The dataset is available under a CC BY-SA 4.0 licence.

### Citation Information

If you use or are inspired by this dataset, please cite:

```
@article{bawden_DiaBLa:-A-Corpus-of_2021,
  author = {Bawden, Rachel and Bilinski, Eric and Lavergne, Thomas and Rosset, Sophie},
  doi = {10.1007/s10579-020-09514-4},
  title = {DiaBLa: A Corpus of Bilingual Spontaneous Written Dialogues for Machine Translation},
  year = {2021},
  journal = {Language Resources and Evaluation},
  publisher = {Springer Verlag},
  volume = {55},
  pages = {635--660},
  url = {https://hal.inria.fr/hal-03021633},
  pdf = {https://hal.inria.fr/hal-03021633/file/diabla-lre-personal-formatting.pdf},
}
```

### Contributions

This dataset was added by Rachel Bawden [@rbawden](https://github.com/rbawden).