---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
- de
license:
- mit
multilinguality:
- multilingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-label-classification
- semantic-similarity-classification
pretty_name: SV-Ident
paperswithcode_id: sv-ident
---

# Dataset Card for SV-Ident

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

- **Homepage:** https://vadis-project.github.io/sv-ident-sdp2022/
- **Repository:** https://github.com/vadis-project/sv-ident
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** svident2022@googlegroups.com

### Dataset Summary

SV-Ident comprises 4,248 sentences from social science publications in English and German. The data is the official data for the Shared Task: “Survey Variable Identification in Social Science Publications” (SV-Ident) 2022. Visit the homepage to find out more details about the shared task.

### Supported Tasks and Leaderboards

The dataset supports:

- **Variable Detection**: identifying whether a sentence contains a variable mention or not.

- **Variable Disambiguation**: identifying which variable from a given vocabulary is mentioned in a sentence. **NOTE**: for this task, you will need to also download the variable metadata from [here](https://bit.ly/3Nuvqdu).

### Languages

The text in the dataset is in English and German, as written by researchers. The domain of the texts is scientific publications in the social sciences.

## Dataset Structure

### Data Instances

```
{
  "sentence": "Our point, however, is that so long as downward (favorable comparisons overwhelm the potential for unfavorable comparisons, system justification should be a likely outcome amongst the disadvantaged.",
  "is_variable": 1,
  "variable": ["exploredata-ZA5400_VarV66", "exploredata-ZA5400_VarV53"],
  "research_data": ["ZA5400"],
  "doc_id": "73106",
  "uuid": "b9fbb80f-3492-4b42-b9d5-0254cc33ac10",
  "lang": "en",
}
```

### Data Fields

The following data fields are provided for documents:

```
`sentence`:       Textual instance, which may contain a variable mention.<br />
`is_variable`:    Label, whether the textual instance contains a variable mention (1) or not (0). This column can be used for Task 1 (Variable Detection).<br />
`variable`:       Variables (separated by a comma ";") that are mentioned in the textual instance. This column can be used for Task 2 (Variable Disambiguation). Variables with the "unk" tag could not be mapped to a unique variable.<br />
`research_data`:  Research data IDs (separated by a ";") that are relevant for each instance (and in general for each "doc_id").<br />
`doc_id`:         ID of the source document. Each document is written in one language (either English or German).<br />
`uuid`:           Unique ID of the instance in uuid4 format.<br />
`lang`:           Language of the sentence.
```

The language for each document can be found in the document-language mapping file [here](https://github.com/vadis-project/sv-ident/blob/main/data/train/document_languages.json), which maps `doc_id` to a language code (`en`, `de`). The variables metadata (i.e., the vocabulary) can be downloaded from this [link](https://bit.ly/3Nuvqdu). Note, that each `research_data` contains hundreds of variables (these can be understood as the corpus of documents to choose the most relevant from). If the variable has an "unk" tag, it means that the sentence contains a variable that has not been disambiguated. Such sentences could be used for Task 1 and filtered out for Task 2. The metadata file has the following format:

```
{
  "research_data_id_1": {
    "variable_id_1": VARIABLE_METADATA,
    ...
    "variable_id_n": VARIABLE_METADATA,
  },
  ...
  "research_data_id_n": {...},
}
```

Each variable may contain all (or some) of the following values:
```
study_title:        The title of the research data study.
variable_label:     The label of the variable.
variable_name:      The name of the variable.
question_text:      The question of the variable in the original language.
question_text_en:   The question of the variable in English.
sub_question:       The sub-question of the variable.
item_categories:    The item categories of the variable.
answer_categories:  The answers of the variable.
topic:              The topics of the variable in the original language.
topic_en:           The topics of the variable in English.
```

### Data Splits

| Split               | Number of sentences                       |
| ------------------- | ------------------------------------      |
| Train               | 3,823                                     |
| Validation          |   425                                     |

## Dataset Creation

### Curation Rationale

The dataset was curated by the VADIS project (https://vadis-project.github.io/).
The documents were annotated by two expert annotators.

### Source Data

#### Initial Data Collection and Normalization

The original data are available at GESIS (https://www.gesis.org/home) in an unprocessed format.

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

The documents were annotated by two expert annotators.

### Personal and Sensitive Information

The dataset does not include personal or sensitive information.

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

VADIS project (https://vadis-project.github.io/)

### Licensing Information

All documents originate from the Social Science Open Access Repository (SSOAR) and are licensed accordingly. The original document URLs are provided in [document_urls.json](https://github.com/vadis-project/sv-ident/blob/main/data/train/document_urlsjson). For more information on licensing, please refer to the terms and conditions on the [SSAOR Grant of Licenses page](https://www.gesis.org/en/ssoar/home/information/grant-of-licences).

### Citation Information

```
@inproceedings{tsereteli-etal-2022-overview,
    title = "Overview of the {SV}-Ident 2022 Shared Task on Survey Variable Identification in Social Science Publications",
    author = "Tsereteli, Tornike  and
      Kartal, Yavuz Selim  and
      Ponzetto, Simone Paolo  and
      Zielinski, Andrea  and
      Eckert, Kai  and
      Mayr, Philipp",
    booktitle = "Proceedings of the Third Workshop on Scholarly Document Processing",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.sdp-1.29",
    pages = "229--246",
    abstract = "In this paper, we provide an overview of the SV-Ident shared task as part of the 3rd Workshop on Scholarly Document Processing (SDP) at COLING 2022. In the shared task, participants were provided with a sentence and a vocabulary of variables, and asked to identify which variables, if any, are mentioned in individual sentences from scholarly documents in full text. Two teams made a total of 9 submissions to the shared task leaderboard. While none of the teams improve on the baseline systems, we still draw insights from their submissions. Furthermore, we provide a detailed evaluation. Data and baselines for our shared task are freely available at \url{https://github.com/vadis-project/sv-ident}.",
}
```

### Contributions

[Needs More Information]