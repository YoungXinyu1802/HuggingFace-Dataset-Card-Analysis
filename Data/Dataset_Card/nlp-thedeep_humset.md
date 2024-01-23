---
annotations_creators:
- expert-generated
language:
- en
- fr
- es
language_creators:
- expert-generated
license:
- apache-2.0
multilinguality:
- multilingual
pretty_name: HumSet
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- humanitarian
- research
- analytical-framework
- multilabel
- humset
- humbert
task_categories:
- text-classification
- text-retrieval
- token-classification
task_ids:
- multi-label-classification
dataset_info:
  features:
  - name: entry_id
    dtype: string
  - name: lead_id
    dtype: string
  - name: project_id
    dtype: string
  - name: lang
    dtype: string
  - name: n_tokens
    dtype: int64
  - name: project_title
    dtype: string
  - name: created_at
    dtype: string
  - name: document
    dtype: string
  - name: excerpt
    dtype: string
  - name: sectors
    sequence:
          class_label:
            names:
                0: Agriculture
                1: Cross
                2: Education
                3: Food Security
                4: Health
                5: Livelihoods
                6: Logistics
                7: Nutrition
                8: Protection
                9: Shelter
                10: WASH
  - name: pillars_1d
    sequence:
        class_label:
          names:
              0: Casualties
              1: Context
              2: Covid-19
              3: Displacement
              4: Humanitarian Access
              5: Information And Communication
              6: Shock/Event
  - name: pillars_2d
    sequence:
        class_label:
          names:
              0: At Risk
              1: Capacities & Response
              2: Humanitarian Conditions
              3: Impact
              4: Priority Interventions
              5: Priority Needs
  - name: subpillars_1d
    sequence:
        class_label:
          names:
              0: Casualties->Dead
              1: Casualties->Injured
              2: Casualties->Missing
              3: Context->Demography
              4: Context->Economy
              5: Context->Environment
              6: Context->Legal & Policy
              7: Context->Politics
              8: Context->Security & Stability
              9: Context->Socio Cultural
              10: Covid-19->Cases
              11: Covid-19->Contact Tracing
              12: Covid-19->Deaths
              13: Covid-19->Hospitalization & Care
              14: Covid-19->Restriction Measures
              15: Covid-19->Testing
              16: Covid-19->Vaccination
              17: Displacement->Intentions
              18: Displacement->Local Integration
              19: Displacement->Pull Factors
              20: Displacement->Push Factors
              21: Displacement->Type/Numbers/Movements
              22: Humanitarian Access->Number Of People Facing Humanitarian Access Constraints/Humanitarian Access Gaps
              23: Humanitarian Access->Physical Constraints
              24: Humanitarian Access->Population To Relief
              25: Humanitarian Access->Relief To Population
              26: Information And Communication->Communication Means And Preferences
              27: Information And Communication->Information Challenges And Barriers
              28: Information And Communication->Knowledge And Info Gaps (Hum)
              29: Information And Communication->Knowledge And Info Gaps (Pop)
              30: Shock/Event->Hazard & Threats
              31: Shock/Event->Type And Characteristics
              32: Shock/Event->Underlying/Aggravating Factors
  
  - name: subpillars_2d
    sequence:
        class_label:
          names:
            0: At Risk->Number Of People At Risk
            1: At Risk->Risk And Vulnerabilities
            2: Capacities & Response->International Response
            3: Capacities & Response->Local Response
            4: Capacities & Response->National Response
            5: Capacities & Response->Number Of People Reached/Response Gaps
            6: Humanitarian Conditions->Coping Mechanisms
            7: Humanitarian Conditions->Living Standards
            8: Humanitarian Conditions->Number Of People In Need
            9: Humanitarian Conditions->Physical And Mental Well Being
            10: Impact->Driver/Aggravating Factors
            11: Impact->Impact On People
            12: Impact->Impact On Systems, Services And Networks
            13: Impact->Number Of People Affected
            14: Priority Interventions->Expressed By Humanitarian Staff
            15: Priority Interventions->Expressed By Population
            16: Priority Needs->Expressed By Humanitarian Staff
            17: Priority Needs->Expressed By Population

  splits:
  - name: train
    num_examples: 117435
  - name: validation
    num_examples: 16039
  - name: test
    num_examples: 15147
---

# Dataset Card for HumSet

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

## Dataset Description

- **Homepage:** [http://blog.thedeep.io/humset/](http://blog.thedeep.io/humset/)
- **Repository:** [https://github.com/the-deep/humset](https://github.com/the-deep/humset)
- **Paper:** [EMNLP Findings 2022](https://aclanthology.org/2022.findings-emnlp.321)
- **Leaderboard:**
- **Point of Contact:**[the DEEP NLP team](mailto:nlp@thedeep.io)

### Dataset Summary

HumSet is a novel and rich multilingual dataset of humanitarian response documents annotated by experts in the humanitarian response community. HumSet is curated by humanitarian analysts and covers various disasters around the globe that occurred from 2018 to 2021 in 46 humanitarian response projects. The dataset consists of approximately 17K annotated documents in three languages of English, French, and Spanish, originally taken from publicly-available resources. For each document, analysts have identified informative snippets (entries) in respect to common humanitarian frameworks, and assigned one or many classes to each entry. See the our paper for details.

### Supported Tasks and Leaderboards

This dataset is intended for multi-label classification 

### Languages

This dataset is in English, French and Spanish

## Dataset Structure


### Data Instances

[More Information Needed]

### Data Fields

- **entry_id**: unique identification number for a given entry. (string)
- **lead_id**: unique identification number for the document to which the corrisponding entry belongs. (string)
- **project_id** unique identification number for the project to which the corrisponding entry belongs. (string)
- **sectors**, **pillars_1d**, **pillars_2d**, **subpillars_1d**, **subpillars_2d**: labels assigned to the corresponding entry. Since this is a multi-label dataset (each entry may have several annotations belonging to the same category), they are reported as arrays of strings. See the paper for a detailed description of these categories. (list)
- **lang**: language. (str)
- **n_tokens**: number of tokens (tokenized using NLTK v3.7 library). (int64)
- **project_title**: the name of the project where the corresponding annotation was created. (str)
- **created_at**: date and time of creation of the annotation in stardard ISO 8601 format. (str)
- **document**: document URL source of the excerpt. (str)
- **excerpt**: excerpt text. (str)

### Data Splits

The dataset includes a set of train/validation/test splits, with 117435, 16039 and 15147 examples respectively.

## Dataset Creation

The collection originated from a multi-organizational platform called <em>the Data Entry and Exploration Platform (DEEP)</em> developed and maintained by Data Friendly Space (DFS). The platform facilitates classifying primarily qualitative information with respect to analysis frameworks and allows for collaborative classification and annotation of secondary data. 

### Curation Rationale

[More Information Needed]

### Source Data

Documents are selected from different sources, ranging from official reports by humanitarian organizations to international and national media articles. See the paper for more informations. 

#### Initial Data Collection and Normalization

#### Who are the source language producers?

[More Information Needed]


#### Annotation process

HumSet is curated by humanitarian analysts and covers various disasters around the globe that occurred from 2018 to 2021 in 46 humanitarian response projects. The dataset consists of approximately 17K annotated documents in three
languages of English, French, and Spanish, originally taken from publicly-available resources. For
each document, analysts have identified informative snippets (entries, or excerpt in the imported dataset) with respect to common <em>humanitarian frameworks</em> and assigned one or many classes to each entry.

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

NLP team at [Data Friendly Space](https://datafriendlyspace.org/)

### Licensing Information

The GitHub repository which houses this dataset has an Apache License 2.0.

### Citation Information

```
@inproceedings{fekih-etal-2022-humset,
    title = "{H}um{S}et: Dataset of Multilingual Information Extraction and Classification for Humanitarian Crises Response",
    author = "Fekih, Selim  and
      Tamagnone, Nicolo{'}  and
      Minixhofer, Benjamin  and
      Shrestha, Ranjan  and
      Contla, Ximena  and
      Oglethorpe, Ewan  and
      Rekabsaz, Navid",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.321",
    pages = "4379--4389",
}
```
