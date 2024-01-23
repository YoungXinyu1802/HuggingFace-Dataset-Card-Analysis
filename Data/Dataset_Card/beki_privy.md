---
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<200K
- 300K<n<400K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
tags:
- pii-detection
train-eval-index:
- config: privy-small
  task: token-classification
  task_id: entity_extraction
  splits:
    train_split: train
    eval_split: test
  metrics:
  - type: seqeval
    name: seqeval
---

# Dataset Card for "privy-english"

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

- **Homepage:** [https://github.com/pixie-io/pixie/tree/main/src/datagen/pii/privy](https://github.com/pixie-io/pixie/tree/main/src/datagen/pii/privy)

### Dataset Summary
A synthetic PII dataset generated using [Privy](https://github.com/pixie-io/pixie/tree/main/src/datagen/pii/privy), a tool which parses OpenAPI specifications and generates synthetic request payloads, searching for keywords in API schema definitions to select appropriate data providers. Generated API payloads are converted to various protocol trace formats like JSON and SQL to approximate the data developers might encounter while debugging applications. 

This labelled PII dataset consists of protocol traces (JSON, SQL (PostgreSQL, MySQL), HTML, and XML) generated from OpenAPI specifications and includes 60+ PII types. 

### Supported Tasks and Leaderboards

Named Entity Recognition (NER) and PII classification. 

### Label Scheme

<details>

<summary>View label scheme (26 labels for 60 PII data providers)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `PERSON`, `LOCATION`, `NRP`, `DATE_TIME`, `CREDIT_CARD`, `URL`, `IBAN_CODE`, `US_BANK_NUMBER`, `PHONE_NUMBER`, `US_SSN`, `US_PASSPORT`, `US_DRIVER_LICENSE`, `IP_ADDRESS`, `US_ITIN`, `EMAIL_ADDRESS`, `ORGANIZATION`, `TITLE`, `COORDINATE`, `IMEI`, `PASSWORD`, `LICENSE_PLATE`, `CURRENCY`, `ROUTING_NUMBER`, `SWIFT_CODE`, `MAC_ADDRESS`, `AGE` |

</details>

### Languages

English

## Dataset Structure

### Data Instances

A sample:
```
{
    "full_text": "{\"full_name_female\": \"Bethany Williams\", \"NewServerCertificateName\": \"\", \"NewPath\": \"\", \"ServerCertificateName\": \"dCwMNqR\", \"Action\": \"\", \"Version\": \"u zNS zNS\"}",
        "masked": "{\"full_name_female\": \"{{name_female}}\", \"NewServerCertificateName\": \"{{string}}\", \"NewPath\": \"{{string}}\", \"ServerCertificateName\": \"{{string}}\", \"Action\": \"{{string}}\", \"Version\": \"{{string}}\"}",
        "spans": [
            {
                "entity_type": "PERSON",
                "entity_value": "Bethany Williams",
                "start_position": 22,
                "end_position": 38
            }
        ],
        "template_id": 51889,
        "metadata": null
}

```

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information

```
@online{WinNT,
  author = {Benjamin Kilimnik},
  title = {{Privy} Synthetic PII Protocol Trace Dataset},
  year = 2022,
  url = {https://huggingface.co/datasets/beki/privy},
}
```

### Contributions

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)