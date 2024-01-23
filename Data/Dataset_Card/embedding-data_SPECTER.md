---
license: mit
language:
- en
paperswithcode_id: embedding-data/SPECTER
pretty_name: SPECTER
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification
---

# Dataset Card for "SPECTER"

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

- **Homepage:** [https://github.com/allenai/specter](https://github.com/allenai/specter)
- **Repository:** [More Information Needed](https://github.com/allenai/specter/blob/master/README.md)
- **Paper:** [More Information Needed](https://arxiv.org/pdf/2004.07180.pdf)
- **Point of Contact:** [@armancohan](https://github.com/armancohan), [@sergeyf](https://github.com/sergeyf), [@haroldrubio](https://github.com/haroldrubio), [@jinamshah](https://github.com/jinamshah)

### Dataset Summary

Dataset containing triplets (three sentences): anchor, positive, and negative. Contains titles of papers.

Disclaimer: The team releasing SPECTER did not upload the dataset to the Hub and did not write a dataset card. 
These steps were done by the Hugging Face team.

## Dataset Structure
Each example in the dataset contains triplets of equivalent sentences and is formatted as a dictionary with the key "set" and a list with the sentences as "value".

Each example is a dictionary with a key, "set", containing a list of three sentences (anchor, positive, and negative):

```
{"set": [anchor, positive, negative]}
{"set": [anchor, positive, negative]}
...
{"set": [anchor, positive, negative]}
```
This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train models using triplets.

### Usage Example
Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:
```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/SPECTER")
```
The dataset is loaded as a `DatasetDict` and has the format:
```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 684100
    })
})
```
Review an example `i` with:
```python
dataset["train"][i]["set"]
```

### Curation Rationale

[More Information Needed](https://github.com/allenai/specter)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/allenai/specter)

#### Who are the source language producers?

[More Information Needed](https://github.com/allenai/specter)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/allenai/specter)

#### Who are the annotators?

[More Information Needed](https://github.com/allenai/specter)

### Personal and Sensitive Information

[More Information Needed](https://github.com/allenai/specter)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/allenai/specter)

### Discussion of Biases

[More Information Needed](https://github.com/allenai/specter)

### Other Known Limitations

[More Information Needed](https://github.com/allenai/specter)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/allenai/specter)

### Licensing Information

[More Information Needed](https://github.com/allenai/specter)

### Citation Information



### Contributions

