---
language:
- de
task_categories:
- text-classification
task_ids:
- text-scoring
---
# AutoNLP Dataset for project: Doctor_DE

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project Doctor_DE.

### Languages

The BCP-47 code for the dataset's language is de.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Ich bin nun seit ca 12 Jahren Patientin in dieser Praxis und kann einige der Kommentare hier ehrlich gesagt \u00fcberhaupt nicht nachvollziehen.<br />\nFr. Dr. Gr\u00f6ber Pohl ist in meinen Augen eine unglaublich nette und kompetente \u00c4rztin. Ich kenne in meinem Familien- und Bekanntenkreis viele die bei ihr in Behandlung sind, und alle sind sehr zufrieden!<br />\nSie nimmt sich immer viel Zeit und auch in meiner Schwangerschaft habe ich mich bei ihr immer gut versorgt gef\u00fchlt, und musste daf\u00fcr kein einziges Mal in die Tasche greifen!<br />\nDas einzig negative ist die lange Wartezeit in der Praxis. Daf\u00fcr nimmt sie sich aber auch Zeit und arbeitet nicht wie andere \u00c4rzte wie am Flie\u00dfband.<br />\nIch kann sie nur weiter empfehlen!",
    "target": 1.0
  },
  {
    "text": "Ich hatte nie den Eindruck \"Der N\u00e4chste bitte\" Er hatte sofort meine Beschwerden erkannt und Abhilfe geschafft.",
    "target": 1.0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='float32', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 280191 |
| valid        | 70050 |
