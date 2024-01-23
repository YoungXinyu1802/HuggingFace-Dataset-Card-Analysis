---
license: mit
language:
- en
paperswithcode_id: embedding-data/Amazon-QA
pretty_name: Amazon-QA
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification
---

# Dataset Card for "Amazon-QA"

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

- **Homepage:** [http://jmcauley.ucsd.edu/data/amazon/qa/](http://jmcauley.ucsd.edu/data/amazon/qa/)
- **Repository:** [More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [Julian McAuley](https://cseweb.ucsd.edu//~jmcauley/#)
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:** 247 MB

### Dataset Summary

This dataset contains Question and Answer data from Amazon.

Disclaimer: The team releasing Amazon-QA did not upload the dataset to the Hub and did not write a dataset card. 
These steps were done by the Hugging Face team.

### Supported Tasks
- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 
### Languages
- English.
## Dataset Structure
Each example in the dataset contains pairs of query and answer sentences and is formatted as a dictionary:
```
{"query": [sentence_1], "pos": [sentence_2]}
{"query": [sentence_1], "pos": [sentence_2]}
...
{"query": [sentence_1], "pos": [sentence_2]}
```
This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train models using similar sentences.
### Usage Example
Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:
```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/Amazon-QA")
```
The dataset is loaded as a `DatasetDict` and has the format:
```python
DatasetDict({
    train: Dataset({
        features: ['query', 'pos'],
        num_rows: 1095290
    })
})
```
Review an example `i` with:
```python
dataset["train"][0]
```
### Data Instances

### Data Fields


### Data Splits

## Dataset Creation

### Curation Rationale

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

#### Who are the source language producers?

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Annotations

#### Annotation process

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

#### Who are the annotators?

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Personal and Sensitive Information

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Discussion of Biases

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Other Known Limitations

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/s)

## Additional Information

### Dataset Curators

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Licensing Information

[More Information Needed](http://jmcauley.ucsd.edu/data/amazon/qa/)

### Citation Information




### Contributions


