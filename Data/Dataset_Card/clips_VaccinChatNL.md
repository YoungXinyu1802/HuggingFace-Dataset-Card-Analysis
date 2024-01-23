---
annotations_creators:
- expert-generated
language:
- nl
language_creators:
- other
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: VaccinChatNL
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- covid-19
- FAQ
- question-answer pairs
task_categories:
- text-classification
task_ids:
- intent-classification
---

# Dataset Card for VaccinChatNL

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
  <!-- - [Curation Rationale](#curation-rationale) -->
  <!-- - [Source Data](#source-data) -->
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  <!-- - [Social Impact of Dataset](#social-impact-of-dataset) -->
  - [Discussion of Biases](#discussion-of-biases)
  <!-- - [Other Known Limitations](#other-known-limitations) -->
- [Additional Information](#additional-information)
  <!-- - [Dataset Curators](#dataset-curators) -->
  <!-- - [Licensing Information](#licensing-information) -->
  - [Citation Information](#citation-information)
  <!-- - [Contributions](#contributions) -->

## Dataset Description

<!-- - **Homepage:**
- **Repository:**
- **Paper:** [To be added]
- **Leaderboard:** -->
- **Point of Contact:**  [Jeska Buhmann](mailto:jeska.buhmann@uantwerpen.be)

### Dataset Summary

VaccinChatNL is a Flemish Dutch FAQ dataset on the topic of COVID-19 vaccinations in Flanders. It consists of 12,833 user questions divided over 181 answer labels, thus providing large groups of semantically equivalent paraphrases (a many-to-one mapping of user questions to answer labels). VaccinChatNL is the first Dutch many-to-one FAQ dataset of this size.

### Supported Tasks and Leaderboards

- 'text-classification': the dataset can be used to train a classification model for Dutch frequently asked questions on the topic of COVID-19 vaccination in Flanders.  


### Languages

Dutch (Flemish): the BCP-47 code for Dutch as generally spoken in Flanders (Belgium) is nl-BE.

## Dataset Structure

### Data Instances

For each instance, there is a string for the user question and a string for the label of the annotated answer. See the [CLiPS / VaccinChatNL dataset viewer](https://huggingface.co/datasets/clips/VaccinChatNL/viewer/clips--VaccinChatNL/train).

```
{"sentence1": "Waar kan ik de bijsluiters van de vaccins vinden?", "label": "faq_ask_bijsluiter"}
```

### Data Fields

- `sentence1`: a string containing the user question
- `label`: a string containing the name of the intent (the answer class)


### Data Splits

The VaccinChatNL dataset has 3 splits: _train_, _valid_, and _test_. Below are the statistics for the dataset.

| Dataset Split | Number of Labeled User Questions in Split               |
| ------------- | ------------------------------------------ |
| Train         | 10,542                                     |
| Validation    |  1,171                                     |
| Test          |  1,170                                     |


## Dataset Creation

<!-- ### Curation Rationale

[More Information Needed] -->

<!-- ### Source Data

[Perhaps a link to vaccinchat.be and some of the website that were used for information] -->

<!-- #### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed] -->

### Annotations

#### Annotation process

Annotation was an iterative semi-automatic process. Starting from a very limited dataset with approximately 50 question-answer pairs (_sentence1-label_ pairs) a text classification model was trained and implemented in a publicly available chatbot. When the chatbot was used, the predicted labels for the new questions were checked and corrected if necessary. In addition, new answers were added to the dataset. After each round of corrections, the model was retrained on the updated dataset. This iterative approach led to the final dataset containing 12,883 user questions divided over 181 answer labels.

#### Who are the annotators?

The VaccinChatNL data were annotated by members and students of [CLiPS](https://www.uantwerpen.be/en/research-groups/clips/). All annotators have a background in Computational Linguistics.

### Personal and Sensitive Information

The data are anonymized in the sense that a user question can never be traced back to a specific individual.

## Considerations for Using the Data

<!-- ### Social Impact of Dataset

[More Information Needed] -->

### Discussion of Biases

This dataset contains real user questions, including a rather large section (7%) of out-of-domain questions or remarks (_label: nlu_fallback_). This class of user questions consists of ununderstandable questions, but also jokes and insulting remarks.

<!-- ### Other Known Limitations

[Perhaps some information of % of exact overlap between train and test set] -->

## Additional Information

<!-- ### Dataset Curators

[More Information Needed] -->

<!-- ### Licensing Information

[More Information Needed] -->

### Citation Information

Will be added asap.

<!-- ### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset. -->
