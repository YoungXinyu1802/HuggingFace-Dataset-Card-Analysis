---
license: apache-2.0
pretty_name: MIMICause
---

# Dataset Card for "MIMICause"

## Table of Contents
- [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks](#supported-tasks)
- [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
- [Additional Information](#additinal-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/)
- **Paper:** [MIMICause: Representation and automatic extraction of causal relation types from clinical notes](https://arxiv.org/abs/2110.07090)
- **Size of downloaded dataset files:** 333.4 KB
- **Size of the generated dataset:** 491.2 KB
- **Total amount of disk used:** 668.2 KB

### Dataset Summary

MIMICause Dataset is a dataset for representation and automatic extraction of causal relation types from clinical notes. The MIMICause dataset requires manual download of the mimicause.zip file from the **Community Annotations Downloads** section of the n2c2 dataset on the [Harvard's DBMI Data Portal](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/) after signing their agreement forms, which is a quick and easy procedure.

The dataset has 2714 samples having both explicit and implicit causality in which entities are in the same sentence or different sentences. The nine semantic causal relations (with directionality) between entitities E1 and E2 in a text snippets are -- (1) Cause(E1,E2) (2) Cause(E2,E1) (3) Enable(E1,E2) (4) Enable(E2,E1) (5) Prevent(E1,E2) (6) Prevent(E2,E1) (7) Hinder(E1,E2) (8) Hinder(E2,E1) (9) Other.

### Supported Tasks

Causal relation extraction between entities expressed implicitly or explicitly, in single or across multiple sentences.


## Dataset Structure

### Data Instances

An example of a data sample looks as follows:
```
{
    "E1": "Florinef",
    "E2": "fluid retention",
    "Text": "Treated with <e1>Florinef</e1> in the past, was d/c'd due to <e2>fluid retention</e2>.",
    "Label": 0
}
```

### Data Fields

The data fields are the same among all the splits.

- `E1`: a `string` value.
- `E2`: a `string` value.
- `Text`: a `large_string` value.
- `Label`: a `ClassLabel` categorical value.

### Data Splits

The original dataset that gets downloaded from the [Harvard's DBMI Data Portal](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/) have all the data in a single split. The dataset loading provided here through huggingface datasets splits the data into the following train, validation and test splits for convenience.

|   name  |train|validation|test|
|---------|----:|---------:|---:|
|mimicause| 1953|    489   | 272|

## Additional Information

### Citation Information
```
@inproceedings{khetan-etal-2022-mimicause,
    title={MIMICause: Representation and automatic extraction of causal relation types from clinical notes},
    author={Vivek Khetan and Md Imbesat Hassan Rizvi and Jessica Huber and Paige Bartusiak and Bogdan Sacaleanu and Andrew Fano},
    booktitle ={Findings of the Association for Computational Linguistics: ACL 2022},
    month={may},
    year={2022},
    publisher={Association for Computational Linguistics},
    address={Dublin, The Republic of Ireland},
    url={},
    doi={},
    pages={},
}
```