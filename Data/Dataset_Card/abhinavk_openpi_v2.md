---
annotations_creators:
- expert-generated
language:
- en
language_creators: []
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: openpi_v2
size_categories:
- 10K<n<100K
source_datasets: []
tags: []
task_categories:
- question-answering
- text-classification
task_ids:
- entity-linking-classification
- natural-language-inference
---

# Dataset Card for openpi_v2

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

Open PI is the first dataset for tracking state changes in procedural text from arbitrary domains by using an unrestricted (open) vocabulary. Our solution is a new task formulation in which just the text is provided, from which a set of state changes (entity, attribute, before, after) is generated for each step, where the entity, attribute, and values must all be predicted from an open vocabulary.

### Supported Tasks and Leaderboards

-    `Task 1`: Given paragraph (e.g., with 5 steps), identify entities that change (challenge: implicit entities, some explicit entities that don’t change)     

-    `Task 3`: Given paragraph, identify the attributes of entity that change (challenge: implicit entities, attributes & many combinations) 

-    `Task 4`: Given paragraph & an entity, identify the sequence of attribute value changes (challenge: implicit attributes) 

-    `Task 7`: Given image url, identify the visual attributes of entity and non-visual attributes of entity that change

### Languages

English

## Dataset Structure

### Data Instances

A typical instance in the dataset:

```
{
    "goal": "goal1_text",
    "steps": [
        "step1_text",
        "step2_text",
        ...
    ],
    "topics": "topic1_annotation",
    "image_urls": [
        "step1_url_text",
        "step2_url_text",
        ...
    ],
    "states": [
        {
            "answers_openpiv1_metadata": {
                "entity": "entity1 | entity2 | ...",
                "attribute": "attribute1 | attribute2 | ...",
                "answers": [
                    "before: step1_entity1_before | step1_entity2_before, after: step1_entity1_after | step1_entity2_after",
                    ...
                ],
                "modality": [
                    "step1_entity1_modality_id | step1_entity2_modality_id",
                    ...
                ]
            },
            "entity": "entity1 | entity2 | ...",
            "attribute": "attribute1 | attribute2 | ...",
            "answers": [
                 "before: step1_entity1_before_merged | step1_entity2_before_merged, after: step1_entity1_after_merged | step1_entity2_after_merged",
                 ...
            ]
        }
    ]
}
```

### Data Fields

The following is an excerpt from the dataset README:

Within "goal", "steps", "topics", and "image_urls", the fields should be self-explanatory. Listed below is an explanation about those within "states": 

#### Fields specific to questions:

### Data Splits

Train, Valid, Dev

## Dataset Creation

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

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.